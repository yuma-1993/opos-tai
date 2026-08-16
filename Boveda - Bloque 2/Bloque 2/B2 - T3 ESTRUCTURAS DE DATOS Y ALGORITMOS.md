---
tags:
  - bloque2
  - tema3
  - estructuras-datos
  - tipos-abstractos-de-datos
  - arboles
  - grafos
  - algoritmos
  - complejidad-algoritmica
  - ordenacion
  - ficheros
  - formatos-fichero
bloque: 2
tema: 3
titulo: Estructuras de datos y algoritmos
estado: por-repasar
---

# Tema 3 · Bloque 2 — Estructuras de datos y algoritmos

> [!abstract] De qué va este tema
> Cubre la relación entre **Tipos Abstractos de Datos (TAD)** y las **Estructuras de Datos (EEDD)** que los implementan (pilas, colas, listas, tablas hash, montículos), profundiza en **árboles** (recorridos, tipos, árboles B) y **grafos** (representación y algoritmos de caminos), repasa los **métodos de acceso y ordenación de ficheros**, la teoría general de **algoritmos** (técnicas de diseño, complejidad, familias de ordenación con su detalle algorítmico), y cierra con un extenso catálogo de **formatos de fichero** (ofimática, imagen, audio, vídeo).

---

## Parte I — Tipos Abstractos de Datos (TAD) y Estructuras de Datos (EEDD)

### 1. TAD vs EEDD: la distinción de fondo

- **TAD (Tipo Abstracto de Dato)**: modelo matemático para definir tipos de datos (primitivas, comportamiento). Es **puro**: define el **qué** (qué operaciones existen y qué hacen), no el cómo.
- **EEDD (Estructura de Datos)**: concepto más concreto, orientado a la implementación. Son las herramientas que nos ayudan a implementar los TAD: definen el **cómo**.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Esta distinción es exactamente la misma que hay en programación orientada a objetos entre una **interfaz** y su **implementación**: un TAD "Pila" solo promete que existe `push`/`pop`/`isEmpty` y que se comportan como LIFO, sin decir si por dentro hay un array o una lista enlazada. Por eso una misma pila se puede reimplementar sin que el código que la usa se entere — es la base del principio de encapsulación.

### 2. Tabla TAD → EEDD que lo implementa

| Tipo Abstracto de Datos | Estructura de Datos |
|---|---|
| List (secuencia) | Array, Lista enlazada |
| Set (conjunto) / Multiset (multiconjunto con repetidos) | Árbol rojo-negro, tabla Hash |
| Queue (cola) / Double-ended queue (bicola) | Array, Lista [doble] enlazada |
| Stack (pila) | Array, Lista enlazada |
| Priority Queue (Heap) | Montículo (propiedad) |
| Tree | Árbol. Algunos con arrays |
| Graph | Matriz, Array de listas enlazadas |
| Associative Array (Diccionario, mapa). Key-value | Tabla Hash |

### 3. Primitivas de los TAD principales

- **Stack / Pila**: `push`, `pop`, `isEmpty`, `peek`/`top`. ≈ **LIFO** (Last In, First Out).
- **Queue / Cola**: `enqueue`, `dequeue`, `isEmpty`, `peek`/`top`. ≈ **FIFO** (First In, First Out).
- **List / Lista**: `isEmpty`, `insertarDelante`, `insertarDetras`, `head`, `tail`. `tail` quita la cabeza y devuelve el resto de la lista. Una lista **no es posicional**, por eso no hay primitiva para recuperar directamente el elemento N.
  - Ejemplo del propio PDF: el 3º elemento se obtiene como `head(tail(tail(Lista)))`.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Ejemplos de uso real para fijar la intuición: una **pila (LIFO)** es la pila de llamadas de un programa (`call stack`) — la última función llamada es la primera en terminar y "salir" de la pila. Una **cola (FIFO)** es una cola de impresión o de mensajes: el primer trabajo que entra es el primero en imprimirse.

### 4. Tabla Hash

Sabe la posición que va a ocupar un elemento al aplicar la **función Hash**. Ejemplo del PDF: `x mod 250`.

