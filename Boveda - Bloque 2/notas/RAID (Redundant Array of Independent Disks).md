> [!abstract]
> RAID combina varios discos físicos para que el sistema operativo los vea como **una única unidad lógica**. El objetivo es mejorar **rendimiento** (velocidad), **seguridad** (tolerancia a fallos) o ambos, a costa de capacidad útil o coste. Puede implementarse por **hardware** (controladora RAID dedicada) o por **software** (el propio SO, ej. Windows Storage Spaces, mdadm en Linux).

> [!note] Diferencia con la nota de [[B2 - T2 PERIFERICOS Y ALMACENAMIENTO]]
> Esa nota trae la versión resumida "de examen" (tablas, fórmulas). Esta nota profundiza en el **porqué** de cada nivel: si entiendes esto, la tabla resumen deja de ser algo que memorizar de carrerilla y pasa a ser algo que puedes **reconstruir razonando**.

## RAID no es backup

> [!important] Trampa clásica de examen
> RAID protege contra el **fallo físico de un disco**. No protege contra: borrar un archivo por error, un ransomware que cifra los datos, o una corrupción lógica del sistema de archivos — porque **todo eso se replica igual de bien** en el disco espejo o en la paridad. Redundancia ≠ copia de seguridad. Un backup real vive en otro sitio (otro medio, otro momento en el tiempo).

## Los tres ingredientes base

Todos los niveles de RAID son combinaciones de solo tres ideas. Entender estas tres es entender todo lo demás:

| Ingrediente | Qué hace | Qué compra | Qué cuesta |
|---|---|---|---|
| **Striping** (división) | Reparte los datos en trozos entre varios discos | Velocidad (paralelizar lecturas/escrituras) | Cero redundancia: si falla un disco, se pierde todo |
| **Mirroring** (espejo) | Duplica el dato entero en otro disco | Redundancia total, sin cálculo | La mitad de la capacidad se pierde siempre |
| **Parity** (paridad) | Guarda un dato "de control" calculado a partir de los demás, que permite reconstruir un disco perdido | Redundancia barata en capacidad | Cálculo extra en cada escritura (CPU/controladora) |

> [!tip] Con esto ya puedes deducir la tabla
> RAID 0 = striping solo. RAID 1 = mirroring solo. RAID 5/6 = striping + parity. RAID 10 = mirroring + striping. No hace falta memorizar cada nivel como un bloque aislado, sino identificar qué ingredientes lleva.

### Cómo funciona la paridad de verdad (XOR)

> [!note] Esto es conocimiento general (no viene literal en la fuente original), pero es la base matemática que explica por qué la paridad "reconstruye" un disco perdido — vale la pena entenderlo para no memorizarlo como magia.

La paridad más simple se calcula con la operación **XOR** (⊕): da 0 si los bits son iguales, 1 si son distintos.

> [!example]
> Tres discos de datos con un byte cada uno: A = `1100`, B = `1010`, C = `0110`.
> Paridad P = A ⊕ B ⊕ C = `0000`.
> Si el disco **B** falla, se recalcula: B = A ⊕ C ⊕ P = `1100 ⊕ 0110 ⊕ 0000` = `1010`. Exacto, se recupera el valor original.

La propiedad clave de XOR es que es **reversible**: si tienes todos los datos menos uno, y tienes la paridad, puedes despejar el que falta. Por eso **un solo disco de paridad basta para tolerar un fallo**, sin necesidad de duplicar toda la información como hace el mirroring.

## Recorrido por los niveles, ya con los ingredientes identificados

### RAID 0 — Striping puro

- **Ingrediente**: striping, sin ningún tipo de redundancia.
- **Redundancia**: ninguna. Si falla un disco, se pierde **todo** el conjunto de datos.
- **Rendimiento**: excelente en lectura y escritura, porque las operaciones se paralelizan entre discos.
- **Mínimo**: 2 discos.
- **Capacidad neta** = nº discos × capacidad del disco más pequeño (100% aprovechado).
- **Uso típico**: edición de vídeo, escenarios donde importa la velocidad y los datos están respaldados en otro sitio.

