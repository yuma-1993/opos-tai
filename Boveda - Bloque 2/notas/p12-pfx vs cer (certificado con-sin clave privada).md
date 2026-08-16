Dentro de los formatos de certificado **X.509**, `.p12`/`.pfx` **incluye** la clave privada asociada al certificado — por eso hay que protegerlo, es un fichero sensible. `.cer`, en cambio, **no incluye** la clave privada: es solo la parte pública del certificado, y se puede compartir sin riesgo.

Es la misma distinción de fondo que separa la clave pública de la clave privada en cualquier esquema de **[[Criptografía asimétrica (clave pública y privada)]]**: aquí se refleja en qué contiene o no cada formato de fichero de certificado.

[[Certificado TLS-SSL (X.509)]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
