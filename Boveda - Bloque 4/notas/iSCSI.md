Es un protocolo que encapsula comandos [[SCSI (Small Computer System Interface)|SCSI]] directamente sobre **TCP/IP**, lo que le permite viajar sobre una red Ethernet normal en vez de necesitar una red Fibre Channel dedicada. Es uno de los protocolos que puede llevar el tráfico de bloque de una [[SAN (Storage Area Network)|SAN]].

> [!note] Conocimiento general (no viene literal del tema)
> El tema lo menciona dentro de la lista de protocolos de la pila de acceso a almacenamiento (junto a FCP, FCIP, TCP, IP, FCoE, Ethernet y FC), sin detallar su funcionamiento; esta definición añade esa aclaración.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[FCP, FCIP y FCoE (protocolos Fibre Channel)]] — resuelven el mismo problema (llevar SCSI por red) usando Fibre Channel en vez de TCP/IP puro.
- [[SAN (Storage Area Network)]] — la red donde circula este protocolo.
