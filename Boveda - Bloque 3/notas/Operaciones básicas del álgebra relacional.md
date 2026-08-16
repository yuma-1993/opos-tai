Toda operación del [[Álgebra relacional vs Cálculo relacional|álgebra relacional]] toma una o dos relaciones y devuelve una nueva relación (propiedad de "cierre").

| Operación | Notación | Qué hace | Ejemplo |
|---|---|---|---|
| Selección | σₚ(R) | Filtra filas (tuplas) que cumplen un predicado P | σ_edad>18(Alumno) → alumnos mayores de edad |
| Proyección | Π_A1,A2,...,An(R) | Extrae columnas (atributos) indicadas | Π_nombre,dni(Alumno) → solo nombre y dni |
| Producto cartesiano | R × S | Combina todas las tuplas de R con todas las de S (todos contra todos) | Libro × Autor → cada libro combinado con cada autor, tenga o no relación real |
| Unión | R ∪ S | Tuplas de R seguidas de las de S (requiere mismo esquema/grado) | Alumnos_Madrid ∪ Alumnos_Barcelona |
| Diferencia | R − S | Tuplas de R que no están en S | Alumnos_matriculados − Alumnos_aprobados = pendientes |

> [!tip] Confusión más común en examen
> σ (selección) filtra **FILAS**. Π (proyección) filtra **COLUMNAS**.

Todas las [[Operaciones derivadas del álgebra relacional|operaciones derivadas]] (intersección, join, división...) se construyen combinando estas cinco básicas.

[[B3 - T1.2 DISENO BBDD]]
[[B3 - T3 SQL]]
