El TAD **List (lista/secuencia)** tiene como primitivas `isEmpty`, `insertarDelante`, `insertarDetras`, `head` (primer elemento) y `tail` (quita la cabeza y devuelve el resto de la lista).

Una característica clave: una lista **no es posicional**, por lo que no existe una primitiva para recuperar directamente el elemento N. Para llegar a él hay que ir combinando `head`/`tail`: por ejemplo, el 3º elemento se obtiene como `head(tail(tail(Lista)))`.

Se implementa típicamente como **array** o como **lista enlazada** propiamente dicha (nodos con puntero al siguiente).

[[TAD vs EEDD]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]

Aparece como ejemplo de colección concreta en el patrón Iterator y en el ejemplo de composición vs. herencia: [[B3 - T4.1 PATRONES DE DISENO Y SOLID|Patrones de diseño y SOLID]].
