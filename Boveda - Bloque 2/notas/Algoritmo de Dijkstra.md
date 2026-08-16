**Dijkstra** es un algoritmo de **camino mínimo** sobre un [[Grafo (conceptos básicos)|grafo]] ponderado: calcula la ruta de menor coste entre dos nodos. Internamente usa una cola de prioridad (implementada con un **[[Montículo (Heap)|montículo]]**) para ir eligiendo siempre el nodo aún no visitado que está más cerca.

**Ejemplo de uso real (ampliación, no viene literalmente del tema)**: es el algoritmo que usan protocolos de enrutamiento como **OSPF** para que cada router calcule la ruta más corta hacia cada destino de la red.

Se diferencia de **[[Prim y Kruskal (árbol de expansión mínima)|Prim/Kruskal]]** en el problema que resuelve: Dijkstra busca el camino más corto **entre dos nodos concretos**, mientras que Prim/Kruskal buscan el coste global mínimo para conectar **todos** los nodos entre sí.

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
