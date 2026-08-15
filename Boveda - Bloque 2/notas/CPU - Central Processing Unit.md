Es quien finalmente procesa los datos del periférico. Cuando recibe el aviso del PIC, suspende momentáneamente su tarea actual, atiende la interrupción y luego reanuda lo que estaba haciendo. Es el destino final del control en el flujo de entrada (ver [[B2 - T2 PERIFERICOS Y ALMACENAMIENTO]]).

> [!note] Alcance de esta nota
> El detalle completo del ciclo **Fetch-Decode-Execute** vive en [[B2 - T1 INFORMATICA BASICA]] — ahí está la versión "de examen". Los registros (MAR, MDR, PC, IR...) tienen su propia nota en [[Registros clave]], los [[Modos de direccionamiento]] la suya, y la comparación de filosofías de diseño en [[CISC vs RISC]] (con [[Pipeline]], [[RISC-V]] y [[SoC vs APU]] aparte). Esta nota se queda con lo que da contexto propio a la CPU como concepto: sus piezas internas mínimas y su evolución de **un núcleo a varios**.

## Componentes principales

- **Unidad de Control (UC)**: el "director de orquesta". Busca instrucciones, las decodifica y coordina qué hace cada parte de la CPU. No calcula nada, solo gobierna.
- **ALU (Unidad Aritmético-Lógica)**: la "calculadora". Suma, resta, AND, OR, desplazamientos de bits... Ejecuta lo que la UC le manda.
- **Decodificador**: traduce el código máquina (binario) a una señal que la CPU entiende como "qué operación hay que hacer".
- **Secuenciador**: el que dispara la ejecución paso a paso de la instrucción ya decodificada.

> [!important] Orden lógico
> Fetch → **Decodificador** (traduce) → **Secuenciador** (dispara los pasos) → **ALU** (si la operación calcula algo), todo bajo el gobierno de la **UC**. Ningún componente hace el trabajo de otro: la UC no calcula, la ALU no decide qué instrucción toca.

## De un núcleo a varios

### Procesador mono-núcleo

Un solo núcleo → ejecuta **una** instrucción/tarea a la vez, de forma estrictamente secuencial. Fue el estándar en las primeras generaciones de CPU (ej. **Pentium**, **Pentium Pro**), donde la **velocidad de reloj** era el factor clave de rendimiento: más frecuencia = instrucciones completadas más rápido, al no poder repartir trabajo entre núcleos.

> [!note] ¿Dónde sobrevive hoy?
> Con la llegada del multi-núcleo, el mono-núcleo quedó relegado a **sistemas embebidos y de control** donde no hace falta paralelismo (electrodomésticos, dispositivos dedicados a una tarea simple).

### Procesador multi-núcleo

Varios núcleos integrados en el mismo chip, cada uno capaz de ejecutar su propio hilo → varias tareas en paralelo real, no solo aparente. El rendimiento sube porque el trabajo se **reparte** entre núcleos en vez de encolarse en uno solo.

- **Dual-core / doble núcleo**: dos procesadores distintos dentro del mismo circuito integrado (ej. **Core 2 Duo**). No es "un núcleo más rápido", son **dos unidades de ejecución completas** compartiendo chip.
- **Quad-core**: cuatro núcleos — mejora notable en cargas que se paralelizan bien: edición de vídeo, juegos, modelado 3D.

> [!important] Arbitraje entre núcleos
> En un procesador multi-núcleo existe un mecanismo de **arbitraje** que reparte el ancho de banda (acceso al bus, a la memoria) entre los núcleos de forma equilibrada, evitando que unos se queden esperando mientras otros acaparan el recurso — el mismo problema de fondo que resuelve un [[PIC - Programmable Interrupt Controller]] al arbitrar varias IRQ, aplicado aquí al acceso a memoria/bus en vez de a interrupciones. Ver [[Bus de comunicación]].

> [!note] Dato histórico/anecdótico
> La llegada de los primeros Dual Core exigió fuentes de alimentación con más potencia y conectores específicos (ej. modelos como la SILVERSTONE ZEUS ST65ZF de la época), porque meter dos núcleos completos en un chip dispara el consumo frente a un mono-núcleo equivalente.

### Mono-núcleo vs multi-núcleo, de un vistazo

| | Mono-núcleo | Multi-núcleo |
|---|---|---|
| Ejecución | Una instrucción/tarea a la vez, secuencial | Varios hilos en paralelo real |
| Factor de rendimiento clave | Velocidad de reloj | Reparto de trabajo entre núcleos + arbitraje |
| Uso hoy | Sistemas embebidos, control simple | Estándar en PC, portátiles, servidores |
| Ejemplo histórico/actual | Pentium, Pentium Pro | Core 2 Duo (2 núcleos), quad-core (4 núcleos) |

---

**Conexiones con otros conceptos TAI:**
- [[B2 - T1 INFORMATICA BASICA]] — arquitectura completa: ciclo Fetch-Decode-Execute, modos de direccionamiento.
- [[Registros clave]], [[Modos de direccionamiento]], [[CISC vs RISC]], [[Pipeline]], [[RISC-V]], [[SoC vs APU]] — desarrollo en profundidad de cada pieza de la arquitectura de la CPU.
- [[B2 - T2 PERIFERICOS Y ALMACENAMIENTO]], [[IRQ - Interrupt Request]], [[ISR - Interrupt Service Rutine]], [[PIC - Programmable Interrupt Controller]], [[controlador]], [[tabla de vectores de interrupción]], [[offset]] — la cadena completa por la que un periférico interrumpe a la CPU.
- [[Bus de comunicación]] — el recurso que el arbitraje entre núcleos reparte, y por el que la CPU habla con el resto del sistema.
