Bus de comunicación **serie**, la evolución profesional de **[[SCSI (Small Computer System Interface)]]**: conserva su "cerebro lógico" (gestión de muchos dispositivos en un mismo bus) pero sobre transmisión serie moderna. Es la interfaz habitual en **servidores y centros de datos**.

- **Identificador**: cambia el ID numérico de SCSI por un **[[WWN (World Wide Name)]]**, un identificador único de 64 bits (como una matrícula mundial irrepetible).
- **Escalabilidad**: con **expansores**, puede manejar hasta **16.384 dispositivos** por dominio.
- **Compatibilidad con SATA**: una controladora SAS puede usar discos **[[SATA (Serial ATA)]]**, pero **no al revés** — compatibilidad en un solo sentido. Dato de examen recurrente (ver también [[SSD (Solid State Drive)]]).

### Velocidades (aprox. se duplican cada generación)

| Versión | Velocidad |
|---|---|
| SAS-1 | 3 Gbps |
| SAS-2 | 6 Gbps |
| SAS-3 | 12 Gbps |
| SAS-4 | 22,5 Gbps |
| SAS-5 | 45 Gbps (en desarrollo) |

> [!important] Idea clave para examen
> SAS es la evolución "profesional" de SCSI (servidores, redundancia, hot-swap), igual que SATA es la evolución "doméstica" de PATA. Ver [[Interfaces]] para la narrativa completa de las cuatro interfaces.

---

**Conexiones con otros conceptos TAI:**
- [[SCSI (Small Computer System Interface)]] — su predecesor lógico en paralelo.
- [[SATA (Serial ATA)]] — el equivalente doméstico, compatible en un solo sentido con SAS.
- [[WWN (World Wide Name)]] — el identificador que sustituye al ID numérico de SCSI.
- [[SSD (Solid State Drive)]] y [[HDD (Hard Disk Drive)]] — discos físicos que pueden usar esta interfaz.
- [[Interfaces]] y [[Bus de comunicación]] — panorama y clasificación general.
