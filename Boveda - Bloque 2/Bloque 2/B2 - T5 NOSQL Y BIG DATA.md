---
tags:
  - bloque2
  - tema5
  - nosql
  - big-data
  - teorema-cap
  - bases-de-datos
  - mongodb
  - redis
  - hadoop
  - mapreduce
bloque: 2
tema: 5
titulo: "NoSQL y Big Data: ventajas/desventajas frente al modelo relacional, teorema CAP, modelos de datos (documentos, clave-valor, grafos, columnas) y ecosistema Big Data (Hadoop, MapReduce, Kafka)"
estado: por-repasar
---

# Tema 5 · Bloque 2 — NoSQL y Big Data

> [!abstract] De qué va este tema
> Por qué existen las bases de datos **NoSQL** (ventajas/desventajas frente al modelo relacional, teorema **CAP**), cómo se clasifican según su **modelo de información** (documentos, clave-valor, grafos, familia de columnas — objetos y XML ya obsoletos), y el ecosistema de tecnologías que dan soporte a **Big Data** (Hadoop, HDFS, MapReduce, Kafka, Mahout, PIG/HIVE/Spark SQL), incluyendo la idea de **persistencia políglota** y la definición de Big Data en términos de las 5 V.

---

## 1. NoSQL: ventajas y desventajas frente al modelo relacional

### Ventajas

- **Productividad en desarrollo**: mejor ajuste que el modelo relacional. Permiten que los esquemas cambien. Esquemas flexibles y agregación.
- **Volumen de datos**: sistemas altamente distribuidos, escalables, de rendimiento alto.

Algunos sistemas incluyen **[[Sharding|SHARDING]]**: particionamiento horizontal de la información. Una vez fijado el criterio es complicado cambiarlo (ej.: tenemos facturas y las dividimos en base a la fecha o el importe).

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El sharding necesita un **criterio de partición** (shard key): por rango (ej. fechas, como en el ejemplo del PDF) o por hash de la clave. El de rango facilita las consultas por rango pero puede concentrar carga en un shard concreto (ej. todas las facturas del mes actual); el hash reparte la carga de forma más uniforme pero pierde la localidad de rango. Por eso el PDF insiste en que, una vez fijado, es complicado cambiarlo: redistribuir todos los datos entre shards con un criterio nuevo es una migración cara.
> Es un particionamiento a nivel de **aplicación/filas** entre nodos distintos; no debe confundirse con el striping de bloques dentro de un mismo array de discos ([[RAID (Redundant Array of Independent Disks)]]), que reparte datos a nivel físico dentro de un único nodo y persigue sobre todo velocidad o tolerancia a fallo de disco, no escalar horizontalmente entre servidores.

### Desventajas

- **No garantizan completamente ACID**. Consistencia eventual (**[[BASE (Basically Available, Soft State, Eventually Consistent)|BASE]]**: *Basically Available, Soft state, Eventually consistent*), ya que la información distribuida tarda en consolidarse.
- **Falta de madurez, experiencia y compatibilidad**. No hay estándares. Te casas con el producto.

> [!important] ACID vs BASE
> El modelo relacional (ver [[B3 - T3 SQL]]) prioriza **[[ACID (transacciones)|ACID]]** (garantías estrictas de consistencia, con [[Niveles de aislamiento y lecturas anómalas (SQL)|niveles de aislamiento]] configurables para controlar qué lecturas anómalas se permiten); muchos NoSQL priorizan **BASE** (disponibilidad y consistencia eventual) a cambio de escalar mejor de forma distribuida. No son incompatibles en abstracto, pero sí una elección de diseño: cuanta más disponibilidad/escalabilidad exiges, más difícil es mantener consistencia estricta en todo momento (esta tensión es precisamente lo que formaliza el teorema CAP del punto siguiente).

---

## 2. [[Teorema CAP (o de Brewer)]]

Tres propiedades:

| Propiedad | Significado |
|---|---|
| **Consistency** | Todos los nodos ven la misma información |
| **Availability** | Toda petición tiene que recibir una respuesta |
| **Partition Tolerance** | El sistema debe seguir funcionando aunque haya fallos en las comunicaciones que segmenten la red de nodos. Si se cae un nodo, el sistema puede recuperarse |

> [!important] Regla del teorema
> Según el teorema, **un sistema no puede asegurar más de dos de las tres características simultáneamente**.

| Combinación | Se sacrifica | Ejemplos (del diagrama del PDF) |
|---|---|---|
| **CA** (Consistency + Availability) | Partition Tolerance | RDBMS: Oracle, MySQL, PostgreSQL, SQL Server |
| **AP** (Availability + Partition Tolerance) | Consistency | Riak, Cassandra, CouchDB, Voldemort, DynamoDB |
| **CP** (Consistency + Partition Tolerance) | Availability | MongoDB, Redis, BigTable, BerkeleyDB, HBase |

