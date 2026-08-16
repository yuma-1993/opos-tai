La memoria RAM (*Random Access Memory*, memoria de acceso aleatorio) es la memoria principal y temporal de un dispositivo: aquí se cargan los datos e instrucciones de los programas que están en uso en cada momento, para que el procesador pueda acceder a ellos a velocidad muy alta. No procesa información ni transfiere datos entre componentes — solo la almacena para que otros la usen.

- **Volátil**: los datos solo se conservan mientras el dispositivo tiene alimentación eléctrica. Al apagarlo, se pierden.
- **Rápida**: muy superior a un [[HDD (Hard Disk Drive)]] o [[SSD (Solid State Drive)]], lo que permite respuestas casi inmediatas.
- **Físicamente**: en ordenadores, la RAM son módulos/tarjetas (normalmente encapsulado **DIMM**) que se conectan a la [[Placa base]]; en portátiles el formato reducido es **SO-DIMM**. En dispositivos móviles suele venir **soldada**.

> [!note] Diferencia con la nota de [[B2 - T1 INFORMATICA BASICA]]
> Esa nota trata la RAM **dentro del ciclo de la CPU** (registros, buses, jerarquía de caché, latencias RAS/CAS). Esta nota se centra en la RAM como **tecnología**: sus familias, por qué existen tantos tipos, y cómo se ha ido acelerando generación tras generación.

## Volátil vs no volátil: la primera gran división

> [!important] Idea clave
> "RAM" y "volátil" no son sinónimos exactos. La inmensa mayoría de la RAM (SRAM, DRAM) sí es volátil, pero existen variantes de **acceso aleatorio no volátiles** (NVRAM, MRAM) que conservan los datos sin alimentación, usando un mecanismo físico distinto al de la carga eléctrica pura.

| Familia | Volátil | Cómo guarda el bit |
|---|---|---|
| **SRAM** | Sí | Biestable (flip-flop), no necesita refresco |
| **DRAM** y derivadas (SDR, DDR...) | Sí | Carga eléctrica en un condensador, necesita **refresco** periódico |
| **NVRAM** | No | RAM de acceso aleatorio con respaldo (p. ej. batería) que evita perder los datos al cortar la alimentación |
| **MRAM** | No | Campo magnético, no carga eléctrica (ver más abajo) |

> [!note] Y la memoria Flash, ¿dónde queda?
> La NAND Flash (la base del [[SSD (Solid State Drive)]]) también es de acceso no volátil, pero **no es RAM**: no es de acceso aleatorio a nivel de bit/byte de la misma forma, se organiza en páginas/bloques y tiene ciclos de escritura limitados. DRAM y NAND comparten la idea de "celda que almacena carga", pero difieren en velocidad y en si esa carga sobrevive sin alimentación.

## SRAM vs DRAM: por qué coexisten

| | **SRAM** | **DRAM** |
|---|---|---|
| Necesita refresco | No | Sí (periódico, para no perder la carga) |
| Velocidad | Mayor | Menor |
| Coste/densidad por bit | Más cara, menos densa | Más barata, más densa (más capacidad en el mismo espacio) |
| Uso típico | **[[Memoria Caché]]** (L1/L2/L3) | **Memoria principal** (los módulos DIMM que se compran) |

> [!important] Por qué la caché es SRAM y la RAM "normal" es DRAM
> No perder tiempo en refrescar la carga es lo que hace a la SRAM más rápida — perfecta para la caché, donde la velocidad importa más que la cantidad. La DRAM sacrifica algo de velocidad (por el refresco) a cambio de ser mucho más barata y densa, ideal para tener muchos GB de memoria principal.

## Evolución de la DRAM: de asíncrona a síncrona

Antes de llegar a la SDRAM (la base de toda la RAM moderna), la DRAM pasó por una fase **asíncrona** (no sincronizada con el reloj del sistema):

