Tres patrones de diseño específicos del contexto **J2EE** (Java Enterprise), pensados para separar responsabilidades en aplicaciones web:

**Intercepting Filter**: en lugar de meter la lógica de seguridad (o cualquier tarea transversal) dentro de cada servlet, se extrae a un *filter* que se coloca delante de los servlets. Así el servlet se limita a su propia lógica de negocio, y el filtro intercepta la petición antes de que llegue.

**Composite View**: para pantallas muy complejas, en vez de construir una única vista monolítica, se compone la pantalla a partir de vistas más pequeñas (*subviews*) que se ensamblan.

**Data Access Object (DAO)**: agrupa en una clase dedicada todo el código de acceso a datos (SQL o JPA), para no tenerlo disperso por las clases de negocio. Es una de las variantes de un patrón de acceso a datos más general, junto con Data Mapper o Active Record.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
