Los tres son protocolos que llevan comandos [[SCSI (Small Computer System Interface)|SCSI]] a través de distintos tipos de red, dentro de la pila de protocolos de acceso a almacenamiento de una [[SAN (Storage Area Network)|SAN]] (junto a [[iSCSI]]):

- **FCP (Fibre Channel Protocol)**: encapsula SCSI sobre una red Fibre Channel nativa.
- **FCIP (Fibre Channel over IP)**: hace un túnel de tráfico Fibre Channel completo sobre una red IP — típico para conectar dos SAN de Fibre Channel a través de una WAN.
- **FCoE (Fibre Channel over Ethernet)**: encapsula Fibre Channel directamente sobre tramas Ethernet, sin pasar por TCP/IP.

> [!note] Conocimiento general (no viene literal del tema)
> El tema solo lista estos protocolos dentro de un diagrama de pila (Application Layers, SCSI Reads & Writes, FCP, FCIP, iSCSI, TCP, IP, FCoE, Ethernet, FC) sin poder reconstruir el orden exacto de capas por problemas de extracción del PDF; esta nota explica qué resuelve cada uno a partir de su nombre y del contexto general de redes de almacenamiento.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[iSCSI]] — la alternativa que encapsula SCSI directamente sobre TCP/IP, sin pasar por Fibre Channel.
- [[SAN (Storage Area Network)]] — la red donde circulan estos protocolos.
