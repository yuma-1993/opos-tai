---
tags:
  - bloque3
  - tema3
  - sql
  - ddl
  - dml
  - dcl
  - tcl
  - transacciones
  - joins
  - triggers
  - procedimientos-almacenados
  - bases-de-datos
bloque: 3
tema: 3
titulo: "SQL: sublenguajes DDL/DML/DCL/TCL, transacciones, JOINs, triggers y procedimientos almacenados"
estado: por-repasar
---

# Tema 3 · Bloque 3 — SQL

> [!abstract] De qué va este tema
> SQL es el lenguaje declarativo (con extensión procedural) para trabajar con bases de datos relacionales: se divide en cuatro sublenguajes (DDL, DML, DCL, TCL) según qué tipo de operación realizan. El tema cubre esos sublenguajes, el control de transacciones y niveles de aislamiento, las consultas (SELECT, subconsultas, JOINs, operadores de conjuntos), y los objetos programables del SGBD (triggers, procedimientos almacenados, cursores).

---

## Parte I — Qué es SQL y su ecosistema

### 1. Definición

**SQL**: lenguaje de 4ª generación (4GL) declarativo, con una extensión procedural para escribir lógica de negocio (procedimientos almacenados). Esa extensión se llama **SQL/PSM** (SQL / Persistent Stored Modules), y cada fabricante la implementa con su propio dialecto: **PL/SQL** (Oracle) y **Transact-SQL** (SQL Server).

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Un lenguaje **declarativo** describe *qué* resultado se quiere, no *cómo* obtenerlo paso a paso (a diferencia de un lenguaje imperativo/procedural como C o Java, donde se detalla cada paso). SQL es declarativo en su núcleo de consulta, pero como hay lógica que no se puede expresar en una sola sentencia declarativa (bucles, condicionales, variables), se añadió una capa procedural (PL/SQL, T-SQL) para cubrir ese hueco.

### 2. Estándares

| Estándar | Novedad principal |
|---|---|
| ANSI:86 | Primer estándar |
| ANSI-92 | Revisión grande. Es la más conocida |
| ISO 9075 SQL:1999 | SQL 3. Introduce triggers |
| ISO 9075 SQL:2003 | Introduce el objeto SEQUENCE |
| ISO 9075 SQL:2006 | XML nativo |
| ISO 9075 SQL:2008 | Sentencia TRUNCATE |
| ISO 9075 SQL:2016 | Compatibilidad JSON |

### 3. Productos (SGBD)

Oracle, Microsoft SQL Server, MySQL/MariaDB, Informix, IBM Db2, PostgreSQL, MaxDB.

### 4. SQLite: un caso especial (RDBMS no cliente/servidor)

- No es un gestor de BD, sino un **formato de fichero**.
- Es **local**, no se usa por red.
- Muy usado en Android.
- Es una **librería** (compatible ACID): permite realizar transacciones.

### 5. ACID y transacción

> [!important] ACID
> **A**tomicidad · **C**onsistencia · **A**islamiento · **D**urabilidad.

**Transacción**: conjunto de sentencias SQL que se tienen que hacer todas o ninguna. Procesos atómicos.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Qué falla si se pierde cada propiedad: sin **Atomicidad**, una transacción puede quedar a medias (ej. se descuenta saldo de una cuenta pero no se abona en la otra). Sin **Aislamiento**, dos transacciones concurrentes pueden ver datos intermedios inconsistentes entre sí — de ahí las lecturas sucias/no repetibles/fantasma que se explican más abajo, en los niveles de aislamiento (Parte III).

---

## Parte II — Los sublenguajes de SQL

### 1. Vista general

| Sublenguaje | Nombre completo | Para qué |
|---|---|---|
| DDL | Lenguaje de Definición de Datos | Creación / borrado / modificación de **objetos** |
| DML | Lenguaje de Manipulación de Datos | Consulta / borrado / modificación / inserción de **datos** |
| DCL | Lenguaje de Control de Datos | Control del **acceso** a los datos |
| TCL | Lenguaje de Control de Transacciones | Control de transacciones (es una parte del DCL) |

