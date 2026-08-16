Una **vista** (`VIEW`) es una tabla virtual definida a partir de una consulta `SELECT`: no almacena datos propios, se calcula al consultarla.

```sql
CREATE VIEW <nom_vista> AS <sentencia_select> [WITH CHECK OPTION]
```

**`WITH CHECK OPTION`**: impide insertar o actualizar registros a través de la vista si el resultado no cumpliría el filtro (`WHERE`) que la define. Ejemplo: con `CREATE VIEW empleados_madrid AS SELECT * FROM empleados WHERE ciudad = 'Madrid' WITH CHECK OPTION`, un `INSERT` a través de esa vista con `ciudad = 'Barcelona'` sería rechazado.

[[B3 - T3 SQL]]
