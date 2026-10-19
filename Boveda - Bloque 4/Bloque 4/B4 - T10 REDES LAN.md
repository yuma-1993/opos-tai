---
tags:
  - bloque4
  - tema10
  - redes
  - lan
  - ethernet
  - vlan
  - dhcp
bloque: 4
tema: 10
titulo: Redes LAN (técnicas de acceso al medio, Ethernet 802.3, dispositivos de interconexión, DHCP, VLAN y estándares IEEE 802)
estado: por-repasar
---

# Tema 10 · Bloque 4 — Redes LAN

> [!abstract] De qué va este tema
> Clasifica los tipos de redes y las técnicas de acceso al medio (MAC), define qué es una LAN y su arquitectura IEEE (LLC y MAC), detalla Ethernet 802.3 (trama, medios, direcciones MAC), recorre los dispositivos de interconexión (repetidores, hubs, bridges, switches, routers, gateways, firewalls, proxies, DMZ) con sus dominios de colisión y difusión, y termina con DHCP, VLAN 802.1q (con la configuración VTP) y el catálogo de estándares IEEE 802.

---

## 1. Tipos de redes

| Tipo | Descripción (PDF) |
|---|---|
| Redes de difusión | Redes *broadcast*. Canal compartido entre todos los terminales. Hub / concentrador |
| Redes punto a punto | Entre pares. El destino es unívoco y no es necesario poner dirección de destino. Modalidades de transmisión: Simplex, Half-Duplex, Duplex o Full-Duplex |

Según la **distancia**:

| Red | Alcance y características |
|---|---|
| PAN | Personal. 10-100 m. Poca información y poca energía. Bluetooth, ZigBee, IoT. 802.15 |
| LAN | IEEE 802.3. 300 m – 1 km |
| MAN | Misma ciudad. 10 – 100 km |
| WAN | Alcance global. Tecnologías: Frame Relay, ATM, PPP, MPLS, HDLC |

---

## 2. Técnicas de acceso al medio (MAC)

Reglas que definen cómo un equipo pone/toma datos en la red. Conocidas como **MAC** (*Medium Access Control*). El PDF las ilustra con un esquema de tres columnas: Acceso controlado (Reserva, Polling, Paso de testigo/token), Acceso aleatorio (Aloha, Aloha ranurado, CSMA 1-persistente, CSMA 1-no persistente, CSMA 1-p persistente, CSMA/CD, CSMA/CA) y Canalización (FDMA, TDMA, CDMA).

### 2.1 Acceso controlado

| Técnica | Descripción (PDF) |
|---|---|
| Reserva | Las estaciones reservan el canal antes de enviar datos. Eficiente si hay pocos terminales |
| Polling | Requiere un control centralizado. La estación central sondea al resto para ver quién quiere enviar y le asigna un tiempo de envío |
| Token / paso de testigo | Se pasa un token por las estaciones. Cuando la estación tiene el token puede transmitir. Pasa el token a la siguiente |

| Variante de token | Norma | Topología | Otros |
|---|---|---|---|
| Token-Bus | 802.4 | Física en bus y lógica en anillo | Cada estación tiene un tiempo para transmitir |
| Token-Ring | 802.5 | Física en estrella y lógica en anillo | Estación central MAU (*Multistation Access Unit*). Admite multicast. Admite prioridad |

### 2.2 Acceso aleatorio

| Técnica | Descripción (PDF) |
|---|---|
| Aloha | La estación que quiere transmitir lo hace y escucha si hay colisión. Si hay colisión, espera un tiempo aleatorio para volver a transmitir |
| Aloha ranurado | Las estaciones transmiten sin escuchar. El tiempo se divide en ranuras. Se transmite al comienzo de la ranura |
| CSMA (*Carrier Sense Multiple Access*) | Las estaciones conocen el estado del canal. Si está libre, transmiten. Si no, esperan |
| CSMA/CD (*Collision Detection*) | Usado en Ethernet 802.3 cuando era half-duplex. Escucha antes de transmitir. Si durante la transmisión detecta una colisión, interrumpe la transmisión y espera |
| CSMA/CA (*Collision Avoid*) | Usado en Wi-Fi |

