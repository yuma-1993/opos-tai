Es un [[Bus de comunicación]] interno de alta velocidad que conecta la [[Placa base]] con tarjetas de expansión y dispositivos como tarjetas gráficas, unidades SSD NVMe, tarjetas de red o controladoras. A diferencia de los buses paralelos antiguos ([[Buses de expansión internos (ISA, PCI, AGP)|ISA, PCI, AGP]]), PCIe utiliza una comunicación serie punto a punto basada en "carriles" (_lanes_) independientes que pueden agruparse (x1, x4, x8, x16) para multiplicar el ancho de banda según las necesidades del dispositivo. Es **bidireccional** (cada carril transmite y recibe datos de forma simultánea mediante líneas separadas), muy escalable y ha evolucionado en sucesivas generaciones (PCIe 3.0, 4.0, 5.0...), duplicando la velocidad en cada una — el mismo patrón de duplicación que en [[USB]], SATA/SAS o las generaciones DDR de [[Memoria RAM]]. Actualmente es el estándar dominante para la conexión interna de dispositivos que requieren gran rendimiento dentro del computador.

Por sus dos señales serie, es también uno de los dos buses que combina **[[Thunderbolt]]** en un único cable (junto a [[DisplayPort (DP)]]).

---

**Conexiones con otros conceptos TAI:**
- [[Buses de expansión internos (ISA, PCI, AGP)]] — la evolución que PCIe culmina.
- [[Thunderbolt]] — lo usa como uno de sus dos buses combinados.
- [[NVMe (Non-Volatile Memory Express)]] y [[SSD (Solid State Drive)]] — el protocolo/dispositivo que más aprovecha PCIe hoy.
- [[Buses]] — índice general de buses.