**QuickSort** tiene complejidad **O(n log n)** en el caso medio y es **recursivo**, basado en **[[Divide y vencerás]]**: se elige un **pivote**, y en una primera pasada se colocan a su izquierda los elementos menores y a su derecha los mayores; después se repite el proceso sobre cada mitad (2 llamadas recursivas de tamaño n/2).

Su **peor caso** es **O(n²)**, y ocurre cuando el pivote elegido resulta ser siempre el menor o el mayor de los valores (la partición deja un lado vacío). Una técnica citada para elegir el pivote es tomar el valor medio a partir de la suma de todos los valores.

**Ampliación (conocimiento general, no viene del tema)**: el caso más habitual en que QuickSort cae en O(n²) es cuando la entrada ya viene ordenada (o casi) y el pivote elegido es siempre el primer o el último elemento. Por eso las implementaciones reales suelen elegir el pivote de forma aleatoria o con la técnica "mediana de tres".

[[Big O (notación de complejidad algorítmica)]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
