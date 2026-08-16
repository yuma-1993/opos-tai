**SQLite** es un caso especial dentro de los RDBMS: no es un gestor de base de datos cliente/servidor, sino un **formato de fichero** — la base de datos entera vive en un único archivo local.

Es **local**: no se accede a él por red como a Oracle, SQL Server o PostgreSQL. Se implementa como una **librería** que la propia aplicación embebe, y aun así es compatible con [[ACID (transacciones)|ACID]], por lo que permite hacer transacciones reales.

Es muy usado en dispositivos con recursos limitados, especialmente en **Android**, donde hace de base de datos local de las apps.

[[B3 - T3 SQL]]
