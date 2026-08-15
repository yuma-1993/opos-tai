Concepto matemático central del modelo relacional: R(A₁, A₂, ..., Aₙ), un conjunto de tuplas (filas) definido sobre unos atributos (columnas). **Esquema/intensión**: R() — la definición de la relación y sus atributos, la "plantilla", no los datos en sí. Frente a eso, la **extensión** son las tuplas que contiene en un momento dado (ver [[Cardinalidad (modelo relacional)]]).

Toda relación debe cumplir tres propiedades obligatorias:

- **Atomicidad**: cada atributo tiene un único valor, no multivaluado (ej. no puedes poner "Madrid, Barcelona" en una celda de ciudad — eso rompe la 1FN de [[Normalización|normalización]]).
- **No repetición de tuplas**: siempre existe una clave que garantiza filas únicas (ver [[Claves (superclave, candidata, primaria, alternativa)]]).
- **Sin orden en tuplas ni en atributos**: da igual el orden de filas o columnas, conceptualmente son un conjunto.

> [!important] Mismo nombre, otro nivel de modelado
> "Relación" aquí no es lo mismo que **Relación** en el modelo Entidad-Relación (Tema 1.1): allí "relación" es el vínculo entre entidades (el rombo, con su [[Grado de una relación (E-R)|grado]], [[Rol (E-R)|rol]] y [[Cardinalidad (E-R)|cardinalidad]]). Aquí, en el modelo relacional, "relación" es sinónimo de **tabla**: R(A₁...Aₙ) con sus filas y columnas. Es el mismo término aplicado a dos niveles de modelado distintos (ver [[Niveles de modelado (Conceptual, Lógico, Físico)]]), y es una de las mayores fuentes de confusión del bloque si no se separan bien los dos usos.

[[B3 - T1.2 DISENO BBDD]]
