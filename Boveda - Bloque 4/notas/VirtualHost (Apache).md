Un **`VirtualHost`** es el bloque de configuración de Apache que permite que un único servidor sirva **varios sitios web distintos**, cada uno con su propia identidad: **`ServerName`**/`ServerAlias` (a qué dominio responde), **`DocumentRoot`** (de dónde sirve los ficheros) y sus propios **`ErrorLog`**/`CustomLog` (dónde registra accesos y errores). Es la base del hosting compartido.

Cuando varios `VirtualHost` escuchan en el mismo puerto HTTPS (`*:443`) con `ServerName` distinto, aparece un problema: el certificado SSL se negocia antes de que el servidor sepa a qué dominio va dirigida la petición (el nombre va dentro de la petición HTTP, todavía cifrada en ese momento). La extensión que lo resuelve es [[SNI (Server Name Indication)]].

[[B4 - T1.3 ADMON SSOO - APACHE]]
