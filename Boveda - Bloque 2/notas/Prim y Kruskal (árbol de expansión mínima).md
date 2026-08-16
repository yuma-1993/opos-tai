**Prim** y **Kruskal** son los dos algoritmos clásicos de **recubrimiento mínimo (árbol de expansión mínima)**: a partir de un grafo conexo ponderado, calculan la forma de llegar de un nodo a todos los demás con el **coste global mínimo** — no el camino más corto entre dos nodos concretos (eso lo resuelve [[Algoritmo de Dijkstra|Dijkstra]]), sino la suma total mínima para que todos queden conectados.

**Ejemplo de uso real (ampliación, no viene literalmente del tema)**: se usan en problemas de diseño de infraestructura, como calcular el tendido de cable con menos coste total que conecte todos los edificios de un campus, sin que importe que el camino entre dos edificios concretos sea el más corto — solo que todos queden conectados al mínimo coste total.

[[Grafo (conceptos básicos)]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
