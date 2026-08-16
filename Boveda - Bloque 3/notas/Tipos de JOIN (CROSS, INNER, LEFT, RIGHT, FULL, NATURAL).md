Los **JOIN** combinan filas de dos (o más) tablas según una condición (`... <tipo_join> JOIN <tabla> ON <condiciones>`). Usando de referencia una relación 1:N Autor→Libro (3 autores, 2 libros, uno de los autores sin libro):

| Tipo de JOIN | Qué devuelve | Filas en el ejemplo |
|---|---|---|
| CROSS JOIN | = `FROM tabla1, tabla2`. Producto cartesiano de las tablas | 6 |
| [INNER] JOIN | Solo las filas coincidentes según la condición | 2 |
| LEFT [OUTER] JOIN | Todas las filas de la tabla izquierda; los campos de la derecha valen NULL si no cumplen la condición. El nº de filas resultante es el nº de filas de la tabla izquierda | 3 |
| RIGHT [OUTER] JOIN | Igual que LEFT pero manda la tabla derecha | 2 |
| FULL [OUTER] JOIN | Manda las dos tablas y rellena con NULL donde una tabla no cumple la condición | 3 |
| NATURAL JOIN | Cuando los campos de ambas tablas tienen el mismo nombre, el propio gestor hace el match automáticamente | — |

> [!example] Fórmula del FULL JOIN
> `reg FULL = reg INNER + (reg LEFT − reg INNER) + (reg RIGHT − reg INNER)` → en el ejemplo: `2 + (3−2) + (2−2) = 2 + 1 + 0 = 3`.

El JOIN de SQL se traduce internamente a un producto cartesiano (×) filtrado (σ) — es literalmente la operación de "join" del [[Álgebra relacional vs Cálculo relacional|álgebra relacional]], que ya se recoge en las [[Operaciones básicas del álgebra relacional|operaciones básicas del álgebra relacional]].

Los JOIN son la razón de ser de un modelo [[Normalización|normalizado]]: al separar los datos en varias tablas para evitar redundancia, hace falta recomponerlos en tiempo de consulta uniendo tablas por sus claves foráneas — es el coste que se paga a cambio de eliminar la redundancia.

[[B3 - T3 SQL]]
