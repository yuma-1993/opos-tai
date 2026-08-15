El pipeline (segmentación) es la técnica que permite que la CPU **avance una instrucción por ciclo de reloj**, en vez de tener que completar todo el ciclo Fetch-Decode-Execute-Store de una instrucción antes de empezar con la siguiente.

## La idea: una cadena de montaje

El Fetch (ir a buscar la instrucción a memoria) es el paso más lento del ciclo. La solución: mientras se hace el Fetch de una instrucción, ya se puede estar **Decodificando** la anterior, y **Ejecutando** la anterior a esa — trabajo en cadena, como una fábrica donde cada estación siempre tiene algo entre manos.

> [!example] Cómo se solapan las fases
> ```
>          ciclo1   ciclo2   ciclo3   ciclo4
> instr.1  Fetch    Decode   Execute  Store
> instr.2           Fetch    Decode   Execute
> instr.3                    Fetch    Decode
> instr.4                             Fetch
> ```
> Sin pipeline, la instrucción 4 no empezaría hasta el ciclo 13 (4 instrucciones × 4 fases cada una). Con pipeline, ya está en marcha en el ciclo 4: el rendimiento no viene de hacer cada instrucción más rápida, sino de que **la CPU nunca deja una fase ociosa**.

## Por qué encaja tan bien con RISC

Ver [[CISC vs RISC]] para el detalle completo, pero la razón de fondo es simple: para solapar fases hace falta poder predecir **cuánto va a tardar cada una**. Las instrucciones RISC, de tamaño fijo y ejecución en un ciclo, hacen esa predicción trivial. Las instrucciones CISC, de tamaño variable y duración distinta según la complejidad, complican mucho más el solapamiento — por eso el x86 moderno tiene que traducir sus instrucciones a micro-operaciones simples antes de poder pipelinearlas (ver el matiz en [[CISC vs RISC]]).

> [!note] Los "atascos" del pipeline (conocimiento general)
> El pipeline no siempre fluye perfecto. Tres problemas típicos, conocidos como *hazards*:
> - **Estructural**: dos fases distintas necesitan el mismo recurso físico a la vez.
> - **De datos**: una instrucción necesita un resultado que la anterior todavía no ha terminado de calcular.
> - **De control**: un salto condicional (`if`) no se sabe si se toma o no hasta que se ejecuta, y para entonces el pipeline ya ha empezado a traer instrucciones "por si acaso" (predicción de salto); si se equivoca, hay que **vaciar** el pipeline y empezar de nuevo por la rama correcta.

> [!important] Pipeline no es lo mismo que multi-núcleo
> El pipeline saca más rendimiento de **un solo núcleo**, solapando fases de instrucciones distintas en el tiempo — es paralelismo *aparente*, una sola unidad de ejecución trabajando sin huecos. El multi-núcleo (ver [[CPU - Central Processing Unit]]) es paralelismo *real*: varias unidades de ejecución completas trabajando literalmente a la vez. Son técnicas independientes y compatibles entre sí — una CPU moderna usa ambas a la vez, en cada uno de sus núcleos.

## 🔑 Resumen ultra-rápido

- Pipeline = solapar Fetch/Decode/Execute/Store de instrucciones consecutivas, como una cadena de montaje.
- Gana rendimiento porque ninguna fase queda ociosa, no porque cada instrucción sea más rápida por sí sola.
- RISC pipelinea mejor por instrucciones de tamaño fijo y duración predecible.
- Hazards: estructural, de datos, de control (salto mal predicho → vaciar el pipeline).
- Pipeline (paralelismo aparente, 1 núcleo) ≠ multi-núcleo (paralelismo real, varios núcleos).

---

**Conexiones con otros conceptos TAI:**
- [[CISC vs RISC]] — por qué RISC encaja mejor con esta técnica.
- [[CPU - Central Processing Unit]] — contraste con el paralelismo real del multi-núcleo.
- [[B2 - T1 INFORMATICA BASICA]] — ciclo Fetch-Decode-Execute-Store base sobre el que se construye el pipeline.
- [[Reloj]] — cada fase del pipeline avanza a golpe de la misma señal de reloj.
