---
tags:
  - bloque4
  - tema9
  - seguridad
  - redes
  - firewall
  - vpn
  - ipsec
bloque: 4
tema: 9
titulo: Seguridad en redes y VPN (cortafuegos, IDS/IPS, SIEM, VPN e IPSec)
estado: por-repasar
---

# Tema 9 · Bloque 4 — Seguridad en redes y VPN

> [!abstract] De qué va este tema
> Dos grandes bloques: la **seguridad perimetral** (tipos de cortafuegos, arquitecturas de referencia con DMZ, sistemas IDS/IPS/SIEM, honeypots y catálogos CVE/CWE) y las **VPN** (tipos, protocolos de tunneling de sitio a sitio y de acceso remoto, autenticación PPP, servidores AAA, interfaces TUN/TAP y la familia IPSec con AH, ESP, IKE y los modos transporte y túnel).

---

## 1. Seguridad perimetral

### 1.1 Cortafuegos / Firewall

Bloquea accesos no autorizados.

| Tipo | Nivel | Descripción (PDF) |
|---|---|---|
| Filtrado de paquetes (*Package Filtering*) | Red y un poco de transporte | Trabaja con IP y puertos. ≈ iptables |
| *Circuit-Level Gateway* | Sesión (ej. TCP) | Controla que el TCP Handshake se haga correctamente |
| *Application Level Gateway* / *Forward Proxy* / *Reverse Proxy* | Aplicación (ej. HTTP) | Productos: Squid, Nginx, Varnish, HAProxy |
| *Stateful Inspection* | — | Tienen información histórica almacenada, para poder tomar mejores decisiones. Ej.: `conntrack` es un módulo que amplía la funcionalidad de iptables |
| *Next Generation* | — | **IPS** (Sistemas de Prevención de Intrusos); **WAF** (*Web Application Firewall*): vulnerabilidades web ya detectadas, OWASP, ejemplo Apache ModSecurity; **UTM** (Gestión Unificada de Amenazas): es un firewall con antivirus, IPS, etc. |

> [!important] NetFilter es el firewall de Linux
> **NetFilter** es el firewall de Linux (no el proxy; así lo corrige la entrada de Actualizaciones del 22/02/2026). Formas de administrarlo / *frontends*: **iptables**, **firewalld** (comando `firewall-cmd`), **nftables** y **ufw**. Ver el apartado de iptables en [[B2 - T4.3 LINUX]].

> [!note] Errata aplicada (Actualizaciones 20_05_2026, entrada de 22/02/2026)
> "Netfilter es el firewall, no el proxy de Linux." El PDF ya lo expresa correctamente.

### 1.2 Arquitecturas de referencia

Basadas en cómo se usan los firewalls.

| Arquitectura | Descripción (PDF) |
|---|---|
| *Screening Router* | Filtrado de paquetes. Separa la red externa de la interna con un único equipo, el router. El router está expuesto |
| *Screened Host* | Solo se permiten conexiones hacia un determinado host. Todo pasa por el *Bastion Host*. El router sigue estando expuesto. Filtrado de paquetes |
| *Dual-Homed Host* | El host tiene 2 tarjetas de red, una para la red interna y otra para la externa. Intercambio a nivel de aplicación. No hay routing, solo "reparto". Establece de dónde a dónde va a permitir que se dialogue. Ej.: si llega algo al puerto 80, se lo entrega al host XX |
| *Screened Subnet* (DMZ) | Este FW solo permitirá acceso a elementos que tengamos en la DMZ: web, DNS autoritativo, MTA, proxy inverso, servidor de VPN, etc. El tráfico de la DMZ a la red interna está prohibido. El router externo generalmente hace PAT (*Port Address Translation*). Red interior "desconectada" lógicamente de la exterior. Podemos tener 1 o más *bastion hosts*, cada uno con diferentes servicios |

- **Bastion Host**: máquina accesible desde el exterior que debemos securizar/fortificar (*hardening*). Hace de proxy frente a otros hosts.
- Diagramas del PDF: Screening Router (Internet → router/filtrado → red interna con un único equipo de separación); Screened Host (Internet → router con filtrado → *Bastion Host* → red interna); Dual-Homed Host (host con dos tarjetas entre Internet y red interna); Screened Subnet (Internet → router externo/firewall → red perimétrica con bastion host(s) → firewall → red interna).
- Forward vs Reverse Proxy (diagrama del PDF): el *forward proxy* se sitúa entre los usuarios/clientes e Internet; el *reverse proxy* se sitúa entre Internet y los servidores de origen (*origin server*).

Ver [[DMZ (zona desmilitarizada)]] (con el ejemplo de la [[Red SARA]], cuyo Área de Conexión se describe como una DMZ con DNS, proxy, IDS, IPS, firewall y proxy inverso).

