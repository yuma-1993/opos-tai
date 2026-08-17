Principio **I** de [[SOLID (principios)|SOLID]]: *make fine grained interfaces that are client specific* — los clientes no deben depender de interfaces que no utilizan.

El problema aparece con una interfaz monolítica: si una clase `ServicioXXX` ofrece `logica1()` y `logica2()`, para un cliente que solo necesita `logica1()`, el método `logica2()` es "basura" que no le hace falta (y viceversa para otro cliente).

La solución es segregar la interfaz en varias más pequeñas y específicas por cliente (`Servicio1` con `logica1()`, `Servicio2` con `logica2()`), aunque la clase que las implementa (`ServicioXXX`) siga siendo la misma por dentro — es como hacer "vistas" distintas de una misma clase según quién la consuma. Esto además permite que esa clase tenga métodos propios que no formen parte de ningún interfaz expuesto, y que en el futuro aparezca una implementación alternativa de las mismas interfaces sin que los clientes se enteren.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
