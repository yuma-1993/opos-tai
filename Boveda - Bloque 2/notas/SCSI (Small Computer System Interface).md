Bus de comunicación **paralelo**, orientado a servidores y equipos profesionales. A un mismo bus SCSI se conectaban entre **7 y 15 dispositivos**, cada uno identificado por un **ID único** (como un DNI dentro del bus) — la versión "profesional" del paralelo, cara y robusta, frente al PATA doméstico de la misma época.

> [!important] Por qué importa aunque esté obsoleto
> SCSI no desaparece sin más: su **lógica de gestión** (muchos dispositivos, cada uno identificado, en un mismo bus) sobrevive en **[[SAS (Serial Attached SCSI)]]**, que coge exactamente esa inteligencia y la pone sobre una transmisión **serie** moderna. Cambia el ID numérico de SCSI por un **[[WWN (World Wide Name)]]** de 64 bits.

> [!tip] El hilo conductor de las interfaces de disco
> Paralelo → serie, en las dos familias: doméstico **PATA → SATA**, profesional **SCSI → SAS**. Ver [[Interfaces]] para la narrativa completa.

---

**Conexiones con otros conceptos TAI:**
- [[SAS (Serial Attached SCSI)]] — su evolución directa en serie.
- [[PATA (Parallel ATA)]] — el equivalente doméstico de la misma generación paralela.
- [[Interfaces]] — panorama completo de la evolución de interfaces de disco.
- [[Bus de comunicación]] — clasificación general paralelo/serie.
- [[B4 - T1.1 ADMON SSOO]] — en SAN, el acceso a la cabina se hace con comandos SCSI a través de la SCSI Layer (protocolos SCSI o FCP).
