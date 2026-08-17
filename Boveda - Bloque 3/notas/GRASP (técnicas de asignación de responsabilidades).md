**GRASP** (*General Responsibility Assignment Software Patterns*): conjunto de técnicas básicas para decidir a qué clase asignar cada responsabilidad, más elementales que los patrones GoF.

- **Information expert**: asignar la responsabilidad a la clase que tiene la información necesaria para realizar esa tarea.
- **Creator**: indica qué clase debe crear instancias de otra, típicamente la que las agrega, contiene o usa de cerca.
- **Controller**: gestiona eventos (que no sean de interfaz de usuario).
- **Indirection**: asigna la responsabilidad a un objeto intermedio para desacoplar dos elementos — es la base conceptual de patrones como [[Facade (patrón GoF)|Facade]] o [[Adapter (patrón GoF)|Adapter]].
- **Low coupling** y **High cohesion**: buscan un acoplamiento bajo y una cohesión alta entre clases, para evitar el código espagueti (flujo complejo e incomprensible).
- **Polymorphism**: asignar la responsabilidad usando operaciones polimórficas cuando el comportamiento varía según el tipo.
- **Protected variations**: identificar los puntos de variación previsibles y ponerles alrededor una interfaz estable, para blindar al resto del sistema de esos cambios.
- **Pure fabrication**: crear una clase que no representa ningún concepto del dominio, solo para lograr bajo acoplamiento/alta cohesión (por ejemplo, una clase de persistencia).

*(Nota: Creator, Indirection, Polymorphism, Protected variations y Pure fabrication proceden de una ampliación de conocimiento general añadida sobre la fuente original, no del PDF importado; el resto sí viene desarrollado en la fuente.)*

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
