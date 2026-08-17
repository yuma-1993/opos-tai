El **diagrama de clases** es el diagrama central de UML: modela las clases del sistema, sus atributos, sus métodos y las relaciones entre ellas. La relación de asociación es equivalente al [[B3 - T1.1 ENTIDAD RELACION|diagrama E/R]], y las [[Relaciones del diagrama de clases UML (asociación, agregación, composición, dependencia, realización)|agregaciones y composiciones son en realidad tipos de asociación]].

Convenciones propias de este diagrama: una línea de asociación se traduce en un **atributo**; si el nombre de una clase (o de un método) aparece en **cursiva**, es **abstracta**; una clase puede implementar una **interface** (el mismo par interfaz/implementación del principio [[Dependency Inversion Principle (DIP)|Dependency Inversion]] de SOLID: depender de la interfaz, no de la clase concreta); y las clases pueden llevar **estereotipos** (`«entity»`, `«enumeration»`...) para precisar su naturaleza.

La **navegabilidad** (las flechas en los extremos de una asociación) es una decisión de **diseño**, no de negocio: indica por qué extremo se puede "recorrer" la relación en el código (ej. de un pedido interesa navegar a sus items, pero no al revés).

[[B3 - T4.2 UML]]
