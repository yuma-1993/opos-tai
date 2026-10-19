---
tags:
  - bloque4
  - tema8
  - http
  - ssl-tls
  - criptografia
  - certificados
  - seguridad
  - redes
bloque: 4
tema: 8
titulo: HTTP, SSL/TLS (arquitectura de Internet, HTTP/1.1-2-3, criptografía y certificados)
estado: por-repasar
---

# Tema 8 · Bloque 4 — HTTP y SSL/TLS

> [!abstract] De qué va este tema
> Recorre la pila web de arriba abajo: la jerarquía de Internet (Tier-1/2/3, IXP, CDN) por donde viaja el tráfico; el protocolo HTTP en sus tres versiones (1.1, 2 y 3) con sus métodos, cabeceras, códigos de respuesta y mecanismos de seguridad (CORS, HSTS, CSP); y la capa que lo protege, SSL/TLS, con su handshake, los algoritmos criptográficos que usa (simétricos, asimétricos, hash/MAC), la firma digital, los certificados X.509v3, su verificación y los almacenes de confianza (con el caso particular de Java y los estándares PKCS).

---

## 1. Arquitectura de Internet: jerarquía

Esquema del PDF: tres niveles (Tier 1, Tier 2, Tier 3) de arriba abajo. Entre redes del mismo nivel hay **peering entre iguales** (privado o público, gratis); entre niveles distintos hay **tránsito** (de pago, "€€€"). Los usuarios de Internet (organizaciones, empresas y clientes residenciales) cuelgan de las redes Tier 3.

| Nivel | Qué es | Detalles del PDF |
|---|---|---|
| TIER-1 | Las redes más importantes: backbone de Internet | Alcance internacional. Requisitos muy elevados. Llamados *Carriers* de Internet. Redes de intercambio de tráfico |
| TIER-2 | Cobertura nacional | Para hablar de TIER-2 a TIER-2 debe haber un contrato/acuerdo de tránsito con TIER-1 |
| TIER-3 | Alcance local | Llamados proveedores de Internet (ISP) |

- Entre 2 AS (Sistemas Autónomos) se usa **BGP**. Dentro de cada AS se usa **IGP**.
- Cada AS tiene un **ASN** (Número de Sistema Autónomo), dado por IANA-RIR.

| Elemento | Descripción (PDF) |
|---|---|
| IXP | Punto de acceso neutro. Evitan el tráfico de tránsito, saltándose los peajes. Mejoran la latencia, el ancho de banda y el coste. Switching (nivel 2). Pueden dar servicio a TIER-2 y 3. Son como cooperativas. Ejemplos: ESPANIX, CATNIX, DE-CIX |
| CDN (*Content Delivery Network*) | Akamai, Cloudflare, CDNJS, etc. Despliegas una copia de tu información en todos los servidores CDN para que el más cercano al cliente sirva la información. Ofrecen alta disponibilidad y rendimiento. Están enganchados a los IXP |

> [!note] Errata aplicada (Actualizaciones 20_05_2026, entrada de 01/05/2025)
> En el apunte original el proveedor CDN aparecía como "Akai"; la corrección oficial es **Akamai**. El PDF ya trae la forma correcta y así queda aquí.

---

## 2. HTTP/1.1

HTTP se pensó para navegar, no para hacer aplicaciones web. **HTTP no tiene estado**: cada llamada al servidor es como si fuese la primera, no tiene memoria; por eso se necesitan las **cookies**. Es **orientado a carácter**, igual que FTP, SMTP, POP3, etc. Modelo **petición-respuesta** (request-response).

> [!note] Errata aplicada (Actualizaciones, 12/09/2024)
> "HTTP es un protocolo orientado a carácter como FTP, **no como TCP**". Es decir, el contraste con TCP (orientado a bytes/flujo) está en la corrección del PDF.

### 2.1 URI, URL y URN

| Término | Función | Esquema |
|---|---|---|
| URI | Identificador de recurso | `http:`, `urn:`, `ftp:`, `mailto:` |
| URL | Localizar | `http:` o `https:` |
| URN | Identificar | `urn:`. Ejemplo: `urn:isbn:444-abc-123` (*isbn* es la temática y *444-abc-123* el valor) |

### 2.2 Formato de la petición (user agent → http server)