- Si la función Hash está mal diseñada, o la tabla es pequeña, **aumentan las colisiones** al haber más duplicados.
- Ya no tarda **O(1)** cuando hay colisión, porque debe buscar dentro de la lista de esa posición.
- La función Hash se usa para **[[Buffering|buffers circulares]]**.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Las dos familias clásicas de resolver colisiones en una tabla hash son: **encadenamiento** (cada posición guarda una lista enlazada con todos los elementos que colisionan ahí — es lo que hace que el PDF diga que "hay que buscar dentro de la lista") y **direccionamiento abierto** (si la posición está ocupada, se busca la siguiente libre según una regla). Cuanto más llena está la tabla (mayor *factor de carga*), más colisiones y peor rendimiento — de ahí que el PDF diga que una tabla pequeña también las aumenta.

### 5. Montículo (Heap)

- **Complejidad**: O(n log(n)) para inserciones (crear) y borrados (reequilibrar).
- Estructura basada en un árbol que cumple con la **propiedad del montículo** (max-heap o min-heap).
- Si se implementa con árbol binario es un **montículo binario**. También se puede implementar con **array**.
- **Max-heap**: la raíz es mayor o igual que todos los elementos que hay debajo.

> [!important] Conexión con el resto del tema
> El montículo es la EEDD que implementa la **Priority Queue** (ver tabla del punto 2) y es también la base de **HeapSort** (Parte VI) y del algoritmo de **Dijkstra** (Parte III), que internamente usa una cola de prioridad para elegir siempre el nodo más cercano aún no visitado.

---

## Parte II — Árboles

### 1. Conceptos básicos de árbol

- Los árboles **siempre tienen raíz**.
- **Hoja**: nodo sin hijos.
- El **nivel** del nodo raíz puede tomar como convención 0 (+) o 1 (-) según la fuente. El árbol vacío tiene 0 niveles.
- **Orden**: número máximo de hijos que puede tener un nodo. Es el máximo **potencial, teórico** — no podemos saberlo si no lo dan explícitamente. Árbol binario: orden 2.
- **Grado de un nodo**: número de hijos directos de ese nodo. El **grado de un árbol** es el máximo grado de sus nodos — es el máximo **real**, limitado por el orden.
- **Peso**: número total de nodos del árbol.
- **Profundidad de un nodo**: número de aristas desde el nodo hasta la raíz. Profundidad del nodo raíz = 0. Se mira **desde abajo hacia arriba**.
- **Altura de un nodo**: trayectoria más larga desde ese nodo hasta una hoja. Se mira **desde arriba hacia abajo**. Altura de las hojas = 0.
- **Factor de equilibrio (FE)**: diferencia de altura entre el subárbol izquierdo y el derecho. Valores 0, +1 y -1 definen un **árbol equilibrado o autobalanceable (AVL)**. Los reequilibrios se producen mediante **rotaciones**.

> [!important] Profundidad vs altura — confusión típica de examen
> Profundidad se mide **de un nodo hacia la raíz** (hacia arriba), altura se mide **de un nodo hacia la hoja más lejana** (hacia abajo). La raíz tiene profundidad 0 pero su altura es la altura total del árbol; una hoja tiene altura 0 pero su profundidad depende de cuántos niveles baja desde la raíz.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El PDF menciona que los reequilibrios en un árbol AVL se hacen mediante rotaciones, pero no detalla el mecanismo: cuando al insertar o borrar un nodo el FE de algún ancestro se sale del rango [-1, +1], se aplica una **rotación simple** (izquierda o derecha) o una **rotación doble** (izquierda-derecha o derecha-izquierda) sobre ese nodo, reorganizando localmente 2 o 3 nodos para devolver el árbol al rango permitido sin romper el orden del árbol binario de búsqueda subyacente.

### 2. Recorridos en profundidad

Son **recursivos**. Cada vez que se llega a un nodo, se vuelve a aplicar la misma regla (Preorden, Inorden o Postorden) sobre él.

| Recorrido | Orden | Regla mnemotécnica |
|---|---|---|
| **Preorden** | 1º Raíz, 2º Subárbol Izquierdo, 3º Subárbol Derecho | **R**ID |
| **Inorden** | 1º Subárbol Izquierdo, 2º Raíz, 3º Subárbol Derecho | I**R**D |
| **Postorden** | 1º Subárbol Izquierdo, 2º Subárbol Derecho, 3º Raíz | ID**R** — el más complejo, porque pinta la raíz del nodo al final |

> [!example] Ejemplo del PDF (árbol de 15 nodos, A–O)
> - **Preorden (RID)**: A, B, D, H, I, E, J, K, C, F, L, M, G, N, O
> - **Inorden (IRD)**: H, D, I, B, E, J, K, A, L, F, M, C, N, G, O
> - **Postorden (IDR)**: H, I, D, J, K, E, B, L, M, F, N, O, G, C, A

