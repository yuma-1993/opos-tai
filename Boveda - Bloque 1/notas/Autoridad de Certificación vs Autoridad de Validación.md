En una PKI (infraestructura de clave pública), la **Autoridad de Validación** suministra información sobre la vigencia de los certificados electrónicos registrados por una Autoridad de Registro y certificados por la **Autoridad de Certificación**.

En la PKI del DNIe, ambas funciones las realizan entidades **distintas**, precisamente para aislar la comprobación de vigencia de un certificado de los datos de identidad de su titular: la Autoridad de Certificación (Dirección General de la Policía, Ministerio del Interior) no tiene acceso a los datos de las transacciones realizadas con los certificados que emite, y las Autoridades de Validación no tienen acceso a la identidad de los titulares. Esta separación refuerza la transparencia del sistema.

Dentro de la Autoridad de Certificación se distingue la **AC Raíz** (de primer nivel; solo emite certificados para sí misma y sus subordinadas) de las **AC Subordinadas** (emiten certificados para los titulares finales, como los del DNIe). Como Prestadores de Servicios de Validación actúan la Fábrica Nacional de Moneda y Timbre - Real Casa de la Moneda (carácter universal) y el Ministerio de Hacienda y Función Pública (para el conjunto de las AAPP).

[[B1 - T6.1 SOCIEDAD DE LA INFORMACION]]

**Conexiones con otros conceptos TAI:**
- [[OCSP frente a CRL]] — protocolo con el que la Autoridad de Validación responde sobre el estado de un certificado.
- [[DNI electrónico (DNIe)]] — ejemplo de PKI donde se aplica esta separación de funciones.
- [[Certificado TLS-SSL (X.509)]] — cualquier certificado X.509 depende de una Autoridad de Certificación que lo emita.