### 2.3 Canalización

| Técnica | Descripción (PDF) |
|---|---|
| FDMA | División por **frecuencia**. Cada señal de entrada se modula con frecuencia portadora distinta (canal). Separación por banda de guarda |
| TDMA | División por **tiempo**. Cada estación tiene un slot de tiempo para emitir. Transmisión síncrona (tiempo fijo) o estadística (tráfico) |
| CDMA | División por **código**. Cada estación tiene un código ortogonal. Todos pueden emitir al mismo tiempo y en la misma frecuencia. El receptor separa y decodifica cada señal |

> [!tip] Mnemotecnia
> CSMA/CD = *Detection* (Ethernet cableada, half-duplex). CSMA/CA = *Avoid* (Wi-Fi). F = frecuencia, T = tiempo, C = código.

---

## 3. Redes LAN

Definición IEEE: "Sistema de comunicación de datos que permite a un cierto número de dispositivos independientes comunicarse directamente entre sí, dentro de un área geográfica reducida y empleando canales físicos de comunicación de velocidad moderada o alta."

Características:

- Medio de transmisión compartido. Redes de difusión.
- Cobertura geográfica limitada (<= 10 km).
- Velocidades de transmisión elevadas (1 Mbps – 10 Gbps).
- Tasas de error de transmisión muy bajas (~10^-9).
- Fácil instalación y explotación.
- Topologías estrella, bus, anillo, etc.

### 3.1 Subniveles LLC y MAC

La IEEE subdivide el **nivel de enlace** de OSI en 2 (diagrama del PDF: bajo el nivel de red, LLC y MAC; sobre LLC se apoyan 802.3 Ethernet, 802.4 Token Bus, 802.5 Token Ring, 802.6 DQDB y FDDI):

| Subnivel | Función |
|---|---|
| LLC (*Logical Link Control*) | Ensambla, desensambla y comprueba direcciones. Nivel lógico. 802.2 |
| MAC (*Medium Access Control*) | Control de acceso al medio físico de modo que múltiples estaciones puedan compartirlo |

Tipos de servicio LLC (no todos los servicios que van sobre LLC tienen las mismas necesidades):

1. No orientado a conexión y sin confirmación. Mejor rendimiento.
2. Orientado a conexión. Mayor garantía.
3. No orientado a conexión y con confirmación. Mezcla de los anteriores.

### 3.2 Elementos de una LAN

| Elemento | Descripción |
|---|---|
| Estaciones de trabajo | Equipos conectados a la red. Nodos |
| Tarjetas de interfaz de red (NIC) | Específica para el tipo de red |
| Sistema cableado | Cables, conectores, etc. NIC → electrónica |
| Electrónica de red | Dispositivos de conexión. Intermediarios |

---

## 4. Ethernet — IEEE 802.3

Ethernet fue el origen y luego se estandarizó como 802.3. Velocidades de 10 Mbps a 400 Gbps (802.3db).

| Aspecto | Dato (PDF) |
|---|---|
| Trama 802.3 | Tiene el campo **longitud**. No se puede definir qué protocolo lleva la trama |
| Trama Ethernet II (DIX Ethernet) | Tiene el campo **ethertype** (es lo que se usa) en sustitución del campo longitud |
| Trama más pequeña | **64 bytes**. Si fuese de menor tamaño, se llama *Runt Frame* |
| Jumbo frame | Payload de **9000 bytes** en lugar de 1500 bytes |
| Topología | Física en bus o estrella (con un switch). Lógica en bus |
| Codificación | Manchester: para no perder sincronismo al mandar muchos 0 o 1 |
| Alcances por medio | Par trenzado 100 m, coax-thin 200 m, coax-thick 500 m, fibra multimodo 2,5 km |
| Nivel de enlace | Subnivel LLC y MAC. Técnica de acceso al medio CSMA/CD |

