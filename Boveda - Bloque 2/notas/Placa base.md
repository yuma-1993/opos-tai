La placa base es la vía de comunicación física entre los componentes del ordenador (microprocesador, tarjetas de expansión, memoria, etc.): proporciona las líneas eléctricas y las señales de control necesarias para que todas las transferencias de datos se lleven a cabo de manera rápida y fiable. Es, literalmente, el soporte físico sobre el que corren todos los [[Bus de comunicación|buses]] del sistema (ver [[Buses]] para el mapa completo).

> [!note] Diferencia con `B2 - T1 INFORMATICA BASICA`
> Esa nota trae la versión resumen de examen (§11). Esta nota conecta cada pieza de la placa con su nota propia — muchas de ellas ya desarrolladas por separado (FSB, buses de expansión, RTC...) — para que la placa base se entienda como el **mapa** que las conecta a todas, no como una lista de siglas sueltas.

## El chipset: el ayudante de la CPU

El chipset es circuitería auxiliar que descarga a la CPU de tareas de coordinación:

- **Northbridge** (Chipset Norte): lo rápido — el acceso a memoria.
- **Southbridge** (Chipset Sur): lo lento — la E/S.

> [!note] Matiz moderno (conocimiento general)
> En las placas actuales, el **controlador de memoria** y los carriles **PCIe** que antes vivían en el Northbridge se han integrado **dentro del propio chip de la CPU**. Lo que queda en la placa como chip aparte es una versión reducida del antiguo Southbridge, a veces llamado **PCH** (Platform Controller Hub) en placas Intel. La distinción Norte/Sur sigue siendo válida para entender el concepto (rápido vs lento), aunque físicamente ya no siempre sean dos chips separados en la placa.

## Cómo se llega a la memoria: del FSB a los enlaces punto a punto

El bus que unía CPU, chipset y memoria era el **[[FSB (Front-Side Bus)]]** — su velocidad la marca el [[Reloj]] del sistema. Hoy está sustituido por enlaces punto a punto dedicados: **QPI**/**DMI** (Intel) o **HyperTransport** (AMD). Ver la nota de FSB para el porqué del cambio (cuello de botella de un bus compartido).

## Ranuras de expansión: de ISA a PCIe

Las tarjetas de expansión (gráficas, de red, de sonido...) se conectan mediante ranuras que han evolucionado de **[[Buses de expansión internos (ISA, PCI, AGP)|ISA/PCI/AGP]]** (paralelo, compartido) a **[[PCI Express (PCIe)]]** (serie, por *lanes*, el estándar actual).

## Jerarquía de caché

La **caché de nivel 1 (L1)** está dentro de la propia CPU, dividida en dos (datos e instrucciones) — similar a la separación de la arquitectura Harvard frente a la memoria principal. L1 y L2 son **por núcleo**; L3 es **compartida** por todos los núcleos del procesador.

> [!note] Dónde profundizar
> El detalle de niveles, correspondencia y tipos de caché está en [[Memoria Caché]]; el *porqué* la caché es rápida (es SRAM, sin refresco) está en [[Memoria RAM]]; las políticas de sustitución y actualización (write-through/write-back) están en [[B2 - T1 INFORMATICA BASICA]] §12. La idea general de "guardar una copia cerca para no ir al sitio lento" es [[Caching]].

## NVRAM de la placa: el reloj que no es el reloj

La placa lleva su propia **NVRAM** (respaldada por una **pila**) para mantener fecha, hora y configuración aunque el equipo esté apagado. Esa fecha/hora es precisamente el **RTC** (Real-Time Clock) descrito en [[Reloj]] — un reloj completamente distinto al que marca los ciclos de ejecución de la CPU, aunque ambos compartan el nombre "reloj". Ver también [[Memoria RAM]] para la NVRAM como familia de memoria no volátil.

## Firmware de arranque: BIOS vs UEFI

| | [[BIOS]] | [[UEFI]] |
|---|---|---|
| Nombre | Basic Input Output System | Unified Extensible Firmware Interface |
| Interfaz | Modo carácter | Gráfica |
| Particionamiento | MBR (hasta 4 particiones) | GPT (más de 4 particiones) |

> [!note] Qué hace en realidad el firmware (conocimiento general)
> Antes de que el sistema operativo exista como tal en memoria, alguien tiene que **encender y comprobar** el hardware (el llamado **POST**, Power-On Self-Test: memoria, teclado, discos...) y luego **entregarle el control** al gestor de arranque del disco. Eso es lo que hacen BIOS/UEFI: el primer código que se ejecuta al pulsar el botón de encendido, antes de que exista ningún sistema operativo cargado.
>
> El detalle de cada uno (por qué MBR limita a 2 TiB, qué es Secure Boot, etc.) está en [[BIOS]] y [[UEFI]] por separado.

## 🔑 Resumen ultra-rápido

- Placa base = soporte físico de todos los buses del sistema.
- Chipset: Northbridge (rápido, memoria) / Southbridge (lento, E/S) — hoy en día parcialmente integrado en la propia CPU.
- FSB (histórico) → QPI/DMI (Intel) / HyperTransport (AMD).
- Ranuras de expansión: ISA → PCI → AGP → PCIe (actual).
- Caché L1/L2 por núcleo, L3 compartida; es SRAM, sin refresco.
- NVRAM de placa + pila = mantiene el RTC (fecha/hora), distinto del reloj de ciclos de la CPU.
- BIOS (carácter, MBR) vs UEFI (gráfico, GPT); ambos hacen el POST antes de arrancar el SO.

---

**Conexiones con otros conceptos TAI:**
- [[Buses]], [[Bus de comunicación]] — el mapa general de buses que la placa soporta físicamente.
- [[FSB (Front-Side Bus)]], [[Buses de expansión internos (ISA, PCI, AGP)]], [[PCI Express (PCIe)]] — desarrollo de cada bus mencionado aquí.
- [[Reloj]] — reloj de ciclos (FSB) vs RTC (NVRAM de placa), dos conceptos distintos que conviven en la placa.
- [[Memoria Caché]], [[Memoria RAM]] y [[Caching]] — tecnología de la caché y de la NVRAM.
- [[CPU - Central Processing Unit]] — a quién sirve todo lo anterior.
- [[BIOS]] y [[UEFI]] — desarrollo completo del firmware de arranque y sus esquemas de particionamiento (MBR/GPT).
- [[B2 - T1 INFORMATICA BASICA]] — versión resumen de examen.
