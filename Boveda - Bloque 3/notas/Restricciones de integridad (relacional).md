Tres reglas que garantizan la coherencia de una base de datos relacional:

- **Valor nulo**: representa ausencia de valor (no es lo mismo que 0, cadena vacía o "desconocido con significado").
- **Integridad de entidad**: ningún atributo de la [[Claves (superclave, candidata, primaria, alternativa)|clave primaria]] puede ser nulo (si es compuesta, ninguno de sus componentes puede serlo).
- **Integridad referencial**: los valores de una clave foránea (FK) deben coincidir con un valor existente en la PK referenciada, **o ser nulos** — la FK sí admite nulo, a diferencia de la PK.

> [!tip]
> La asimetría es la clave para no confundirlas: la PK nunca puede ser nula (integridad de entidad); la FK sí puede serlo, siempre que cuando tenga valor, ese valor exista en la tabla referenciada (integridad referencial).

[[B3 - T1.2 DISENO BBDD]]
[[B3 - T3 SQL]]
