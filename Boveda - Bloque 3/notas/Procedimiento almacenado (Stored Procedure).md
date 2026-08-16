Un **procedimiento almacenado** (*stored procedure*) es un script de base de datos: lógica de negocio que se ejecuta (`CALL`) en el ámbito del propio SGBD, en vez de en la aplicación cliente. Acepta parámetros de entrada (`IN`), de salida (`OUT`) y de entrada/salida (`INOUT`), pero **a diferencia de una función, un procedimiento no retorna ningún valor**.

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

Dentro del cuerpo se pueden usar [[Cursor (SQL)|cursores]] para recorrer resultados, condicionales (`IF`/`CASE`) y las sentencias TCL propias de una transacción. Si se llena el registro (log) de transacciones mientras se ejecuta, la sentencia falla y la operación se deshace.

Se escribe en el dialecto procedural del fabricante — ver [[SQL-PSM, PL-SQL y Transact-SQL]].

[[B3 - T3 SQL]]
