La forma declarativa de consultar (ver [[Álgebra relacional vs Cálculo relacional]]): se describe la condición que deben cumplir los resultados, no los pasos para obtenerlos. Dos variantes:

**Cálculo relacional de tuplas** — la variable representa una tupla completa: `{ t / Θ(t) }`, donde t es una variable de tipo tupla y Θ(t) la fórmula/predicado que t debe cumplir.

> [!example]
> `{ t / Libro(t) ∧ t.isbn="..." }` → todas las tuplas t que pertenecen a Libro y cuyo isbn es ese valor. Equivale conceptualmente a `SELECT * FROM Libro WHERE isbn='...'` en SQL.

**Cálculo relacional de dominios** — las variables representan valores individuales de atributos (no la tupla completa): `{ (x, y, z) / P(x, y, z) }`. Cada componente (x, y, z) es un dominio/atributo suelto, y P es el predicado que deben cumplir conjuntamente.

> [!example]
> `{ (A, B, C) / (A, B, C) ∈ Vuelos ∧ A='Madrid' }` → todas las combinaciones (A,B,C) que sean una tupla real de Vuelos y donde el origen sea Madrid.

> [!important] Diferencia clave tuplas vs dominios
> En el de tuplas la variable es la fila entera; en el de dominios, cada variable es una columna suelta y se combinan mediante el predicado.

[[B3 - T1.2 DISENO BBDD]]
