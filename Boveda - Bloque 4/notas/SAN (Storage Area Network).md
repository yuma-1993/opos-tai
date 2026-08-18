Es un sistema de almacenamiento compartido al que varios servidores acceden a través de una **red de almacenamiento independiente de la red de máquinas** (switches FC o IP) — los servidores que la usan necesitan acceso a las dos redes a la vez. El acceso es en modo **bloque** (el sistema de ficheros sigue viviendo arriba, en el servidor; abajo solo hay bloques), usando comandos [[SCSI (Small Computer System Interface)|SCSI]] a través de la SCSI Layer, con los protocolos SCSI o FCP. Los switches IP son más lentos pero más baratos; los switches FC (Fiber Channel) son más caros pero más rápidos. Las cabinas de discos de una SAN también se llaman **cabinas de almacenamiento** o **Storage Arrays**. Marca comercial habitual: EMC.

**¿Por qué hace falta esto?**
El servidor "cree" que el disco es local (accede en bloque, como si lo tuviera puesto físicamente), aunque en realidad está al otro lado de una red dedicada — eso permite compartir cabinas de disco grandes entre varios servidores sin perder la velocidad de acceso a bloque. VMware Xserver, por ejemplo, coge el almacenamiento para sus máquinas virtuales de discos de SAN.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[HBA (Host Bus Adapter)]] — la tarjeta con la que cada host se conecta a la SAN, identificada por su [[WWN (World Wide Name)|WWN]].
- [[LUN y LUN Masking]] y [[Zoning (SAN)]] — los dos mecanismos de control de acceso dentro de una SAN.
- [[iSCSI]] y [[FCP, FCIP y FCoE (protocolos Fibre Channel)]] — los protocolos que llevan los comandos SCSI a través de la red de la SAN.
- [[DAS (Direct Attached Storage)]] y [[NAS (Network Attached Storage)]] — las otras dos formas de almacenamiento compartido/directo.
- [[B2 - T4.2 WINDOWS Y SISTEMAS OPERATIVOS MOVILES]] — diagrama de un Windows Server con rol File Services que monta el almacenamiento real desde una SAN por Fibre Channel.