### RAID 1 — Mirroring puro

- **Ingrediente**: mirroring, sin striping.
- **Qué hace**: cada bloque se **duplica** en dos (o más) discos: uno primario, otro espejo.
- **Redundancia**: total, no usa paridad, usa copia exacta.
- **Rendimiento**: buena lectura (puede leer de cualquier copia), escritura normal (hay que escribir dos veces).
- **Mínimo**: 2 discos.
- **Desventaja**: solo aprovechas el 50% de la capacidad total.
- **Capacidad neta** = (nº discos × capacidad del más pequeño) / 2.
- **Uso típico**: sistemas críticos donde no puedes permitirte perder datos (ej. servidores de bases de datos pequeños).

### RAID 2 y 3 — Striping + parity a grano muy fino (bit/byte)

Característica común: **todos los discos participan a la vez en cada operación de E/S** (una petición usa todos los discos simultáneamente), porque cada pieza de datos es tan pequeña (un bit, un byte) que necesita a todos los discos para reconstruir siquiera una unidad útil de información.

> [!important] Por qué esto es un problema
> Si todos los discos están ocupados sirviendo **una sola** petición, no pueden atender otra petición distinta a la vez. Es rápido para transferir un archivo enorme, pero pésimo si llegan muchas peticiones pequeñas simultáneas (el caso típico de un servidor con muchos usuarios). Esta es la razón real de que RAID 2 y 3 estén en desuso frente a RAID 4/5/6.

#### RAID 2

- Distribuye los **bits** entre M discos de datos + N discos de paridad, calculada con **código Hamming** (detecta y corrige errores, no solo detecta).
- Nivel **teórico**, nunca se implementó comercialmente (los discos modernos ya tienen su propia corrección de errores interna, hace innecesario RAID 2).
- 3 o más discos. Capacidad según configuración (3+2, 7+3, 15+4...): el número de discos de paridad depende del número de bits de datos (a más discos de datos, proporcionalmente menos discos de paridad necesarios, según Hamming).

#### RAID 3

- Distribuye **tiras de información** (bytes) entre M discos + **1 disco dedicado a paridad**.
- 3 o más discos.
- **Capacidad neta** = (nº discos − 1) × capacidad del disco más pequeño.
- Problema práctico: como cada operación usa todos los discos a la vez, no se pueden paralelizar varias peticiones distintas simultáneamente → mal rendimiento con muchas peticiones pequeñas concurrentes. Poco usado hoy.

### RAID 4, 5 y 6 — Striping + parity a grano grueso (bloques)

Mismo ingrediente que 2/3 (striping + paridad), pero con tiras de **bloques** en vez de bits/bytes. Al ser el trozo más grande, **cada disco puede atender peticiones distintas de forma independiente** — mejor para muchos accesos concurrentes pequeños, típico de servidores. Esta es la única diferencia conceptual real entre "la familia 2/3" y "la familia 4/5/6": el tamaño del trozo que se reparte.

#### RAID 4

- Igual que RAID 3, pero con tiras de **bloques** en vez de bytes: M discos de datos + **1 disco fijo de paridad**.
- 3 o más discos.
- **Capacidad neta** = (nº discos − 1) × capacidad del disco más pequeño.
- **Problema**: el disco de paridad es un **cuello de botella**, porque cada escritura implica escribir también en ese único disco → se satura. Por eso RAID 5 lo mejora.

#### RAID 5

- Igual concepto, pero la paridad se **distribuye rotando entre todos los discos** (no hay un disco fijo de paridad) → elimina el cuello de botella de RAID 4.
- 3 o más discos.
- Tolera **1 fallo** de disco (con la paridad se reconstruye el disco perdido, con el mecanismo XOR de arriba).
- **Capacidad neta** = (nº discos − 1) × capacidad del disco más pequeño.
- **El más usado** en la práctica: buen equilibrio capacidad/seguridad/rendimiento. Ejemplo: 4 discos de 1 TB en RAID 5 → 3 TB útiles, tolera 1 fallo.

