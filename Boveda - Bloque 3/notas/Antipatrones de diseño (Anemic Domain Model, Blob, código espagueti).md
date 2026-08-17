Los **antipatrones** son la contrapartida directa de los patrones y técnicas de buen diseño ([[GRASP (técnicas de asignación de responsabilidades)|GRASP]]/[[SOLID (principios)|SOLID]]): errores de diseño recurrentes y conocidos.

- **Anemic Domain Model**: clases de dominio sin ningún comportamiento, solo datos. Viola *Information expert*: la lógica que debería vivir en la clase que tiene los datos se traslada a clases de servicio externas.
- **Blob** (también llamado *God Object*): un objeto todopoderoso que concentra demasiadas responsabilidades. Viola *Single Responsibility* y *High cohesion*.
- **Código espagueti**: código con poca estructuración, de flujo complejo e incomprensible. Es justo lo que *Low coupling*/*High cohesion* y patrones como [[Chain of Responsibility (patrón GoF)|Chain of Responsibility]] o [[State (patrón GoF)|State]] buscan evitar.

*(Nota: la relación de cada antipatrón con el principio GRASP/SOLID que viola procede de una ampliación de conocimiento general añadida sobre la fuente original, no del PDF importado; los tres antipatrones en sí sí vienen en la fuente.)*

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
