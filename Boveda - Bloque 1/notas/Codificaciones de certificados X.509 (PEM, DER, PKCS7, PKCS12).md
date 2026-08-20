Los certificados [[Certificado TLS-SSL (X.509)|X.509]] definen su estructura de datos apoyándose en ASN.1, y esa estructura se puede codificar de dos formas:

| Codificación | Tipo | Extensiones |
|---|---|---|
| Base64/ASCII | PEM | `.pem`, `.crt`, `.cer`, `.key` |
| Base64/ASCII | PKCS#7 | `.p7b`, `.p7c` |
| Binario | DER | `.der`, `.cer` |
| Binario | PKCS#12 | `.pfx`, `.p12` |

Es un eje distinto al de si el fichero incluye o no la clave privada (ver [[p12-pfx vs cer (certificado con-sin clave privada)]]): esta tabla clasifica **cómo se codifican los bytes** (texto Base64 legible o binario puro), no qué contienen.

[[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]]
