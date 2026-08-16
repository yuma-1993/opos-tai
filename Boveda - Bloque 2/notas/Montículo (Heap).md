Un **montículo (Heap)** es una EEDD basada en árbol que cumple la **propiedad del montículo**: en un **max-heap**, la raíz es siempre mayor o igual que todos los elementos que hay debajo (existe también el min-heap, con la relación inversa). Es la EEDD que implementa el TAD **Priority Queue**.

Se puede implementar como **árbol binario** (montículo binario) o como **array**. Tanto las inserciones como los borrados/reequilibrios tienen complejidad **O(n log n)**.

**Por qué es un concepto bisagra del tema**: el montículo es la base de **[[HeapSort]]** (se meten todos los datos en un max-heap y se extrae el máximo repetidamente) y también del algoritmo de **[[Algoritmo de Dijkstra|Dijkstra]]**, que usa internamente una cola de prioridad para elegir siempre el nodo aún no visitado más cercano.

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
