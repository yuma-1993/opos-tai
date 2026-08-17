Principio de diseño: cuando dos clases **no** cumplen una relación "es un/a" verdadera, no deben unirse por herencia, sino que la clase que necesita reutilizar código de otra debe guardarla como **atributo interno** (composición/asociación) y delegar en ella.

Ejemplo: una `Pila` **no hereda** de `Lista` (heredar implicaría que una Pila "es una" Lista, lo cual no es conceptualmente cierto), sino que **reutiliza por composición**, guardando una `Lista` como atributo interno y delegando `push()`/`pop()` en sus métodos `add()`/`get()`. Ver [[Pila (Stack)]] y [[Lista enlazada (TAD)]].

La herencia crea un acoplamiento muy fuerte (la clase hija depende de los detalles internos de la clase padre y se rompe si esta cambia), mientras que la composición permite intercambiar la implementación interna sin afectar al resto. Es la misma idea que subyace al patrón [[Strategy (patrón GoF)|Strategy]] y al principio de [[Liskov Substitution Principle (LSP)|Liskov]]: si no hay una relación "es un/a" real, la herencia es un mal diseño. Es también la misma distinción que separa un TAD de su [[TAD vs EEDD|EEDD]] (interfaz vs. implementación).

*(Nota: la explicación del acoplamiento herencia/composición y su relación con Strategy y Liskov procede de una ampliación de conocimiento general añadida sobre la fuente original, no del PDF importado.)*

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
