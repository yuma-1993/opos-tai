Sin partes móviles, basado normalmente en memoria **Flash NAND**: almacena datos en celdas de transistores mediante carga eléctrica.

> [!note] No todo SSD es flash
> Un SSD también puede fabricarse con **RAM** (DRAM) en vez de NAND. Se usa cuando hace falta **acceso ultrarrápido pero no persistencia** tras un corte de corriente: al ser memoria **volátil**, necesita alimentación constante (a veces con batería/condensador de respaldo). Es un caso nicho/de alto rendimiento; la norma en el mercado es NAND flash.

#### Organización física de la NAND

- La celda es un **transistor de puerta flotante** (*floating gate*): almacena el bit atrapando carga eléctrica de forma aislada. En la **3D NAND** moderna, muchas usan **charge trap** en vez de puerta flotante, pero el concepto de fondo es el mismo: carga atrapada = bit.
- Jerarquía de organización: la NAND se agrupa en matrices llamadas **bloques**; las filas de esa matriz son las **páginas**.

> [!important] Regla de oro de la gestión NAND
> Se **lee y escribe por páginas**, pero se **borra por bloques enteros**. De esta asimetría nacen **TRIM**, el **garbage collection** interno y el **write amplification** (escribir más datos físicamente de los que pide el sistema, por tener que reubicar páginas válidas antes de borrar un bloque).

#### Tecnologías de fabricación (bits por celda)

| Tipo | Bits/celda | Velocidad/durabilidad | Coste |
|---|---|---|---|
| **SLC** (Single) | 1 bit | Máxima velocidad y ciclos de escritura (más duradera) | Más cara |
| **MLC** (Multi) | 2 bits | Intermedia | Media |
| **TLC** (Triple) | 3 bits | Más lenta, menos ciclos | Barata (uso doméstico habitual) |
| **QLC** (Quad) | 4 bits | La más lenta y menos duradera | La más barata |

> [!important]
> A más bits por celda → mayor capacidad por el mismo espacio físico, pero menor velocidad y vida útil (más desgaste por escritura).

#### Componentes internos destacables

| Componente | Función |
|---|---|
| **Controlador** | Chip que gestiona las escrituras/lecturas, el *wear leveling* (repartir el desgaste entre celdas) y el *garbage collection*. |
| **Condensador(es)** | Mantiene la **integridad de los datos de la caché** el tiempo justo para volcarlos a la NAND si la alimentación se corta **inesperadamente**. |

> [!important] PLP (Power Loss Protection)
> Característica típica de **SSD empresariales**: un condensador preserva los datos que están en la caché ante un corte eléctrico repentino. Frase muy "citable" en examen tal cual.

#### Interfaces específicas de SSD

- **M.2**: formato físico tipo "tarjeta de memoria" que reemplaza a **mSATA**. No define un único protocolo: puede llevar señal **SATA** (M.2 SATA, más lento, limitado a ~6 Gbps) o **PCIe/NVMe** (M.2 NVMe, mucho más rápido).
  - Nomenclatura de tamaño: **M2 2280** = 22 mm de ancho × 80 mm de largo.
- **[[NVMe (Non-Volatile Memory Express)]]**: protocolo diseñado específicamente para SSD (no usa SATA), se conecta directamente al bus **[[PCI Express (PCIe)]]**, usando típicamente **4 lanes/carriles**. Mucho menor latencia que AHCI/SATA porque está diseñado desde cero para flash.
- **PCIe** (bus subyacente que usa NVMe): bus de datos serie, hasta **16 lanes**. Velocidad por generación (por lane, en GT/s = giga-transferencias/segundo):
  - PCIe 6: 64 GT/s
  - PCIe 7: 128 GT/s
  - (Patrón: cada generación duplica, potencia de 2: 2⁶=64, 2⁷=128)
- **U.2**: interfaz orientada a **servidores**, permite conectar SSD NVMe con conector similar a SAS/SATA. Ventaja clave: **hot-swapping** (sustitución en caliente sin apagar el equipo), típico en entornos de alta disponibilidad.

> [!note] Las tres familias de interfaz de disco
> Vistas en conjunto ([[Interfaces]]), un disco se conecta hoy por **SATA**, **SAS** o **PCIe**. El SSD puede usar cualquiera de las tres (SATA/M.2 SATA en consumo, SAS o U.2 en servidor, PCIe/NVMe cuando se busca el máximo rendimiento). Un dato de examen: una controladora **SAS admite discos SATA**, pero una controladora SATA **no admite discos SAS** (compatibilidad en un solo sentido).

#### Factores de forma

