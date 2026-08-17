Patrón **estructural** que resuelve estructuras de objetos poco flexibles, permitiendo un diseño más escalable. Un **elemento** puede ser **simple** o **compuesto**; si es compuesto, puede contener a su vez elementos simples o compuestos, en una relación **recursiva** (por ejemplo, `Sección` ◇ `División` ◇ `Estante` ◇ `Balda` ◇ `Producto`). Esto permite todas las combinaciones posibles y que, si el día de mañana aparece un nuevo tipo de contenedor, se pueda introducir minimizando el impacto sobre el resto del diseño.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