Campos de la trama (diagrama del PDF): Source MAC, Destination MAC, Type/Length, Payload, FCS.

> [!note] Errata aplicada (Actualizaciones 20_05_2026)
> "Si la trama Ethernet mide **menos de 64 bytes**, se llama Runt Frame." El PDF ya lo expresa así.

### 4.1 Especificaciones: 10BASE-T

| Parte | Significado |
|---|---|
| 10 | Velocidad |
| BASE | Transmisión de la señal en banda base (sin modular) |
| T | Par de cobre |
| F | Fibra óptica |
| S / L / E | Ventana S / ventana L / ventana E |

### 4.2 Direcciones MAC

6 octetos (48 bits). Los 3 primeros (**OUI**, *Organisationally Unique Identifier*) identifican al fabricante y los 3 últimos al interfaz (*NIC Specific*).

| Bit del primer octeto | Valor | Significado |
|---|---|---|
| Último bit (b0) | 0 / 1 | 0: unicast. 1: **multicast** |
| Penúltimo bit (b1) | 0 | Interfaz física. Dirección única asignada por el fabricante (*globally unique*, OUI enforced) |
| Penúltimo bit (b1) | 1 | Interfaz virtual (hipervisores, contenedores, etc.), local (*locally administered*). Dirección sobrescrita por sw o por el administrador |

- Trama multicast comienza por **01:00:5E**. En nivel 3 de red sería **224.X.X.X**. El switch ayuda a hacer la multidifusión.
- Broadcast: `FF:FF:FF:FF:FF:FF`.

---

## 5. Dispositivos de interconexión

### 5.1 Dominios de colisión y de difusión

| Concepto | Descripción (PDF) |
|---|---|
| Dominio de colisión | Conjunto de nodos que comparten el mismo medio de transmisión y compiten por el acceso. Puede haber colisiones (en un hub se producen). Cuanto más grande es (mayor número de equipos) peor es el rendimiento de la red. Para mejorarlo se **segmenta** la red. Si queda un solo equipo en cada dominio de colisión se habla de **microsegmentación** |
| Dominio de difusión | Direcciones de broadcast `FF:FF:FF:FF:FF:FF`. Conjunto de estaciones de una misma LAN que pueden recibir mensajes de broadcast de otra estación de la red |
| Tormentas de broadcast | Se producen en redes mal diseñadas o en las que existan caminos redundantes no previstos (bucles). Un mensaje broadcast puede quedarse en la red indefinidamente, degradándola o colapsándola |

### 5.2 Comparativa de dispositivos

| Dispositivo | Nivel OSI | Dominios de colisión | Dominios de difusión | Notas (PDF) |
|---|---|---|---|---|
| Repetidor | 1 (físico) | Extiende el dominio de colisión (malo) | Comparte | Regenera y amplifica la señal cuando hay atenuación. Reenvía todos los datos |
| Concentrador / Hub | 1 (sin lógica) | Comparte | Comparte | Conexión de equipos adyacentes mediante bus común. La señal entra por un puerto y se reparte a todos los demás, por lo que se divide la velocidad entre todos los puertos |
| Puente / Bridge | 1 y 2 | Separa (1 por cada interfaz) | No separa | Separan redes a nivel de enlace. Interconectan redes locales con distintos medios físicos. Aprenden las MAC y las almacenan en una tabla. Filtrado y reenvío de tramas (software). Maneja grupos, de modo que solo pasa información al otro lado cuando hace falta |
| Conmutador / Switch | 2 | Separa | No separa | Evolución de los bridges transparentes. Ver 5.3 |
| Encaminador / Router | hasta 3 | Separa | Separa | El tráfico de difusión se queda en cada subred |
| Pasarela / Gateway | 4 - 7 | — | — | Interconectan redes con protocolos de alto nivel diferentes y aseguran que los datos de una red son compatibles con los de la otra. Ventajas: permiten la interconexión de protocolos. Desventajas: muy caros; la conversión de protocolos supone una alta carga en el gateway, pudiendo producirse cuellos de botella si la red no está optimizada |