```
verbo /url HTTP/1.1
Host: www.loquesea.com
Accept: image/gif, ...
Accept-Language: es-ES
Accept-Encoding: gzip, deflate
[línea en blanco]
Request Body (Ejemplo: formulario)
```

Las líneas `Host`, `Accept`... son los **headers**; tras la línea en blanco va el cuerpo de la petición (por ejemplo, un formulario). (El PDF escribe "Accept-Languaje"; la cabecera correcta es `Accept-Language`.)

### 2.3 Verbos / métodos / acciones

- **Método seguro (safe)**: no modifica el recurso. Solo lectura. Los métodos seguros son idempotentes.
- **Método idempotente**: da el mismo resultado aunque se ejecute muchas veces. Garantiza estabilidad. Ver [[Idempotencia]] (concepto visto en gestión de configuración).

| Método | Qué hace | Safe | Idempotente |
|---|---|---|---|
| GET | Obtiene el recurso | Sí | Sí |
| HEAD | Obtiene solo los headers, no el recurso | Sí | Sí |
| PUT | Pone un recurso en la url. Crea o reemplaza | — | Sí |
| POST | Envía datos a la url. No es idempotente porque puede que cree un recurso nuevo en lugar de reemplazarlo. No se refiere a un recurso concreto | — | No |
| PATCH | Modificaciones parciales, "PUT parcial" | — | (no marcado en el PDF) |
| TRACE | Similar a *echo*: el servidor devuelve lo que recibe. Usado para depurar | Sí | Sí |
| OPTIONS | Qué puedo hacer con el recurso, qué métodos soporta la url. Seguridad | Sí | Sí |
| DELETE | El estado del recurso se queda como borrado | — | Sí |
| CONNECT | Túnel HTTPS a través de un proxy | — | (no marcado en el PDF) |

> [!important] Idempotente no es lo mismo que seguro
> Seguros (solo lectura): GET, HEAD, TRACE, OPTIONS. Idempotentes: los anteriores **más** PUT y DELETE. POST es el único método típico que NO es idempotente.

- HTTP/1.1 no tenía método PUSH y se suplió con un API.
- **Cabecera ETag**: contiene un código hash. Es una validación de caché que sirve para comprobar si el recurso que tengo en caché es el mismo que está en el servidor y así me evito descargarlo. Con `If-None-Match: ... hash`, si tengo la última versión, el servidor me devolverá el código **304**.

### 2.4 WebDAV

Es un *plugin*, una extensión de verbos HTTP para tratar el espacio de URL como si fuese un sistema de ficheros remoto (≈ FTP). Verbos: `MKCOL` (crea directorios), `MOVE` (mueve un recurso de una URI a otra), `COPY`, `LOCK`, `UNLOCK`.

### 2.5 Headers

| Request (las genera el navegador) | Response (las genera el servidor web) |
|---|---|
| `Authorization: BASIC Qxe32ba...` (ya viene implementada en Apache) | `Cache-control: max-age=3600` |
| `Cache-control: no-cache` | `Content-disposition: attachment; filename=...` |
| `Accept: text/html` (tipos MIME que el navegador sabe tratar) | `Content-Encoding: gzip` |
| `Accept-Charset: utf-8` | `Content-Length:` (del body) |
| `Accept-Language: es-ES` (idioma del navegador) | `Content-Range: bytes 21010-47021/47022` |
| `Accept-Encoding: gzip, deflate` (algoritmos de compresión que acepta el navegador) | `Date:` (fecha del fichero) |
| `Content-Type:` (tipo MIME del body) | `Location: url` (indica al navegador la url a la que debe redirigirse) |
| `Content-Length:` (longitud del body) | `Last-Modified:` |
| `Cookie:` (todas las del dominio; el navegador manda todas en cada petición, aunque el servidor no las pida) | `Transfer-Encoding: chunked` (gzip, etc.) |
| `Date:` | `WWW-Authenticate: Basic` |
| `Host: www.loquesea.com` (por si un servidor da servicio a varios dominios) | `Server:` (identifica al servidor. Ejemplo: Nginx) |
| `Range: bytes=500-599` | `Access-Control-Allow-Origin: *` (dominio). El CDN permite a cualquiera hacer peticiones. Podríamos filtrar por dominio |
| `Connection: keep-alive` | `Set-Cookie: <nombre_cookie> = <valor-cookie>` |
| `User-Agent:` (identifica al browser) | |
| `Access-Control-Request-Method: GET` | |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> La cabecera `Host` es la que permite que un mismo servidor sirva varios dominios en la misma IP: es el equivalente a nivel HTTP de lo que el SNI resuelve a nivel TLS. Ver [[VirtualHost (Apache)]] y [[SNI (Server Name Indication)]].

