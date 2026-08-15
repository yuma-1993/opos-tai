Modelo de 3 niveles para lograr la independencia entre lo físico y lo lógico en una base de datos ya relacional en funcionamiento:

```
Usuarios
   ↓
NIVEL EXTERNO     → Vistas (lo que ve cada usuario/aplicación)
   ↓
NIVEL CONCEPTUAL  → Tablas/relaciones (el esquema lógico completo de la BD)
   ↓
NIVEL INTERNO     → Almacenamiento físico, índices, estructuras de acceso
```

- **Independencia física** (interno ↔ conceptual): cambiar cómo se almacenan los datos no afecta al esquema conceptual.
- **Independencia lógica** (conceptual ↔ externo): cambiar el esquema conceptual, si se hace con cuidado, no debería romper las vistas externas.

> [!important]
> Relación directa con las [[Reglas de Codd]] 8 y 9: esta arquitectura es el mecanismo que las hace posibles.

> [!note] No confundir con los niveles Conceptual/Lógico/Físico del diseño
> ANSI/SPARC no es lo mismo que los [[Niveles de modelado (Conceptual, Lógico, Físico)]] del Tema 1.1: aquellos describen el **proceso de diseño** desde el análisis (E/R) hasta la implementación en un SGBD concreto; ANSI/SPARC describe los **niveles de una base de datos relacional ya construida y en funcionamiento** (vistas de usuario, esquema lógico, almacenamiento físico). Son ideas relacionadas pero no intercambiables.

[[B3 - T1.2 DISENO BBDD]]