> [!important] Hub vs switch vs router
> Hub: un único dominio de colisión y de difusión (el ancho de banda se reparte). Switch: separa dominios de colisión pero **no** de difusión (el ancho de banda no se reparte entre puertos). Router: separa **ambos**. Las VLAN permiten separar dominios de difusión en un switch.

### 5.3 Conmutadores / Switches

- Trabajan a nivel 2; evolución de los bridges transparentes. Separan dominios de colisión pero no de difusión.
- A diferencia de los hubs el ancho de banda no se reparte entre los distintos puertos.
- Encaminamiento gracias a **tablas MAC**.
- Los puertos pueden trabajar a diferentes velocidades y modos de funcionamiento (half-duplex y full-duplex, aunque ahora todo es full-duplex).
- El reenvío de tramas se realiza mediante **hardware**, por lo que es más eficiente que un bridge.
- Permite la **agregación de enlaces**, aumentando así el ancho de banda de los puertos unidos (*ether-channel* o *port-channel* en Cisco).
- Conecta host to host. Utilizan algoritmos de **Spanning Tree**.
- Soporte para redes virtuales (VLAN-802.1q), segmentando y dividiendo las redes: se pueden crear redes diferentes para generar dominios de difusión distintos. Cada host solo verá a otros equipos de su red. Para encaminar información de un equipo de una red a otro equipo de otra red hay que hacerlo explícitamente usando sw de nivel 3, haciendo routing.

### 5.4 Spanning Tree

| Algoritmo | Norma |
|---|---|
| STP | 802.1d |
| MSTP | 802.1s |
| RSTP | 802.1w |
| SPB | 802.1aq |

**BPDU** (*Bridge Protocol Data Units*): tramas con información del protocolo Spanning Tree (STP). Los switches mandan BPDU con multicast. Hay dos tipos:

- BPDU de **configuración**, para proveer información a todos los switches.
- **TCN** (*Topology Change*), avisa sobre cambios en la topología.

### 5.5 Cortafuegos, proxies y DMZ

| Elemento | Descripción (PDF) |
|---|---|
| Cortafuegos / Firewall | Restringe el intercambio de tráfico entre redes. También se pueden usar para segmentar una LAN en subredes. Las restricciones se establecen mediante reglas. Según el nivel al que operen las reglas: filtrado de paquetes (nivel 3); a nivel de circuito, con una lista de las conexiones válidas (nivel 4); a nivel de aplicación, restringiendo el tráfico de ciertas aplicaciones |
| Proxy | Equipo que actúa de intermediario para el acceso a servicios. Funciones: centralización y control de tráfico entre clientes y servidores; NAT de salida, asignando la misma IP de salida a todos los usuarios de la red local; cacheado de contenidos, agilizando el acceso a páginas accedidas recientemente |
| Proxy directo o *forward* | Situado en la parte de los clientes, permitiéndoles el acceso a los servicios o servidores |
| Proxy inverso o *reverse* | Situado por delante de los servidores que prestan servicio a los clientes. Es más seguro que el directo, pues el servidor solo aceptará peticiones del proxy y no de los clientes |
| DMZ (zona desmilitarizada) | Zona en la que se suelen ubicar los servidores accesibles desde el exterior de la organización. Subred aislada del exterior y de la LAN por los cortafuegos. En la DMZ: servidores web, DNS, servidor de correo, etc. En la LAN: servidores corporativos y repositorios de datos (servidores de aplicaciones, bbdd, buzones de correo, etc.) |

