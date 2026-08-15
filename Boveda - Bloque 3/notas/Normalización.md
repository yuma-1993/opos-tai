Técnica que se aplica en el modelo lógico, después del [[Tipo de Entidad y Entidad|E/R]], para eliminar redundancia (información repetida innecesariamente) mediante el análisis de las [[Dependencia funcional|dependencias funcionales]] entre atributos.

**¿Por qué importa la redundancia?**
- Gasta espacio de almacenamiento.
- Genera anomalías de actualización: si un dato repetido cambia, hay que actualizarlo en varios sitios (riesgo de inconsistencia si se olvida alguno).

> [!important] Trade-off de normalizar
> ✅ Elimina redundancia e inconsistencias.
> ❌ Genera más tablas → hacen falta más JOINs en las consultas → peor rendimiento en lectura.
>
> Por eso a veces se desnormaliza deliberadamente (en sistemas de solo lectura tipo Data Warehouse, o cuando el rendimiento de consulta importa más que ahorrar espacio).

El resultado práctico de aplicar normalización son las [[Formas normales (1FN a 6FN)]], una escala acumulativa de niveles de "limpieza" del esquema.

[[B3 - T1.2 DISENO BBDD]]
