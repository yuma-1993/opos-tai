Un **grafo** es una red de nodos (vértices) unidos por aristas — a diferencia de un [[Árbol (conceptos básicos)|árbol]], **no tiene raíz**. Puede ser **dirigido** (dígrafo) o **no dirigido**, **conexo** o **inconexo**, **cíclico** o **acíclico**; un **multigrafo** es aquel con más de una arista entre los mismos dos vértices, y un grafo **etiquetado o ponderado** lleva un peso numérico en cada arista.

- **Orden del grafo**: número de vértices.
- **Grado de un vértice**: número de arcos incidentes en él.
- **Grado del grafo**: suma de los grados de todos sus vértices.
- **Tamaño**: número de aristas.

Se puede representar como **lista de adyacencia** (array de vértices + listas enlazadas de vecinos — eficiente en memoria si el grafo es poco denso) o como **matriz de adyacencia** (matriz N×N que indica si hay arista entre cada par de vértices — consulta en O(1) pero desperdicia memoria si hay muchos nodos y pocas aristas).

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
