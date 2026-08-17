Patrón **estructural** que proporciona un servicio intermedio de alto nivel (por agregación) para desacoplar subsistemas entre sí. Es una clase con métodos de alto nivel cuyo objetivo es minimizar el acoplamiento entre las clases de un subsistema cliente y las clases de otro subsistema que ofrece servicios: la clase Facade no solo centraliza las peticiones de los clientes, también les ofrece una interfaz de más alto nivel que la de las clases internas. Si el proceso de negocio cambia, basta con cambiar la implementación de la fachada.

Para crear el objeto de la clase Facade se suele usar primero [[Singleton (patrón GoF)|Singleton]] (esa clase solo se crea una vez) y después [[Factory Method (patrón GoF)|Factory Method]] (porque puede haber implementaciones distintas de la fachada según el cliente que la use).

**Proxy vs. Facade vs. Adapter**: ver [[Proxy (patrón GoF)]].

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