La [[Reglas de Codd|Regla 5 de Codd]] ("Sublenguaje de datos completo") exige justamente que exista un lenguaje único que cubra definición, manipulación y consulta — SQL es el ejemplo que la propia regla cita.

> [!important]
> El PDF clasifica explícitamente **TCL como una parte del DCL**, no como un sublenguaje totalmente independiente — es una distinción que varía según la fuente y puede ser objeto de pregunta trampa.

### 2. DDL — Lenguaje de Definición de Datos

| Verbo | Objetos (ejemplos del PDF) |
|---|---|
| CREATE | TABLE / INDEX / VIEW / PROCEDURE |
| DROP | SEQUENCE / FUNCTION / TYPE / TRIGGER |
| ALTER | DOMAIN / SCHEMA / ROLE |

> [!note]
> En la práctica los tres verbos (CREATE/DROP/ALTER) se pueden aplicar a cualquier tipo de objeto; el PDF simplemente reparte los ejemplos entre los tres para no repetir.

Descripción de los objetos:

| Objeto | Descripción |
|---|---|
| Table | Los objetos (tablas) en sí |
| Index | Estructura de datos que sirve para agilizar búsquedas mediante el uso de **[[Árbol B, B+ y B-estrella|árboles B]]** |
| Domain | Dominio de valores |
| Procedure y Function | SQL/PSM |
| Triggers | Procedimientos que se ejecutan a partir de un evento |
| Schema | Forma de agrupar tablas |
| Role | Para dar de alta permisos y funcionalidades a usuarios |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Un índice tipo **árbol B (B-tree)** organiza las claves en un árbol balanceado con varios hijos por nodo, lo que permite localizar un registro en muy pocos saltos (orden logarítmico) incluso con millones de filas, en vez de recorrerlas todas una a una (full scan).

**CONSTRAINTS** (restricciones):

| Constraint | Qué hace |
|---|---|
| PRIMARY KEY | Identifica de forma única cada fila (es una [[Claves (superclave, candidata, primaria, alternativa)|clave candidata]] elegida como principal) |
| FOREIGN KEY | Referencia la PK de otra tabla (aplica la [[Restricciones de integridad (relacional)|integridad referencial]]) |
| CHECK | Restringe valores según una condición (ej: `campo > 0`) |
| UNIQUE | Garantiza valores únicos; a diferencia de PK, **admite un único NULL** |

> [!example] CREATE TABLE completo
> ```sql
> CREATE TABLE distribuidores (
>   dist_id CHAR(4) NOT NULL,
>   dist_nombre VARCHAR(40),
>   sales_rep INT,
>   zip CHAR(5),
>   CONSTRAINT pk_dist_id PRIMARY KEY (dist_id),
>   CONSTRAINT fk_emp_id
>     FOREIGN KEY (sales_rep)              -- campos
>     REFERENCES empleados (empid),        -- tabla y campos
>   CONSTRAINT uniq_zip UNIQUE (zip),      -- clave candidata
>   CONSTRAINT chk_zip CHECK (zip LIKE '[0-9][0-9][0-9][0-9][0-9]')
> );
> ```

**ALTER TABLE**:

```sql
ALTER TABLE nom_tabla ADD COLUMN nom_col <tipo> <atributos>
ALTER TABLE nom_tabla ALTER COLUMN nom_col SET DEFAULT valor
ALTER TABLE nom_tabla ALTER COLUMN nom_col SET NOT NULL
ALTER TABLE nom_tabla ALTER COLUMN nom_col SET DATA TYPE <tipo>
ALTER TABLE nom_tabla DROP COLUMN nom_col
ALTER TABLE nom_tabla ADD <restriccion>
```

### 3. DML — Lenguaje de Manipulación de Datos

Sentencias: **SELECT · UPDATE · INSERT · DELETE · MERGE** (mezcla registros de una tabla sobre otra).

> [!note]
> El propio PDF apunta que **TRUNCATE podría considerarse DML** según el fabricante (aunque formalmente esté definida en DDL — ver Parte V).

### 4. DCL — Lenguaje de Control de Datos

- **GRANT**: da permisos.
- **REVOKE**: quita permisos.

