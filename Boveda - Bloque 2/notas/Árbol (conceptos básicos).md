Un **árbol** es una EEDD que **siempre tiene raíz** (a diferencia de un [[Grafo (conceptos básicos)|grafo]], que no la tiene). Una **hoja** es un nodo sin hijos, y el **peso** del árbol es su número total de nodos.

- **Orden**: número máximo de hijos que puede tener un nodo (el máximo teórico/potencial). Un árbol binario tiene orden 2.
- **Grado de un nodo**: número de hijos directos que tiene ese nodo en concreto. El **grado del árbol** es el máximo grado real de todos sus nodos, limitado por el orden.
- **Profundidad de un nodo**: número de aristas desde ese nodo hasta la raíz — se mide **de abajo hacia arriba**. La raíz tiene profundidad 0.
- **Altura de un nodo**: trayectoria más larga desde ese nodo hasta una hoja — se mide **de arriba hacia abajo**. Las hojas tienen altura 0.

**Profundidad vs altura — confusión típica de examen**: profundidad se mide de un nodo hacia la raíz (hacia arriba); altura se mide de un nodo hacia la hoja más lejana (hacia abajo). La raíz tiene profundidad 0, pero su altura es la altura total del árbol; una hoja tiene altura 0, pero su profundidad depende de cuántos niveles baja desde la raíz.

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]

Aparece como ejemplo de colección concreta en el patrón Iterator: [[B3 - T4.1 PATRONES DE DISENO Y SOLID|Patrones de diseño y SOLID]].
