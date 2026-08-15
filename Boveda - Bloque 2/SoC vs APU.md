Dos formas de "meter más de un componente en el mismo chip", que no significan lo mismo aunque se confunden a menudo.

- **SoC** (System on a Chip): **todo** integrado en un solo chip → CPU, GPU, RAM, controladores de E/S, módem, etc. Típico en móviles y tablets.
- **APU** (Accelerated Processing Unit): caso más concreto y limitado, **solo CPU + GPU** en el mismo chip. Término popularizado sobre todo por AMD.

> [!important]
> SoC es más amplio que APU: **todo APU podría verse como un SoC muy incompleto** (le falta integrar RAM, módem, etc.), pero no todo SoC es un APU (un SoC de móvil integra muchísimo más que "solo" CPU+GPU).

> [!note] Ejemplos para fijarlo (conocimiento general, no viene de la fuente original)
> **SoC**: los chips de los smartphones (ej. familias Snapdragon o Apple Silicon), que integran CPU, GPU, módem y más en una sola pieza. **APU**: procesadores de escritorio/portátil que combinan CPU y gráficos integrados en el mismo chip (ej. la gama AMD Ryzen con gráficos Radeon integrados), sin llegar a integrar todo lo que sí integra un SoC móvil.

> [!tip] Por qué existen
> Integrar más componentes en un mismo chip reduce el espacio físico necesario, acorta las distancias que tiene que recorrer la señal (más velocidad, menos consumo) y abarata la fabricación al necesitar menos piezas separadas — la misma lógica de fondo que lleva a un procesador [[CPU - Central Processing Unit|multi-núcleo]] a meter varios núcleos en un único chip en vez de en chips separados.

## 🔑 Resumen ultra-rápido

- SoC = todo el sistema (CPU+GPU+RAM+módem...) en un chip; típico en móviles.
- APU = solo CPU+GPU en un chip; término más asociado a AMD en PC de escritorio/portátil.
- SoC ⊃ APU en alcance de integración.

---

**Conexiones con otros conceptos TAI:**
- [[CPU - Central Processing Unit]] — la misma lógica de integración que lleva al diseño multi-núcleo.
- [[CISC vs RISC]] — los SoC móviles suelen usar núcleos de diseño RISC (ARM) por su menor consumo.
- [[B2 - T1 INFORMATICA BASICA]] — sección de arquitectura de computadores donde se introduce esta distinción.