### 2.6 Seguridad en HTTP

| Mecanismo | Qué es (PDF) |
|---|---|
| Autenticación BASIC | No está cifrada, solo codificada. Errores 401 y 403 para autenticación |
| Política CORS | Si el navegador detecta una redirección, pregunta al destino si puede acceder a ese recurso viniendo de ese origen. Si el destino dice que no, el navegador corta la redirección. A la acción de preguntar se le llama **preflight**. Va por recurso. Error 405 (método no permitido). Ejemplo: el navegador envía `Access-Control-Request-Method: GET` (método que quiero realizar) y el destino responde `Access-Control-Allow-Methods: GET, HEAD` (métodos permitidos) |
| Técnica HSTS | Se fuerza al navegador a ir por HTTPS. Cabecera `Strict-Transport-Security:`. Error 301 (para mover de http a https) |
| Técnica CSP | Más avanzada y restrictiva que CORS. Protege frente a *cross site scripting*. Cabecera `Content-Security-Policy:`. Contenido separado por ";". `self` indica que ese recurso solo puedes descargarlo del origen. Autentificas orígenes de descarga. Va por tipo de recurso (`*-src`): `script-src`, `image-src`, `style-src`, etc. |

> [!important] CORS vs CSP
> CORS: el navegador pregunta al destino (preflight) si un origen puede acceder a un recurso; va **por recurso**. CSP: más avanzada y restrictiva, protege frente a XSS autenticando los orígenes de descarga; va **por tipo de recurso** (`script-src`, `image-src`, `style-src`...).

---

## 3. Códigos de respuesta

| Familia | Significado | Códigos del PDF |
|---|---|---|
| 100 | Informativos | — |
| 200 | Éxito | **200** OK típico. **201** Created: se ha creado un nuevo recurso (ejemplo PUT). **202** Accepted: recibido pero no procesado (ejemplo procesos batch) |
| 300 | Redirecciones | **301** movido permanentemente. **302** movido temporalmente. **304** no se ha modificado desde la última request |
| 400 | Problemas con la solicitud del cliente | **400** Bad Request. **401** No autorizado: requiere autenticación al cliente y muestra pop-up de usuario y contraseña; el servidor no sabe quién eres y debes identificarte. **403** Prohibido: el usuario no tiene permiso y no puede entrar. **404** Not Found. **405** Método no permitido (por ejemplo, solo puedes hacer GET y estás haciendo POST). **413** Request/Body muy grande (ejemplo: fichero demasiado grande para que lo procese el servidor) |
| 500 | Error o problema al procesar la solicitud en el servidor. Fallo interno del servidor | **500** Internal Error (genérico). **502** Bad Gateway. **503** Servicio no disponible |

> [!tip] 401 vs 403
> 401 = "no sé quién eres, identifícate" (pop-up de usuario y contraseña). 403 = "sé quién eres, pero no tienes permiso".

---

## 4. HTTP/2 y HTTP/3

### 4.1 HTTP/2

Fue una revisión en profundidad de HTTP/1.1, pero no se hizo de cero, sino que derivó de **SPDY**, un protocolo de Google (SPDY fue la antesala de HTTP/2).

- Usa **una única conexión TCP** para realizar múltiples solicitudes.
- **Compresión de headers** por defecto.
- **Priorización de flujos**.
- No requiere TLS, ya que lo lleva implementado "en sus tripas".
- Es **binario**, ya no es modo carácter.
- **Server PUSH**: similar al API de HTML5 *Server Sent Event* (SSE) o WebSocket que usaba HTTP/1.1.
- **Multiplexación**: sobre varias request (img, js, css) se genera una única response con todo. Optimiza el ancho de banda.
- **Frame**: unidad mínima de intercambio. Tipos importantes: DATA y HEADERS.
- **Stream**: es una secuencia de frames.

Diagrama del PDF: entre el cliente (navegador) y el servidor hay una única conexión TCP con una capa de *HTTP/2 Framing Layer* en cada extremo. Las requests (GET /styles.css, GET /script.js, GET /image.jpg) viajan como streams distintos (Stream 5, 7, 9...) intercalados en esa conexión, y las responses (headers y body de cada stream) vuelven también intercaladas por la misma conexión.