El PDF ilustra con dos arquitecturas concretas la diferencia entre un sistema AP y uno CP:

- **Apache Cassandra (AP)**: arquitectura en **anillo** de nodos (`NODE`) sin nodo maestro — modelo peer-to-peer, cualquier nodo puede atender lecturas/escrituras.
- **MongoDB (CP)**: el *Client Application Driver* hace *writes* y *reads* contra un nodo **Primary**, que replica a nodos **Secondary** (arquitectura de *replica set*, con un único punto de escritura consistente).

> [!note] Ampliación (conocimiento general, no viene del PDF)
> En la práctica el propio Brewer matizó años después que la elección "2 de 3" es una simplificación: durante una partición de red sí hay que elegir entre C y A, pero **fuera de una partición** (que es la situación normal) el sistema puede ofrecer ambas. Por eso muchos sistemas CP como MongoDB no están "sacrificando disponibilidad todo el tiempo", sino solo durante los cortes de red — el teorema describe el compromiso en el peor caso, no el comportamiento habitual del sistema.

---

## 3. Clasificación de NoSQL según el modelo de información

Objetos y XML ya han quedado obsoletos como modelos NoSQL (el PDF los incluye en la tabla comparativa, pero sin productos activos asociados).

| Documentos | Familia Columnas | Clave-Valor | Grafos |
|---|---|---|---|
| MongoDB | Cassandra | REDIS | Neo4J |
| CouchDB | Hbase | RIAK | OrientDB (*) |
| OrientDB (*) | Hypertable | Voldemort | FlockDB |
| ArangoDB (*) | Bigtable | ArangoDB (*) | InfiniteGraph |
| DynamoDB (*) | | OrientDB (*) | HyperGraphDB |
| RavenDB | | DynamoDB (*) | ArangoDB (*) |
| TerraStore | | SimpleDB | AllegroGraph |

> [!note] Los productos marcados con `(*)` (OrientDB, ArangoDB, DynamoDB) aparecen en más de una columna de la tabla del PDF.

### 3.1 Documentos (ejemplo: [[MongoDB]])

En MongoDB se manejan **colecciones de documentos** con formato **JSON**. No hace falta definir un esquema — todo es JSON. Cada vez que se inserta un documento se le asocia un campo `id` que se genera automáticamente. Pueden añadirse más o menos campos y no pasa nada. De forma nativa indexa todo lo que se va introduciendo. Podría enlazarse con Alfresco para almacenar información binaria.

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

- `db`: objeto BD. `users`: colección. `find`: método.
- `db.facturas`: si no existe la colección `facturas`, se crea automáticamente.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Que MongoDB "indexe de forma nativa todo lo que se va introduciendo" no es magia: por debajo, sus índices (igual que en la mayoría de motores relacionales) suelen implementarse con estructuras tipo **[[Árbol B, B+ y B-estrella|árbol B/B+]]**, la misma familia de estructura que hace eficiente un índice en un SGBD relacional — la diferencia de MongoDB es que crea automáticamente el índice del campo `_id` desde el primer insert, sin que el desarrollador tenga que declararlo.

### 3.2 Clave-Valor (ejemplo: [[Redis|REDIS]])

Usado para muchas cosas ≈ una gran [[Tabla Hash|tabla hash]]. Se usa como gestor de datos de apoyo, a modo de **[[Memoria Caché|caché]] de 1er nivel**.

En REDIS, cada clave tiene asociado un tipo de dato con sus operaciones:

| Tipo | Operaciones |
|---|---|
| strings | `get`, `set` |
| sets | `sadd`, `smembers` |
| lists | `lpush`, `lrange` |
| hashes | `hmset`, `hmget`, `hset`, `hget`, `hgetall` |

> [!example] Caso de uso real (del PDF)
> Twitter usa REDIS para montar el *timeline* de la página de inicio de cada usuario. La monta poco a poco, no en el momento en que te conectas.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Que REDIS se use como "caché de 1er nivel" no significa que sea solo volátil: soporta persistencia en disco (snapshots RDB y/o *append-only file*), por lo que puede sobrevivir a un reinicio. Lo que lo hace apto como caché es que toda la estructura de datos vive en memoria (acceso rapidísimo), no que sea necesariamente efímero.

### 3.3 [[Bases de datos de grafos (NoSQL)|Grafos]]

El sistema se basa en información contenida en **nodos** y **aristas** — la misma noción de [[Grafo (conceptos básicos)|grafo]] vista en estructuras de datos. Usado en rutas de transporte, análisis forense, etc. Tanto los nodos como las relaciones (vértices) contienen *properties* (información). Cuentan con numerosos algoritmos implementados:

