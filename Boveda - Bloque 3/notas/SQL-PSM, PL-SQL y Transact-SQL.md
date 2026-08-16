**SQL/PSM** (SQL / Persistent Stored Modules) es la extensión procedural de SQL: añade a la base declarativa del lenguaje (SELECT, INSERT...) las construcciones necesarias para escribir lógica de negocio completa — variables, bucles, condicionales — dentro de [[Procedimiento almacenado (Stored Procedure)|procedimientos almacenados]] y [[Trigger (disparador) SQL|triggers]].

Cada fabricante de SGBD implementa esta extensión con su propio dialecto, no existe una única sintaxis universal: **PL/SQL** es el dialecto de Oracle, y **Transact-SQL** (T-SQL) es el de Microsoft SQL Server.

**¿Por qué hace falta esto?** SQL es un lenguaje declarativo: describe *qué* resultado se quiere, no *cómo* obtenerlo paso a paso. Pero hay lógica que no se puede expresar en una sola sentencia declarativa (bucles, condicionales, variables) — SQL/PSM cubre ese hueco añadiendo una capa procedural encima del núcleo declarativo.

[[B3 - T3 SQL]]
