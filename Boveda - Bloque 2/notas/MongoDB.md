**MongoDB** es una base de datos NoSQL orientada a **documentos**: maneja **colecciones de documentos** con formato **JSON**. No hace falta definir un esquema — todo es JSON, y pueden añadirse más o menos campos a un documento sin problema. Cada vez que se inserta un documento se le asocia un campo `id` generado automáticamente, y MongoDB indexa de forma nativa todo lo que se va introduciendo.

```
db.users.insertOne(
  {"name":"sue",
   "age":26,
   "status":"pending"})

db.users.find(
  {"age":{$gt:18}},              → filtro
  {"name":1, "address":1}        → proyección
).limit(5)                       → cursor

db.users.updateOne()
db.users.deleteMany()
```

`db` es el objeto base de datos, `users` es la colección, `find` es el método. Si se referencia una colección que no existe (ej. `db.facturas`), MongoDB la crea automáticamente.

En el **[[Teorema CAP (o de Brewer)|teorema CAP]]**, MongoDB es un sistema **CP**: el *Client Application Driver* hace lecturas y escrituras contra un nodo **Primary**, que replica a nodos **Secondary** (arquitectura de *replica set*, con un único punto de escritura consistente) — sacrifica disponibilidad total a cambio de consistencia.

MongoDB también incluye su propio **[[MapReduce]]** para agregaciones, por ejemplo para totalizar pedidos por cliente agrupando por `cust_id` y sumando `amount`.

**Ampliación (conocimiento general, no viene del tema):** que MongoDB "indexe de forma nativa todo lo que se va introduciendo" no es magia: por debajo, sus índices (igual que en la mayoría de motores relacionales) suelen implementarse con estructuras tipo **[[Árbol B, B+ y B-estrella|árbol B/B+]]** — la diferencia es que MongoDB crea automáticamente el índice del campo `_id` desde el primer insert, sin que el desarrollador tenga que declararlo.

[[Teorema CAP (o de Brewer)]]
[[Árbol B, B+ y B-estrella]]
[[MapReduce]]
[[B2 - T5 NOSQL Y BIG DATA]]
