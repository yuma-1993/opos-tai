**MapReduce** es un algoritmo/modelo de **computación distribuida**. El nombre significa "reducción de mapas": mapea muchos nodos al estar la información distribuida, y reduce/trocea la información. Se parte de muchos datos a los que se les hace un mapeo (**map**) y sobre ese mapeo se realiza un cálculo de agregación (**reduce**). En cada nodo hay una pieza `MAP_REDUCE` encargada de esto.

**Ejemplo: totalizar pedidos por cliente**
```
db.orders.mapReduce(
  map:    function() { emit(this.cust_id, this.amount); },
  reduce: function(key, values) { return Array.sum(values); },
  query:  { status: "A" },
  out:    "order_totals"
)
```
Colección `orders` (documentos de entrada, filtrados por `status: "A"`):
- `{cust_id:"A123", amount:500, status:"A"}`
- `{cust_id:"A123", amount:250, status:"A"}`
- `{cust_id:"B212", amount:200, status:"A"}`
- `{cust_id:"A123", amount:300, status:"D"}` ← excluido por la query (`status` no es `"A"`)

**Map**: emite pares `(cust_id, amount)` → se agrupan por clave: `{"A123":[500,250]}`, `{"B212":[200]}`.
**Reduce**: suma los valores de cada grupo → colección `order_totals`: `{_id:"A123", value:750}`, `{_id:"B212", value:200}`.

**Ampliación (conocimiento general, no viene del tema):** MapReduce (el motor clásico de **[[Hadoop]]**) escribe resultados intermedios a disco entre cada fase, lo que lo hace robusto pero relativamente lento para trabajos iterativos. **Spark** (que aparece como una de las capas de consulta, "Spark SQL") resuelve esto manteniendo los datos en memoria entre operaciones cuando es posible, por lo que en muchos casos de uso ha sustituido a MapReduce como motor de cómputo, aunque siga apoyándose en HDFS como sistema de ficheros.

[[MongoDB]]
[[Hadoop]]
[[B2 - T5 NOSQL Y BIG DATA]]