| Tecnología | Año / contexto | Mejora clave | Tiempo de acceso |
|---|---|---|---|
| **FPM-RAM** (Fast Page Mode) | Popular con 486 y primeros Pentium | Inspirada en el *Burst Mode* del Intel 486: el controlador envía **una** dirección y recibe esa **y varias consecutivas** sin tener que volver a direccionar cada vez | 70 o 60 ns |
| **EDO-RAM** (Extended Data Output) | 1994 | Direcciona la siguiente columna **mientras** todavía se está leyendo la anterior, eliminando estados de espera | 40 o 30 ns |
| **BEDO-RAM** (Burst EDO) | 1997, competidora directa de la SDRAM | Generadores internos de direcciones, accede a más de una posición por ciclo (~50% mejor que EDO) | — |

> [!note] Por qué BEDO perdió la carrera
> BEDO nunca se comercializó a gran escala: Intel y otros fabricantes apostaron por los esquemas **síncronos** (SDRAM), que además de heredar ideas de direccionamiento añadían señales de reloj propias — y esa fue la vía que se consolidó.

> [!tip] Analogía para FPM/EDO
> Es como recorrer una calle: la primera vez necesitas el nombre completo de la calle (la dirección), pero para las casas siguientes solo hace falta el número — no hay que repetir todo el proceso de direccionamiento.

**SDRAM** (Synchronous DRAM) sincroniza sus operaciones con el reloj del sistema, y es la familia que ha llegado hasta hoy: primero como **SDR** y después como **DDR**.

## SDR vs DDR: la base de toda RAM moderna

- **SDR** (Single Data Rate): realiza **una** operación de lectura/escritura por ciclo de reloj.
- **DDR** (Double Data Rate): realiza **dos** operaciones por ciclo — una en el **flanco de subida** y otra en el **flanco de bajada** de la señal —, duplicando el rendimiento efectivo sin duplicar la frecuencia.

> [!example] ¿Qué significa "operación por ciclo de reloj"?
> Un ciclo de reloj completo va de 0 a 1 y vuelve a 0. La SDR aprovecha un solo momento de ese ciclo para leer/escribir; la DDR aprovecha **dos** momentos (subida y bajada), literalmente el doble de trabajo al mismo reloj.

> [!example] Cálculo real: DDR-400 / PC-3200
> Bus de 200 MHz. Al ser DDR, se dobla: 200 × 2 = 400 (de ahí "DDR-400"). Con un canal de 64 bits (8 bytes): 200 × 2 × 8 B = **3200 MB/s**, de ahí el nombre comercial **PC-3200** (su capacidad máxima de transferencia). Mismo cálculo que aparece en [[B2 - T1 INFORMATICA BASICA]].

### Generaciones DDR SDRAM

| Generación | Rasgo diferencial | Dato clave |
|---|---|---|
| **DDR** | Primera con doble tasa de datos | Base de la que parten todas las siguientes |
| **DDR2** | Búferes de E/S al doble de frecuencia que el núcleo → 4 transferencias por ciclo de reloj | Opera a 0 y 1,8 V (frente a 0–2,5 V de DDR) → **~50% menos consumo** |
| **DDR3** | Integrados de 1 a 8 GiB (hasta 16 GiB por módulo) | Bajo voltaje (1,5–1,2 V) → menor consumo global, aunque con **latencia proporcionalmente mayor**, compensada por más velocidad de transferencia |
| **DDR4** | 288 pines DIMM, canales de memoria independientes | 1,6–3,2 Gb por pin; tasa de transferencia hasta **3200 MT/s** |
| **DDR5** | Arquitectura de **canal dividido**: cada módulo son dos sub-canales independientes de 32 bits | Hasta **8400+ MT/s**; frecuencia base 4800 MHz; reguladores de voltaje montados en el propio módulo (ya no en la placa base); pasa de 12 a 16 canales, llevando el límite de 64 GB a **128 GB** en placas de consumo |

