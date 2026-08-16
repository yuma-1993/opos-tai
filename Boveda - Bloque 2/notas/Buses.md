Un bus es una vía compartida que interconecta y da servicio a varios dispositivos — la teoría general (serie/paralelo, síncrono/asíncrono, interno/externo) vive en **[[Bus de comunicación]]**. Esta nota es el **índice**: qué buses hay en el temario y dónde está cada uno.

> [!note] Diferencia con `B2 - T1 INFORMATICA BASICA`
> La tema trae la tabla resumen de examen (§3). Aquí se organiza **todo el mapa de buses** de la bóveda, con el detalle de cada uno en su propia nota.

## El trío interno de la CPU

| Bus                      | Función                                                                          |
| ------------------------ | -------------------------------------------------------------------------------- |
| **[[Bus de control]]**   | Dice si es lectura o escritura, y quién tiene el control del bus en cada momento |
| **[[Bus de dirección]]** | Dice **dónde** (qué dirección de memoria/dispositivo)                            |
| **[[Bus de datos]]**     | Transporta **qué** (la instrucción o el dato en sí)                              |

> [!tip] Truco
> Dirección = dónde. Datos = qué. Control = qué hacer con ello y quién manda ahora.

## Buses internos de sistema y expansión

- **[[FSB (Front-Side Bus)]]** — bus histórico CPU↔chipset↔memoria, hoy sustituido por enlaces punto a punto (QPI/DMI, HyperTransport).
- **[[Buses de expansión internos (ISA, PCI, AGP)]]** — evolución de las tarjetas de expansión hasta llegar a PCIe.
- **[[PCI Express (PCIe)]]** — el bus de expansión serie actual, usado por gráficas, SSD NVMe, red...

## Buses/interfaces de almacenamiento

- **[[SCSI (Small Computer System Interface)]]** → **[[SAS (Serial Attached SCSI)]]** — línea profesional (paralelo → serie).
- **[[PATA (Parallel ATA)]]** → **[[SATA (Serial ATA)]]** — línea doméstica (paralelo → serie).
- **[[NVMe (Non-Volatile Memory Express)]]** — el escalón siguiente, sobre PCIe.
- Narrativa completa de esta familia en **[[Interfaces]]**.

## Buses/interfaces externas

- **[[USB]]** — el estándar universal actual.
- **[[Thunderbolt]]** — PCIe + DisplayPort combinados en un solo cable.
- **[[FireWire (IEEE 1394)]]** — obsoleto, precursor especializado desplazado por USB.
- **[[DisplayPort (DP)]]** — vídeo/audio digital.

## 🔑 Resumen ultra-rápido

- Trío interno: Control (qué hacer) + Dirección (dónde) + Datos (qué).
- Sistema/expansión: FSB (histórico) → QPI/DMI/HyperTransport; ISA → PCI → AGP → PCIe.
- Almacenamiento: SCSI→SAS (profesional) y PATA→SATA (doméstico), ambos paralelo→serie; NVMe va un paso más allá sobre PCIe.
- Externos: FireWire (obsoleto) → USB (universal) / Thunderbolt (PCIe+vídeo combinados).
- Patrón transversal: casi toda evolución de buses va de **paralelo a serie** y **cada generación tiende a doblar la velocidad**.