### 4.2 HTTP/3

- La semántica sigue existiendo.
- Aspectos nuevos: control de flujo, flujo, priorización, técnica PUSH.
- El gran cambio es que HTTP/3 va sobre el protocolo **QUIC**, que va sobre **UDP**.

| Versión | Transporte | Formato | Rasgos clave |
|---|---|---|---|
| HTTP/1.1 | TCP | Carácter | Sin estado, petición-respuesta, sin PUSH |
| HTTP/2 | TCP (única conexión) | Binario | Derivado de SPDY, multiplexación, compresión de headers, TLS integrado (no requerido), Server PUSH |
| HTTP/3 | QUIC sobre UDP | — | Misma semántica; control de flujo, priorización, PUSH |

---

## 5. SSL/TLS

SSL/TLS (versiones TLS 1.2 y TLS 1.3) se usa para cifrar un canal HTTP (HTTPS), FTP (FTPS), email (SMTP, IMAP, POP3), LDAP (LDAPS), etc.

### 5.1 Las tres dimensiones de la seguridad

La criptografía sirve para asegurar la **Confidencialidad, Integridad y Autenticidad**, que son las dimensiones de la seguridad que se pueden asegurar respecto a un activo de tipo información.

| Dimensión | Qué garantiza |
|---|---|
| Confidencialidad | El secreto, el cifrado de la información |
| Integridad | Que nadie ha modificado la información en el transcurso de la comunicación. No busca saber si el contenido es bueno, sino si ha llegado bien |
| Autenticidad | La autoría: que quien te manda la información es quien dice ser |

Relacionado: [[No repudio (irrenunciabilidad)]] (no repudio como propiedad adicional de la firma).

### 5.2 Arquitectura de subprotocolos

Pila: HTTP / SSL-TLS / TCP / IP. SSL/TLS se compone de:

| Capa | Contenido |
|---|---|
| Higher-Layer Subprotocols | *Change Cipher Spec* (20), *Alert* (21), *Handshake* (22: fases), *Application Data* (23) |
| TLS Record Subprotocol | Encargada de **cifrar, comprimir y generar MAC** (CIA). Se indica qué se transporta: 20, 21, 22 o 23 |

Fases del Handshake: *Client-hello*, *Server-hello*, *Client-key-exchange* y *Finished*; con el intercambio de la **pre-master** y la generación del **master secret**.

### 5.3 Handshake de SSL/TLS

Este flujo es para **autentificar al servidor**. *Mutual Authentication* es cuando el servidor te pide elegir tu propio certificado. **El objetivo del Handshake es generar una clave simétrica.**

| Paso | Trama | Contenido |
|---|---|---|
| 1 | Cliente → Servidor: `client-hello` | Versión SSL, nº aleatorio, extensiones. Lista de *cipher suites*: lista de algoritmos de cifrado que el cliente sabe manejar (simétrico para cifrar el canal, asimétricos para cifrar la clave simétrica y el algoritmo para calcular la MAC) |
| 2 | Servidor → Cliente: `server-hello` | *Cipher suite* elegida (ejemplo: `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA_256`), certificado del servidor, nº aleatorio, Session ID, lista de CA que reconoce, extensiones. Se valida el certificado del servidor |
| 3 | Cliente → Servidor: intercambio PRE-master | Clave *pre-master* cifrada con la clave pública del servidor |
| 4 | Generación del *master secret* | Servirá para generar la clave simétrica de sesión |
| 5 | `Finished` | Cliente y servidor ya tienen la clave simétrica y se puede cifrar el canal |

> [!important] Por qué funciona
> Como en el certificado del servidor viene la clave pública, el cliente puede mandar cifrada la clave simétrica y solo el servidor podrá descifrarla con su clave privada. Ver [[Criptografía asimétrica (clave pública y privada)]] y [[Certificado TLS-SSL (X.509)]]. Para servir varios certificados en una misma IP: [[SNI (Server Name Indication)]].

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Lectura de la cipher suite del ejemplo: `ECDHE` = intercambio de clave (Diffie-Hellman de curva elíptica efímero), `RSA` = algoritmo de autenticación/firma, `AES_128_GCM` = cifrado simétrico del canal, `SHA_256` = función hash usada. Ver [[Diffie-Hellman]].