> [!note]
> El PDF señala que **`CALL procedure`** algunos fabricantes lo consideran DML, no DCL — clasificación ambigua entre fuentes.

```sql
GRANT <privilegios> ON <objeto> TO <grantee> [WITH GRANT OPTION]
```
- `<privilegios>`: SELECT, UPDATE, INSERT, DELETE, ALL, USAGE (ej: para secuencias) + lista de columnas; EXECUTE (para procedimientos).
- `<objeto>`: tabla u otro objeto de BD.
- `<grantee>`: usuarios o roles.
- `WITH GRANT OPTION`: permite que el grantee delegue ese permiso a otros.

```sql
REVOKE <privilegios> ON <objeto> FROM <grantee>
```

### 5. TCL — Lenguaje de Control de Transacciones

| Sentencia | Qué hace |
|---|---|
| COMMIT | Confirma los cambios de la transacción |
| ROLLBACK | Deshace los cambios de la transacción. Previenen inconsistencias |
| SAVEPOINT | Crea un punto de salvaguarda; un ROLLBACK puede deshacer solo hasta ese punto |
| RELEASE SAVEPOINT | Quita el savepoint |
| SET TRANSACTION | Configura la transacción |
| START TRANSACTION | Empieza la transacción |
| END TRANSACTION | Finaliza la transacción |

---

## Parte III — Transacciones en profundidad

### 1. Locales vs distribuidas

Las transacciones pueden ser **locales** (1 solo SGBD) o **distribuidas** (two-phase commit, entre varios sistemas).

- **Monitor Transaccional**: CICS y Tuxedo.
- En **JEE** el monitor transaccional está dentro del servidor de aplicaciones (JBoss, WebLogic, WebSphere). La API de Java para hablar con el monitor transaccional es **JTA**.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El **two-phase commit** (commit en dos fases) es el protocolo típico para coordinar una transacción distribuida: en la fase de *preparación* el coordinador pregunta a todos los participantes si pueden confirmar su parte; solo si todos responden que sí, el coordinador ordena el *commit* definitivo a todos (si alguno falla, se ordena rollback a todos). Así se garantiza atomicidad aunque la transacción abarque varios sistemas.

### 2. Niveles de aislamiento y bloqueos (SET TRANSACTION)

| Isolation Level | Lectura sucia | Lectura no repetible | Lectura fantasma |
|---|---|---|---|
| READ UNCOMMITTED | SI | SI | SI |
| READ COMMITTED | NO | SI | SI |
| REPEATABLE READ | NO | NO | SI |
| SERIALIZABLE | NO | NO | NO |

- **READ UNCOMMITTED**: leo datos no consolidados (no confirmados).
- **READ COMMITTED**: es el método usado por defecto.
- **REPEATABLE READ**: si tx1 consulta y tx2 cambia y hace commit, tx1 no tendrá los nuevos datos de tx2 hasta que termine su propia transacción — desde que tx1 inicia, trabaja siempre con los mismos datos.
- **SERIALIZABLE**: pone las transacciones en fila. 0% problemas de concurrencia. ↓ Rendimiento, ↑ Seguridad.

Definiciones:
- **Lectura sucia**: leer datos aún no confirmados (de otra transacción que podría hacer rollback).
- **Lectura no repetible**: si tx1 es muy larga, tx2 puede alterar los datos que usaba tx1; si tx1 vuelve a leer, los datos habrán cambiado.
- **Lectura fantasma**: no se bloquean rangos/grupos de datos, solo filas concretas. Tx1 puede recuperar un rango 1-5 y tx2 insertar un registro con valor 3 — tx1 no vería ese valor 3 al releer.

> [!important]
> Se pueden bloquear filas o columnas. **El bloqueo de tabla completa solo se consigue con SERIALIZABLE.**

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Muchos SGBD modernos (PostgreSQL, MySQL/InnoDB) no implementan estos niveles solo con bloqueos, sino con **MVCC** (Multi-Version Concurrency Control): cada transacción ve una "foto" consistente de los datos en un instante dado, sin necesidad de bloquear tanto. Esto no quita que, a mayor nivel de aislamiento, más mecanismos de control hacen falta y menor es el rendimiento en concurrencia — el trade-off rendimiento/seguridad se mantiene igual.

