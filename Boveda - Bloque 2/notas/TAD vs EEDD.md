Un **TAD (Tipo Abstracto de Dato)** es un modelo puramente matemático que define un tipo de dato desde fuera: qué operaciones (primitivas) existen y qué hacen, sin decir nada sobre cómo se implementan por dentro. Define el **qué**.

Una **EEDD (Estructura de Datos)** es la pieza concreta que da vida a un TAD: la herramienta real con la que se implementa. Define el **cómo**. Un mismo TAD puede tener varias EEDD que lo implementen — por ejemplo, el TAD `List` (secuencia) se puede implementar con un `Array` o con una `Lista enlazada`, y el TAD `Stack` (pila, LIFO) también se puede montar sobre cualquiera de las dos.

**¿Por qué hace falta esto?**
Es la misma distinción que hay en programación orientada a objetos entre una interfaz y su implementación: un TAD "Pila" solo promete que existen `push`, `pop` e `isEmpty`, y que se comportan como LIFO, sin decir si por dentro hay un array o una lista enlazada. Por eso una misma pila se puede reimplementar sin que el código que la usa se entere — es la base del principio de encapsulación. (Ampliación, no viene literalmente del tema.)

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]

Esta misma distinción (interfaz vs. implementación) es la base del ejemplo de composición vs. herencia y del principio de Inversión de Dependencias: [[B3 - T4.1 PATRONES DE DISENO Y SOLID|Patrones de diseño y SOLID]].
