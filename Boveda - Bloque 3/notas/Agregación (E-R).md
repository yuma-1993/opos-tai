En el modelo Entidad-Relación, permite tratar una relación completa (o un conjunto de entidades) como si fuera una entidad de orden superior, para poder relacionarla a su vez con otra entidad. Ej: la relación `Empleado — trabaja_en — Proyecto` se agrega como un bloque, y ese bloque se relaciona con `Jefe` que la supervisa. Sirve para simplificar y agrupar partes del modelo que conceptualmente forman una unidad.

> [!note] Conocimiento general (no forma parte de la fuente del temario)
> Ojo con este mismo nombre en otros contextos: en UML/POO, "agregación" significa otra cosa — una relación todo-parte tipo "tiene un" (ej. un `Coche` tiene `Ruedas`), sin implicar que el todo controle la existencia de la parte. No debe confundirse con este uso E-R, que consiste en convertir una relación entera en una entidad para poder seguir relacionándola.

[[B3 - T1.1 ENTIDAD RELACION]]
