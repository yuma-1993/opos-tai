El **diagrama de máquina de estados** (o de transición de estados) expresa el comportamiento dinámico de una parte del sistema: cómo transitan los objetos de una clase concreta entre sus distintos estados posibles, y con qué condiciones. Se usa para clases con comportamiento dinámico (hay correspondencia directa con la clase que modela), y ayuda a plantear pruebas unitarias porque cada transición lleva asociadas condiciones. Es la antesala natural del patrón de diseño [[State (patrón GoF)|State]].

Si la condición de una transición aparece entre corchetes `[…]`, se denomina **guarda** — por ejemplo, en una cuenta de usuario, la transición de `New` a `Active` podría llevar la guarda `[isVerified()] activate/`.

*(Ampliación, no viene literal de la fuente):* este tipo de diagrama se basa en los *statecharts* de David Harel (1987), que añadieron a las máquinas de estado finito clásicas la posibilidad de anidar estados y ejecutarlos en paralelo — de ahí que un diagrama de estados UML pueda representar sistemas más complejos que un simple autómata de estados finitos.

[[B3 - T4.2 UML]]
