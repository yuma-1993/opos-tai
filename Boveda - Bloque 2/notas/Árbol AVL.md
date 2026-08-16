Un **árbol AVL** es un [[Árbol Binario de Búsqueda (ABB)|ABB]] **equilibrado o autobalanceable**: para cada nodo, el **Factor de Equilibrio (FE)** — la diferencia de altura entre su subárbol izquierdo y su subárbol derecho — se mantiene siempre en 0, +1 o -1.

Cuando una inserción o un borrado rompe ese rango, el árbol se reequilibra mediante **rotaciones**. El **árbol de Fibonacci** es un caso particular de árbol AVL.

**Ampliación (conocimiento general, no viene del tema)**: cuando el FE de algún nodo se sale del rango [-1, +1], se aplica una **rotación simple** (izquierda o derecha) o una **rotación doble** (izquierda-derecha o derecha-izquierda), reorganizando localmente 2 o 3 nodos para devolver el árbol al rango permitido sin romper el orden del ABB subyacente.

[[Árbol (conceptos básicos)]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
