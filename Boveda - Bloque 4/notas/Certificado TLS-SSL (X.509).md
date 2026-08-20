Un **certificado TLS/SSL** (formato **X.509**) es un fichero que vincula una clave pública con una identidad (un dominio, normalmente), firmado por una **autoridad de certificación (CA)** que da fe de esa vinculación. En Apache se configura con **`SSLCertificateFile`** (el certificado) y **`SSLCertificateKeyFile`** (la clave privada asociada), junto con `SSLEngine on` para activar HTTPS en el `VirtualHost`.

Por debajo usa el mismo mecanismo de [[Criptografía asimétrica (clave pública y privada)]] — un par de clave pública/privada —, pero añade una pieza que ese mecanismo por sí solo no tiene: la firma de una CA, que permite a cualquier visitante confiar en el certificado sin haberlo visto antes.

**No confundir con las claves de SSH**: el certificado X.509 y la clave RSA de usuario/host de SSH (`id_rsa`/`id_rsa.pub`, `ssh_host_rsa_key`...) son dos sistemas de PKI distintos que resuelven problemas distintos — cifrar una web pública para cualquier visitante frente a autenticar una sesión de administración remota.

[[B4 - T1.3 ADMON SSOO - APACHE]]
[[B4 - T1.2 ADMON SSOO - SSH]]
[[B2 - T4.2 WINDOWS Y SISTEMAS OPERATIVOS MOVILES]] — gestión de estos certificados en Windows con `certutil` y con `netsh http add sslcert`.
[[B1 - T6.1 SOCIEDAD DE LA INFORMACION]] — el Certificado de Firma del DNIe es también un certificado X.509v3 estándar (con el bit Content Commitment / No Repudio activo), el mismo formato que un certificado TLS/SSL de servidor, pero vinculado a la identidad de una persona física en vez de a un dominio.
[[B1 - T9.1 INSTRUMENTOS DE ACCESO]] — los certificados cualificados de sede electrónica, de sello electrónico y de empleado público de las AAPP también son certificados X.509, con el mismo mecanismo de fondo aplicado a un uso jurídico-administrativo.
[[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]] — la política de firma del ENI (XAdES/PAdES/CAdES) exige certificados reconocidos conforme al Reglamento eIDAS, que son certificados X.509 codificados en PEM/DER/PKCS#7/PKCS#12.
