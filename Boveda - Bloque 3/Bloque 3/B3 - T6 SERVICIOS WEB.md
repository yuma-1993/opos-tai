---
tags:
  - bloque3
  - tema6
  - servicios-web
  - soap
  - wsdl
  - rest
  - graphql
  - grpc
  - soa
  - esb
  - jax-ws
  - jax-rs
  - jwt
  - oauth
  - integracion
bloque: 3
tema: "6"
titulo: "Servicios web: SOAP/WSDL/UDDI, WS-Security, REST (HATEOAS, JWT, JAX-RS), GraphQL, gRPC, SOA y ESB"
estado: por-repasar
---

# Tema 6 · Bloque 3 — Servicios web

> [!abstract] De qué va este tema
> Cuando las funcionalidades de una aplicación se reparten entre máquinas, hacen falta mecanismos para invocarlas a distancia: primero RPC/CORBA/RMI/DCOM, hoy los servicios web. El tema compara los estilos actuales (SOAP+WSDL con estándares W3C/OASIS, REST, GraphQL y gRPC), detalla SOAP/WSDL/WS-Security y las anotaciones de JAX-WS y JAX-RS, la seguridad REST (OAuth, JWT) y cierra con la arquitectura SOA y el bus ESB que integran servicios.

> [!tip] Cómo estudiarlo
> Hay un único esquema que ordena todo: qué estándar/estilo es, quién lo creó, qué formato usa (XML, JSON, binario) y cuántos *endpoints* tiene. Ver la tabla comparativa de la sección 2 y la de cierre.

---

## 1. Historia

Se distribuyen las funcionalidades de las aplicaciones entre diferentes máquinas. Antes todo estaba en una sola máquina.

| Tecnología | Qué es |
|---|---|
| **RPC** | Remote Procedure Call. Va sobre TCP |
| **CORBA** | Common Object Request Broker Architecture. Cliente Java → **ORB** → Servidor C++. Producto: **Orbix**. (Concepto de intermediario: [[Broker Pattern]]) |
| **RMI** | Remote Method Invocation. Cliente Java → JRE → Servidor Java |
| **DCOM** | Distributed Component Object Model. **De Microsoft** |

---

## 2. Servicios: los cuatro estilos

| Estilo | Origen / estándar | Formato | Endpoints | Notas |
|---|---|---|---|---|
| **WSDL + SOAP** | Estándares de la **W3C** | **XML** | **Único** endpoint | |
| **REST** | **No** estándar | **HTTP + JSON** | **Múltiples** endpoints | RESTful API. La misma API para todo el mundo |
| **GraphQL** | De **Facebook** | | **Único** endpoint | Permite a cada cliente especificar la petición de datos |
| **gRPC** | De **Google** | | | Es como RPC sobre HTTP. Busca el **rendimiento** |

---

## 3. Estándares de la W3C y OASIS

La **WS-I Basic Profile** (WebService Interoperability) es una especificación fundamental. Define **3 lenguajes, 3 documentos**:

| Documento | Para qué | Detalles |
|---|---|---|
| **WSDL** | Descripción de servicios | Ver sección 4 |
| **UDDI** | Registro de servicios | Es de **OASIS**, no de la W3C. **No se usa**. **JAXR** es el API de Java para conectarte a un servicio UDDI |
| **SOAP** | Protocolo basado en XML sobre HTTP | Un documento SOAP es un documento XML. **JAX-WS** es el API de Java para crear e invocar servicios SOAP (AXIS2, CXF, JbossWS, Metro (GlassFish)). Solo con anotaciones se definen los servicios. Todo en Java, no se toca nada de XML |

Las tres "páginas" de UDDI:

| Páginas | Contenido |
|---|---|
| **Blancas** | Información de contacto |
| **Amarillas** | Categorización |
| **Verdes** | Información técnica de acceso al servicio |

### Otras recomendaciones importantes

#### WS-Security