### 1.3 Sistemas de protección contra intrusos

| Sistema | Naturaleza | Descripción (PDF) | Productos |
|---|---|---|---|
| IDS (*Sistemas de Detección de Intrusos*) | Pasivos | Analizan tráfico de un único sitio. Sniffer de red que detecta incidencias y las registra. Puede generar alarmas usando SNMP. Busca patrones/firmas de ataque y comportamientos anormales | — |
| NIDS | IDS | Vigila la red. Captura tráfico de la red | SNORT, Suricata |
| HIDS | IDS | Vigila cambios en un host. Suelen centrarse en abusos de privilegios | OSSEC, SAGAN, TRIPWIRE |
| IPS (*Sistemas de Prevención de Intrusos*) | Activos | IDS + acción contra el ataque (bloqueo o descarte de paquetes o acciones) | SNORT, Suricata, OSSEC, Sagan, Bro, Fail2Ban, AJDE, Samhain |
| SIEM (*Gestión de Eventos e Información de Seguridad*) | Pasivos | Analizan la información de **muchos sitios**, recogiendo los logs | ELK, Qradar, Metron, OSSIM, Gloria/Mónica (CCN) |

- Subtipos de IPS: **NIPS** (network), **WIPS** (wireless), **HIPS** (host), **NBA** (detecta comportamientos anómalos en la red).
- SIEM: el administrador establece qué mensajes son relevantes. Se centraliza e interpreta la información para aplicar IA y ML. La información de los logs debe **normalizarse y correlacionarse**. Al bruto se aplican reglas para obtener un neto. Ese neto se llama **Evento**.
- **OSSIM** integra: nmap (análisis de puertos), snort (IPs), nagios (monitorización de red), nikto (análisis de vulnerabilidades).
- Gloria/Mónica son productos del CCN: ver [[CCN-CERT]].
- **Honeypots**: sistema configurado con vulnerabilidades para atraer a los atacantes y estudiarlos. Separado de la red real.

> [!important] IDS vs IPS vs SIEM
> IDS: pasivo, analiza un único sitio, detecta y registra. IPS: activo (IDS + acción contra el ataque: bloquea o descarta). SIEM: pasivo, analiza información de muchos sitios recogiendo logs, los normaliza y correlaciona.

### 1.4 Catálogos de vulnerabilidades

| Catálogo | Qué es (PDF) |
|---|---|
| CVE (*Common Vulnerabilities and Exposures*) | Vulnerabilidades asociadas a un **producto concreto**. Vulnerabilidades de día 0: según se publican las usan los atacantes hasta que los fabricantes de sw y empresas las solucionan |
| CWE (*Common Weakness Enumeration*) | Vulnerabilidad **no asociada a ningún producto**. Es como lo que hace OWASP |

---

## 2. VPN (Red Privada Virtual)

Extensión de una LAN a través de una red pública. Reduce los costes al no necesitar líneas dedicadas. Ofrece mecanismos de **confidencialidad, integridad y autenticación (CIA)**. Referencia: **Guía CCN 836**.

| Tipo de VPN | Descripción (PDF) |
|---|---|
| De acceso remoto | Integración de un equipo de un empleado en la red de la organización |
| De sitio a sitio | Integración de sedes de una organización. De router a router |
| De equipo a equipo | No se tiene acceso a las redes a las que pertenezcan los equipos |

Diagramas del PDF: VPN de acceso remoto (equipo cliente remoto con software VPN → Internet → firewall → concentrador VPN) y VPN de sitio a sitio (concentradores VPN con firewall en cada sede unidos a través de Internet).

### 2.1 Protocolos de tunneling

No son punto a punto al atravesar Internet. Son **estáticos**, al ser siempre los mismos extremos.

#### VPN sitio a sitio

- **Familia IPSec** (ver sección 3).
- **GRE**: protocolo para encapsular datos. IP protocol **47**. **No seguro**. Usado con otros para dar seguridad. El payload de GRE es el paquete IP de tráfico privado. GRE va sobre paquete IP con IPs públicas porque atraviesa Internet. Podría llevar IPv4 dentro e IPv6 fuera o al revés.

#### VPN de acceso remoto

| Protocolo | Nivel | Descripción (PDF) |
|---|---|---|
| PPTP | 2 (enlace) | Encripta y autentica. Para encriptar usa la extensión MPPE. Usa GRE |
| L2F | 2 (enlace) | Encripta y autentica. No encripta por sí solo |
| L2TP / IPSec | 2 (enlace) | Encriptación y autenticación. Encripta con IPSec. Sobre UDP |
| SSL/TLS | Transporte | Producto: OpenVPN |
| SSTP | — | Usa SSL |
| SSH | Aplicación | — |
| WireGuard | Red | App y protocolo. Trabaja a nivel de red |