### 3. Tipos de árboles

- **Árboles binarios**:
  - **Árbol Binario de Búsqueda (ABB)**: su recorrido **inorden (IRD)** devuelve los elementos **ordenados**.
  - **Árbol de Fibonacci**: es un caso particular de AVL.
- **Árboles equilibrados (autobalanceables)**: FE es -1, 0 o +1. Ejemplos: **AVL, AA, Rojo-Negro, Splay, Árbol B o multicamino**.
- **Árbol B**: muy usado en **bases de datos y sistemas de ficheros**.
  - Cada nodo puede tener **más de 2 hijos**. Orden M: cada nodo tiene como máximo M hijos.
  - Mantiene los datos **ordenados**.
  - Inserciones y borrados en tiempo **log(n)** para las reestructuraciones de los nodos.
  - Cada nodo, excepto la raíz, tiene como **mínimo M/2 claves**.
  - Es un árbol **equilibrado**.
- **Árbol B+**: los **nodos internos solo contienen claves y punteros** (no datos). Los **nodos hoja están enlazados entre sí** para facilitar recorridos por niveles (rangos).
- **Árbol B***: el algoritmo de inserción garantiza una **densidad de ocupación de 2/3**. Es un árbol muy denso.

> [!important] Por qué los árboles B dominan en bases de datos
> El PDF ya adelanta que se usan "en bases de datos y sistemas de ficheros" — esto conecta directamente con el **acceso indexado / ISAM** de la Parte IV: un índice de base de datos suele ser, por dentro, un árbol B o B+.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> La razón práctica de que los árboles B (y no un ABB binario normal) se usen para índices de disco es que cada **nodo** de un árbol B se diseña para ocupar exactamente un **bloque de disco** (por eso tiene muchos hijos y no solo 2): así, cada vez que hay que bajar un nivel en el árbol solo hace falta **una lectura de disco**, que es la operación cara. Un árbol B+ es preferible para bases de datos relacionales porque, al tener las hojas enlazadas entre sí, permite recorrer rangos de valores (`WHERE edad BETWEEN 20 AND 30`) sin tener que volver a subir por el árbol.

---

## Parte III — Grafos

### 1. Conceptos básicos

Un **grafo** es una red de nodos. **No hay raíz** como en los árboles. Pueden ser:

- **Dirigidos** (dígrafos) / **no dirigidos**.
- **Conexos** / **inconexos**.
- **Cíclicos** / **acíclicos**.
- **Multigrafos**: donde hay más de una arista entre 2 vértices, más de un camino.
- **Etiquetados o ponderados**: con peso numérico en las aristas, para representar lo bien o mal que va ese enlace en la red.

| Métrica | Definición |
|---|---|
| **Orden del grafo** | Número de vértices/nodos |
| **Grado de un vértice** | Número de arcos incidentes en ese vértice |
| **Grado de un grafo** | Suma de los grados de sus vértices |
| **Tamaño** | Número de aristas/caminos |

### 2. Representación de los grafos

- **Lista de adyacencia**: array de vértices + listas enlazadas (cada vértice apunta a la lista de sus vecinos).
- **Array/matriz de adyacencia**: matriz N×N donde cada celda indica si hay arista entre dos vértices. **Desperdicia memoria si hay muchos nodos** (la mayoría de celdas quedan a 0 en grafos poco densos).

> [!important] Cuándo usar cada representación
> Lista de adyacencia = eficiente en memoria para grafos **poco densos** (pocas aristas por nodo). Matriz de adyacencia = más simple y rápida para consultar "¿existe arista A-B?" en O(1), pero cara en memoria si el grafo es grande y poco denso.

### 3. Algoritmos sobre grafos

El PDF distingue **2 tipos de funcionalidades**, dado un grafo, para calcular el camino de ir de A a B (relacionadas con TCP/IP, es decir, con enrutamiento de redes):

#### 3.1 Camino mínimo

Orientados a obtener el camino mínimo entre 2 nodos.

| Algoritmo |
|---|
| DIJKSTRA |
| BELLMAN-FORD |
| FLOYD-WARSHALL — el resultado es **todos los pares** de caminos mínimos del grafo |
| JOHNSON |
| VITERBI |
| A* |

> [!example] Ejemplo del PDF
> Camino 1→3 en un grafo ponderado: `caminos[1][3] = 13`, con ruta `1 → 2 → 4 → 3`.

#### 3.2 Recubrimiento mínimo (árbol de expansión mínima)