La WS-I Basic Profile **no incluye nada de seguridad**. **OASIS** creó este estándar, que consiste en una **cabecera en el mensaje SOAP**:

- **Firmar** mensajes SOAP (**XML Signature**; ver [[XMLDSIG]]).
- **Cifrar** mensajes SOAP (**XML Encryption**).
- **Autenticación del cliente**:
  - `UsernameToken`: para mandar credenciales.
  - `BinarySecurityToken`: para mandar certificados **X509**, **SAML Token**, **Kerberos Ticket**, etc. (sobre los certificados X.509: [[Certificado TLS-SSL (X.509)]] y [[Codificaciones de certificados X.509 (PEM, DER, PKCS7, PKCS12)]]).

#### MTOM

Para **envío de datos binarios**. Incluido en la **v1.2 de la WS-I BP**. Usa **MIME** (`application/xop+xml`; ver [[Tipo MIME]]). El servicio web es **liviano**, ya que el archivo binario va por **fuera**, por HTTP, y **Apache** sí está preparado para gestionar elementos pesados.

> [!important] Qué es de quién
> W3C: WSDL y SOAP. **OASIS**: UDDI y WS-Security. WS-I Basic Profile: el conjunto de los tres documentos (WSDL, UDDI, SOAP); MTOM va en su v1.2.

---

## 4. WSDL

Definición del servicio. Se **genera automáticamente en XML a partir del código del servicio**.

| Elemento | Qué define | Etiqueta |
|---|---|---|
| **types** | Definición de los tipos usados en los mensajes. **XSD** | `<wsdl:types>` |
| **message** | Definición de las entradas y salidas de las operaciones. Antes se definen sus tipos | `<wsdl:message…` |
| **portType / interface** | Asocia mensajes con operaciones. Antes mensajes | `<wsdl:operation>` dentro de `<wsdl:portType…` |
| **binding** | Define los **protocolos de comunicación** usados. `transport="https://schemas.xmlsoap.org/soap/http"`. También podría ir sobre **smtp** | `<wsdl:binding…` |
| **service** | Conjunto de puertos y direcciones de acceso. **EndPoint** | `<wsdl:service…` |

- La **versión 2.0** da soporte para **REST** (WSDL sirve para documentar y definir un servicio REST).
- En la 2.0 **`portType` pasa a llamarse `interface`**.

> [!example] Diagrama WSDL 1.1 vs 2.0 (del PDF)
> | | WSDL 1.1 | WSDL 2.0 |
> |---|---|---|
> | Raíz | `definitions` | `description` |
> | Sección **abstracta** | `types`, `message`, `portType` (operation → input/output) | `types`, `interface` (operation → input/output) |
> | Sección **concreta** | `binding`, `service` (port) | `binding`, `service` (endpoint) |
>
> En 1.1 existe el elemento `message`; en 2.0 desaparece como sección propia y `portType` se llama `interface`. El `port` del `service` pasa a `endpoint`.

> [!tip] Truco
> Orden de lectura de un WSDL: **T**ypes → **M**essage → **P**ortType → **B**inding → **S**ervice (de lo abstracto a lo concreto).

> [!note] Ampliación (conocimiento general, no viene del PDF)
> La división del diagrama en "sección abstracta" (qué hace el servicio: types, message, portType) y "sección concreta" (cómo y dónde se accede: binding, service) es la forma habitual de describir un WSDL, y es coherente con el esquema del PDF.

### Ejemplo en .NET: Calculator

