Principio **D** de [[SOLID (principios)|SOLID]]: *depend on abstractions, not on concretions* — hay que depender de interfaces (abstracciones), no de clases concretas (implementaciones).

Las interfaces apenas cambian, pero las implementaciones sí; por eso es mejor que una clase dependa de una interfaz (`Servicio1`) que de la implementación concreta que hay detrás (`ServicioXXX`). **Spring** es un framework de inyección de dependencias que aplica este principio: la anotación `@Autowired` hace que, en tiempo de arranque, el contenedor de Spring resuelva qué implementación concreta debe inyectar en una variable declarada con el tipo abstracto, sin que la clase que la usa tenga que hacer `new` explícitamente — el código cliente solo conoce la interfaz.

Está directamente relacionado con [[Factory Method (patrón GoF)|Factory Method]], donde el cliente también depende de la abstracción y nunca de la implementación concreta que se instancia por debajo.

*(Nota: la explicación de `@Autowired` como aplicación práctica de este principio procede de una ampliación de conocimiento general añadida sobre la fuente original, no del PDF importado.)*

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
[[B3 - T4.2 UML]] (relación de realización: clase que implementa una interface)
