Es un sistema de almacenamiento compartido al que se accede por la **red IP normal** (Ethernet), igual que a cualquier otro recurso de red. A diferencia de DAS y SAN, el acceso es en modo **fichero**: el sistema de ficheros vive abajo, en el propio NAS, y protocolos como **NFS** o **CIFS** son solo una vista instrumental de esos ficheros (el servidor pide ficheros, no bloques — el trabajo de sistema de ficheros ya lo hace el propio NAS). Si el NAS tiene una tarjeta HBA a Fibre Channel, el sistema de ficheros usado es **ZFS**. Marcas comerciales: Netapp, Qnap, Synology.

> [!tip] Regla mnemotécnica (conocimiento general)
> NAS = "ficheros compartidos por la red normal".

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[DAS (Direct Attached Storage)]] y [[SAN (Storage Area Network)]] — las otras dos formas de almacenamiento, ambas en modo bloque (frente al modo fichero de NAS).
