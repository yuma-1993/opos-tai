Es la técnica que consiste en guardar una **copia temporal de los datos que se usan con frecuencia** en una memoria más rápida, para no tener que ir a buscarlos una y otra vez al dispositivo lento donde están originalmente. La idea es: "si ya traje este dato hace poco y probablemente lo vuelva a necesitar, me lo quedo cerca y a mano". Así, la próxima vez que se pida, se sirve al instante desde la copia rápida en lugar de repetir el acceso lento. Ejemplos típicos: la caché de la CPU (que guarda datos de la RAM), la caché de disco, o la caché del navegador (que guarda páginas web ya visitadas para no descargarlas de nuevo).

[[Técnicas de gestión de datos en memoria intermedia]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]] (mismo mecanismo de fondo que la memoización en programación dinámica)
[[B2 - T4.1 SISTEMAS OPERATIVOS]] (la TLB de la MMU cachea la tabla de páginas con esta misma idea)
