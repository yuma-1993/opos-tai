Notación gráfica estándar del modelo Entidad-Relación de Peter Chen:

| Elemento | Notación |
|---|---|
| [[Entidad fuerte y entidad débil\|Entidad fuerte]] | Rectángulo simple (una sola línea) |
| [[Entidad fuerte y entidad débil\|Entidad débil]] | Rectángulo de doble línea |
| [[Atributo (E-R)\|Atributo]] (normal/simple) | Óvalo/elipse simple |
| Clave primaria | Óvalo con el nombre del atributo subrayado (línea continua) |
| Clave parcial (discriminante) | En entidad débil: óvalo con el nombre subrayado con línea discontinua |
| Atributo multivaluado | Óvalo de doble línea |
| Atributo derivado | Óvalo con línea discontinua (todo el contorno punteado) |
| Atributo compuesto | Óvalo "padre" conectado a varios óvalos "hijo" (sub-atributos), formando un pequeño árbol |

> [!important] Clave foránea
> En el modelo E-R de Chen **no existe** representación gráfica de clave foránea, porque las FK son un concepto del modelo lógico/relacional (Tema 1.2), no del conceptual. En Chen, esa dependencia se representa mediante la propia relación (el rombo) entre las entidades.

[[B3 - T1.1 ENTIDAD RELACION]]
