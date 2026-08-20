Es el DNI que **acredita electrónicamente la identidad personal** de su titular y permite la **firma electrónica de documentos**. Regulado por el Real Decreto 255/2025, todas las personas físicas o jurídicas, públicas o privadas, reconocen su eficacia para acreditar identidad y datos personales, y para acreditar la identidad del firmante y la integridad de los documentos que firma. Lo expiden los órganos del **Ministerio del Interior** (Dirección General de la Policía).

Incorpora un **chip criptográfico** que contiene, entre otros datos, un certificado electrónico para autenticar, un certificado electrónico para firmar, el certificado de la Autoridad de Certificación emisora y las claves para su utilización. Es un certificado **[[Certificado TLS-SSL (X.509)|X.509v3 estándar]]** — el mismo formato que se usa para asegurar un sitio web con TLS/SSL, aunque aquí la identidad vinculada es la de una persona física.

Es un dispositivo de **"Dual Interface"**: interfaz con contactos (lector de tarjetas) e interfaz sin contactos (NFC). La custodia de las claves privadas la realiza siempre el propio titular: la clave privada no puede extraerse del chip, y el acceso se protege con un **PIN** que nunca abandona la tarjeta.

Para el detalle completo (tabla de vigencia por edad, zonas del chip, algoritmos criptográficos soportados, versión digital vía app MiDNI) ver la nota de tema.

[[B1 - T6.1 SOCIEDAD DE LA INFORMACION]]

**Conexiones con otros conceptos TAI:**
- [[Reglamento eIDAS (UE) 910-2014]] — el DNIe es el ejemplo típico de dispositivo cualificado que alcanza el nivel más alto (4/Alto) de identificación eIDAS.
- [[Ley 6-2020, de servicios electrónicos de confianza]] — marco legal de los certificados cualificados que lleva el DNIe.
- [[No repudio (irrenunciabilidad)]] — propiedad que garantiza su Certificado de Firma.
- [[Autoridad de Certificación vs Autoridad de Validación]] — describe la PKI que emite y valida sus certificados.
- [[OCSP frente a CRL]] — mecanismo de validación de sus certificados.
- [[Criptografía asimétrica (clave pública y privada)]] — el chip genera pares de claves RSA para autenticación y firma.
- [[p12-pfx vs cer (certificado con-sin clave privada)]] — distinción de formato aplicable a sus certificados exportados.
- [[Middleware]] — DNIeDroid es el middleware que usan las apps Android para comunicarse con el DNIe.
