**BASE** (*Basically Available, Soft state, Eventually consistent*) es el modelo de consistencia típico de las bases de datos NoSQL: la información distribuida tarda en consolidarse, así que en vez de garantizar consistencia estricta en todo momento, se acepta que en un instante dado distintos nodos puedan tener versiones ligeramente distintas del dato, hasta que **eventualmente** convergen.

Es la contrapartida de **[[ACID (transacciones)|ACID]]**, el modelo del mundo relacional. Los sistemas NoSQL no garantizan completamente ACID a cambio de escalar mejor de forma distribuida; no son incompatibles en abstracto, pero sí una elección de diseño: cuanta más disponibilidad/escalabilidad se exige, más difícil es mantener consistencia estricta en todo momento — esta es precisamente la tensión que formaliza el **[[Teorema CAP (o de Brewer)|teorema CAP]]**.

[[ACID (transacciones)]]
[[Niveles de aislamiento y lecturas anómalas (SQL)]]
[[B2 - T5 NOSQL Y BIG DATA]]
