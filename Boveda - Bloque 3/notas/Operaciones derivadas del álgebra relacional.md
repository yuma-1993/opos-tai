Se construyen combinando las [[Operaciones básicas del álgebra relacional|operaciones básicas]] — no añaden potencia expresiva nueva, solo comodidad.

- **Intersección**: `R ∩ S = R − (R − S)`. Tuplas presentes en ambas relaciones. Se deriva restando dos veces con diferencia.
- **Unión natural / Inner Join**: `R ⋈ S = Π_A1,A2...An(σθ(R × S))`. Es una proyección de una selección sobre el producto cartesiano: primero cruzas todo con todo (×), luego filtras solo las combinaciones que cumplen la condición de igualdad (σθ), luego te quedas con las columnas necesarias, eliminando la duplicada (Π).
  - θ (theta) es la condición del join; cuando es una igualdad se llama **EquiJoin**.
  - Ejemplo: `Libro ⋈ Autor` (por ID_Autor) → solo libros con su autor correspondiente, no el cruce completo.
- **División**: `R / S`. Dado A(x, y) y B(y), devuelve los valores de x tales que, para todo valor y presente en B, existe la tupla (x, y) en A.
  - Es la operación que responde a preguntas tipo "todos": ej. `Matricula(alumno, asignatura) / Asignatura_obligatoria(asignatura)` → alumnos matriculados en todas las asignaturas obligatorias.
  - Es la operación menos intuitiva del álgebra; suele aparecer en examen justo por eso.
- **Outer Joins**: variantes del join que conservan tuplas sin correspondencia (rellenando con NULL), en vez de descartarlas como el inner join. (Left, Right, Full).
- **Renombrado**: `ρ_a/b(R)`. Cambia el nombre de un atributo o de la relación completa, sin alterar los datos. Útil, por ejemplo, para poder hacer un self-join (cruzar una tabla consigo misma necesita nombres distintos para cada "copia").

[[B3 - T1.2 DISENO BBDD]]
