Es la tarjeta que conecta un servidor (host) a una red de almacenamiento tipo [[SAN (Storage Area Network)|SAN]]. Tiene una dirección única de 64 bits llamada [[WWN (World Wide Name)|WWN]]: puede identificarse por su **WWNN** (Node Name, de 8 bytes) —que es el de toda la cabina—, o por su **WWPN** (Port Name, también de 8 bytes) —una tarjeta tiene un único puerto, así que un único WWPN—.

Se puede obtener información de una tarjeta HBA con comandos como `syminq hba`, `/usr/sbin/hbanyware/hbacmd listHBAs` o `systool -c fc_host -v`.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[WWN (World Wide Name)]] — el identificador único que lleva grabado el HBA.
- [[SAN (Storage Area Network)]] — la red a la que conecta el HBA.
- [[Zoning (SAN)]] — usa el WWN del HBA para definir qué hosts pueden verse entre sí en el switch FC.