Diagrama del PDF: forward proxy entre los clientes (red interna) e Internet; reverse proxy entre Internet y los servidores de trabajo (*responding workers*). DMZ: Internet — firewall — red DMZ (router, web server, mail server) — firewall — LAN de la empresa.

Más detalle de firewalls, arquitecturas y DMZ en [[B4 - T9 SEGURIDAD EN REDES Y VPN]] y en [[DMZ (zona desmilitarizada)]].

---

## 6. Protocolo DHCP

Sirve para asignar una IP a un equipo. Va sobre **UDP**. Mnemotecnia **DORA**. Puertos UDP: **servidor 67, cliente 68**.

### 6.1 Métodos de asignación de direcciones IP

| Método | Descripción (PDF) |
|---|---|
| Manual o estática | Asigna una dirección IP a una máquina determinada (ej.: en base a la MAC) |
| Automática | Asigna una dirección IP de un pool a una máquina cliente la primera vez que hace la solicitud al servidor DHCP y hasta que el cliente la libera (si no es permanente) |
| Dinámica | El único método que permite la **reutilización dinámica** de las direcciones IP de un pool (tiene un tiempo de "préstamo") |

### 6.2 Proceso DORA

| Paso | Mensaje | Descripción | Puertos | Destino (MAC / IP) |
|---|---|---|---|---|
| 1. Descubrimiento (**D**iscover) | DHCPDISCOVER | El cliente pregunta qué DHCP hay | Origen 68, destino 67 | MAC `FF:FF:FF:FF:FF:FF` / IP `255.255.255.255` |
| 2. Oferta (**O**ffer) | DHCPOFFER | Los servidores DHCP reservan una IP y la ofrecen, indicando el tiempo de *lease* (arrendamiento) | Origen 67, destino 68 | MAC del cliente / IP propuesta |
| 3. Solicitud (**R**equest) | DHCPREQUEST | El cliente pide a un servidor DHCP esa IP. Usa broadcast para avisar al resto de servidores DHCP de la IP elegida y para que puedan liberar las IPs ofrecidas | Origen 68, destino 67 | MAC `FF:FF:FF:FF:FF:FF` / IP `255.255.255.255` |
| 4. Confirmación (**A**ck) | DHCPACK | El servidor confirma | Origen 67, destino 68 | MAC del cliente / IP del cliente |

> [!tip] Puertos DHCP
> Servidor = 67; cliente = 68. Los mensajes del cliente (DISCOVER, REQUEST) salen del 68 al 67; los del servidor (OFFER, ACK) del 67 al 68.

Ver también la configuración de red con DHCP en Debian en [[B2 - T4.3 LINUX]].

---

## 7. VLAN — IEEE 802.1q

- Permiten crear grupos de usuarios servidos por uno o varios switches, **separando dominios de difusión por sw**.
- El switch por defecto crea la **VLAN 1** con todos los equipos. En un switch defines las VLAN y asignas los hosts.
- Mediante el protocolo **VTP** (*VLAN Trunk Protocol*) se propaga la definición de VLAN al resto de switches. También **GVRP** (*Generic VLAN Registration Protocol*) y **MVRP** (*Multiple VLAN Registration Protocol*).
- Para configurar VLAN en el nivel 2 hay puertos **etiquetados o Trunk (troncales)** y puertos **no etiquetados o Access (de acceso)**. Terminología Cisco (Trunk / Access).
- 802.1q es una modificación de la trama Ethernet que mete una **cabecera de 4 bytes** (*tagging* o encapsulación) donde se informa el id de la VLAN (**12 bits: 4096 redes**). Quien pone la etiqueta es el switch.
- El tráfico etiquetado va por los puertos trunk, para las conexiones entre puertos troncales. Los hosts no saben a qué VLAN pertenecen, por lo que el tráfico será no etiquetado y va por puertos de tipo access.
- Diagrama del PDF: trama Ethernet (Source MAC, Destination MAC, Type/Length, Payload, FCS) y trama con 802.1Q (se inserta el campo "802.1q Tag" entre Source MAC/Destination MAC y Type/Length); enlace Access (longitud variable) frente a enlace Trunk (802.1Q tag, +4 bytes).