| Formato | Uso |
|---|---|
| **2,5"** | El más habitual en portátiles y sustitución directa de HDD. |
| **3,5"** | Formato clásico de HDD; los primeros SSD también lo adoptaron por compatibilidad de bahía. |
| **M.2** | Tarjeta pequeña enchufada directamente a la placa base (ver nomenclatura arriba). |
| **NF1** (NGSFF, a veces "M.3") | Formato **empresarial** tipo "regla" (Samsung), alta densidad en servidores. Precursor del **EDSFF**. |

#### SSD vs HDD: ventajas y desventajas

> [!tip] Muy preguntable
> Este cuadro comparativo es de los que más aparecen en test. Apréndetelo cerrado. Compárese con la arquitectura mecánica del [[HDD (Hard Disk Drive)]].

| | **SSD** | **HDD** |
|---|---|---|
| Partes móviles | **No** (más resistente a golpes) | Sí (platos + cabezales) |
| Arranque | Más rápido (no espera velocidad de giro) | Más lento |
| Tiempo de acceso / latencia | **Mucho menor** | Mayor |
| Velocidad de transferencia | **Mayor** | Menor |
| Consumo energético | **Menor** (bueno para portátiles) | Mayor |
| Ruido/calor | Menor | Mayor |
| Capacidad máxima | Menor (aunque la brecha se reduce) | **Mayor** |
| Coste por GB | Más caro | **Más barato** |
| Vida útil | Limitada por **TBW** (ciclos de escritura) | Limitada por desgaste mecánico |

> [!note] Matiz sobre la vida útil
> El límite examinable a retener es que la vida del SSD se mide en **TBW** (TeraBytes Written) y que las **unidades más pequeñas duran menos** (menos celdas entre las que repartir el desgaste). En uso doméstico normal un SSD moderno dura años; el escenario donde el HDD sigue ganando es escritura masiva y continua (ej. un NAS grabando vídeo 4K a diario), no el uso cotidiano.

#### SSD y sistema operativo

> [!important] Por qué el SO necesita "enterarse" de que hay un SSD
> Los sistemas de archivos se diseñaron pensando en **HDD**. Aplicados sin adaptar a un SSD provocan **degradación del rendimiento con el uso** (solo recuperable con un formateo total). Por eso los SO modernos **detectan** que la unidad es SSD y cambian su comportamiento.

- **Desfragmentación**: debe **desactivarse** en SSD. No aporta nada (el acceso aleatorio ya es inmediato, no hay cabezal que mover) y **reduce su vida útil** al consumir ciclos de escritura innecesarios.
- **Alineación de partición/sectores**: los SSD usan sectores de **4 KiB**; los HDD antiguos usaban **512 bytes** (más adelante también 4 KiB). Alinear la partición evita el ciclo *lectura-modificación-escritura* y mejora el rendimiento.
- **TRIM**: comando que avisa al SSD de qué páginas ya no contienen datos válidos (tras borrar un archivo), para que el controlador pueda hacer *garbage collection* con antelación en vez de descubrirlo en el momento de escribir.

| Versión de Windows | Comportamiento ante un SSD |
|---|---|
| **Windows Vista** | No preparado de serie para SSD: solo optimizaba la **alineación de partición**. Incluyó **ReadyBoost** (aprovechar memorias USB como caché), pensado sobre todo para HDD. |
| **Windows 7** | Primer Windows **optimizado de serie** para SSD sin perder compatibilidad con HDD. Al detectar un SSD, automáticamente: activa **TRIM**, desactiva **desfragmentador**, **Superfetch** y **ReadyBoost**, y ajusta el sistema de arranque y la alineación. |
| **Windows 8/10/11** | La herramienta "Optimizar unidades" **sí actúa** sobre un SSD, pero lo que hace es enviar **TRIM/retrim**, no una desfragmentación clásica. |

#### SSD como caché (ZFS)

En **Solaris/OpenSolaris**, con el sistema de archivos **ZFS**, un SSD puede usarse como acelerador en dos modos, solos o combinados:

- **ZIL** (*ZFS Intent Log*), sobre un dispositivo **SLOG**: acelera las **escrituras síncronas**.
- **L2ARC** (*Level 2 Adaptive Replacement Cache*): **caché de lectura** de segundo nivel.

---

**Conexiones con otros conceptos TAI:**
- [[HDD (Hard Disk Drive)]] — comparativa directa (tabla de arriba) y contraste de arquitectura mecánica vs electrónica.
- [[Interfaces]] y [[WWN (World Wide Name)]] — SAS como una de las tres familias de interfaz, e identificador de dispositivo en entornos SAS/servidor.
- [[NVMe (Non-Volatile Memory Express)]] y [[PCI Express (PCIe)]] — el "camino rápido" que aprovecha al máximo un SSD.
- RAID (Parte III de B2-T2 Periféricos y almacenamiento) — un SSD puede ser el disco físico dentro de cualquier nivel RAID; el TBW y el *wear leveling* importan especialmente en RAID 5/6 por el desgaste añadido de la paridad.