- **PageRank**: mide la influencia transitiva o la conectividad.
- **Shortest Path** con [[Algoritmo de Dijkstra|Dijkstra]] o A*.
- **Strongly Connected Components** con Tarjan.

### 3.4 [[Familia de Columnas (NoSQL)|Familia de Columnas]]

Cada fila puede tener diferentes columnas — **desnormalizado**. Cada columna tiene su **timestamp** asociado, generado por el propio producto.

**4 dimensiones**: Keyspace – Column Family – Rowkey – Column.

El diagrama del PDF describe la jerarquía así: un **Keyspace** (≈ Schema) contiene **Column Families** (≈ Table); cada Column Family tiene **Settings** y filas (**Row**), cada fila tiene una **Row Key** y varias **Columns**, y cada columna guarda (Key, Value) + **Timestamp**.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> "Desnormalizado" aquí significa lo contrario de lo que se persigue en el modelo relacional (ver [[Normalización]]): en vez de evitar redundancia dividiendo en tablas normalizadas, el modelo de columnas duplica y agrupa deliberadamente los datos que se van a leer juntos, para que una lectura típica no necesite hacer JOIN entre varias tablas — se optimiza para lectura rápida a costa de espacio y de la dificultad de mantener consistentes los datos duplicados.

---

## 4. Ecosistema de tecnologías Big Data

| Tecnología | Función |
|---|---|
| **Mahout** | Machine Learning |
| **PIG** | Capa para hacer consultas sobre los datos |
| **HIVE** | Capa para hacer consultas sobre los datos |
| **Spark SQL** | Capa para hacer consultas sobre los datos |
| **[[Apache Kafka]]** | Sincroniza los datos entre Hadoop/Map_Reduce y NoSQL, enlazando ambos sistemas |
| **YARN / MESOS** | Gestión del clúster de Hadoop (≈ k8s) |
| **HDFS** | Sistema de Ficheros Distribuido |

El diagrama del PDF sitúa `YARN o MESOS` (gestión del clúster) por encima de `HDFS` (sistema de ficheros distribuido), formando juntos **[[Hadoop]]**; `Apache Kafka` aparece en medio, conectando el bloque `Map_Reduce` (Hadoop) con el bloque `NoSQL`, sincronizando los datos entre ambos.

### 4.1 [[Persistencia políglota]]: Hadoop/MapReduce vs NoSQL

> [!important] Persistencia políglota
> A unos casos de uso les va bien Hadoop y a otros NoSQL — no es "uno mejor que el otro", sino herramientas para problemas distintos.

| | Map_Reduce (Hadoop) | NoSQL |
|---|---|---|
| Modo | **Batch** | **Interactivo / Realtime** |
| Fortaleza | Potencia de cómputo masiva | Rápidas lecturas y escrituras |
| Dónde viven los datos | Distribuidos en nodos HDFS; la información está en ficheros | — |

> [!note] Del PDF: "La principal diferencia es el tiempo de respuesta."

### 4.2 [[MapReduce]]: algoritmo de computación distribuida

En cada nodo hay una pieza **MAP_REDUCE**. El nombre significa **reducción de mapas**: mapea muchos nodos al estar la información distribuida, y reduce/trocea la información. Se tienen muchos datos a los que se les hace un mapeo (**map**) y sobre ese mapeo se hace un cálculo (**reduce**).

> [!example] Ejemplo del PDF: totalizar pedidos por cliente
> ```
> db.orders.mapReduce(
>   map:    function() { emit(this.cust_id, this.amount); },
>   reduce: function(key, values) { return Array.sum(values); },
>   query:  { status: "A" },
>   out:    "order_totals"
> )
> ```
> Colección `orders` (documentos de entrada, filtrados por `status: "A"`):
> - `{cust_id:"A123", amount:500, status:"A"}`
> - `{cust_id:"A123", amount:250, status:"A"}`
> - `{cust_id:"B212", amount:200, status:"A"}`
> - `{cust_id:"A123", amount:300, status:"D"}` ← excluido por la query (`status` no es `"A"`)
>
> **Map**: emite pares `(cust_id, amount)` → se agrupan por clave: `{"A123":[500,250]}`, `{"B212":[200]}`.
> **Reduce**: suma los valores de cada grupo → colección `order_totals`: `{_id:"A123", value:750}`, `{_id:"B212", value:200}`.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> MapReduce (el motor clásico de Hadoop) escribe resultados intermedios a disco entre cada fase, lo que lo hace robusto pero relativamente lento para trabajos iterativos. **Spark** (que aparece en el PDF como "Spark SQL", una de las capas de consulta) resuelve esto manteniendo los datos en memoria entre operaciones cuando es posible, por lo que en muchos casos de uso ha sustituido a MapReduce como motor de cómputo, aunque siga apoyándose en HDFS como sistema de ficheros.