- PPTP, L2F y L2TP son **no seguros** porque eran líneas dedicadas. Nivel de enlace.
- **SSL, SSH y SSTP usan menos overhead**.
- Diagrama del PDF: encapsulado L2TP: cabeceras nuevas del túnel (Ethernet, IP, UDP, L2TP) delante del paquete original (Ethernet Header, IP Header, TCP Segment, Data), que pasa a ser el *tunnel payload*.

Para SSH como túnel ver [[Túneles SSH (-L y -R)]]; para TLS ver [[B4 - T8 HTTP SSL TLS]].

### 2.2 Sistemas de autenticación típicos de PPP

| Sistema | Funcionamiento |
|---|---|
| PAP | Manda la contraseña en ASCII y **en claro** |
| CHAP | El servidor manda un reto/*challenge* al host para que lo resuelva usando su clave (la tiene el usuario y el servidor) |
| EAP | Extendido. Usa certificados digitales |

### 2.3 Servidores de autenticación

Junto al servidor de VPN está uno de estos productos: **Radius, Kerberos, TACACS+, Diameter**. Son sistemas **AAA**:

| Letra | Significado |
|---|---|
| Autenticación | user/pass |
| Autorización | Para acceder o no al recurso |
| Contabilización (*Accounting*) | Facturación por uso |

### 2.4 TUN / TAP

Interfaces virtuales. Es el encargado de pasar de una pila OSI a otra para envolver los datos privados y meterlos en el túnel. Conectan la pila privada con la pública. **TUN** a nivel de red; **TAP** a nivel de enlace. (Diagrama del PDF "TUN & TAP in the network stack": entre las dos pilas de siete capas, TUN conecta a nivel de capa 3 y TAP a nivel de capa 2.)

---

## 3. Familia IPSec

Familia de protocolos que **autentican y cifran** paquetes de datos enviados sobre IP. TUN cambia de pila. IPv6 incluye de forma nativa IPSec. Incluye mecanismo de autenticación mutua y negociación de claves criptográficas. El PDF añade literalmente: "No garantizan la confidencialidad" (dato sin más explicación en la fuente).

### 3.1 Protocolos

| Protocolo | IP Protocol | Qué asegura | Detalles (PDF) |
|---|---|---|---|
| AH (*Authentication Header*) | **51** | Integridad, autenticación de origen y evita ataques de *replay* (playback/repetición/reinyección) | En el datagrama se incrusta una cabecera para meter seguridad. Los 2 routers deben tener la misma clave |
| ESP (*Encapsulating Security Payload*) | **50** | Confidencialidad, integridad y autenticación de origen | Cifra el payload con AES. Podría configurarse sin cifrado, solo para autentificar, pero está desaconsejado |
| IKE / ISAKMP / OAKLEY / IKE2 (*Internet Key Exchange*) | — | Intercambio de claves | Ver más abajo |

Campos importantes de **AH**:

- *Integrity Check Value*: HMAC. Usa la clave y el datagrama privado.
- *Security Parameters Index* (SPI): identifica los parámetros de seguridad y junto con la IP determinan la **SA**.
- *Sequence Number*: usado para evitar ataques de replay.

Campos importantes de **ESP**:

- *Security Parameters Index*.
- *Sequence Number*.
- *Payload DATA*: utiliza 3DES / AES. AES tiene menos vulnerabilidades.
- *Authentication DATA*: HMAC. ≈ *Integrity Check Value*.

**IKE / ISAKMP / OAKLEY / IKE2**: protocolos para el intercambio de claves (DH – Diffie-Hellman), intercambio de opciones criptográficas entre pares, autenticación entre pares (funciona tanto con certificados X.509 como con una *pre-shared key*) y gestión de las **Asociaciones de Seguridad** (*Security Association*, SA) en cada dirección de la comunicación.

- Una **SA** es un grupo lógico de parámetros de seguridad. Es una tabla donde cada registro es una SA. Entre cada par de routers hay parámetros de seguridad distintos, distintas claves (R1: R1→R2; R1→R3; R1→R4).
- La SA viene de IKE/ISAKMP. ≈ Handshake SSL/TLS. Ver [[Diffie-Hellman]] y [[Certificado TLS-SSL (X.509)]].

> [!tip] Números a memorizar
> AH = IP protocol 51 (A de "Authentication", sin cifrar). ESP = IP protocol 50 (cifra). GRE = IP protocol 47.

### 3.2 Modos de funcionamiento (tanto para AH como para ESP)

| Modo | Uso | Descripción (PDF) |
|---|---|---|
| Transporte | Host to host | Solo la carga útil del paquete IP se cifra y autentica. El enrutamiento no se toca. Más usado con AH. No modificas el tráfico, solo lo autenticas. No se cogen todos los campos para hacer el hash, ya que el TTL, por ejemplo, se va decrementando |
| Túnel | Site to site | Todo el paquete IP es cifrado o autenticado, por eso hay que encapsularlo en otro paquete IP. Siempre que hay un túnel, se mete una nueva cabecera. Al envolver hay que meter una nueva cabecera |

Diagramas del PDF (estructura de los paquetes):

| Protocolo y modo | Estructura |
|---|---|
| AH transporte | IP HDR + AH + Data; autenticado excepto campos mutables |
| AH túnel | New IP HDR + AH + IP HDR + Data; autenticado excepto campos mutables en la nueva cabecera IP |
| ESP transporte | IP HDR + ESP HDR + Data + ESP Trailer + ESP Auth; cifrado: Data (y trailer); autenticado: ESP HDR + Data + Trailer |
| ESP túnel | New IP HDR + ESP HDR + IP HDR + Data + ESP Trailer + ESP Auth; cifrado: IP HDR + Data; autenticado: desde ESP HDR |
| Esquema modo transporte | Dos hosts con IPSec, comunicación segura extremo a extremo; paquete IP1 IP2 ESP TCP Datos |
| Esquema modo túnel | Hosts sin IPSec, con gateways IPSec A y B; comunicación en claro hasta el gateway, segura entre gateways; paquete IPA IPB ESP IP1 IP2 TCP Datos |

Productos: **SonicWall, FortiNet**.

---

## 🔑 Resumen ultra-rápido

- Firewalls: filtrado de paquetes (IP y puertos, ≈ iptables), circuit-level (sesión, TCP handshake), application level gateway / proxy (Squid, Nginx, Varnish, HAProxy), stateful (conntrack), next generation (IPS, WAF/ModSecurity/OWASP, UTM).
- NetFilter = firewall de Linux; frontends: iptables, firewalld (`firewall-cmd`), nftables, ufw. Netfilter no es el proxy.
- Arquitecturas: Screening Router (router expuesto), Screened Host (bastion host), Dual-Homed Host (2 tarjetas, nivel de aplicación, sin routing), Screened Subnet/DMZ (DMZ -> interna prohibida, PAT en router externo, 1 o más bastion hosts).
- IDS pasivo (NIDS: SNORT/Suricata; HIDS: OSSEC/SAGAN/TRIPWIRE); IPS activo (NIPS, WIPS, HIPS, NBA; Fail2Ban, Bro, AJDE, Samhain); SIEM pasivo, multi-sitio, normaliza y correlaciona logs -> Evento (ELK, Qradar, Metron, OSSIM, Gloria/Mónica CCN). Honeypot = trampa aislada.
- CVE = vulnerabilidad de un producto concreto (día 0); CWE = debilidad sin producto (como OWASP).
- VPN = LAN extendida sobre red pública, CIA, Guía CCN 836. Tipos: acceso remoto, sitio a sitio, equipo a equipo.
- Sitio a sitio: IPSec y GRE (IP protocol 47, no seguro). Acceso remoto: PPTP (MPPE, GRE), L2F, L2TP/IPSec (UDP) en nivel 2; SSL/TLS (OpenVPN, transporte), SSTP, SSH (aplicación), WireGuard (red). SSL/SSH/SSTP: menos overhead.
- PPP: PAP (claro), CHAP (reto), EAP (certificados). AAA: Radius, Kerberos, TACACS+, Diameter.
- TUN (red) / TAP (enlace): interfaces virtuales para meter tráfico en el túnel.
- IPSec: AH (protocolo 51: integridad + origen + anti-replay, HMAC, SPI, Sequence Number); ESP (protocolo 50: confidencialidad + integridad + origen, AES/3DES); IKE/ISAKMP/OAKLEY/IKE2 (DH, certificados X.509 o PSK, gestiona SA). Modo transporte (host a host, solo payload) vs modo túnel (site to site, nueva cabecera IP).

---

## Conexiones con otros temas

- [[B4 - T8 HTTP SSL TLS]]: TLS como VPN de transporte (OpenVPN, SSTP), certificados X.509, Diffie-Hellman, HMAC; la SA de IPSec se compara con el handshake TLS.
- [[B4 - T10 REDES LAN]]: dispositivos de interconexión (firewalls, proxies, DMZ) y segmentación en LAN.
- [[B2 - T4.3 LINUX]]: iptables / Netfilter.
- [[DMZ (zona desmilitarizada)]] · [[Red SARA]] · [[CCN-CERT]].
- [[Túneles SSH (-L y -R)]] · [[B4 - T1.2 ADMON SSOO - SSH]]: SSH como mecanismo de túnel de nivel de aplicación.