| Puerto | Etiquetado | Quién lo usa |
|---|---|---|
| Trunk (troncal) | Etiquetado | Conexiones entre switches (puertos troncales) |
| Access (acceso) | No etiquetado | Hosts (no saben a qué VLAN pertenecen) |

### 7.1 Configuración VTP (comandos del PDF)

| Objetivo | Comando | Qué hace |
|---|---|---|
| Configuración actual | `show vlan brief` | Muestra las VLAN existentes. La VLAN 1 se crea por defecto |
| Switch como servidor VTP | `vtp mode server` | Establece el switch en modo servidor |
| | `vtp domain TAI` | Configura el nombre del dominio VTP |
| | `vtp password 1234` | Establece la contraseña del dominio VTP |
| | `show vtp status` | Muestra la configuración del dominio VTP |
| | `show vtp password` | Muestra la contraseña del dominio VTP |
| Resto de switches como clientes VTP | `vtp mode client` | Establece el switch en modo cliente |
| | `vtp domain TAI` | Los clientes deben pertenecer al mismo dominio |
| | `vtp password 1234` | Establece la contraseña del dominio VTP |
| Configurar las VLAN en el switch servidor | `show vlan brief` | Para verificar las nuevas VLAN y sus nombres |
| Enlaces troncales entre switches | `switchport mode trunk` | Establece el modo troncal para el enlace troncal |
| | `switchport trunk native vlan XX` | Establece la VLAN de administración, sin etiquetar |
| | `show interface fa0/1 switchport` | Muestra el estado del enlace |
| | `show vtp status` | Muestra el estado VTP del switch |
| Asignar VLAN a los puertos | `switchport mode access` | Establece el modo acceso de los enlaces de acceso |
| | `switchport access vlan XX` | Asigna una VLAN a un puerto de acceso |

---

## 8. Estándares IEEE 802

ANSI, a través del IEEE, define los estándares 802 para la estandarización del nivel físico y enlace en redes PAN, LAN y MAN.

| Estándar | Descripción |
|---|---|
| 802.1q | VLAN |
| 802.1d | STP |
| 802.1s | MSTP |
| 802.1w | RSTP |
| 802.1aq | SPB |
| 802.1x | Control de acceso a redes en base a puertos |
| 802.2 | Control del enlace lógico. LLC (*Logical Link Control*) |
| 802.3 | Ethernet |
| 802.3u | 100BASE-TX y 100BASE-FX. 100 Mbps. Fast Ethernet |
| 802.3z | 1000BASE-X. Fibra óptica 1 Gbps. Giga Ethernet |
| 802.3ab | 1000BASE-T. Par trenzado. 1 Gbps. Giga Ethernet |
| 802.3ae | 10GBASE-SR y 10GBASE-LR. 10 Gbps |
| 802.3ba | 40 Gbps y 100 Gbps |
| 802.3af | PoE (*Power over Ethernet*). Máx. de 15,4 W por boca |
| 802.3at | PoE+. Máx. de 30 W por boca |
| 802.3bt | PoE++ (type 3: 60 W máx., type 4: 100 W máx. por boca) |
| 802.4 | Token Bus |
| 802.5 | Token Ring |
| 802.6 | Redes MAN DQDB (*Distributed Queue Dual Bus*) |
| 802.8 | FDDI (*Token Passing*) |
| 802.11 | Inalámbrica (Wi-Fi, *Wireless Fidelity*) |
| 802.15 | Inalámbrica PAN |
| 802.15.1 | Bluetooth |
| 802.15.4 | ZigBee (*Low Rate WPAN*) |
| 802.16 | WiMAX. Tecnología inalámbrica en entorno MAN |