A partir de un grafo conexo ponderado se calcula la forma de llegar de un nodo a todos los demás. Es el **coste global mínimo** para llegar a todos los nodos — es la suma global mínima.

| Algoritmo |
|---|
| PRIM |
| KRUSKAL |

#### 3.3 Otros

- **FORD-FULKERSON**: caminos para **maximizar el flujo**.
- **TARJAN**: identifica **grupos fuertemente conexos**.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Ejemplos de uso real que ayudan a fijar la diferencia entre las dos familias: **Dijkstra** es el algoritmo que usan protocolos de enrutamiento como **OSPF** para que cada router calcule la ruta más corta hacia cada destino de la red. **Prim/Kruskal** (árbol de expansión mínima) se usan en problemas de diseño de infraestructura, como calcular el tendido de cable con menos coste total que conecte todos los edificios de un campus sin necesidad de que el camino entre dos edificios concretos sea el más corto — solo que todos queden conectados al mínimo coste total.

---

## Parte IV — Ficheros: acceso y ordenación

### 1. Tipos de acceso a ficheros

| Tipo de acceso | Descripción |
|---|---|
| **Secuencial** | Ejemplo: cinta. Búsqueda desde el inicio. Borrado **lógico**, ya que no puede hacerse físicamente. Se añade al final. |
| **Directo** | Se accede directamente a los registros. Una clave del registro, o una función sobre la clave, nos posiciona en el archivo. |
| **Indexado** | Es lo más novedoso. Un fichero para el **índice** y otro para los **datos**. Se busca la clave en el índice y este nos da la posición en el archivo de datos. |
| **Híbrido o ISAM** | Acceso **indexado** para el índice y **secuencial** para los datos. Ejemplo: MyISAM de MySQL. |

> [!important] ISAM conecta con los árboles B de la Parte II
> El índice de un acceso indexado o ISAM se implementa típicamente con un **árbol B o B+** — es la misma idea que aparece en la Parte II al decir que los árboles B se usan "en bases de datos y sistemas de ficheros".

### 2. Ordenación de ficheros externa

La ordenación externa (cuando los datos no caben en memoria, hay que ordenar en el propio fichero) puede ser:

- **Mezcla directa**: se hacen particiones y se ordena por pares.
- **Mezcla natural**: los trozos pueden ser variables, al encontrarnos tramos que ya vienen ordenados dentro de los datos de entrada.

---

## Parte V — Algoritmos: teoría, diseño y complejidad

### 1. Qué es un algoritmo

**Algoritmo**: conjunto de reglas que, aplicadas sistemáticamente a un conjunto de datos apropiados de entrada, resuelven un problema en un número finito de pasos elementales. **Un algoritmo debe terminar.**

### 2. Medios de expresión de un algoritmo

- **[[Flujograma|Diagramas de flujo]]** (estandarizados por ISO).
- **Pseudocódigo**.
- **Sistemas formales** (matemáticos).

### 3. Técnicas de análisis y diseño de algoritmos

| Técnica | Descripción |
|---|---|
| **Divide y vencerás** | Top-Down: divide el problema en subproblemas más pequeños del mismo tipo. |
| **Voraces (Greedy)** | Utilizan la opción óptima en cada paso, sin reconsiderar decisiones pasadas. |
| **Probabilísticos** | Montecarlo, Las Vegas. |
| **Backtracking** | Explora el árbol de soluciones. Prueba **todas** las posibilidades. Tarda mucho. |
| **Ramificación y poda** | Optimización de Backtracking: recuerda resultados anteriores para no repetir pasos. |
| **Programación dinámica** | Combina subproblemas óptimos. "Bottom-Up" o "Top-Down" + **memoización** (cachear resultados parciales para resolver ese subproblema en el futuro). |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Un ejemplo clásico para distinguir Backtracking de Programación Dinámica es el cálculo de Fibonacci: calculado de forma **recursiva ingenua** repite el cálculo de los mismos subproblemas una y otra vez (equivalente al "prueba todo" de Backtracking); con **memoización** (guardar en una tabla/caché cada resultado ya calculado) se evita recalcular, bajando la complejidad de exponencial a lineal. El concepto de memoización aquí es el mismo mecanismo de fondo que el [[Caching]]: guardar un resultado ya obtenido para no tener que recalcularlo/releerlo.

### 4. Complejidad espacial y temporal — Big O Notation

Representa la complejidad de un algoritmo. **Big O** es la **cota superior asintótica**.

De menor a mayor complejidad:

| Notación | Nombre |
|---|---|
| O(1) | Constante |
| O(log(n)) | Logarítmica |
| O(n) | Lineal |
| O(n log(n)) | n logarítmica |
| O(n²) | Cuadrática |
| O(2ⁿ) | Exponencial |
| O(n!) | Factorial |
| O(nⁿ) | Potencial Exponencial |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Intuición numérica para fijar el orden de magnitud, con n=20: O(log n) ≈ 4-5 pasos, O(n) = 20 pasos, O(n log n) ≈ 86 pasos, O(n²) = 400 pasos, O(2ⁿ) ≈ 1.048.576 pasos, O(n!) ≈ 2,4 × 10¹⁸ pasos. La diferencia entre O(n log n) (algoritmos de ordenación "buenos") y O(n²) (algoritmos "ingenuos") se vuelve brutal según crece n, que es justo por lo que en el examen importa distinguir bien qué algoritmo de ordenación tiene cada complejidad (Parte VI).

### 5. Clasificaciones de algoritmos de ordenación

- **Interno** (memoria) / **Externo** (fichero).
- **Natural**: tarda lo mínimo si la entrada ya está ordenada. Es "listo", se aprovecha de que los datos ya vienen ordenados.
- **Estable**: mantiene el orden relativo original de los datos. Ordena las claves iguales según estuviesen colocadas — no desordena claves iguales entre sí.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> La estabilidad importa cuando se ordena por más de un criterio en pasos sucesivos: por ejemplo, si primero ordenas una lista de empleados por nombre y luego, con un algoritmo **estable**, la vuelves a ordenar por departamento, dentro de cada departamento seguirán apareciendo ordenados por nombre (porque el segundo ordenamiento no altera el orden relativo de los que tienen la misma clave de departamento). Con un algoritmo inestable ese orden secundario se pierde.

### 6. Familias de algoritmos de ordenación

| Familia | Algoritmos | Idea |
|---|---|---|
| **Exchange Sorts** | Burbuja / Quick Sort / Cocktail (burbuja bidireccional) | Intercambiar y mover datos |
| **Selection Sorts** | Selección / Heap Sort | Busca la información (el mínimo/máximo) |
| **Insertion Sorts** | Inserción / Shell Sort | Busca dónde insertar. Shell Sort inserta con pasos más grandes para encontrar el sitio de X |
| **Merge Sorts** | Merge Sort | Mezclar |
| **Distribution Sorts** | Bucket Sort o Bin Sort / Radix Sort | No hacen comparaciones. Tienen "cajones" y distribuyen entre ellos en base a un criterio |

### 7. Tabla comparativa de complejidades

| Algorithm | Best | Average | Worst (tiempo) | Worst (espacio) |
|---|---|---|---|---|
| **Quicksort** | O(n log(n)) | O(n log(n)) | O(n²) | O(log(n)) |
| **Mergesort** | O(n log(n)) | O(n log(n)) | O(n log(n)) | O(n) |
| **Timsort** | O(n) | O(n log(n)) | O(n log(n)) | O(n) |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) |
| **Shell Sort** | O(n) | O((n log(n))²) | O((n log(n))²) | O(1) |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> **Timsort** no se explica en detalle en el PDF más allá de aparecer en la tabla, pero merece mención porque es el algoritmo de ordenación por defecto de **Python** (`sorted()`, `list.sort()`) y de **Java** (`Collections.sort()` para objetos): es un híbrido entre Merge Sort e Insertion Sort, diseñado para aprovechar tramos ya ordenados en datos reales — coherente con que su mejor caso sea O(n), igual que un algoritmo "natural".

---

## Parte VI — Algoritmos de ordenación en detalle

### Burbuja

**O(n²)**. Va desplazando el número más grande a base de comparaciones e intercambios entre elementos **adyacentes**. En el mejor caso tarda O(n), haciendo un algoritmo **natural** que detecte que la secuencia de datos ya está ordenada y así no hacer intercambios.

### Inserción Directa

**O(n²)**. Busca el lugar donde insertar el dato y desplaza los siguientes elementos para hacer hueco. Si en lugar de buscar secuencialmente hace una **búsqueda binaria**, entonces se conoce como **Inserción binaria**. La complejidad de la búsqueda en un árbol binario de búsqueda es O(log(n)).

### MergeSort

**O(n log(n))**. Es **recursivo**. Primero divide la lista en sublistas hasta llegar al **caso trivial** (el más sencillo, que se puede resolver directamente por comparación). Luego mezcla las sublistas para obtener una lista ordenada: **particiona, particiona, particiona... y fusiona, fusiona**.