### 5.4 Vulnerabilidades de SSL/TLS

Lista del PDF (solo se citan los nombres):

- Ataque de renegociación
- Ataque de reversión de versiones
- Ataque BEAST
- Ataques CRIME
- Ataques BREACH
- Ataque Logjam
- Ataque POODLE
- Ataque de truncamiento

---

## 6. Algoritmos criptográficos

| Tipo | Características (PDF) | Algoritmos |
|---|---|---|
| Simétricos (C) | Una sola clave para cifrar y descifrar. Muy eficientes, rápidos computacionalmente. Usados para cifrar cosas grandes. Problema de distribución de la clave | 3DES, RC5, IDEA, AES |
| Asimétricos (C) | Usan 2 claves. Lo que se hace con una se deshace con la otra: si cifras con la clave pública, descifras con la privada y al revés. Son lentos: no podemos usarlos para cosas grandes ni para cifrar un canal de comunicaciones. No distribuye claves | RSA, DSA, DH (para intercambio de clave simétrica), EC (Curva Elíptica: modifica parte del algoritmo de RSA, DSA y DH) y ElGamal |
| MIC / HMAC | Generan un código pequeño de un documento o mensaje | SHA-1, SHA-2, SHA-3, MD5 |

- Tamaño del resumen: **SHA-1 (160 bits)**, **SHA-256 (256 bits)**, **SHA3-512 (512 bits)**, **MD5 (128 bits)**.
- **MIC** (Código de Integridad del Mensaje): genera un resumen (hash) del mensaje. Integridad (I): hash solo del mensaje. Ver [[Función hash criptográfica]].
- **MAC/HMAC** (Código de Autenticación del Mensaje / MAC basado en HASH): necesita mensaje **y clave** para asegurar autenticidad (IA).

> [!tip] Siglas del PDF
> (C) = Confidencialidad, (I) = Integridad, (A) = Autenticidad. MIC = I; MAC/HMAC = I + A; firma digital = I + A.

### 6.1 Firma digital

El emisor entrega al receptor el documento y una información adicional que resulta de **cifrar (C) con la clave privada del emisor (A) el hash calculado del documento (I)**. Busca garantizar la Integridad y la Autenticación. El receptor puede comprobar la Autenticidad con la clave pública del emisor. Ver [[Firma electrónica vs Sello electrónico]].

### 6.2 Sistemas híbridos (SSL y PGP)

La clave simétrica se intercambia de forma asimétrica (por ejemplo con DH, ya que la clave es pequeña). Así se soluciona el problema de intercambio de clave. Luego se cifra el canal de forma simétrica (por ejemplo con AES, ya que el canal es grande).

---

## 7. Certificados X.509v3

Pueden emitirse para un **servidor (dominio)** o para una **persona** (física o jurídica). Es un documento expedido y firmado por una **Autoridad de Certificación (CA)**. En la legislación española se conocen como **PSC (Prestador de Servicios de Confianza)**. Ver [[Certificado TLS-SSL (X.509)]] y [[Autoridad de Certificación vs Autoridad de Validación]].

> [!note] Errata aplicada (Actualizaciones, 14/05/2025)
> El estándar de los certificados X509v3 es el **PKCS#12** y no "PCKS#12". El PDF ya lo trae correcto.

### 7.1 Extensiones de fichero

| Extensión | Contenido |
|---|---|
| `.cer` | Solo parte pública |
| `.pem` | Formato de exportación en Base64 |
| `.pfx` y `.p12` | Formato binario. Protegido con contraseña. Parte pública y clave privada. Estándar PKCS#12 |

Ver [[Codificaciones de certificados X.509 (PEM, DER, PKCS7, PKCS12)]] y [[p12-pfx vs cer (certificado con-sin clave privada)]].

### 7.2 Campos más importantes

| Campo | Contenido (PDF) |
|---|---|
| Versión | — |
| Número de serie | — |
| Id del algoritmo usado por la CA para firmar | — |
| Emisor | CA que lo emite. No todos los navegadores reconocen todas las CA |
| Validez | — |
| Sujeto | Para quién se emite. Dominio. **SAN** (*Subject Alternative Name*): se expide para un dominio principal y otros dominios asociados. **Wildcard**: se expide para un dominio y todos sus subdominios, como `*.loquesea.com`. Ejemplo: loquesea.com, correo.loquesea.com, ftp.loquesea.com, etc. |
| Algoritmo de la clave pública del sujeto | — |
| Clave pública del sujeto | — |
| Firma digital | Creada por la CA. Se hace un hash de todo lo anterior (I) y luego se cifra (C) con la clave privada de la CA para asegurar la autenticidad (A) de la CA |

