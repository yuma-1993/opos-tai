**RadixSort** tiene complejidad **O(n·K)**, donde K es el número de cifras de los valores a ordenar. Se basa en distribuir los números en casilleros según sus dígitos, en sucesivas pasadas.

- **LSD (Least Significant Digit)**: usa primero el dígito menos significativo.
- **MSD (Most Significant Digit)**: usa primero el dígito más significativo.

Cuando los números se meten en los casilleros (*buckets*), se insertan ya ordenados dentro de cada uno; primero se distribuye según un dígito y luego según el siguiente.

[[BucketSort o BinSort]]
[[Big O (notación de complejidad algorítmica)]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
