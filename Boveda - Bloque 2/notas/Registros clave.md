Los registros son la memoria más rápida que existe en un ordenador: están **dentro** de la propia [[CPU - Central Processing Unit]], no en la RAM. Son la cúspide de la [[Jerarquía de memoria]] (Registros → Caché → Memoria Principal → Resto) precisamente porque no hay ningún bus de por medio para acceder a ellos: el circuito ya está ahí mismo.

> [!note] Diferencia con `B2 - T1 INFORMATICA BASICA`
> Esa nota trae la lista de registros como parte del ciclo Fetch-Decode-Execute. Esta nota se centra en **por qué existe cada registro**: a qué bus o componente conecta, y cómo encajan entre sí durante un ciclo completo.

## Los registros, uno por uno, y a qué se conectan

| Registro | Nombre completo | Qué guarda | Conecta con |
|---|---|---|---|
| **MAR** | Memory Address Register | La dirección de memoria a la que se va a acceder | [[Bus de dirección]] — es literalmente el registro que pone la dirección **en** ese bus |
| **MDR** | Memory Data Register | El dato que se lee/escribe de esa dirección | [[Bus de datos]] — el registro que pone o recoge el dato **de** ese bus |
| **AC** | Acumulador | Resultados intermedios de operaciones | La ALU, que lee y escribe sobre él en cada cálculo |
| **PC** | Program Counter (Instruction Pointer en Intel) | La dirección de la **siguiente** instrucción | Se copia al MAR al empezar cada Fetch, y se actualiza al terminar el ciclo |
| **IR / CIR** | Instruction Register | La instrucción **actual**, ya traída de memoria | El Decodificador, que la traduce en la señal de "qué operación es" |
| **Flags** | — | Banderas de estado (cero, acarreo, paridad...) | Las escribe la ALU tras cada operación; las lee la CPU para decidir saltos condicionales |

> [!important] MAR y MDR son los "guantes" con los que la CPU toca el bus
> No es casualidad que sus nombres incluyan "Memory": son el punto de contacto exacto entre la CPU y el exterior. La CPU nunca pone una dirección directamente en el [[Bus de dirección]] "de la nada" — primero la coloca en el MAR, y el MAR es lo que realmente sale al bus. Lo mismo con el MDR y el [[Bus de datos]].

## Cómo se usan en un ciclo completo (Fetch)

1. El **PC** contiene la dirección de la próxima instrucción → se copia al **MAR**.
2. El **MAR** pone esa dirección en el [[Bus de dirección]].
3. La memoria responde y el dato (la instrucción) llega por el [[Bus de datos]] hasta el **MDR**.
4. El contenido del **MDR** se traslada al **IR**, donde queda como "la instrucción actual".
5. El **Decodificador** interpreta el IR; si hace falta calcular algo, la **ALU** trabaja con el **AC** y actualiza las **Flags**.
6. El **PC** se incrementa, listo para el siguiente Fetch.

> [!important] Diferencia clave: PC vs IR
> El **PC** apunta a lo que viene (la dirección de la siguiente instrucción). El **IR** contiene lo que se está ejecutando ahora mismo (la instrucción ya traída). Uno es un puntero hacia el futuro inmediato; el otro es el presente de la CPU.

> [!note] Este modelo es una simplificación didáctica (conocimiento general)
> El esquema MAR/MDR/AC/PC/IR/Flags es el modelo clásico de enseñanza de arquitectura de computadores (nivel de transferencia entre registros), no una lista literal de los registros que se ven en ensamblador x86. En x86 no se programa directamente sobre un "MAR" o un "MDR" — son internos al microarquitectura —, y en vez de un único **acumulador** hay varios registros de propósito general (EAX, EBX, ECX, EDX...), aunque EAX históricamente hereda el rol de acumulador. Para el examen, el modelo simplificado es el que se pregunta.

## 🔑 Resumen ultra-rápido

- Registros = memoria más rápida posible, dentro de la CPU, cúspide de la jerarquía de memoria.
- MAR ↔ Bus de dirección. MDR ↔ Bus de datos. Son el punto de contacto físico CPU-bus.
- PC = siguiente instrucción. IR = instrucción actual. AC = resultados intermedios (ALU). Flags = estado tras la última operación.
- Ciclo Fetch: PC → MAR → bus de dirección → memoria → bus de datos → MDR → IR → Decodificador → (ALU/AC/Flags si hace falta) → PC++.
- El modelo MAR/MDR/AC es didáctico; x86 real usa registros de propósito general en vez de un único acumulador.

---

**Conexiones con otros conceptos TAI:**
- [[B2 - T1 INFORMATICA BASICA]] — ciclo Fetch-Decode-Execute completo, jerarquía de memoria.
- [[Bus de dirección]] y [[Bus de datos]] — los buses a los que MAR y MDR dan acceso directo.
- [[CPU - Central Processing Unit]] — UC, ALU, Decodificador y Secuenciador, que operan junto a estos registros.
- [[Jerarquía de memoria]] y [[Memoria Caché]] — el siguiente escalón, justo debajo de los registros.
- [[Reloj]] — cada paso del ciclo (Fetch, Decode, Execute) avanza a golpe de reloj.