### 7.3 Formatos y versiones de firma admitidos con las Administraciones Públicas

El portal **Valide** y la aplicación **@Firma** permiten la firma de documentos electrónicos en los formatos XAdES, CAdES y PAdES. Ver [[@Firma]], [[AutoFirma]], [[CAdES, XAdES y PAdES (formatos de firma avanzada)]] y [[Perfiles de firma AdES (BES a A)]].

| Formato | Uso (PDF) |
|---|---|
| XAdES | Ficheros de tamaño pequeño (hasta 4 MB) |
| CAdES | Ficheros de tamaño grande (a partir de 4 MB) |
| PAdES | Para ver la información de tu firma y el contenido una vez firmado (PDF) |

### 7.4 Proceso de verificación de un certificado de servidor

1. Se comprueba la **validez**.
2. Se comprueba que ha sido **emitido para el dominio** desde el que nos lo hemos descargado.
3. Se verifica que está **bien firmado** (I+A).
4. Se comprueba que la **CA** la tenemos registrada en los **almacenes de confianza** (Chrome tira del de Windows, pero Firefox, Adobe, etc. tienen los propios).
5. Se comprueba el **estado de revocación** con **OCSP** (protocolo online en base al número de serie) o **CRL** (se descarga la lista de certificados revocados de la CA). Ver [[OCSP frente a CRL]].

---

## 8. Java y los almacenes de confianza

- Java **no** tira de los almacenes de confianza de Windows.
- Fichero con CA de confianza por defecto: `JAVA_HOME/jre/lib/security/cacerts` (password `changeit`).
- Almacenes específicos: formato **JKS** (*Java Key Store*). Se leen con la herramienta gráfica **KeyStore Explorer**. Similar a `.cer`, `.pem`, `.pfx`, `.p12`.
- Herramienta del JDK para crearlos, etc.: **`keytool`**, herramienta de línea de comandos parecida a **OpenSSL** (para tener SSL en Linux).
- Librerías de terceros de criptografía: **BouncyCastle**.

| Propiedad del sistema | Significado |
|---|---|
| `javax.net.ssl.KeyStore` | Almacén (path) del JKS con la clave privada |
| `javax.net.ssl.KeyStorePassword` | Contraseña de ese almacén |
| `javax.net.ssl.trustStore` | Almacén JKS con CA adicionales en las que se confía |
| `javax.net.ssl.trustStorePassword` | Contraseña de ese almacén |
| `javax.net.debug = all` | Depuración |

---

## 9. Estándares PKCS (Public-Key Cryptography Standards)

| PKCS | Nombre | Comentarios (PDF) |
|---|---|---|
| PKCS#1 | RSA | Define el formato del cifrado RSA |
| PKCS#3 | Intercambio de claves Diffie-Hellman | Establecer conjuntamente una clave secreta compartida, usando un canal |
| PKCS#5 | Cifrado basado en contraseñas | — |
| PKCS#7 | Sintaxis del mensaje criptográfico | Usado para firmar y/o cifrar mensajes en PKI. Usado para diseminar certificados. Base para el estándar S/MIME, actualización del estándar CAdES. **Clave Pública** |
| PKCS#8 | Sintaxis de la información de clave privada | — |
| PKCS#10 | Solicitud de certificación | Formato de mensajes enviados a una Autoridad de Certificación para solicitar certificación de clave pública |
| PKCS#11 | Interfaz de dispositivo criptográfico (*Cryptographic Token Interface* / cryptoki) | Define un API genérico de acceso a dispositivos criptográficos |
| PKCS#12 | Sintaxis de intercambio de información personal | Define un formato de fichero usado comúnmente para almacenar claves privadas con su certificado de clave pública protegido mediante clave simétrica. **Clave Privada** |
| PKCS#13 | Criptografía de curva elíptica | — |
| PKCS#15 | Formato de información de dispositivo criptográfico | Permite a los usuarios de dispositivos criptográficos identificarse con aplicaciones independientemente de la implementación del PKCS#11 cryptoki u otro API |