> [!important] Patrón que se repite en toda la informática de buses/memoria
> DDR2→DDR3→DDR4→DDR5 sigue el mismo patrón que ves en [[PCI Express (PCIe)]] (PCIe 6→7) o en SATA/SAS/USB dentro de [[B2 - T2 PERIFERICOS Y ALMACENAMIENTO]]: **cada generación aproximadamente dobla la velocidad** y suele bajar el voltaje/consumo. Si en examen no recuerdas el número exacto, razona por duplicación.

### Rambus: la vía que no ganó

Familia de DRAM propietaria, alternativa a la SDRAM/DDR estándar: **RDRAM** (Rambus DRAM) y sus sucesoras **XDR** y **XDR2** (eXtreme Data Rate). No llegaron a desplazar a la DDR como estándar de memoria principal de consumo.

## RAM especializada (uso concreto, no memoria principal genérica)

| Tipo | Para qué | Detalle |
|---|---|---|
| **VRAM** (*Video RAM*) | Memoria gráfica | **Dual-Ported**: puede ser escrita por la CPU y leída por el RAMDAC **al mismo tiempo**. En procesadores de 8 bits era la única memoria accesible directamente por el chip gráfico (la CPU debía pasar por él). Variante **SONIC/SAM**: un registro lineal de acceso secuencial (como una cinta) que alimenta al RAMDAC sin necesitar cálculo de direcciones, por lo que se puede leer más rápido que la RAM normal. |
| **GDDR** | Tarjetas gráficas | Sigue el estándar DDR (dos transferencias por ciclo), pero optimizada para **frecuencias de reloj más altas**, acortando los tiempos de acceso frente a la DDR convencional — necesario por el enorme volumen de datos que procesa una GPU. |
| **HBM** (*High Bandwidth Memory*) | Aceleradores gráficos de alto rendimiento y dispositivos de red | Interfaz de alto rendimiento para **DRAM apiladas en 3D**. |
| **LPDDR** (*Low Power DDR*) | Dispositivos móviles | Variante DDR orientada a bajo consumo (ver tabla de tipos de memoria en [[B2 - T1 INFORMATICA BASICA]]). |

> [!example] Dato curioso (VRAM > RAM)
> Algunos modelos japoneses de MSX2 tenían **64 KiB de RAM** pero **128 KiB de VRAM** — la memoria de vídeo podía superar a la memoria principal del propio equipo.

## No volátiles emparentadas con la RAM

- **NVRAM** (*Non-Volatile RAM*): RAM de acceso aleatorio que no pierde los datos al cortar la alimentación, típicamente porque lleva **una pila/batería** de respaldo (ej. la NVRAM de la placa base que mantiene fecha, hora y configuración de la BIOS/UEFI).
- **MRAM** (*Magnetoresistive RAM*): en desarrollo desde los años 90; no usa carga eléctrica sino **campos magnéticos**. Cada celda tiene dos discos ferromagnéticos separados por una fina capa aislante: uno fijo (imán permanente con polaridad dada) y otro que varía según un campo externo; una malla de estas celdas forma el chip. No se ha generalizado porque Flash y DRAM ya cubren de sobra las necesidades del mercado, aunque en teoría combinaría velocidad tipo RAM con persistencia sin alimentación.

## Qué se guarda en la RAM y qué pasa si se llena

- El sistema operativo y sus procesos.
- Las aplicaciones abiertas (navegador, editor de texto, juegos).
- Datos temporales de uso frecuente (pestañas del navegador, portapapeles).

> [!important] Memoria virtual
> Si la RAM se llena, el sistema recurre al disco ([[HDD (Hard Disk Drive)]] o [[SSD (Solid State Drive)]]) como "RAM virtual" (swap). Es mucho más lento que la RAM real, y es la causa típica de que un equipo con poca RAM se sienta lento aunque la CPU esté descansada.

## Latencias: las cuatro fases de un mismo acceso

