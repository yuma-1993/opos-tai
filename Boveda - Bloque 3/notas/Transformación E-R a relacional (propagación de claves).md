Reglas fijas para pasar del diagrama Entidad-Relación (Tema 1.1) al modelo relacional (tablas):

| Elemento E/R | Transformación |
|---|---|
| Entidad | Se convierte en una relación (tabla) |
| Relación 1:N | Propagación de clave: la PK del lado "1" viaja como FK al lado "N". Ej: `Autor(ID_Autor, Nombre)` → `Libro(ID_Libro, Titulo, ID_Autor)` |
| Relación M:N | No se puede propagar clave (generaría repetición). Se crea una relación nueva con clave compuesta por las PKs de ambas entidades. Ej: `Empleado(ID_Emp, Nombre)`, `Departamento(ID_Dep, Desc)` → `Trabajo(ID_Emp, ID_Dep)` |
| Relación N-aria (≥3 entidades) | Igual que M:N: nueva relación con clave compuesta por las PKs de todas las entidades participantes |

Clasificación por nº de entidades participantes: unaria (1) → binaria (2) → ternaria (3) → cuaternaria (4) → n-aria (≥5). Es la misma idea que el [[Grado de una relación (E-R)|grado E-R]], nombrada aquí desde el punto de vista de la transformación.

**[[Generalización y Especialización|Generalización/Especialización]] (herencia)**: tres estrategias posibles para pasar una jerarquía a tablas:

1. **Una sola relación** con un atributo discriminador que indica el subtipo — mezcla campos de todos los subtipos, muchos quedarán nulos según el tipo.
2. **Una relación por cada subtipo**, sin tabla para el supertipo — cada una repite los atributos comunes.
3. **Una relación por subtipo + una para el supertipo**, unidas por PK/FK — la más normalizada, evita redundancia.

La [[Entidad fuerte y entidad débil|entidad débil]] se transforma en una tabla cuya PK incluye la FK de la entidad fuerte de la que depende (ej. `Factura(ID_Factura)` → `LineaFactura(ID_Factura, NumLinea)`).

[[B3 - T1.2 DISENO BBDD]]
[[B3 - T1.1 ENTIDAD RELACION]]
