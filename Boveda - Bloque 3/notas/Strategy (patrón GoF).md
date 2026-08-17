Patrón de **comportamiento** similar a [[Command (patrón GoF)|Command]], pero orientado a un **algoritmo concreto**: separa distintas implementaciones de un mismo método detrás de una interfaz común, de modo que se puedan intercambiar (por ejemplo, distintos algoritmos de ordenación — Burbuja, Merge, QuickSort — todos implementando la misma interfaz `AlgOrdenacion`).

**Strategy vs. State vs. Template Method** (los tres "encapsulan comportamiento variable", y se confunden en examen): Strategy intercambia un **algoritmo completo desde fuera** (el cliente elige la estrategia); [[State (patrón GoF)|State]] cambia el comportamiento de un objeto según su **estado interno**, y es el propio objeto el que transiciona de un estado a otro; [[Template Method (patrón GoF)|Template Method]] fija el **esqueleto** del algoritmo en la clase base y delega solo pasos concretos a las subclases, sin poder alterar el orden de esos pasos.

*(Nota: la comparación de los tres procede de una ampliación de conocimiento general añadida sobre la fuente original, no del PDF importado.)*

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