#### RAID 6

- Como RAID 5, pero con **doble paridad distribuida** (dos bloques de paridad distintos, **P** y **Q**, calculados con algoritmos diferentes — el segundo ya no puede ser un simple XOR, porque XOR solo permite despejar una incógnita, y aquí puede haber dos discos caídos a la vez).
- Necesita **N+2 discos**, mínimo 4.
- Tolera **2 fallos simultáneos**.
- **Capacidad neta** = (nº discos − 2) × capacidad del disco más pequeño.
- Uso típico: almacenamiento grande donde durante la reconstrucción (*rebuild*) tras un fallo, un segundo fallo sería catastrófico (discos muy grandes tardan mucho en reconstruirse, y durante ese *rebuild* el array ya está en un estado más vulnerable).

## Niveles anidados (Nested/Hybrid RAID)

Combinan dos niveles RAID en dos capas: primero se forman grupos con un nivel, y esos grupos se tratan como "discos virtuales" para el segundo nivel.

### RAID 0+1 ("espejo de divisiones")

```
[Disco A + Disco B] = Grupo RAID 0 ─┐
                                     ├── espejados entre sí (RAID 1)
[Disco C + Disco D] = Grupo RAID 0 ─┘
```

Si falla un disco, **todo su grupo RAID 0 queda inutilizado** (aunque el otro grupo entero sigue funcionando como respaldo).

### RAID 1+0 / RAID 10 ("división de espejos")

```
[Disco A ↔ Disco B] = Par RAID 1 ─┐
                                    ├── striping entre pares (RAID 0)
[Disco C ↔ Disco D] = Par RAID 1 ─┘
```

Si falla un disco, solo se pierde la redundancia de **su pareja concreta**; el resto de pares no se ven afectados. Es más resistente a fallos múltiples que RAID 0+1.

> [!important] Diferencia clave para el examen
> En RAID 10, puedes perder hasta la mitad de los discos (uno de cada pareja) sin perder datos. En RAID 01, perder un disco en cada grupo (2 discos totales, uno por cada mitad) destruye todo el array. **RAID 10 es más robusto**, por eso se prefiere en la práctica.
>
> El truco para no confundirlos leyendo el nombre al revés de lo esperado: en "X+Y", **la capa exterior (la que ves si el array se rompe) es la Y** (la última). RAID **0+1** = por fuera es un espejo (1) de grupos striping; RAID **1+0** = por fuera es un striping (0) de parejas espejo.

## JBOD (Just a Bunch Of Disks)

- **No es RAID real** (no aplica ni striping ni redundancia): simplemente concatena varios discos para que el SO los vea como uno solo (como una partición extendida).
- Aprovecha el **100%** de la capacidad de todos los discos, incluso si son de tamaños distintos (no está limitado por el disco más pequeño, a diferencia de RAID).
- **Sin redundancia**: si falla un disco, se pierden solo los datos almacenados físicamente en ese disco (los demás siguen accesibles), a diferencia de RAID 0 donde falla todo el conjunto.

> [!tip] JBOD vs RAID 0, la confusión más típica
> Ambos suman capacidad sin redundancia, pero **JBOD no reparte datos entre discos** (cada archivo vive entero en un disco), mientras que RAID 0 sí trocea cada archivo entre todos. Por eso perder un disco en JBOD solo afecta a "sus" archivos, y perder un disco en RAID 0 afecta a todo.

### Regla general de capacidad (para RAID con striping/parity)

Si mezclas discos de distinto tamaño, RAID trata a todos como si tuvieran el tamaño del **más pequeño** (el resto de espacio de los discos mayores se desperdicia).

> [!example]
> Discos de 120 GB y 320 GB → el sistema los trata como si ambos fueran de 120 GB. En RAID 0 (sin redundancia): capacidad = 2 × 120 GB = **240 GB** (se pierden 200 GB del disco grande).

