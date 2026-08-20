**Redis** es una base de datos NoSQL de tipo **clave-valor**, usada para muchas cosas ≈ una gran **[[Tabla Hash|tabla hash]]**. Se usa habitualmente como gestor de datos de apoyo, a modo de **[[Memoria Caché|caché]] de 1er nivel**.

En Redis, cada clave tiene asociado un tipo de dato con sus propias operaciones:

| Tipo | Operaciones |
|---|---|
| strings | `get`, `set` |
| sets | `sadd`, `smembers` |
| lists | `lpush`, `lrange` |
| hashes | `hmset`, `hmget`, `hset`, `hget`, `hgetall` |

**Caso de uso real:** Twitter usa Redis para montar el *timeline* de la página de inicio de cada usuario. La monta poco a poco, no en el momento en que el usuario se conecta.

En el **[[Teorema CAP (o de Brewer)|teorema CAP]]**, Redis se clasifica como sistema **CP** (junto a MongoDB, BigTable, BerkeleyDB y HBase).

**Ampliación (conocimiento general, no viene del tema):** que Redis se use como "caché de 1er nivel" no significa que sea solo volátil: soporta persistencia en disco (snapshots RDB y/o *append-only file*), por lo que puede sobrevivir a un reinicio. Lo que lo hace apto como caché es que toda la estructura de datos vive en memoria (acceso rapidísimo), no que sea necesariamente efímero.

[[Tabla Hash]]
[[Memoria Caché]]
[[Teorema CAP (o de Brewer)]]
[[B2 - T5 NOSQL Y BIG DATA]]
