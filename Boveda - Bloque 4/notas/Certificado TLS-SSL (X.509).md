Un **certificado TLS/SSL** (formato **X.509**) es un fichero que vincula una clave pública con una identidad (un dominio, normalmente), firmado por una **autoridad de certificación (CA)** que da fe de esa vinculación. En Apache se configura con **`SSLCertificateFile`** (el certificado) y **`SSLCertificateKeyFile`** (la clave privada asociada), junto con `SSLEngine on` para activar HTTPS en el `VirtualHost`.

Por debajo usa el mismo mecanismo de [[Criptografía asimétrica (clave pública y privada)]] — un par de clave pública/privada —, pero añade una pieza que ese mecanismo por sí solo no tiene: la firma de una CA, que permite a cualquier visitante confiar en el certificado sin haberlo visto antes.

**No confundir con las claves de SSH**: el certificado X.509 y la clave RSA de usuario/host de SSH (`id_rsa`/`id_rsa.pub`, `ssh_host_rsa_key`...) son dos sistemas de PKI distintos que resuelven problemas distintos — cifrar una web pública para cualquier visitante frente a autenticar una sesión de administración remota.

[[B4 - T1.3 ADMON SSOO - APACHE]]
[[B4 - T1.2 ADMON SSOO - SSH]]