> [!tip] Sufijos de 802.3
> u = Fast (100 Mbps), z / ab = Giga (1 Gbps, fibra / par trenzado), ae = 10 Gbps, ba = 40 y 100 Gbps; af / at / bt = PoE (15,4 W / 30 W / 60-100 W).

---

## 🔑 Resumen ultra-rápido

- Tipos: difusión (hub) vs punto a punto (simplex, half-duplex, full-duplex). Por distancia: PAN (10-100 m, 802.15), LAN (802.3, 300 m–1 km), MAN (10-100 km), WAN (Frame Relay, ATM, PPP, MPLS, HDLC).
- Acceso al medio: controlado (reserva, polling, token: Token-Bus 802.4 / Token-Ring 802.5 con MAU), aleatorio (Aloha, Aloha ranurado, CSMA, CSMA/CD en Ethernet half-duplex, CSMA/CA en Wi-Fi), canalización (FDMA frecuencia, TDMA tiempo, CDMA código).
- LAN: medio compartido, <= 10 km, 1 Mbps–10 Gbps, error ~10^-9. IEEE divide enlace en LLC (802.2) y MAC.
- Ethernet: 10 Mbps–400 Gbps (802.3db). 802.3 = campo longitud; Ethernet II = ethertype. Trama mínima 64 bytes (menos = Runt Frame). Jumbo frame 9000 bytes (vs 1500). Manchester. 100 m par trenzado, 200 m coax-thin, 500 m coax-thick, 2,5 km fibra multimodo.
- MAC: 48 bits, OUI (3 primeros, fabricante) + NIC (3 últimos). Último bit del primer octeto = 1: multicast (01:00:5E ↔ 224.x.x.x). Penúltimo bit 0 = física, 1 = virtual/local. Broadcast FF:FF:FF:FF:FF:FF.
- Dominios: hub = un dominio de colisión y de difusión; bridge/switch separan colisión pero no difusión; router separa ambos. Microsegmentación = un equipo por dominio de colisión. Tormenta de broadcast por bucles.
- Switch: nivel 2, tablas MAC, reenvío por hardware, agregación de enlaces (ether-channel/port-channel), Spanning Tree (STP 802.1d, MSTP 802.1s, RSTP 802.1w, SPB 802.1aq; BPDU de configuración y TCN), VLAN 802.1q.
- Gateway: niveles 4-7, caros, cuellos de botella. Firewall: paquetes (3), circuito (4), aplicación. Proxy: control, NAT de salida, caché; inverso más seguro. DMZ: web, DNS, correo; LAN: aplicaciones, bbdd, buzones.
- DHCP (UDP 67 servidor / 68 cliente): DORA = Discover (broadcast), Offer, Request (broadcast), Ack. Asignación manual, automática o dinámica (la única con reutilización, lease).
- VLAN 802.1q: VLAN 1 por defecto; etiqueta de 4 bytes con id de 12 bits (4096 redes) puesta por el switch; puertos trunk (etiquetado) vs access (sin etiquetar); VTP/GVRP/MVRP propagan VLAN; comandos `vtp mode server/client`, `switchport mode trunk/access`, `switchport access vlan XX`.
- PoE: 802.3af 15,4 W; 802.3at 30 W; 802.3bt 60 W (type 3) / 100 W (type 4).

---

## Conexiones con otros temas

- [[B4 - T9 SEGURIDAD EN REDES Y VPN]]: cortafuegos, proxies, DMZ y arquitecturas de referencia ampliados; VPN para extender la LAN.
- [[DMZ (zona desmilitarizada)]]: la DMZ de este tema y su ejemplo en la Red SARA.
- [[B2 - T4.3 LINUX]]: configuración de red en Linux (DHCP, iptables).
- [[B4 - T8 HTTP SSL TLS]]: capa de aplicación y transporte sobre la que corre el tráfico de la LAN.
