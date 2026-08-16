Un **árbol B** es un árbol **equilibrado** en el que cada nodo puede tener **más de 2 hijos** (a diferencia de un árbol binario): de **orden M**, cada nodo tiene como máximo M hijos y, salvo la raíz, como mínimo M/2 claves. Mantiene los datos siempre **ordenados**, con inserciones y borrados en tiempo **log(n)**. Es muy usado en **bases de datos y sistemas de ficheros**.

- **Árbol B+**: variante en la que los **nodos internos solo contienen claves y punteros** (no datos), y los **nodos hoja están enlazados entre sí**, lo que facilita recorrer rangos de valores por niveles.
- **Árbol B\***: variante cuyo algoritmo de inserción garantiza una **densidad de ocupación de 2/3** — es un árbol muy denso.

**Por qué dominan en bases de datos (ampliación, no viene literalmente del tema)**: cada nodo de un árbol B se diseña para ocupar exactamente un **bloque de disco** (de ahí que tenga muchos hijos y no solo 2), así que bajar un nivel en el árbol cuesta **una sola lectura de disco**, la operación cara. El árbol B+ es preferible en bases de datos relacionales porque, al tener las hojas enlazadas, permite recorrer rangos (`WHERE edad BETWEEN 20 AND 30`) sin volver a subir por el árbol. Esta es la EEDD que suele haber detrás del índice de un acceso **[[Tipos de acceso a ficheros (secuencial, directo, indexado, ISAM)|indexado o ISAM]]**.

[[Árbol (conceptos básicos)]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
[[B3 - T3 SQL]]
