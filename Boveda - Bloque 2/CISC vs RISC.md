La CPU puede seguir dos filosofías de diseño de su conjunto de instrucciones (ISA): **CISC** o **RISC**.

> [!note] Diferencia con `B2 - T1 INFORMATICA BASICA`
> Esa nota trae la tabla resumen de examen. Esta nota se queda con el **porqué histórico** de cada enfoque y con lo que de verdad las distingue hoy, más allá de la lista de rasgos.

## Por qué nacieron dos filosofías distintas

> [!note] Contexto histórico (conocimiento general, no literal de la fuente)
> **CISC** nació en una época en la que la memoria era **cara y escasa**: convenía que cada instrucción hiciera "mucho trabajo" (operaciones complejas directamente sobre memoria) para que los programas ocuparan menos espacio, aunque eso obligara a una **lógica programada** (microcódigo) más lenta para interpretarlas. **RISC** nació cuando la memoria se abarató y los compiladores mejoraron: ya no hacía falta exprimir cada instrucción, así que se simplificaron al máximo (una por ciclo, tamaño fijo) para poder ejecutar muchísimas, muy rápido, con **lógica cableada** (hardware puro, sin intérprete de por medio).

| | CISC | RISC |
|---|---|---|
| Instrucciones | Complejas, varios ciclos de reloj | Simples, 1 ciclo de reloj |
| Lógica | Programada (microcódigo) | Cableada (hardware) |
| Modos direccionamiento | Muchos | Pocos |
| Tamaño instrucción | Variable | Fijo |
| Consumo/temperatura | Mayor | Menor |
| Ejemplo | Intel/AMD (x86) | ARM, RISC-V |

> [!important] Idea clave
> CISC hace más "en una sola instrucción" (más trabajo para el hardware/microcódigo en cada paso). RISC simplifica cada instrucción al mínimo pero se apoya en ejecutar muchas más, muy rápido — por eso combina tan bien con la técnica de **[[Pipeline]]**: instrucciones de tamaño fijo y simples son mucho más fáciles de solapar en cadena.

> [!note] La línea se ha difuminado (conocimiento general)
> Los procesadores x86 modernos (CISC "de cara al programador") en realidad **traducen internamente** cada instrucción compleja a micro-operaciones simples tipo RISC antes de ejecutarlas, y sí usan pipeline y ejecución fuera de orden por dentro. La distinción CISC/RISC sigue siendo real a nivel de **ISA** (el conjunto de instrucciones que ve el programador), pero por dentro del chip las técnicas se han mezclado.

## Variantes abiertas: RISC-V

**[[RISC-V]]** es un estándar RISC **abierto y libre de regalías** — cualquiera puede diseñar su propio procesador sobre él sin pagar licencias, a diferencia de ARM.

> [!tip] Arduino, de pasada
> **Arduino** (hardware y software libre, licencia GPL) no es una arquitectura de procesador, pero comparte con RISC-V la misma filosofía de "abierto y libre" aplicada a la democratización del acceso a la computación.

## 🔑 Resumen ultra-rápido

- CISC = instrucciones complejas, microcódigo, nació cuando la memoria era cara. RISC = instrucciones simples de 1 ciclo, lógica cableada, nació cuando compiladores/memoria lo permitieron.
- RISC pipelinea mejor por tener instrucciones de tamaño fijo y simples.
- Por dentro, el x86 moderno (CISC) también usa micro-ops estilo RISC y pipeline — la distinción es de ISA, no de circuito interno.
- RISC-V = RISC abierto y sin licencias, frente a ARM (RISC con licencia de pago).

---

**Conexiones con otros conceptos TAI:**
- [[B2 - T1 INFORMATICA BASICA]] — tabla resumen de examen y contexto del ciclo Fetch-Decode-Execute.
- [[Pipeline]] — la técnica que aprovecha al máximo el diseño RISC.
- [[RISC-V]] — variante abierta de RISC, con detalle propio.
- [[SoC vs APU]] — otra clasificación de diseño de chip, en la misma sección del temario.
- [[CPU - Central Processing Unit]] — componentes internos (UC, ALU, Decodificador, Secuenciador) que ejecutan estas instrucciones.
