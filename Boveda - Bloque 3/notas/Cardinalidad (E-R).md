Indica cuántas ocurrencias de una entidad se pueden asociar con cuántas ocurrencias de la otra, a través de una interrelación. Se expresa como un par **(mínimo, máximo)** en cada extremo de la relación, e incluye la obligatoriedad (si el mínimo es 0 o 1) — algo que el [[Tipo de correspondencia]] no recoge.

> [!important] El matiz que más se falla en examen
> El número que pones en un extremo es el que le corresponde "leyendo hacia el otro lado". Si al lado de `Autor` pones (1,N), significa que por cada Libro hay entre 1 y N Autores: la cardinalidad puesta junto a una entidad describe cuántas veces participa esa entidad, vista desde la otra.

Ej: cardinalidades `Autor (1,1)` y `Libro (0,N)` → el tipo de correspondencia que se deduce es 1:N (mirando solo los máximos), pero la cardinalidad además dice que un `Libro` puede no tener autor asignado todavía (mínimo 0).

> [!important] Mismo nombre, otro nivel de modelado
> No confundir con la **Cardinalidad en el modelo relacional** (Tema 1.2), que no tiene nada que ver con mínimos y máximos de una relación: allí es simplemente el número de filas (tuplas) que tiene una tabla en un momento dado. Ver [[Cardinalidad (modelo relacional)]].

[[Grado de una relación (E-R)]]
[[B3 - T1.1 ENTIDAD RELACION]]
