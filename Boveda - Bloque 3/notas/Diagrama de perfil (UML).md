El **diagrama de perfil** aplica el mecanismo de extensión [[Mecanismos de extensión UML (estereotipos, restricciones, valores etiquetados, perfiles)|Perfil]] para adaptar UML a una plataforma tecnológica concreta (.NET, Java, etc.), dando de alta elementos que no existen en el UML nativo. Se crea un **estereotipo** propio (por ejemplo `EJB`) que luego se puede usar en cualquier diagrama como `<<EJB>>` — es, en la práctica, equivalente a hacer que ese estereotipo "herede" de una metaclase existente (`Component`).

Ej. del perfil Java EJB 3.0 de la fuente: la metaclase `«Metaclass» Component` se extiende con el estereotipo `«stereotype» EJB`, del que heredan a su vez `Session EJB` (con `Stateless EJB` / `Stateful EJB`), `Entity EJB` y `Message EJB`.

[[B3 - T4.2 UML]]
