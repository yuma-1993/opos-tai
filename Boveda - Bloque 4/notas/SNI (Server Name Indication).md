**SNI (Server Name Indication)** es una extensión de TLS que envía el nombre de dominio **sin cifrar** durante el propio saludo (*handshake*) TLS, antes de completar el cifrado de la conexión.

**¿Por qué hace falta esto?** Sin SNI, un servidor con varios sitios en el mismo puerto (varios `VirtualHost` en `*:443`, por ejemplo) no podría elegir qué certificado presentar: el nombre de dominio pedido normalmente viaja dentro de la petición HTTP, que en HTTPS ya va cifrada, y esa cifra depende justamente del certificado que hay que elegir primero. SNI rompe ese círculo enviando el dominio en claro solo durante el saludo inicial, para que el servidor pueda seleccionar el certificado correcto antes de cifrar el resto de la conexión.

Prácticamente todos los navegadores y las versiones modernas de Apache lo soportan.

[[VirtualHost (Apache)]]
[[B4 - T1.3 ADMON SSOO - APACHE]]