### Spare (disco de repuesto)

Disco extra, sin usar, conectado a la controladora. Si un disco activo falla, el *spare* **entra automáticamente** a sustituirlo y el RAID reconstruye (*rebuild*) la información redundante sobre él, sin intervención manual inmediata.

## Cuadro resumen comparativo

| RAID | Ingredientes | Mínimo discos | Tolera fallos | Capacidad neta | Rendimiento |
|---|---|---|---|---|---|
| 0 | Striping | 2 | 0 | N × menor | Máximo (lectura/escritura) |
| 1 | Mirroring | 2 | 1 (por réplica) | (N × menor)/2 | Buena lectura |
| 3 | Striping (byte) + parity | 3 | 1 | (N−1) × menor | Malo con concurrencia |
| 4 | Striping (bloque) + parity fija | 3 | 1 | (N−1) × menor | Cuello de botella en paridad |
| 5 | Striping (bloque) + parity rotada | 3 | 1 | (N−1) × menor | Buen equilibrio (el más usado) |
| 6 | Striping (bloque) + doble parity | 4 | 2 | (N−2) × menor | Como RAID 5, algo más lento en escritura |
| 10 | Mirroring + striping | 4 | varios (1 por pareja) | (N × menor)/2 | Excelente + seguro |
| JBOD | Ninguno (concatenación) | 2 | 0 (parcial) | Suma total de todos | Ninguna mejora |

## 🔑 Resumen ultra-rápido

- RAID no es backup: protege de fallo físico de disco, no de borrado accidental, ransomware o corrupción lógica.
- Tres ingredientes: **striping** (velocidad, cero redundancia), **mirroring** (redundancia total, 50% capacidad), **parity/XOR** (redundancia barata, coste de cálculo).
- XOR permite reconstruir un disco perdido si tienes el resto + la paridad; con doble paridad (RAID 6) se toleran 2 fallos.
- RAID 2/3 (bit/byte) vs RAID 4/5/6 (bloque): el tamaño del trozo decide si todos los discos trabajan siempre juntos (mal con concurrencia) o de forma independiente (bien con concurrencia).
- RAID 4 → RAID 5: mover la paridad de un disco fijo a rotarla resuelve el cuello de botella.
- RAID 10 > RAID 0+1 en resistencia a fallos múltiples (capa exterior mirror vs capa exterior striping).
- JBOD ≠ RAID 0: JBOD no trocea archivos entre discos, RAID 0 sí.
- Capacidad con discos desiguales: todos "bajan" al tamaño del disco más pequeño (excepto JBOD, que suma todo).

---

**Conexiones con otros conceptos TAI:**
- [[B2 - T2 PERIFERICOS Y ALMACENAMIENTO]] — versión resumida de examen de este mismo contenido, dentro de la Parte III del tema.
- [[HDD (Hard Disk Drive)]] y [[SSD (Solid State Drive)]] — los discos físicos que forman cualquier array RAID; el TBW y el *wear leveling* del SSD importan especialmente en RAID 5/6 por la escritura extra que genera la paridad.
- [[DMA]] — igual que RAID delega trabajo repetitivo (mover datos) en un controlador dedicado para liberar a la CPU, una controladora RAID hardware delega el cálculo de paridad y el reparto de bloques sin intervención del procesador principal.
- [[B4 - T1.1 ADMON SSOO]] — en administración de sistemas, RAID aparece como la capa física que puede quedar debajo de un LVM (comando `mdadm`), y su callout "RAID no es backup" conecta directamente con las estrategias de backup de ese tema.
- [[Sharding]] y [[B2 - T5 NOSQL Y BIG DATA]] — el sharding de NoSQL reparte datos entre **nodos** distintos (partición lógica a nivel de aplicación); RAID reparte datos entre **discos** dentro de un mismo nodo (partición física). Son capas de distribución distintas, no hay que confundirlas.
