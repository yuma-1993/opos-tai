**Sharding** es el **particionamiento horizontal** de la información: en vez de guardar todos los datos en un solo nodo, se reparten entre varios nodos según un criterio (ej. tenemos facturas y las dividimos según la fecha o el importe). Es una de las técnicas que permiten a algunos sistemas NoSQL escalar en volumen de datos, siendo sistemas altamente distribuidos y de alto rendimiento.

Una vez fijado el criterio de partición (*shard key*), es **complicado cambiarlo**.

**Ampliación (conocimiento general, no viene del tema):** el criterio de partición puede ser por **rango** (ej. fechas, como en el ejemplo de facturas) o por **hash** de la clave. El de rango facilita las consultas por rango pero puede concentrar carga en un shard concreto (ej. todas las facturas del mes actual); el hash reparte la carga de forma más uniforme pero pierde la localidad de rango. Por eso, una vez fijado, es complicado cambiarlo: redistribuir todos los datos entre shards con un criterio nuevo es una migración cara.

Es un particionamiento a nivel de **aplicación/filas** entre nodos distintos; no debe confundirse con el *striping* de bloques dentro de un mismo array de discos ([[RAID (Redundant Array of Independent Disks)]]), que reparte datos a nivel físico dentro de un único nodo y persigue sobre todo velocidad o tolerancia a fallo de disco, no escalar horizontalmente entre servidores.

[[B2 - T5 NOSQL Y BIG DATA]]
