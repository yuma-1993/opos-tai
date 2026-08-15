Clasificación general y simplificada de una relación E-R: **1:1, 1:N o N:M**. Solo mira el **máximo** de cada lado de la [[Cardinalidad (E-R)|cardinalidad]], ignorando los mínimos (y por tanto, ignorando la obligatoriedad).

- (1,1) y (1,N) → **1:N**. Ej: un `Autor` (1) escribe muchos `Libros` (N), pero cada `Libro` tiene un único `Autor`.
- (1,N) y (1,N) → **N:M**. Ej: un `Alumno` cursa varias `Asignaturas`, y una `Asignatura` tiene varios `Alumnos`.
- (1,1) y (1,1) → **1:1**. Ej: `Persona` — tiene — `DNI`.

> [!tip] Truco para no confundirlo con Cardinalidad
> Tipo de correspondencia = la "categoría" (1:1 / 1:N / N:M), útil para hablar en general de la relación. Cardinalidad = el detalle exacto (mín,máx) que se pone en el diagrama junto a cada entidad, y de donde sale esa categoría — la cardinalidad es el dato en bruto, el tipo de correspondencia es su resumen.

[[B3 - T1.1 ENTIDAD RELACION]]