---

## Parte IV — Consultas SQL (DML en detalle)

### 1. SELECT

```sql
SELECT [ALL | DISTINCT] item1 AS alias, ...
FROM tabla | vista AS alias, ...
[<tipo_join> JOIN <tabla> ON <condicion_join>]
WHERE <condicion_busqueda> [AND | OR | NOT <condicion_busqueda>] ...
GROUP BY <campo(s)>
HAVING <condicion_sobre_los_grupos>
ORDER BY campo1 [ASC | DESC], ...
```

- `item1` puede ser: columna, cálculo, subconsulta, o función de agregado/escalar (SUM, MAX/MIN, AVG...).

> [!important] COUNT(*) vs COUNT(columna)
> **COUNT(\*)**: sí cuenta los nulos. **COUNT(columna)**: no cuenta los nulos de esa columna.

> [!tip]
> `GROUP BY` y `HAVING` siempre van de la mano: `HAVING` filtra sobre los grupos que ya ha formado `GROUP BY` (a diferencia de `WHERE`, que filtra filas antes de agrupar).

### 2. INSERT / UPDATE / DELETE

```sql
INSERT INTO <tabla> (col1, col2, ...) VALUES ('...', '...', ...)
INSERT INTO <tabla> (col1, col2, ...) SELECT ...

UPDATE <tabla> SET col1 = val1, col2 = val2 WHERE <condicion>
-- val puede ser: DEFAULT / NULL / resultado de una Query

DELETE FROM <tabla> WHERE <condicion>
```

### 3. Subconsultas (dentro del WHERE)

```sql
SELECT ... FROM tabla1 WHERE EXISTS (subquery)
```
→ Subconsulta **correlacionada**: hace referencia a columnas de la consulta externa/principal. Devuelve `true` si la subquery devuelve alguna fila.

```sql
WHERE col1 [NOT] IN (SELECT col2 FROM ...)
```
→ `IN` es el operador de conjuntos.

```sql
WHERE col1 <operador> ANY / SOME (SELECT col2 FROM ...)
WHERE col1 <operador> ALL (SELECT col2 FROM ...)
```
→ `<operador>`: `=`, `>=`, `<`... y también funciones de agregado.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Ejemplo de subconsulta correlacionada usando las tablas del apartado de JOINs (más abajo): `SELECT nombre FROM Autor a WHERE EXISTS (SELECT 1 FROM Libro l WHERE l.id_autor = a.id)` → devuelve los autores que tienen al menos un libro. Es "correlacionada" porque la subconsulta interna (`l.id_autor = a.id`) depende de la fila actual de la consulta externa (`a`), así que se re-evalúa por cada fila.

### 4. JOINs

```
... <tipo_join> JOIN <tabla> ON <condiciones>
```

Ejemplo usado como referencia (Autor 1:N Libro):

**Autor**

| id | nombre |
|---|---|
| 1 | dani |
| 2 | pepe |
| 3 | luis |

**Libro**

| id | titulo | id_autor |
|---|---|---|
| 10 | xx | 1 |
| 20 | yy | 2 |

| Tipo de JOIN | Qué devuelve | Filas en el ejemplo |
|---|---|---|
| CROSS JOIN | = `FROM tabla1, tabla2`. Producto cartesiano de las tablas | 6 |
| [INNER] JOIN | Solo las filas coincidentes según la condición | 2 |
| LEFT [OUTER] JOIN | Todas las filas de la tabla izquierda; los campos de la derecha valen NULL si no cumplen la condición. El nº de filas resultante es el nº de filas de la tabla izquierda | 3 |
| RIGHT [OUTER] JOIN | Igual que LEFT pero manda la tabla derecha | 2 |
| FULL [OUTER] JOIN | Manda las dos tablas y rellena con NULL donde una tabla no cumple la condición | 3 |
| NATURAL JOIN | Cuando los campos de ambas tablas tienen el mismo nombre, el propio gestor hace el match automáticamente | — |

