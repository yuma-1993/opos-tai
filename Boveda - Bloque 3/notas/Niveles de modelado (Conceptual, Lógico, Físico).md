Antes de construir una base de datos real se pasa por tres niveles de abstracción, cada uno más concreto que el anterior, y cada paso es una **traducción con reglas fijas**, no una reinvención: `Modelo Conceptual` → (reglas de transformación) → `Modelo Lógico` → `Modelo Físico`.

- **Conceptual**: qué datos existen y cómo se relacionan, independiente de toda tecnología. Aquí vive el [[Tipo de Entidad y Entidad|modelo Entidad-Relación]]. Ej: "un Autor escribe Libros".
- **Lógico**: cómo se estructuran esos datos según un paradigma concreto (relacional, jerárquico, red), pero todavía sin sintaxis de un SGBD concreto. Aquí es donde se aplica la normalización.
- **Físico**: cómo se implementa realmente en un SGBD concreto (tipos de datos exactos, índices, motor de almacenamiento). Ej: sentencias `CREATE TABLE` en un motor concreto.

El modelo conceptual no sabe ni le importa si al final será MySQL o PostgreSQL — esa decisión solo aparece en el nivel físico.

Este mismo esquema de tres niveles reaparece dos veces en el temario: primero como marco general del análisis de datos, y después, ya dentro del modelo relacional, como la **arquitectura ANSI/SPARC** (Externo/Conceptual/Interno), que es una idea relacionada pero no idéntica — ANSI/SPARC describe los niveles de una base de datos ya relacional en funcionamiento (vistas de usuario, esquema lógico, almacenamiento), no la transformación desde el análisis conceptual hasta la implementación física.

[[B3 - T1.1 ENTIDAD RELACION]]
[[B3 - T1.2 DISENO BBDD]]