### QuickSort

**O(n log(n))**. Es **recursivo**. Se elige un **pivote**. En la primera pasada, los menores del pivote se colocan a la izquierda y los mayores a la derecha. En la segunda pasada se hacen 2 llamadas de T(n/2). El **peor caso** sería O(n²) si el pivote es el menor o el mayor de los valores. Ejemplo de técnica para elegir el pivote (del propio PDF): se suman todos los valores y se obtiene el valor medio.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El caso más habitual en el que QuickSort cae en su peor caso O(n²) es cuando la entrada **ya viene ordenada (o casi)** y el pivote elegido es siempre el primer o el último elemento — porque entonces cada partición deja un lado vacío. Por eso las implementaciones reales suelen elegir el pivote de forma aleatoria o mediante la técnica "mediana de tres", para evitar ese escenario adversario.

### HeapSort (o Montículos)

**O(n log(n))**. Consiste en meter todos los datos en un montículo **Max-Heap** y luego se realizan N llamadas a `EliminarMax()`, dando como resultado un montículo menor que el elemento extraído en cada paso. La construcción y la reconstrucción del montículo es bastante eficiente.

### Selección

**Siempre O(n²)**. Primero busca el mínimo y lo coloca el primero. Luego busca el siguiente mínimo y lo coloca después. "Busco y coloco."

### RadixSort

**O(n·K)** (K = número de cifras). Se basa en el número de cifras de los números a ordenar.

- **LSD** (Least Significant Digit) usa el dígito menos significativo primero.
- **MSD** (Most Significant Digit) usa el más significativo primero.

