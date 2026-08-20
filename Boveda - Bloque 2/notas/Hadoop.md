**Hadoop** es el framework de referencia para procesar grandes volúmenes de datos en modo **batch**. Está formado por dos piezas que trabajan juntas:

- **HDFS** (*Hadoop Distributed File System*): sistema de ficheros distribuido, donde los datos viven repartidos en ficheros a lo largo de varios nodos.
- **YARN / MESOS**: gestión del clúster de Hadoop (un papel comparable al de k8s).

Su fortaleza es la **potencia de cómputo masiva** (ver **[[MapReduce]]**, el algoritmo clásico que se ejecuta sobre Hadoop), no la rapidez de respuesta puntual — de ahí que en el ecosistema Big Data se combine con NoSQL siguiendo la idea de **[[Persistencia políglota]]**, y que **[[Apache Kafka]]** sea la pieza que sincroniza los datos entre Hadoop/MapReduce y NoSQL.

[[MapReduce]]
[[Apache Kafka]]
[[Persistencia políglota]]
[[B2 - T5 NOSQL Y BIG DATA]]
