| Clave | Definición | Ejemplo |
|---|---|---|
| Superclave | Cualquier conjunto de atributos que identifica unívocamente una tupla (puede ser redundante/no mínima) | {DNI, ColorOjos}, {DNI, FecNac}, {DNI} |
| Clave candidata | Superclave mínima (no se puede quitar ningún atributo sin perder unicidad) | {DNI}, {NumSS} |
| Clave primaria (PK) | La clave candidata elegida para identificar la tabla | DNI |
| Clave alternativa | Claves candidatas no elegidas como PK | NumSS (si se eligió DNI) |

> [!important]
> Toda clave candidata es superclave, pero no toda superclave es candidata (solo las mínimas). La PK es siempre una clave candidata, nunca una superclave "sobrante".

La PK nunca puede tener valores nulos (ver [[Restricciones de integridad (relacional)]]), y es lo que garantiza la propiedad de "no repetición de tuplas" de toda [[Relación (modelo relacional) - esquema y propiedades|relación]].

[[B3 - T1.2 DISENO BBDD]]