Cuando los números se meten en los casilleros/*buckets*, se insertan ordenados. Primero se distribuyen en base a un dígito y luego el siguiente.

### BucketSort o BinSort

**O(n)**. Distribuye los números en casilleros y, dentro de cada casillero, se aplica el criterio que sea, dividiendo en más casilleros recursivamente o usando algoritmos de ordenación.

> [!example] Ejemplo del PDF
> Casilleros: 0-100, 101-200, 201-300... Luego, dentro de un casillero, subdividir de nuevo: 0-50, 51-100, 101-150, etc.

---

## Parte VII — Tipos de fichero y formatos

### 1. Ejecutables e instalables

| Extensión | Descripción |
|---|---|
| **exe** | Ejecutable de Microsoft |
| **msi** | Instalable de Microsoft |
| **pkg / dmg** | Instalable de Mac |
| **deb** | Instalable de Linux Debian y derivados (ej. Ubuntu) |
| **rpm** | Instalable de Linux RedHat y derivados (ej. CentOS) |
| **tar.gz** | Comprimido básico de Linux |

### 2. Otros formatos de propósito general

| Extensión | Descripción |
|---|---|
| **vcf** | vCard file |
| **p12 / pfx** | Certificado X.509 **con** su clave privada |
| **cer** | Certificado X.509 **sin** su clave privada |
| **eml** (RFC 2822) / **msg** | Formato de **un** correo electrónico |
| **mbox** | Contenedor de correos electrónicos (RFC 4155) |
| **pst / ost** | Buzones de Outlook |
| **nsf** | Buzones de Lotus. Lotus Notes (Cliente) y Lotus Domino (Servidor) |
| **apk / aab** | Instalable de Android. `aab` es el nuevo instalable, con todas las versiones de diferentes plataformas, para instalar la que aplique |
| **ipa** | Instalable de iOS |
| **csv** | Texto formateado separado por comas (`,`) o por punto y coma (`;`) |
| **swf** | Fichero con "película" Flash |
| **epub** | Libro electrónico |

> [!important] Certificado con o sin clave privada
> `p12`/`pfx` **incluye** la clave privada (hay que protegerlo, es sensible), `cer` **no la incluye** (es la parte pública, se puede compartir sin riesgo).

### 3. Ofimática

| Suite | Extensiones |
|---|---|
| **Microsoft (< 2007)** | `.xls`, `.doc`/`.dot` — formato propietario **OLE** |
| **Microsoft (>= 2007, OOXML)** | `.docx`/`.docm`/`.dotx`/`.dotm` (t = template; m = macro), `.xlsx`/`.xlsm`/`.xlsb`, `.pptx`/`.pptm`/`.potx`/`.potm`/`.ppsx`/`.ppsm` — formato **OOXML** (Office Open XML), estándar **ECMA 376**. Es un **.zip** con muchos ficheros XML dentro |
| **Open Office** | `.odt`/`.ott`/`.ods`/`.odp`/`.odg`/`.odc`/`.odf`/`.odi`/`.odh`/`.odb` |
| **PDF** | Estándar **ISO 32000-1:2008**. **PDF/A**: archivo a largo plazo. **PDF/UA**: accesibilidad universal. **PDF/X**: para impresoras. Relacionados: **PS** (PostScript), **PCL** |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El hecho de que un `.docx` sea "un .zip con ficheros XML dentro" se puede comprobar de forma práctica: renombrando cualquier `.docx` a `.zip` y abriéndolo con un descompresor normal, se ven las carpetas internas (`word/`, `_rels/`, etc.) con el XML del documento. Esto explica por qué OOXML se considera un formato **abierto** frente al antiguo `.doc` (formato binario propietario OLE, no legible sin la especificación de Microsoft).

### 4. Tipos de fichero de imagen

| Formato | Características |
|---|---|
| **jpeg / jpg** | Joint Photographic Experts Group. Compresión **con pérdida**. Existen variantes sin pérdida como JPEG2000 / Lossless JPEG |
| **png** | Compresión **sin pérdida**. Transparencia. **No** animación. True color (24 bits) |
| **gif** | 256 colores. Animación y transparencia. Compresión **LZW sin pérdida** |
| **tiff** | Etiquetado o *tagged*. Lo hay con y sin compresión. Multipágina |
| **bmp** | De Microsoft. Compresión **RLE** sin pérdida |
| **svg** | Scalable Vector Graphics. Tipo MIME `image/svg+xml`. Herramienta: InkScape. En HTML5 se incrusta dentro del HTML de forma nativa |
| **webp** | Con y sin pérdida. Desarrollado por Google |

> [!note] Tipo MIME
> Formato `tipo/subtipo`. Ejemplos del PDF: `image/gif`, `text/html`, `application/javascript`, `video/mpeg`, `application/pdf`. Lo usan los navegadores para identificar qué se está procesando.

### 5. Ficheros binarios y detección de tipo

- **Fichero binario**: la *signature* o **magic number** son los N primeros bytes que identifican qué tipo de fichero es.
- **Apache Tika**: librería de Java que detecta y extrae los metadatos de los ficheros mediante la detección del *magic number*.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Ejemplos concretos de *magic number* para fijar la idea: un PNG siempre empieza por los bytes `89 50 4E 47` (que en ASCII incluye la cadena "PNG"), y un PDF siempre empieza por la cadena literal `%PDF-`. Es por esto que renombrar un fichero cambiándole la extensión **no cambia su tipo real** — el sistema/la aplicación que lo abre puede (y a veces lo hace, como Apache Tika) inspeccionar esos primeros bytes en vez de fiarse de la extensión.

### 6. Audio

| Formato | Descripción |
|---|---|
| **MP3** | De ISO. MPEG-1 y MPEG-2 Audio Layer III. Moving Picture Experts Group. Compresión con pérdida. Transformada de Fourier discreta. Etiquetas **ID3** para catalogar/identificar autor, título, género, etc. |
| **AAC** | Sucesor de MP3. Con pérdida. MPEG-4 Audio (`.m4a`, `.m4b`, `.aac`, `.3gp`) |
| **FLAC** | Free Lossless Audio Codec |
| **ALAC** | Como FLAC pero de Apple |
| **AC3** | Compresión con pérdida. Multicanal. Laboratorios Dolby |
| **OPUS** | Compresión con pérdida. Xiph.Org Foundation. Extensión `.opus` |
| **VORBIS** | Compresión con pérdida. Xiph.Org Foundation. Extensión `.ogg` |

### 7. Vídeo

| Contenedor | Descripción |
|---|---|
| **MKV** | Contenedor. Estándar abierto |
| **AVI** | Contenedor. Microsoft. Audio Video Interleave |
| **ASF** | Contenedor. Microsoft. Contiene WMA y WMV |
| **OGG** | Contenedor. Estándar abierto. Xiph.Org Foundation |
| **3GP** | Contenedor. Para teléfonos móviles |
| **MP4** | Contenedor. MPEG-4 Part 14 |
| **MOV** | Contenedor. Apple. Extensión QT |
| **MPG** | Contenedor. MPEG-1 = VHS o CD. MPEG-2 = DVD. MPEG-4 = HD |
| **WEBM** | Contenedor basado en MKV. Vorbis/Opus (audio) y VP8/VP9/AV1 (vídeo) |

**Codecs**: DIVX, XDIV, AVC (H.264), HEVC (H.265), VVC (H.266), WMV, VP8, VP9, AV1.

> [!important] Contenedor vs codec — distinción clave de examen
> Un **contenedor** (MP4, MKV, AVI...) es el formato con "cajones" para meter el audio y el vídeo — como una caja que agrupa pistas. El **codec** (H.264, VP9, AAC...) es el algoritmo que realmente comprime/descomprime esas pistas dentro del cajón. Un mismo contenedor (ej. MKV) puede llevar dentro distintos codecs de vídeo y audio.

---

## 🔑 Resumen ultra-rápido (para repaso)

- **TAD** = qué hace (interfaz, puro); **EEDD** = cómo lo implementa (concreto). Stack≈LIFO, Queue≈FIFO. Lista no es posicional: 3º elemento = `head(tail(tail(Lista)))`.
- **Tabla Hash**: función Hash decide posición (ej. `x mod 250`); colisiones si tabla pequeña o función mala.
- **Montículo (Heap)**: O(n log n) inserción/borrado; max-heap = raíz mayor que todo lo de abajo; base de Priority Queue, HeapSort y Dijkstra.
- **Árboles**: profundidad (nodo→raíz, hacia arriba) vs altura (nodo→hoja, hacia abajo). FE de -1/0/+1 = AVL, reequilibrio por rotaciones.
- Recorridos: **Preorden RID** (Raíz-Izq-Der), **Inorden IRD** (Izq-Raíz-Der, da orden en un ABB), **Postorden IDR** (Izq-Der-Raíz).
- **Árbol B**: >2 hijos, orden M, mín. M/2 claves, usado en BD/ficheros. **Árbol B+**: hojas enlazadas, internos solo claves+punteros. **Árbol B***: densidad 2/3.
- **Grafos**: no tienen raíz. Orden=nº vértices, grado=arcos incidentes, tamaño=nº aristas. Representación: lista de adyacencia (eficiente, poco denso) vs matriz (rápida consulta, gasta memoria).
- Camino mínimo: **Dijkstra, Bellman-Ford, Floyd-Warshall (todos los pares), Johnson, Viterbi, A***. Recubrimiento mínimo: **Prim, Kruskal**. Otros: **Ford-Fulkerson** (flujo máximo), **Tarjan** (componentes fuertemente conexos).
- Acceso a ficheros: **secuencial** (cinta, borrado lógico) < **directo** (clave→posición) < **indexado** (fichero índice + fichero datos) < **ISAM/híbrido** (índice indexado + datos secuencial, ej. MyISAM).
- Diseño de algoritmos: **Divide y vencerás**, **Voraces**, **Probabilísticos** (Montecarlo/Las Vegas), **Backtracking** (prueba todo), **Ramificación y poda** (Backtracking + memoria), **Programación dinámica** (subproblemas + memoización).
- **Big O**: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!) < O(nⁿ).
- Ordenación: **natural** (rápido si ya viene ordenado), **estable** (no reordena claves iguales), **interno/externo** (memoria/fichero).
- Familias: Exchange (Burbuja, QuickSort), Selection (Selección, HeapSort), Insertion (Inserción, Shell), Merge (MergeSort), Distribution (BucketSort, RadixSort — sin comparaciones).
- Complejidades clave: Burbuja/Inserción/Selección = O(n²); MergeSort/QuickSort(medio)/HeapSort = O(n log n); QuickSort peor caso = O(n²) (pivote mal elegido); RadixSort = O(nK); BucketSort = O(n); Timsort = mejor caso O(n) (usado en Python/Java).
- Ficheros: OOXML (docx...) = zip de XML, ECMA 376; DOC/OLE = binario propietario; PDF = ISO 32000-1:2008.
- Imagen: jpg (con pérdida), png (sin pérdida, transparencia, sin animación), gif (256 colores, animación, LZW), tiff (multipágina), bmp (RLE), svg (vectorial, XML), webp (Google).
- Magic number = primeros bytes que identifican el tipo real de fichero, independiente de la extensión (Apache Tika lo usa).
- Audio: MP3 (ISO, con pérdida, ID3), AAC (sucesor MP3), FLAC/ALAC (sin pérdida), OPUS/VORBIS (Xiph.Org).
- Vídeo: **contenedor** (MP4, MKV, AVI...) ≠ **codec** (H.264, VP9...) — el contenedor es la caja, el codec comprime lo de dentro.
