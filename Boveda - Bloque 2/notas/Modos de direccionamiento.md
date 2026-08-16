Formas que tiene una instrucción de máquina de indicarle a la CPU **dónde se encuentra el operando** (el dato) con el que tiene que trabajar: cómo se calcula o se obtiene la dirección de memoria (o el valor) que va a usar la operación.

> [!important] No confundir con [[Direccionamiento]]
> Esa otra nota habla de **CHS vs LBA**: cómo se numera un sector dentro de un **disco**. Esta nota habla de algo distinto aunque suene parecido: cómo una **instrucción de máquina** le dice a la CPU dónde está el dato con el que va a trabajar (en un registro, en la propia instrucción, en una dirección de memoria...). Ambas resuelven "¿dónde está el dato?", pero una a nivel de disco y otra a nivel de instrucción — es fácil mezclarlas solo por el nombre.

## Los cuatro modos básicos

No todas las instrucciones necesitan el dato de la misma manera: a veces el propio código de operación ya deja claro implícitamente de dónde sacarlo (**implícito**), otras veces el dato viaja incluido en la propia instrucción sin necesidad de ir a buscarlo a ningún sitio (**inmediato**), otras veces la instrucción indica directamente la dirección de memoria donde está el dato (**directo o absoluto**), y en los casos más complejos la instrucción apunta a una dirección que a su vez contiene otra dirección, siendo esta última la que finalmente señala dónde está el dato real (**indirecto**).

| Modo | ¿Dónde está el dato? | Ejemplo |
|---|---|---|
| **Implícito** | Ya se sabe por la propia operación (ej: *pop* de una pila) | `top()` |
| **Inmediato** | El dato viene **dentro** de la instrucción, no hay que ir a buscarlo | `MOV AX, 12` |
| **Directo/Absoluto** | La instrucción da la **dirección de memoria** donde está el dato | `MOV A, 17H` |
| **Indirecto** | La instrucción da una dirección, y **en esa dirección hay otra dirección** donde está el dato real | (doble salto) |

> [!tip] Truco para recordarlo: cuenta los "saltos"
> Cada modo añade un salto más hasta llegar al dato real. **Inmediato** = 0 saltos (el dato ya está ahí, dentro de la instrucción). **Directo** = 1 salto (voy a la dirección y ahí está el dato). **Indirecto** = 2 saltos (voy a la dirección, ahí hay otra dirección, y ahí sí está el dato).

> [!note] Un quinto modo muy citado (conocimiento general, no viene literal en la fuente)
> Muchos temarios añaden el **direccionamiento por registro**: el operando está directamente en un registro de la CPU (ej. `ADD AX, BX`), no en memoria. Es, en cuanto a "saltos", como el inmediato (0 saltos hasta el dato), pero en vez de venir dentro de la instrucción ya está cargado en un registro — el acceso más rápido posible, porque ni siquiera toca el [[Bus de dirección]] o el [[Bus de datos]] para buscarlo.

## Por qué esto conecta con CISC vs RISC

> [!important] Idea clave
> Cuantos más modos de direccionamiento soporta un procesador, más flexible es a la hora de acceder a memoria, pero también más compleja resulta su circuitería. Por eso **CISC** suele tener muchos modos y **RISC** muy pocos, priorizando la simplicidad y la velocidad — ver [[CISC vs RISC]].

## Dónde encaja en el ciclo de ejecución

El modo de direccionamiento se decide al **decodificar** la instrucción: el Decodificador no solo identifica la operación, también identifica cómo interpretar sus operandos. Si el modo es directo, la dirección resultante acaba en el **MAR** camino del [[Bus de dirección]]; si es inmediato o por registro, ni siquiera hace falta ir a memoria (ver [[Registros clave]]).

## 🔑 Resumen ultra-rápido

- Implícito (0 saltos, ya se sabe) → Inmediato (0 saltos, el dato va en la instrucción) → Directo (1 salto, la instrucción da la dirección) → Indirecto (2 saltos, la dirección apunta a otra dirección).
- Por registro: variante de acceso instantáneo, el dato ya está en un registro de la CPU.
- Más modos = más flexible pero más complejo → CISC. Menos modos = más simple y rápido → RISC.
- No confundir con [[Direccionamiento]] (CHS vs LBA), que es direccionamiento de **sectores de disco**, no de operandos de instrucción.

---

**Conexiones con otros conceptos TAI:**
- [[Direccionamiento]] — el otro "direccionamiento" del temario (CHS vs LBA en disco); mismo nombre, nivel distinto.
- [[CISC vs RISC]] — por qué el número de modos soportados diferencia ambas filosofías.
- [[Registros clave]] y [[Bus de dirección]] — a dónde van a parar los modos directo/indirecto/registro durante la ejecución.
- [[B2 - T1 INFORMATICA BASICA]] — versión resumen de examen, dentro de la arquitectura de computadores.
