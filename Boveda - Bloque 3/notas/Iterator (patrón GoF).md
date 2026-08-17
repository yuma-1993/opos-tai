Patrón de **comportamiento** que permite recorrer (iterar) una colección de objetos sin que el cliente necesite conocer el tipo concreto de esa colección. El objeto `Iterator` aísla al cliente de la colección subyacente: el cliente solo llama a `next()`/`hasNext()`. Para conseguirlo hacen falta clases especializadas en recorrer cada tipo de colección, todas ellas ofreciendo el mismo interfaz de recorrido.

Sin este patrón, el cliente tendría que conocer la API específica de cada colección concreta ([[Lista enlazada (TAD)|Lista]], [[Árbol (conceptos básicos)|Árbol]], [[Tabla Hash|Hash]], [[Grafo (conceptos básicos)|Grafo]]) para recorrerla; con Iterator, todas implementan el mismo interfaz `Iterador` y el cliente puede recorrer cualquiera de ellas con el mismo código, por polimorfismo.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