> [!example] Fórmula del FULL JOIN
> `reg FULL = reg INNER + (reg LEFT − reg INNER) + (reg RIGHT − reg INNER)` → en el ejemplo: `2 + (3−2) + (2−2) = 2 + 1 + 0 = 3`.

> [!tip]
> σ/Π de las [[Operaciones básicas del álgebra relacional|operaciones básicas del álgebra relacional]] (Tema 1.2) tienen su equivalente aquí: el JOIN de SQL se traduce internamente a un producto cartesiano (×) filtrado (σ) — es literalmente la operación de "join" del [[Álgebra relacional vs Cálculo relacional|álgebra relacional]].

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Los JOIN son la razón de ser de un modelo normalizado: al separar los datos en varias tablas para evitar redundancia ([[Normalización]]), es necesario recomponerlos en tiempo de consulta uniendo tablas por sus claves foráneas — es el coste que se paga a cambio de eliminar la redundancia.

### 5. Operadores de conjuntos (UNION / INTERSECT / EXCEPT)

```sql
<select lista_cols>
UNION [ALL]
<select lista_cols>
```

- Requisito: las queries deben ser **compatibles** — mismo nº de columnas y mismo tipo.
- `UNION ALL` **no elimina** filas duplicadas (a diferencia de `UNION` a secas).
- `EXCEPT` e `INTERSECT` son también operadores de conjuntos, con el mismo requisito de compatibilidad.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> `UNION ALL` suele ser más rápido que `UNION` precisamente porque no tiene que hacer el paso extra de comprobar y eliminar duplicados.

### 6. MERGE

Fusiona una tabla origen (**source**) sobre una tabla destino (**target**) en base a una condición de búsqueda:

- Si un registro existe en las dos tablas → se **actualiza** el destino.
- Si un registro existe solo en el origen → se **inserta** en el destino.

```sql
MERGE INTO <nom_tabla_target>
USING <nom_tab_source>
ON <condicion_busqueda>
WHEN MATCHED
  THEN UPDATE SET col1 = ...
WHEN NOT MATCHED
  THEN INSERT (col1, ...) VALUES (..., ...)
```

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Esta operación es conocida coloquialmente como **UPSERT** (UPDATE + INSERT) en muchos entornos, aunque MERGE es la sentencia estándar SQL para esa lógica.

---

## Parte V — TRUNCATE en profundidad

> [!important] TRUNCATE — puntos clave del PDF
> - No se borra la tabla para después crearla (según el último examen de GSI oficial referenciado en el PDF).
> - Hace un borrado rápido, marcando zonas de memoria de golpe (extents = data pages).
> - **Se salta los controles** que sí respeta la sentencia DELETE.
> - Deja intactos nombres de columnas, índices y estructuras — la estructura de la tabla persiste.
> - En **Oracle** hace COMMIT automáticamente, por lo que **no se puede deshacer**.
> - No se quedan registros en el fichero de log.
> - **No usa WHERE** (borra todas las filas siempre).
> - En **MySQL** necesitas tener privilegio de **DROP**, porque internamente sí borra la tabla y la vuelve a crear.

> [!note]
> El propio PDF presenta a la vez "no se borra la tabla para crearla de nuevo" (afirmación general) y "en MySQL sí borra y crea de nuevo" (comportamiento específico de ese SGBD) — se han transcrito ambas afirmaciones literalmente tal como aparecen en la fuente, sin resolver la aparente tensión entre ellas.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> En muchos SGBD (ej. MySQL, SQL Server), TRUNCATE también reinicia los contadores de las columnas autoincrementales/IDENTITY a su valor inicial, algo que DELETE no hace.

---

## Parte VI — Triggers (disparadores)

**Triggers**: lógica de negocio con 1 o N sentencias que se ejecuta a partir de un evento sobre determinados objetos.

Pseudotablas / pseudorregistros según el momento del cambio:

| Momento | Oracle | MS SQL Server |
|---|---|---|
| Antes del cambio | Old | Deleted |
| Después del cambio | New | Inserted |

Restricciones:
- No aceptan parámetros.
- No pueden usar START TRANSACTION / COMMIT / ROLLBACK — no se puede meter una transacción dentro de un trigger.

Tipos: de fila o de sentencia. ¿Cuándo se disparan?

