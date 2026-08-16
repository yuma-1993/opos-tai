Antes de [[PCI Express (PCIe)]], las tarjetas de expansión (gráficas, de red, de sonido...) se conectaban a la placa base mediante buses **paralelos y compartidos**, la misma familia de diseño que PATA o SCSI en almacenamiento (ver [[Bus de comunicación]]). Su evolución es una más de tantas historias "paralelo → serie" del temario.

## ISA (Industry Standard Architecture)

El bus de expansión más antiguo de los tres. Paralelo, de baja velocidad, compartido por todos los dispositivos conectados a él. Quedó obsoleto mucho antes que PCI y no se usa en equipos actuales.

## PCI (Peripheral Component Interconnect)

Sucesor de ISA: bus paralelo **genérico y compartido**, usado para conectar todo tipo de tarjetas de expansión (gráficas, red, sonido, capturadoras...) durante los años 90 y 2000. Al ser compartido, todos los dispositivos conectados se repartían el mismo ancho de banda.

## AGP (Accelerated Graphics Port)

A diferencia de PCI (genérico), AGP nace como un bus **dedicado en exclusiva a la tarjeta gráfica** — el primer paso hacia sacar los gráficos del bus compartido y darles una vía propia de alto rendimiento. También obsoleto hoy.

## PCIe: el punto de llegada

**PCI Express** rompe con el esquema paralelo/compartido: es serie, punto a punto, organizado en *lanes* agrupables (x1, x4, x8, x16), y sirve tanto para gráficas como para SSD NVMe, red o cualquier tarjeta de expansión moderna. Ver [[PCI Express (PCIe)]] para el detalle completo.

| Bus | Transmisión | Alcance | Estado |
|---|---|---|---|
| **ISA** | Paralelo | Genérico, baja velocidad | Obsoleto |
| **PCI** | Paralelo | Genérico, compartido | Obsoleto |
| **AGP** | Paralelo | Dedicado a gráficos | Obsoleto |
| **PCIe** | Serie (lanes) | Genérico, alto rendimiento | Actual |

> [!important] El hilo conductor
> ISA → PCI es "más generación del mismo esquema paralelo compartido". PCI → AGP es "quitarle los gráficos al bus compartido y darles vía propia". AGP → PCIe es el salto de fondo: de paralelo a serie, igual que PATA→SATA o SCSI→SAS en almacenamiento.

---

**Conexiones con otros conceptos TAI:**
- [[PCI Express (PCIe)]] — el estándar actual, sucesor final de esta cadena.
- [[B2 - T2 PERIFERICOS Y ALMACENAMIENTO]] — tabla de buses gráficos dentro de la Parte IV.
- [[Bus de comunicación]] — clasificación general paralelo vs serie en la que encaja esta evolución.
