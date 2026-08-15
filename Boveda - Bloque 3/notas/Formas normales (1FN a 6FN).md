Niveles acumulativos de [[Normalización]]: para estar en 3FN, antes hay que cumplir 1FN y 2FN.

#### 1FN — Atomicidad
No hay grupos repetitivos: cada atributo tiene un único valor atómico (no multivaluado).
- ❌ Incorrecto: `Alumno(DNI, Nombre, Telefonos="600111222, 600333444")`
- ✅ Correcto: separar en otra tabla `Telefono(DNI, Numero)`.

#### 2FN — Sin dependencias parciales
Está en 1FN y todo atributo no principal depende completamente de la clave (no de una parte de ella).

> [!tip] Truco del temario
> Si la clave es simple (un solo atributo), la 2FN se cumple automáticamente — el problema solo aparece con claves compuestas.

> [!example]
> R(A, B, C, D, E), clave = A+B. A+B → C ✅ correcto (depende de toda la clave). A → D ❌ incorrecto (D depende solo de una parte de la clave). Solución: R1(A, B, C, E) + R2(A, D).

#### 3FN — Sin dependencias transitivas
Está en 2FN y ningún atributo no principal depende de otro atributo no principal (solo de la clave). Dependencia transitiva: {A,B} → C y C → D.

> [!example]
> R(A, B, C, D, E), clave = A+B. A+B → C ✅. C → D ❌ (transitiva). Solución: R1(A, B, C, E) + R2(C, D).

#### FNBC — Boyce-Codd (afinamiento de la 3FN)
Cubre un caso que la 3FN deja pasar: cuando un atributo no-clave determina parte de la clave (caso raro, con claves candidatas solapadas). Regla: se cumple si y solo si todo determinante es clave candidata.

> [!important] FNBC vs 3FN
> No son la misma regla: la 3FN solo exige que los atributos no-clave no dependan de otros no-clave; la FNBC exige además que *todo* determinante (incluso si determina parte de la clave) sea clave candidata. Toda FNBC es 3FN, pero no toda 3FN es FNBC.

> [!example]
> R(A, B, C), donde C determina A, pero C no es clave candidata (y A forma parte de la clave). Hay que eliminar esa dependencia: R1(C, A) + resto.

#### 4FN — Sin dependencias multivaluadas no triviales
Se cumple si toda [[Dependencia multivaluada (DMV)|DMV]] no trivial está implicada por una clave candidata.

> [!example] Ejemplo clásico — Imparticion(Asignatura, Profesor, Curso)
>
> | Asignatura | Profesor | Curso |
> |---|---|---|
> | Calculo | Ana | Primero |
> | Calculo | Ana | Segundo |
> | Calculo | Luis | Primero |
> | Calculo | Luis | Segundo |
>
> Cálculo lo dan Ana y Luis, y se imparte en Primero y Segundo — pero profesor y curso no están relacionados entre sí, solo cada uno con la asignatura. Al mezclarlos en una tabla se genera un producto cartesiano artificial. Solución: separar en R1(Asignatura, Profesor) y R2(Asignatura, Curso).

#### 5FN — Forma normal de proyección-unión
Se cumple si toda dependencia de combinación (join dependency) está implicada por claves candidatas. No se puede deducir solo de la estructura de la tabla: hay que analizar los datos reales y su semántica. Caso raro, poco frecuente en la práctica/examen.

#### 6FN
Relaciones con PK + como mucho un atributo más. Descomposición extrema, tablas muy pequeñas. Uso muy específico (ej. bases de datos temporales/históricas).

### Cuadro resumen

| FN | Elimina | Problema que ataca |
|---|---|---|
| 1FN | Valores multivaluados | Atomicidad |
| 2FN | Dependencias parciales | Solo aplica con clave compuesta |
| 3FN | Dependencias transitivas | No-clave → No-clave |
| FNBC | Determinantes que no son clave candidata | Caso especial no cubierto por 3FN |
| 4FN | Dependencias multivaluadas no triviales | Mezcla de hechos independientes |
| 5FN | Dependencias de combinación (join) | Depende de datos/semántica |
| 6FN | — | Relaciones mínimas (PK + 1 atributo) |

[[Dependencia funcional]]
[[B3 - T1.2 DISENO BBDD]]