- **AFTER** o **BEFORE** + **INSTEAD OF** → combinados con **INSERT / UPDATE / DELETE**.

> [!example]
> ```sql
> CREATE TRIGGER auditar_phone_book
>   AFTER UPDATE ON phone_book FOR EACH ROW
> BEGIN
>   -- FOR EACH STATEMENT: se ejecutaría una vez por sentencia, no por registro
>   INSERT INTO phone_book_auditoria (col1, ...)
>   VALUES (auditoria_seq.nextval, 'UPDATE', OLD.col1, OLD.col2, NEW.col1, NEW.col2, SYSDATE);
> END;
> ```

> [!important]
> **INSTEAD OF** anula la sentencia disparadora y solo tiene efecto el cuerpo del trigger. Ejemplo de uso: seguridad, convertir un DELETE en un INSERT en una tabla de auditoría.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Usos típicos de los triggers, más allá de la auditoría del ejemplo: aplicar reglas de negocio complejas que un simple CHECK no puede expresar, mantener datos derivados/agregados sincronizados automáticamente, o replicar cambios hacia otra tabla/sistema.

---

## Parte VII — Procedimientos almacenados y cursores

**PROCEDURES**: son scripts de base de datos. Lógica de negocio que se ejecuta (`CALL`) en el ámbito del SGBD. Aceptan parámetros de entrada, salida y entrada/salida, pero **a diferencia de las funciones, los procedimientos no retornan valor**.

```sql
CREATE PROCEDURE <nom_proc> (IN | OUT | INOUT <nom_param> <tipo>, ...)
LANGUAGE ________
AS $$
BEGIN
  -- SELECT/CURSOR ... FOR UPDATE
  -- IF / CASE
  ...
  COMMIT;
END;
$$
```

> [!example] Cursores
> Un **cursor** es un objeto que permite recorrer el resultado de una sentencia. Un `DataReader` (.NET) y un `ResultSet` (JDBC), por debajo, son cursores.
> ```sql
> var_reg cursor_tabla%ROWTYPE; -- define la variable con la estructura del cursor cursor_tabla
> ...
> FETCH cursor_tabla INTO var_reg;
> ...
> ```

Si se llena el registro (log) de transacciones, la sentencia que se está ejecutando falla y se deshace la operación.

Cuando se hacen operaciones de inserción, actualización o borrado, se pueden hacer por bloques de X registros, con `LIMIT`, `ROWID`, etc.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Los cursores procesan fila a fila, lo contrario del enfoque "por conjuntos" (set-based) que es natural en SQL — por eso suelen ser más lentos que una sentencia SQL equivalente que opere sobre todo el conjunto de filas a la vez. Se usan cuando la lógica realmente necesita tratar cada fila de forma distinta (no siempre es posible expresarlo en una sola sentencia declarativa).

---

## Parte VIII — Otras sentencias útiles

```sql
EXPLAIN PLAN
```
→ Sentencia que muestra el **plan de ejecución** que va a seguir el SGBD, para sentencias SELECT, INSERT, UPDATE y DELETE. Es la secuencia de operaciones que realiza el SGBD.

```sql
CREATE INDEX <nom_indice> ON <nom_tabla> (<nom_campo1>, <nom_campo2>);

CREATE VIEW <nom_vista> AS <sentencia_select> [WITH CHECK OPTION]
-- WITH CHECK OPTION: no permite insertar ni actualizar registros si no cumplen la sentencia de la vista

CALL <nom_procedure> [(<lista_params>)]   -- separador de parámetros: ","
EXEC <nom_procedure> <lista_params>        -- separador de parámetros: ","
```

`CREATE INDEX` es lo que materializa físicamente el mecanismo de [[Tipos de acceso a ficheros (secuencial, directo, indexado, ISAM)|acceso indexado o ISAM]] descrito en Bloque 2, normalmente implementado con el árbol B/B+ mencionado en la Parte II.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> La sintaxis de `EXPLAIN PLAN` varía por SGBD: MySQL y PostgreSQL usan `EXPLAIN <sentencia>`; Oracle usa `EXPLAIN PLAN FOR <sentencia>` y luego consulta el resultado con `DBMS_XPLAN`.
>
> Ejemplo de `WITH CHECK OPTION`: si `CREATE VIEW empleados_madrid AS SELECT * FROM empleados WHERE ciudad = 'Madrid' WITH CHECK OPTION`, un `INSERT` a través de esa vista con `ciudad = 'Barcelona'` sería rechazado, porque no cumpliría la condición `WHERE` que define la vista.

