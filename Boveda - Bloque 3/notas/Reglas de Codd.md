Las 13 reglas (0 a 12) que definen qué debe cumplir un SGBD para considerarse verdaderamente relacional (en la práctica, ningún SGBD comercial las cumple al 100%).

| Regla | Nombre | Idea |
|---|---|---|
| 0 | Regla fundamental | El sistema debe gestionar la BD usando solo sus capacidades relacionales |
| 1 | Información | Todos los datos se representan como valores en tablas |
| 2 | Acceso garantizado | Todo dato es accesible sin ambigüedad vía (tabla, columna, PK) |
| 3 | Tratamiento de nulos | Los nulos se tratan de forma sistemática, distintos de 0/blanco |
| 4 | Catálogo dinámico en línea | El diccionario de datos (metadatos) se consulta igual que los datos normales (con el mismo lenguaje, ej. SQL) |
| 5 | Sublenguaje de datos completo | Existe un lenguaje único que cubre definición, manipulación y consulta (ej. SQL) |
| 6 | Actualización de vistas | Las vistas actualizables reflejan cambios de forma consistente |
| 7 | Inserción/actualización/borrado de alto nivel | Se opera sobre conjuntos de filas, no una a una |
| 8 | Independencia física | Cambios de almacenamiento (ej. renombrar un fichero) no afectan a apps/tablas |
| 9 | Independencia lógica | Cambios en el esquema lógico no rompen las aplicaciones (más difícil de lograr que la 8) |
| 10 | Independencia de integridad | Las reglas de integridad viven en el catálogo, no en el código de las apps |
| 11 | Independencia de distribución | Una BD distribuida se usa igual que si fuera local |
| 12 | No subversión | Un lenguaje de bajo nivel no puede saltarse las reglas de integridad definidas a alto nivel |

> [!tip] Truco memorístico
> Reglas 8, 9, 10, 11 son todas de "independencia de algo" — física, lógica, integridad, distribución.

Las reglas 8 y 9 (independencia física y lógica) son precisamente lo que materializa la [[Arquitectura ANSI-SPARC]].

[[B3 - T1.2 DISENO BBDD]]
[[B3 - T3 SQL]]
