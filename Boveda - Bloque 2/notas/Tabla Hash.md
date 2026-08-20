Una **tabla Hash** es la EEDD que implementa el TAD **Associative Array / Diccionario (clave-valor)** y también el TAD **Set/Multiset**. Sabe en qué posición va a colocar un elemento aplicando una **función Hash** sobre su clave (ejemplo típico: `x mod 250`).

Si la función Hash está mal diseñada, o la tabla es pequeña, **aumentan las colisiones** (varios elementos que caen en la misma posición). Cuando hay colisión, la búsqueda ya no es O(1), porque hay que buscar dentro de la lista de esa posición.

**Ampliación (conocimiento general, no viene del tema)**: las dos familias clásicas para resolver colisiones son el **encadenamiento** (cada posición guarda una lista enlazada con todos los elementos que colisionan ahí — es justo lo que obliga a "buscar dentro de la lista") y el **direccionamiento abierto** (si la posición está ocupada, se busca la siguiente libre según una regla). Cuanto más llena está la tabla (mayor *factor de carga*), más colisiones y peor rendimiento.

La función Hash se usa también en [[Buffering|buffers circulares]].

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]

Aparece como ejemplo de colección concreta en el patrón Iterator: [[B3 - T4.1 PATRONES DE DISENO Y SOLID|Patrones de diseño y SOLID]].

El modelo clave-valor de las bases de datos NoSQL (ej. REDIS) es, en esencia, una tabla hash distribuida: [[B2 - T5 NOSQL Y BIG DATA]].

[[Redis]] — el producto que ejemplifica este modelo clave-valor.
