Interfaz de conexión de alta velocidad desarrollada por **Intel junto con Apple**, con nombre en clave original **Light Peak**. Su idea central: **combinar dos buses en un mismo conector físico**.

> [!important] La idea que lo explica todo
> Thunderbolt transmite **[[PCI Express (PCIe)]]** (datos de alta velocidad) y **[[DisplayPort (DP)]]** (vídeo) como **dos señales serie independientes** por el mismo cable, y además reparte energía DC por ese mismo cable. Un solo puerto, tres cosas a la vez: datos, vídeo y alimentación.

## Características

- **Múltiples protocolos**: puede encapsular también HDMI y Ethernet dentro de la misma conexión.
- **QoS** (Quality of Service): prioriza el tráfico según el tipo (ej. vídeo en tiempo real frente a una simple transferencia de archivo).
- **Bidireccional**: transmite y recibe simultáneamente por el mismo canal.
- **Daisy-chain**: permite encadenar varios periféricos desde un único puerto (hasta seis dispositivos, según el estándar).

## Versiones

| Versión | Velocidad | Conector |
|---|---|---|
| Thunderbolt 1 | 10 Gbps | Mini DisplayPort |
| Thunderbolt 2 | 20 Gbps | Mini DisplayPort |
| Thunderbolt 3 | 40 Gbps | **USB-C** (admite dispositivos USB) |
| Thunderbolt 4 | 40 Gbps | USB-C |
| Thunderbolt 5 | — | USB-C |

> [!note] A partir de Thunderbolt 3, el conector es USB-C
> Esto permite que un mismo puerto físico acepte tanto periféricos Thunderbolt como dispositivos USB normales — aunque no todo puerto USB-C es Thunderbolt. Un puerto Thunderbolt 3 sí admite ambos.

> [!tip] Patrón de duplicación, otra vez
> TB1→TB2→TB3 dobla la velocidad en cada salto (10→20→40 Gbps), el mismo patrón de "cada generación dobla" que ves en PCIe, SATA/SAS, USB o las generaciones DDR de [[Memoria RAM]].

---

**Conexiones con otros conceptos TAI:**
- [[PCI Express (PCIe)]] y [[DisplayPort (DP)]] — los dos buses que Thunderbolt combina.
- [[USB]] — comparte conector desde TB3 y es su principal "competidor/complemento" en conectividad externa.
- [[FireWire (IEEE 1394)]] — el bus especializado de alto rendimiento que precedió a este rol.
- [[B2 - T2 PERIFERICOS Y ALMACENAMIENTO]] — cuadro comparativo Thunderbolt vs USB en la Parte V.