---

## 🔑 Resumen ultra-rápido (para repaso)

- SQL: 4GL declarativo + extensión procedural (SQL/PSM = PL/SQL en Oracle, Transact-SQL en SQL Server).
- Hitos de estándares: ANSI-92 (el más conocido), SQL:1999 (triggers), SQL:2003 (SEQUENCE), SQL:2006 (XML), SQL:2008 (TRUNCATE), SQL:2016 (JSON).
- SQLite: no es un SGBD, es un formato de fichero/librería local, ACID, muy usado en Android.
- ACID = Atomicidad, Consistencia, Aislamiento, Durabilidad. Transacción = todo o nada.
- 4 sublenguajes: DDL (objetos), DML (datos), DCL (accesos), TCL (transacciones — parte del DCL según esta fuente).
- DDL: CREATE/DROP/ALTER sobre TABLE, INDEX (árbol B), DOMAIN, PROCEDURE/FUNCTION, TRIGGER, SCHEMA, ROLE. Constraints: PK, FK, CHECK, UNIQUE (admite un NULL).
- DML: SELECT, UPDATE, INSERT, DELETE, MERGE. TRUNCATE podría considerarse DML según fabricante.
- DCL: GRANT/REVOKE (privilegios, objeto, grantee, WITH GRANT OPTION = delegación).
- TCL: COMMIT/ROLLBACK, SAVEPOINT/RELEASE SAVEPOINT, SET/START/END TRANSACTION.
- Transacciones locales (1 SGBD) vs distribuidas (two-phase commit). Monitor transaccional: CICS, Tuxedo; en JEE, dentro del servidor de apps, API JTA.
- Niveles de aislamiento (de menos a más seguro): READ UNCOMMITTED (todo falla) → READ COMMITTED (por defecto) → REPEATABLE READ → SERIALIZABLE (0% concurrencia, único que bloquea tabla completa).
- Lectura sucia (no confirmado) / no repetible (cambia entre 2 lecturas) / fantasma (aparecen filas nuevas en un rango).
- SELECT: FROM/JOIN → WHERE → GROUP BY → HAVING → ORDER BY. COUNT(*) cuenta nulos, COUNT(columna) no.
- Subconsultas: EXISTS (correlacionada), IN (conjuntos), ANY/SOME/ALL + comparador.
- JOINs: CROSS (cartesiano) > LEFT/RIGHT (todas de un lado + NULL) > FULL (todas + NULL de ambos) > INNER (solo coincidencias). FULL = INNER + (LEFT−INNER) + (RIGHT−INNER). NATURAL: empareja por nombre de columna automáticamente.
- UNION requiere queries compatibles (mismo nº columnas y tipo); UNION ALL no elimina duplicados. INTERSECT/EXCEPT también son operadores de conjuntos.
- MERGE: fusiona source sobre target — MATCHED → UPDATE, NOT MATCHED → INSERT.
- TRUNCATE: rápido, sin WHERE, se salta controles, mantiene estructura, sin log, autocommit en Oracle (irreversible); en MySQL necesita privilegio DROP.
- Triggers: BEFORE/AFTER/INSTEAD OF + INSERT/UPDATE/DELETE, FOR EACH ROW/STATEMENT. No aceptan parámetros ni pueden gestionar transacciones. INSTEAD OF anula la sentencia original.
- Procedimientos: no retornan valor (a diferencia de funciones), parámetros IN/OUT/INOUT, se invocan con CALL. Cursores recorren resultados fila a fila (DataReader/ResultSet por debajo).
- EXPLAIN PLAN: plan de ejecución del SGBD. CREATE VIEW ... WITH CHECK OPTION: bloquea inserts/updates que no cumplan el filtro de la vista.
</content>
