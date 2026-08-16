Es el mecanismo que crea zonas a nivel del switch FC para aislar unos host-cliente de otros — la misma idea que una **VLAN**, pero aplicada a una red de almacenamiento. Cada zona comprende una parte de la cabina, unos determinados hosts y una parte del switch. Cada host que accede al switch FC necesita una tarjeta [[HBA (Host Bus Adapter)|HBA]] con su identificador único [[WWN (World Wide Name)|WWN]] (≈ una MAC), y el zoning se define en base a esos WWN, pudiendo llegar a definir reglas por WWN concreto o incluso por cada puerto del switch.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[WWN (World Wide Name)]] y [[HBA (Host Bus Adapter)]] — el identificador y la tarjeta sobre los que se basan las zonas.
- [[LUN y LUN Masking]] — el mecanismo complementario, a nivel de cabina en vez de a nivel de switch.
- [[SAN (Storage Area Network)]] — la red donde existe el zoning.
