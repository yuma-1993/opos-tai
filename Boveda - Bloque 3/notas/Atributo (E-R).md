Una característica o propiedad de una [[Tipo de Entidad y Entidad|entidad]]. Ej: `Autor` tiene los atributos `nombre`, `fecha_nacimiento`, `nacionalidad`. Cada atributo toma sus valores de un [[Dominio]] (el conjunto de valores que tienen sentido para él).

Según la notación de Chen, un atributo se clasifica en varios tipos que no son excluyentes entre sí:

| Tipo | Qué es | Ejemplo |
|---|---|---|
| Simple | Un único valor atómico, no se puede dividir más | `nacionalidad` |
| Compuesto | Se descompone en sub-atributos con sentido propio | `Dirección` → `Calle`, `Número`, `Ciudad` |
| Multivaluado | Puede tomar varios valores a la vez para una misma entidad | `Teléfonos` de una persona |
| Derivado | Se calcula a partir de otro atributo, no se almacena de forma independiente | `Edad`, derivada de `fecha_nacimiento` |
| Clave (primaria) | Identifica de forma única cada ocurrencia de la entidad | `DNI` de una `Persona` |

> [!note]
> Esta clasificación de atributos es la misma que luego se traduce a la notación gráfica de Chen (ver [[Notación de Chen]]).

[[B3 - T1.1 ENTIDAD RELACION]]