---

## 5. [[Big Data]]: definición y las 5 V

**Big Data**: paradigma para hacer posible la recopilación, almacenamiento, gestión, análisis y visualización, potencialmente en condiciones de tiempo real, de grandes conjuntos de datos con características heterogéneas. Gestión y análisis de grandes volúmenes de datos que no pueden tratarse de manera convencional, dado que superan los límites y capacidades de las herramientas de software normalmente utilizadas para la captura, gestión y procesamiento de datos. El objetivo del Big Data, mediante análisis de gran cantidad de datos, es encontrar patrones repetitivos para obtener información suficiente que permita la toma de decisiones de forma automática.

> [!tip] Las 5 V del Big Data (del PDF)
> **Volumen, Variedad, Velocidad, Veracidad, Valor.**

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El PDF solo enumera las 5 V sin definirlas; su significado habitual es: **Volumen** (cantidad de datos), **Variedad** (datos estructurados, semiestructurados y no estructurados mezclados), **Velocidad** (ritmo al que se generan y deben procesarse), **Veracidad** (fiabilidad/calidad de los datos, que pueden venir con ruido o ser incompletos) y **Valor** (utilidad real que se extrae del análisis — sin esto, las otras cuatro V son solo coste).

---

## 🔑 Resumen ultra-rápido

- NoSQL — ventajas: productividad (esquemas flexibles, agregación), escalabilidad y volumen (sharding = partición horizontal, criterio difícil de cambiar).
- NoSQL — desventajas: no ACID completo (BASE: Basically Available, Soft state, Eventually consistent), falta de madurez/estándares.
- Teorema CAP (Brewer): Consistency, Availability, Partition Tolerance — máximo 2 de 3. CA=RDBMS clásico; AP=Riak/Cassandra/CouchDB/Voldemort/DynamoDB; CP=MongoDB/Redis/BigTable/BerkeleyDB/HBase.
- Cassandra = anillo de nodos sin maestro (AP); MongoDB = Primary + Secondary, replica set (CP).
- Modelos NoSQL: Documentos (MongoDB, JSON sin esquema), Clave-Valor (Redis, ≈ hash table, caché 1er nivel), Grafos (nodos+aristas+properties; PageRank, Dijkstra/A*, Tarjan), Familia de Columnas (Cassandra/HBase, desnormalizado, Keyspace-ColumnFamily-Rowkey-Column). Objetos y XML: obsoletos.
- Big Data stack: Mahout (ML), PIG/HIVE/Spark SQL (consultas), Kafka (sincroniza Hadoop↔NoSQL), Hadoop = YARN/MESOS (clúster, ≈k8s) + HDFS (FS distribuido).
- Persistencia políglota: Hadoop/MapReduce = batch, cómputo masivo, datos en HDFS; NoSQL = rápidas lecturas/escrituras, interactivo/realtime. La diferencia clave es el tiempo de respuesta.
- MapReduce = map (mapea/distribuye) + reduce (agrega/trocea el cálculo); ejemplo clásico: `mapReduce` de MongoDB para totalizar pedidos por cliente.
- Big Data: recopilación/almacenamiento/gestión/análisis/visualización de datos heterogéneos a gran escala, para encontrar patrones y automatizar decisiones. 5 V: Volumen, Variedad, Velocidad, Veracidad, Valor.

---

**Conexiones con otros conceptos TAI:**
- [[ACID (transacciones)]] y [[Niveles de aislamiento y lecturas anómalas (SQL)]] — el contraste ACID (relacional) vs BASE (NoSQL, consistencia eventual).
- [[B3 - T3 SQL]] — el modelo relacional frente al que se define NoSQL por contraste.
- [[Tabla Hash]] — el modelo clave-valor de REDIS es, en esencia, una tabla hash distribuida.
- [[Memoria Caché]] — REDIS como caché de 1er nivel comparte la misma idea de acceso rapidísimo en memoria.
- [[Grafo (conceptos básicos)]] y [[Algoritmo de Dijkstra]] — la base teórica (nodos/aristas, camino mínimo) detrás de las bases de datos de grafos.
- [[Árbol B, B+ y B-estrella]] — la estructura típica detrás de la indexación nativa de documentos (ej. MongoDB).
- [[RAID (Redundant Array of Independent Disks)]] — distinta capa de "repartir datos entre varias unidades" (striping físico de disco) frente al sharding NoSQL (partición lógica entre nodos).
