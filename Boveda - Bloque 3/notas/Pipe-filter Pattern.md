Patrón de **arquitectura** para el filtrado de información en un único sentido: los datos entran por una fuente (*source*), pasan por una tubería (*pipe*) hasta un filtro (*filter*) que los transforma, de ahí a la siguiente tubería y el siguiente filtro, y así sucesivamente hasta llegar a un sumidero final (*sink*): `Source → Pipe 1 → Filter 1 → Pipe 2 → Filter 2 → Pipe 3 → Sink`.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
