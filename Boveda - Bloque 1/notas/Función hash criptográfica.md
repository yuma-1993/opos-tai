Una **función hash** toma un documento (de cualquier tamaño) y produce un resumen de longitud fija, llamado **residuo** o *message digest*. Es la base de la firma electrónica "básica": Documento → Hash → residuo → cifrado con la clave privada (ver [[Criptografía asimétrica (clave pública y privada)]]) → firma.

Algoritmos habituales: **SHA-256/384/512**, **SHA-1** (160 bits) y **MD5** (128 bits).

> [!note] Ampliación (conocimiento general, no viene del PDF de origen)
> Una función hash criptográfica es **determinista** (el mismo documento siempre produce el mismo resumen), **no reversible** (no se puede reconstruir el documento a partir del resumen) y **sensible a cualquier cambio mínimo** (cambiar un solo carácter del documento produce un resumen completamente distinto — "efecto avalancha"). Por eso sirve para comprobar la **integridad**: si el documento se altera después de firmarlo, su hash ya no coincide con el que se firmó.

[[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]]