- `http://dneonline.com/calculator.asmx`: la extensión **`.asmx`** indica que es un WS de **.NET**. El motor ASP.NET ofrece **documentación automática** de un WS (la página lista las operaciones: *Add*, *Divide*, *Multiply*, *Subtract*).
- `http://dneonline.com/calculator.asmx?wsdl`: se indica `?wsdl` para poder ver el XML correspondiente al documento WSDL.
- Los WSDL los crea el motor de WS **automáticamente a partir del código fuente**.
- Hay una etiqueta **`operation`** por cada servicio: `<wsdl:operation name="Add">`.
- El WSDL de ejemplo declara en `wsdl:types` (XSD) elementos como `Add` (con `intA` e `intB`, tipo `s:int`), `AddResponse` (`AddResult`), `Subtract`, `SubtractResponse`, `Multiply`...
- La página recomienda cambiar el namespace por defecto (`http://tempuri.org/`) antes de hacer público el servicio; se hace con el atributo `WebService` y su propiedad `Namespace` (en C#, VB y C++).

Más sobre servicios SOAP en .NET: [[B3 - T5.3 .NET]].

---

## 5. SOAP

- Basado en **XML**. Realiza las peticiones por **HTTP con POST** y genera las respuestas por HTTP con códigos **200** o **500**.
- Los servicios web SOAP **siempre se invocan con POST**, por definición, ya que mandamos cuerpo del mensaje. Un GET no tiene body.

### Petición

```xml
POST /endpoint HTTP/1.1
Host: …
Content-type: application/soap+xml
SOAPAction: url

<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/...">
  <soap:Header>
    <wsse:Security soap:actor="http://www.gob..." xmlns:wsse="http://docs.oasis-open.org/....xsd" xmlns:wsu="http://....xsd" xmlns:soapenv="http://...">
      <wsse:Username>
        <xenc:EncryptedData>…</xenc:EncryptedData>
      </wsse:Username>
      <wsse:Password>
        <xenc:EncryptedData>…</xenc:EncryptedData>
      </wsse:Password>
    </wsse:Security>
  </soap:Header>
  <soap:Body>
    <m:GetStockPrice> … </m:GetStockPrice>
  </soap:Body>
</soap:Envelope>
```

### Respuesta con error

```xml
<soap:Envelope xmlns:soap="http://www.w3c.org/...">
  <soap:Body>
    <soap:Fault>
      <faultcode>soap:Server</faultcode>
      <faultstring>Error interno en el servidor</faultstring>
      <detail>
        <ns3:errorInfo xmlns:ns3="urn:…" xmlns:ns2="urn:…">
          <code>500</code>
          <description>Error interno en el servidor</description>
        </ns3:errorInfo>
      </detail>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
```

| Parte del mensaje SOAP | Contenido |
|---|---|
| `soap:Envelope` | Documento XML raíz |
| `soap:Header` | Cabecera. Aquí va la seguridad **WS-Security** (`wsse:Security`, con `Username` y `Password` cifrados con `xenc:EncryptedData`) |
| `soap:Body` | Cuerpo: la operación (ej. `m:GetStockPrice`) o, en error, el `soap:Fault` (`faultcode`, `faultstring`, `detail`) |

Otras definiciones del PDF:

- **`wsse`** es un *namespace*, un prefijo.
- **XSD** (XML Schema Definition): lenguaje de esquema usado para describir la estructura y las restricciones de los contenidos de los documentos XML de una forma muy precisa.
- **SwagerHub** (sic en el PDF) es un **API manager**, para poder gobernar y gestionar todas nuestras APIs.

---

## 6. Cliente SOAP en Java y herramientas

- Parte cliente en Java: herramienta **`wsimport`**, que crea los `.java` y los `.class` a partir de un WS ya publicado.

```bash
wsimport -d . -p es.igae.calculadora.cliente -keep url_del_wsdl?WSDL
```

  `calculator.java` será la clase principal para llamar a los métodos. Dentro estarán las anotaciones **`@WebServiceClient`**.
- **SoapUI**: herramienta para hacer **pruebas** de WS ya implementados. Crea un *request* de ejemplo en base al WSDL. Hace la parte cliente.

### Principales anotaciones JAX-WS

| Anotación | Dónde / para qué | Propiedades |
|---|---|---|
| **`@WebService`** | Especifica que la clase que la contiene ha de convertirse en un servicio web | `name` (por defecto nombre de la clase; equivale a `wsdl:portType`) · `targetNamespace` (namespace del servicio) · `serviceName` (nombre del servicio; equivale a `wsdl:service`; por defecto nombre de la clase + sufijo "Service") · `endpointInterface` (nombre del endpoint; permite desligar la interfaz de la implementación) · `portName` (nombre del puerto; equivale a `wsdl:portName`; por defecto nombre del servicio web + sufijo "Port") · `wsdlLocation` (ya no se usa en JAX-WS 2.0) |
| **`@WebMethod`** | Sobre un método: expone esa operación en el servicio web | `operationName` (por defecto el nombre del método) · `action` (el espacio de nombres de la operación) · `exclude` (a `true` excluye la operación del servicio) |
| **`@WebParam`** | Dentro de los parámetros de un método: personaliza el mapeo de un parámetro concreto entre el dato expuesto en el servicio y el tipo Java | `name` (nombre del parámetro expuesto) · `targetNamespace` |
| **`@WebResult`** | Sobre un método: personaliza el mapeo del resultado | `name` · `targetNamespace` |
| **`@RequestWrapper`** | En la cabecera de un método: indica la clase Java que mapea la petición del WS para ese método | `localName` (nombre de la operación tal como estará en el WSDL generado) · `targetNamespace` · `className` (clase Java que encapsula la petición) |

> [!important] Equivalencias JAX-WS ↔ WSDL
> `@WebService(name)` = `wsdl:portType` · `serviceName` = `wsdl:service` (sufijo por defecto "Service") · `portName` = `wsdl:portName` (sufijo por defecto "Port").

---

## 7. REST

- **REST** es un **estilo de arquitectura para servicios hipermedia**. Nace de una **tesis doctoral**. Nada que ver con SOAP. **REST es la parte teórica**.
- La **API RESTful** es una interfaz que dos sistemas utilizan para intercambiar información de manera segura a través de Internet; es la **implementación de REST sobre HTTP**.

### Principios fundamentales

| Principio | Detalle |
|---|---|
| Cliente-Servidor **sin estado** | Como HTTP |
| Operaciones bien definidas | **Verbos HTTP + Recursos (URLs)** |
| Sintaxis para identificar recursos | **URI**. Entidades de negocio: nóminas, empleados, etc. |
| **Navegación hipermedia: HATEOAS** | *Hypermedias As The Engine Of Application State*. De un empleado no se devuelve todo, sino lo mínimo, y se ofrecen otros recursos para obtener el resto de datos (dirección, puesto, etc.). Si aparece `"links"` es que se está usando HATEOAS |

```json
{
  "departmentId": 10,
  "departmentName": "Administration",
  "locationId": 1700,
  "managerId": 200,
  "links": [
    {
      "href": "10/employees",
      "rel": "employees",
      "type": "GET"
    }
  ]
}
```

- **JAX-RS** es el API de Java para servicios REST (Apache CXF, Jersey, RESTeasy (JBoss), Restlet). Jersey, RESTeasy y Restlet están dentro de los servidores de aplicación (Weblogic, Websphere).
- Se crea un servicio para obtener información o para gestionar usuarios (altas/bajas/consultas), **mapeado con los verbos HTTP**.
- **Meter verbos en las URIs es mala práctica**. Va en contra de la teoría. Las URIs deben ser solo recursos. Ej.: `/borrar_usuario` no sería un recurso REST válido según la teoría. La realidad difiere.

### Ejemplos de URIs (las consultas son siempre GET)

| Petición | Resultado |
|---|---|
| `GET /users` | 200 + JSON con todos los usuarios |
| `GET /users/1` | Un usuario |
| `GET /users/1/direcciones` | Direcciones del usuario 1 |
| `PUT /users/123` + JSON (Body) | 200 (actualizado) o 201 (creado) o 40X (error) |
| `POST /users` + JSON (Body) | **No idempotente** (ver [[Idempotencia]]) |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> La nota [[Idempotencia]] define el concepto en el contexto de la gestión de configuración, pero la definición general (repetir la operación produce el mismo resultado que hacerla una vez) es la que explica por qué `PUT` sí es idempotente y `POST` no: repetir un `POST /users` puede crear usuarios duplicados.

### Documentación de APIs

**WADL, WSDL 2.0, RAML y Swagger/OpenAPI.**

### Seguridad REST

No hay seguridad específica. Se usa: **OAuth / JWT / HTTP Basic** (autenticación) y **TLS** (confidencialidad; ver [[B4 - T8 HTTP SSL TLS]]).

**OAuth / JWT**: autenticación **basada en token**. Mandas tu certificado o tus credenciales y te envían un token. Cabecera: `Authorization: Bearer xxxxxxx`.

| | OAuth | JWT (JSON Web Token) |
|---|---|---|
| Cabecera | `Authorization: Bearer 234j354mn645…` | `Authorization: Bearer Header.Payload.Signature` |
| El token | Es un número que **no significa nada** | Tiene una **estructura definida, un significado**. Codificado en **Base64** |
| Firma | | La clave solo la tiene el **servidor**; se genera un **HMAC** usando el algoritmo que se define en la cabecera (Header) y el resultado se mete en el campo **Signature** |
| Payload | | Metadatos, información **no sensible**, predefinidos o creados por nosotros (ej. el rol de una persona). Se llaman **claims/privilegios**, **estandarizados por IANA** |

Claims de ejemplo:

| Claim | Significado |
|---|---|
| `sub` | **Subject**. Identifica el objeto o usuario en nombre del cual fue emitido el JWT |
| `exp` | **Expiration time**. Marca temporal a partir de la cual el JWT **no** tiene que ser aceptado |
| `iat` | **Issued at**. Marca temporal en la que el JWT fue emitido |

Cada vez que un usuario manda una petición se manda el token para identificarse, ya que **no tiene estado** (es *stateless*).

### Principales anotaciones de JAX-RS

Para mapear una clase recurso (un POJO) como un recurso web:

| Anotación | Función |
|---|---|
| `@Path` | Ruta de acceso relativa para una clase recurso o método |
| `@GET`, `@PUT`, `@POST`, `@DELETE`, `@HEAD` | Tipo de petición HTTP de un recurso |
| `@Produces` | Tipos de medios MIME de **respuesta** |
| `@Consumes` | Tipos de medios de **petición** aceptados |

Para los parámetros, extraen información de la solicitud. Toman una clave que se utiliza para buscar el valor requerido:

| Anotación | Enlaza el parámetro a... |
|---|---|
| `@PathParam` | Un segmento de ruta |
| `@QueryParam` | El valor de un parámetro de consulta |
| `@MatrixParam` | El valor de un parámetro de matriz |
| `@CookieParam` | Un valor de cookie |
| `@HeaderParam` | Un valor de cabecera HTTP |
| `@FormParam` | Un valor de formulario |
| `@DefaultValue` | Valor por defecto para los enlaces anteriores cuando la clave no se encuentra |
| `@Context` | Devuelve el contexto del objeto (ej.: `@Context HttpServletRequest request`) |

---

## 8. GraphQL

- Lo desarrolló **Facebook**. Describes los datos en el servidor y **el cliente decide qué datos solicita**. **Único endpoint**.
- En PHP, un servidor GraphQL conocido es **Lighthouse**, que se integra con **Laravel** (framework para desarrollar apps en PHP).
- **Apollo Client**: librería de JS que permite tratar datos del servidor GraphQL.

| Concepto | Qué es |
|---|---|
| **Query** | Donde definimos las operaciones de **consulta** que se pueden realizar a nuestro servicio web |
| **Mutation** | Operaciones que **alteran** la información de nuestro servicio web |

## 9. gRPC

- Lo desarrolló **Google**. Usa **IDL** (implementaciones/interfaces), que es como WSDL.
- Basado en **Protocol Buffers o Protobuf** (definición del *message*, formato de intercambio de datos).
- Se manda en **formato binario sobre HTTP/2**, al estilo RPC.
- La comunicación entre **Kubernetes** y los contenedores se hace mediante gRPC. El servicio/estándar **CRI** está definido con esto.

---

## 10. Arquitectura SOA

La arquitectura orientada a los servicios (**SOA**) es un tipo de diseño de software que permite **reutilizar sus elementos** gracias a las interfaces de servicios que se comunican a través de una red con un lenguaje común. Se rige por los principios descritos en el **manifiesto SOA**. Ver [[SOA (arquitectura orientada a servicios)]].

- Es un **estilo de arquitectura de TI** que se apoya en la orientación a servicios. La **orientación a servicios** es una forma de pensar en servicios, su construcción y sus resultados.
- **Servicio**: representación lógica de una **actividad de negocio** que tiene un resultado de negocio específico.

> [!example] Diagrama SOA (del PDF)
> **SOA** se compone de: *Application frontend*, *Service*, *Service repository*, *Service bus*. Un **Service** se descompone en *Contract*, *Implementation* e *Interface*; la *Implementation* en *Business logic* y *Data*.

## 11. ESB (Bus de Servicio Empresarial)

Modelo de arquitectura de software que gestiona la **comunicación entre servicios web**. Actúa como **capa intermedia (middleware)** para comunicar los diferentes sistemas de una empresa. Ver [[ESB (Enterprise Service Bus)]], [[Middleware]] y [[Event-Bus Pattern]].

- El ESB **no ofrece una funcionalidad necesaria** en una empresa, pero **facilita las tareas de integración** entre diferentes sistemas que usan lenguajes, estándares y formatos de información distintos.
- Una de sus funciones será **recibir mensajes en diferentes estándares y transformarlos a otros distintos** para que sea posible el entendimiento entre los extremos.

> [!example] Diagrama ESB (del PDF)
> Un único bus (**ESB**) en el centro al que se conectan sistemas dispares: Redmine, Jira, WordPress, Twitter, Sage, SAP, Microsoft Dynamics, Facebook, Salesforce.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Una arquitectura de microservicios comparte con SOA la idea de dividir la funcionalidad en servicios, pero a otra escala; ver [[B4 - T3.3 MICROSERVICIOS]].

---

## Comparativa final de estilos

| | SOAP | REST | GraphQL | gRPC |
|---|---|---|---|---|
| Creador / estándar | W3C (estándar) | Tesis doctoral; estándar de facto | Facebook | Google |
| Formato | XML | JSON sobre HTTP | (el cliente elige los datos) | Binario (Protobuf) sobre HTTP/2 |
| Descripción | WSDL | WADL, WSDL 2.0, RAML, Swagger/OpenAPI | Query / Mutation | IDL (≈ WSDL) |
| Endpoints | Único | Múltiples | Único | |
| Verbo HTTP | Siempre POST | GET/PUT/POST/DELETE/HEAD | | |
| Java | JAX-WS | JAX-RS | | |
| .NET | `.asmx` + `[WebMethod]` | Web API (`ApiControler`) | | |
| Seguridad | WS-Security (OASIS) | OAuth / JWT / HTTP Basic + TLS | | |

---

## 🔑 Resumen ultra-rápido

- Historia: RPC (sobre TCP), CORBA (ORB, Orbix, Java↔C++), RMI (Java↔Java), DCOM (Microsoft).
- Estilos: WSDL+SOAP (W3C, XML, endpoint único) · REST (no estándar, HTTP+JSON, múltiples endpoints) · GraphQL (Facebook, el cliente elige datos, endpoint único) · gRPC (Google, RPC sobre HTTP/2 binario, rendimiento).
- WS-I Basic Profile = 3 documentos: WSDL (descripción), UDDI (registro; de OASIS; no se usa; JAXR; páginas blancas/amarillas/verdes), SOAP (XML sobre HTTP; JAX-WS: AXIS2, CXF, JbossWS, Metro).
- WS-Security (OASIS): cabecera SOAP; firmar (XML Signature), cifrar (XML Encryption), autenticar (UsernameToken, BinarySecurityToken: X509, SAML, Kerberos). MTOM: binarios, v1.2 de WS-I BP, MIME `application/xop+xml`, el archivo va fuera.
- WSDL (generado del código): types (XSD) → message → portType (interface en 2.0) → binding (protocolo; también smtp) → service (endpoint). WSDL 2.0 soporta REST.
- SOAP: siempre POST (GET no tiene body); respuesta 200 o 500; `Envelope` → `Header` (WS-Security) + `Body` (o `Fault`: faultcode, faultstring, detail). Cabeceras `Content-type: application/soap+xml` y `SOAPAction`.
- Herramientas: `wsimport` (cliente Java desde WSDL, `@WebServiceClient`), SoapUI (pruebas SOAP), Postman (REST), SwaggerHub (API manager).
- JAX-WS: `@WebService` (name=portType, serviceName=service +"Service", portName +"Port"), `@WebMethod`, `@WebParam`, `@WebResult`, `@RequestWrapper`.
- REST: estilo (teoría) de una tesis doctoral; RESTful = REST sobre HTTP. Sin estado, verbos + recursos (URI), HATEOAS (`links`). Sin verbos en las URIs. PUT 200/201/40X; POST no idempotente.
- Seguridad REST: OAuth (token opaco) / JWT (Header.Payload.Signature, Base64, HMAC con clave del servidor, claims IANA: sub, exp, iat) / HTTP Basic / TLS. Stateless: se manda el token en cada petición (`Authorization: Bearer`).
- JAX-RS: `@Path`, `@GET/@PUT/@POST/@DELETE/@HEAD`, `@Produces` (respuesta), `@Consumes` (petición), `@PathParam`, `@QueryParam`, `@MatrixParam`, `@CookieParam`, `@HeaderParam`, `@FormParam`, `@DefaultValue`, `@Context`. Implementaciones: CXF, Jersey, RESTeasy, Restlet.
- Documentación de APIs: WADL, WSDL 2.0, RAML, Swagger/OpenAPI.
- GraphQL: Query (consultar) y Mutation (alterar); Lighthouse (PHP/Laravel), Apollo Client (JS). gRPC: IDL ≈ WSDL, Protobuf, binario sobre HTTP/2; Kubernetes↔contenedores y CRI.
- SOA: estilo de arquitectura que reutiliza elementos mediante interfaces de servicio en red con lenguaje común (manifiesto SOA); servicio = actividad de negocio con resultado específico. ESB: middleware que integra sistemas heterogéneos y transforma mensajes entre estándares.
- .NET: SOAP `.asmx` (`WebService` + `[WebMethod]`, WCF), REST Web API (`ApiControler`, devuelve status codes).

**Conexiones con otros conceptos TAI:**
- [[B3 - T5.3 .NET]] — servicios SOAP (`.asmx`) y REST (Web API) en .NET.
- [[SOA (arquitectura orientada a servicios)]], [[ESB (Enterprise Service Bus)]], [[Middleware]], [[Broker Pattern]], [[Event-Bus Pattern]] — arquitectura de integración.
- [[XMLDSIG]] — firma XML usada en WS-Security.
- [[Certificado TLS-SSL (X.509)]] y [[B4 - T8 HTTP SSL TLS]] — certificados y TLS para la confidencialidad.
- [[Tipo MIME]] — tipos MIME en MTOM y en `@Produces`/`@Consumes`.
- [[Idempotencia]] — PUT frente a POST.
- [[B4 - T3.3 MICROSERVICIOS]] — evolución de la idea de servicios.
