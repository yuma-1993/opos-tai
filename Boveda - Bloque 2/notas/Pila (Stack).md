Un **Stack o pila** es un TAD que se comporta en **LIFO** (Last In, First Out): el último elemento que entra es el primero que sale. Sus primitivas son `push` (añadir), `pop` (quitar el último añadido) e `isEmpty`/`peek` (consultar sin quitar).

Se puede implementar con un **array** o con una **lista enlazada**, indistintamente — la elección de EEDD no cambia el comportamiento LIFO que promete el TAD.

**Ejemplo real**: la pila de llamadas de un programa (`call stack`) es una pila — la última función llamada es la primera en terminar y "salir" de la pila. (Ampliación, no viene literalmente del tema.)

[[TAD vs EEDD]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]

Ejemplo de diseño OO que usa esta idea (composición, no herencia): [[B3 - T4.1 PATRONES DE DISENO Y SOLID|Patrones de diseño y SOLID]] — `Pila` reutiliza `Lista` guardándola como atributo interno, sin heredar de ella.