Una celda de DRAM se localiza como una casilla dentro de una rejilla (**tablero**/banco): primero hay que decir en qué **fila** y luego en qué **columna**. Acceder a un dato no es instantáneo — pasa por varias fases, cada una con su propio tiempo:

| Latencia | Qué mide |
|---|---|
| **ACTIVE** | Tiempo en activar un tablero (abrir la fila donde está el dato) |
| **RAS** (*Row Address Strobe*) | Tiempo en colocarse sobre una fila |
| **CAS** (*Column Address Strobe*) | Tiempo en colocarse sobre una columna o celda, ya dentro de la fila activada |
| **PRECHARGE** | Tiempo en desactivar un tablero (cerrar la fila abierta, antes de poder activar una distinta) |

> [!important] Lo que se pregunta en examen: el total
> El tiempo que tarda la memoria en proporcionar el dato es la suma **ACTIVE + RAS + CAS**. El **PRECHARGE** no siempre entra en esa cuenta: solo hace falta cuando el siguiente acceso pide una fila **distinta** a la que ya está abierta — si el dato siguiente cae en la misma fila, no hay que precargar nada y el acceso es más rápido.

> [!note] Dónde se ve esto en la práctica (conocimiento general)
> Estas latencias son las que aparecen en la notación comercial de un módulo, por ejemplo **DDR4-3200 CL16**: el "CL16" es la latencia CAS expresada en **ciclos de reloj** (16 ciclos), no en nanosegundos — por eso, a igual CL, un módulo con más MHz es en la práctica más rápido en tiempo real, aunque el número CL sea el mismo.

## 🔑 Resumen ultra-rápido

- RAM = memoria principal, volátil, rápida. Módulos DIMM (SO-DIMM en portátiles) o soldada en móviles.
- Volátil (SRAM, DRAM) vs no volátil de acceso aleatorio (NVRAM con batería, MRAM con magnetismo) — la Flash del SSD es no volátil pero no es RAM.
- SRAM = sin refresco, rápida, cara → caché. DRAM = con refresco, barata, densa → memoria principal.
- DRAM asíncrona (histórica): FPM → EDO → BEDO, cada una reduce tiempos de espera; perdieron frente a la síncrona (SDRAM).
- SDR = 1 operación/ciclo. DDR = 2 operaciones/ciclo (subida y bajada) → duplica rendimiento sin duplicar frecuencia.
- Generaciones DDR2→DDR5: cada una dobla velocidad aprox. y baja voltaje — mismo patrón que PCIe/SATA/SAS/USB.
- Rambus (RDRAM/XDR/XDR2): vía alternativa a DDR que no se impuso.
- RAM especializada: VRAM (dual-ported, gráficos), GDDR (DDR de alta frecuencia para GPU), HBM (DRAM 3D apilada), LPDDR (bajo consumo, móvil).
- Si la RAM se llena, el SO usa el disco como memoria virtual → mucho más lento.
- Latencia total = ACTIVE + RAS + CAS. PRECHARGE solo cuenta si hay que cambiar de fila. El "CL" comercial (ej. CL16) es la latencia CAS en ciclos de reloj.

---

**Conexiones con otros conceptos TAI:**
- [[B2 - T1 INFORMATICA BASICA]] — RAM dentro del ciclo de la CPU: jerarquía de memoria, caché SRAM, latencias RAS/CAS/ACTIVE/PRECHARGE, políticas write-through/write-back.
- [[SSD (Solid State Drive)]] — contraste volátil (RAM) vs no volátil (NAND Flash), y el caso nicho de SSD fabricados con RAM.
- [[Jerarquía de memoria]] y [[Memoria Caché]] — el escalón inmediatamente más rápido que la RAM.
- [[Reloj]] — las latencias RAS/CAS/ACTIVE/PRECHARGE se cuentan en ciclos de esa misma señal.
- [[PCI Express (PCIe)]] y [[B2 - T2 PERIFERICOS Y ALMACENAMIENTO]] — el mismo patrón de "cada generación dobla la velocidad" que en las generaciones DDR.
