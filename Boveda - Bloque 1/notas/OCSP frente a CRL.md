El **Online Certificate Status Protocol (OCSP)** es el protocolo de comprobación del estado de un certificado en línea: un cliente OCSP envía una petición sobre el estado de un certificado concreto a la Autoridad de Validación, que responde con su estado (válido, revocado...). El servicio de validación está siempre disponible.

Se considera **más práctico que usar CRL** (Listas de Revocación de Certificados). La diferencia práctica: una **CRL** es una lista completa de todos los certificados revocados que el cliente debe descargar entera y consultar localmente (puede ser grande y quedar desactualizada entre publicaciones); **OCSP** consulta en tiempo real el estado de un único certificado concreto, sin descargar la lista completa.

[[B1 - T6.1 SOCIEDAD DE LA INFORMACION]]

**Conexiones con otros conceptos TAI:**
- [[Autoridad de Certificación vs Autoridad de Validación|Autoridad de Certificación vs Autoridad de Validación]] — es la Autoridad de Validación quien responde a las peticiones OCSP.
- [[DNI electrónico (DNIe)]] — sus certificados se validan mediante OCSP.
- [[Certificado TLS-SSL (X.509)]] — la revocación de certificados X.509 en general también se apoya en OCSP/CRL.
