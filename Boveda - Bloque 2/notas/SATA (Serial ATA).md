Bus de comunicación **serie e interno**, sucesor de **[[PATA (Parallel ATA)]]**. Es el estándar más común hoy para conectar discos duros y SSD en equipos de consumo.

- **Un dispositivo por cable** (sin master/slave), cable más fino y largo que el de PATA.
- **Bidireccional** y admite **hot-plug** (conexión/desconexión en caliente).
- Pensado para **consumo doméstico**, no para exprimir al máximo el rendimiento — de ahí que su techo de velocidad quede por debajo de [[SAS (Serial Attached SCSI)]] o de [[NVMe (Non-Volatile Memory Express)]].

### Velocidades (se duplican cada generación)

| Versión | Velocidad |
|---|---|
| SATA-1 | 1,5 Gbps |
| SATA-2 | 3 Gbps |
| SATA-3 | 6 Gbps (actual) |

> [!note] SATA también existe en formato SSD
> El [[SSD (Solid State Drive)]] puede llevar señal SATA sobre conector **M.2** (M.2 SATA), limitado a los mismos ~6 Gbps de SATA-3 — mucho más lento que un M.2 NVMe. El protocolo que usa un SSD por SATA es **AHCI**, con bastante más latencia que NVMe por estar diseñado originalmente pensando en discos mecánicos, no en flash.

---

**Conexiones con otros conceptos TAI:**
- [[PATA (Parallel ATA)]] — su predecesor paralelo.
- [[SAS (Serial Attached SCSI)]] — el equivalente profesional/servidor.
- [[NVMe (Non-Volatile Memory Express)]] y [[SSD (Solid State Drive)]] — por qué SATA/AHCI se queda corto para flash.
- [[Interfaces]] y [[Bus de comunicación]] — panorama y clasificación general.
