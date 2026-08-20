El **teorema CAP** (o teorema de Brewer) dice que un sistema distribuido no puede garantizar simultáneamente más de **dos de estas tres propiedades**:

- **Consistency** (Consistencia): todos los nodos ven la misma información.
- **Availability** (Disponibilidad): toda petición recibe una respuesta.
- **Partition Tolerance** (Tolerancia a particiones): el sistema sigue funcionando aunque haya fallos en las comunicaciones que segmenten la red de nodos; si se cae un nodo, el sistema puede recuperarse.

Según qué dos propiedades se prioricen (y cuál se sacrifica), los sistemas se agrupan en tres combinaciones:

| Combinación | Se sacrifica | Ejemplos |
|---|---|---|
| **CA** (Consistency + Availability) | Partition Tolerance | RDBMS clásicos: Oracle, MySQL, PostgreSQL, SQL Server |
| **AP** (Availability + Partition Tolerance) | Consistency | Riak, Cassandra, CouchDB, Voldemort, DynamoDB |
| **CP** (Consistency + Partition Tolerance) | Availability | [[MongoDB]], [[Redis]], BigTable, BerkeleyDB, HBase |

Dos arquitecturas concretas ilustran la diferencia entre AP y CP: **Apache Cassandra (AP)** usa un **anillo** de nodos sin maestro (modelo peer-to-peer, cualquier nodo atiende lecturas/escrituras); **[[MongoDB]] (CP)** usa un nodo **Primary** que recibe las escrituras y replica a nodos **Secondary** (arquitectura de *replica set*, con un único punto de escritura consistente).

**Ampliación (conocimiento general, no viene del tema):** en la práctica, el propio Brewer matizó años después que la elección "2 de 3" es una simplificación: durante una partición de red sí hay que elegir entre C y A, pero fuera de una partición (la situación normal) el sistema puede ofrecer ambas. Por eso sistemas CP como MongoDB no están "sacrificando disponibilidad todo el tiempo", solo durante los cortes de red.

[[B2 - T5 NOSQL Y BIG DATA]]