> [!important] PKCS#7 vs PKCS#12
> PKCS#7: mensajes firmados/cifrados y diseminación de certificados (**clave pública**, base de S/MIME y CAdES). PKCS#12: fichero con la **clave privada** más su certificado, protegido por contraseña (`.pfx`/`.p12`).

---

## 🔑 Resumen ultra-rápido

- Internet: Tier-1 (backbone, carriers, internacional), Tier-2 (nacional, tránsito con Tier-1), Tier-3 (local, ISP). Peering entre iguales gratis; tránsito entre niveles de pago. BGP entre AS, IGP dentro; ASN lo da IANA-RIR. IXP (nivel 2, neutro, cooperativas: ESPANIX, CATNIX, DE-CIX); CDN (Akamai, Cloudflare, CDNJS) enganchados a IXP.
- HTTP/1.1: sin estado (cookies), orientado a carácter como FTP/SMTP/POP3, petición-respuesta. URI = URL (localizar) + URN (identificar).
- Seguros: GET, HEAD, TRACE, OPTIONS. Idempotentes: esos + PUT + DELETE. POST no es idempotente. PATCH = PUT parcial. CONNECT = túnel HTTPS vía proxy.
- ETag + If-None-Match: si coincide, 304. WebDAV: MKCOL, MOVE, COPY, LOCK, UNLOCK.
- Seguridad HTTP: BASIC (codificada, no cifrada), CORS (preflight, por recurso), HSTS (`Strict-Transport-Security`, fuerza HTTPS), CSP (`Content-Security-Policy`, anti-XSS, por tipo de recurso `*-src`).
- Códigos: 200/201/202; 301/302/304; 400/401/403/404/405/413; 500/502/503. 401 = identifícate; 403 = prohibido.
- HTTP/2: deriva de SPDY, una conexión TCP, binario, multiplexación, compresión de headers, Server PUSH, frame (DATA/HEADERS) y stream. HTTP/3: sobre QUIC/UDP.
- TLS (1.2 y 1.3): Confidencialidad, Integridad, Autenticidad. Subprotocolos 20 (Change Cipher Spec), 21 (Alert), 22 (Handshake), 23 (Application Data). Handshake: client-hello, server-hello (+certificado), pre-master cifrada con clave pública del servidor, master secret, Finished; objetivo = clave simétrica.
- Simétricos (3DES, RC5, IDEA, AES): rápidos, problema de distribución. Asimétricos (RSA, DSA, DH, EC, ElGamal): lentos, no para canales. Híbrido = DH/asimétrico para la clave + AES para el canal.
- Hash: SHA-1 160, SHA-256 256, SHA3-512 512, MD5 128 bits. MIC = I; HMAC = I + A (con clave). Firma digital = hash cifrado con clave privada del emisor.
- X.509v3: `.cer` (público), `.pem` (Base64), `.pfx`/`.p12` (binario, con privada, PKCS#12). SAN (varios dominios) vs Wildcard (`*.dominio`). XAdES (<= 4 MB), CAdES (>= 4 MB), PAdES (PDF).
- Verificación de certificado: validez, dominio, firma, CA en almacén de confianza, revocación (OCSP por nº de serie / CRL).
- Java: `cacerts` (password `changeit`), JKS, `keytool`, KeyStore Explorer, BouncyCastle, propiedades `javax.net.ssl.*`.
- PKCS: #1 RSA, #3 DH, #5 contraseñas, #7 mensaje (público, S/MIME), #8 clave privada, #10 solicitud, #11 cryptoki, #12 intercambio personal (privada), #13 curva elíptica, #15 formato de dispositivo.

---

## Conexiones con otros temas

- [[B4 - T1.2 ADMON SSOO - SSH]]: SSH usa también criptografía asimétrica, pero para autenticar sesiones de administración; TLS cifra tráfico de servicios.
- [[B4 - T1.3 ADMON SSOO - APACHE]]: configuración de certificados TLS en el servidor web y VirtualHost; [[SNI (Server Name Indication)]].
- [[Certificado TLS-SSL (X.509)]] · [[Criptografía asimétrica (clave pública y privada)]] · [[Diffie-Hellman]] · [[Función hash criptográfica]] · [[OCSP frente a CRL]].
- Bloque 1 (firma y certificados con las AAPP): [[@Firma]], [[AutoFirma]], [[CAdES, XAdES y PAdES (formatos de firma avanzada)]], [[Firma electrónica vs Sello electrónico]].
