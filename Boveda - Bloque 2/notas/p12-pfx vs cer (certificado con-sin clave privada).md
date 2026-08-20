Dentro de los formatos de certificado **X.509**, `.p12`/`.pfx` **incluye** la clave privada asociada al certificado — por eso hay que protegerlo, es un fichero sensible. `.cer`, en cambio, **no incluye** la clave privada: es solo la parte pública del certificado, y se puede compartir sin riesgo.

Es la misma distinción de fondo que separa la clave pública de la clave privada en cualquier esquema de **[[Criptografía asimétrica (clave pública y privada)]]**: aquí se refleja en qué contiene o no cada formato de fichero de certificado.

[[Certificado TLS-SSL (X.509)]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
[[B1 - T6.1 SOCIEDAD DE LA INFORMACION]] — la misma distinción de formato aplica a los certificados X.509 del DNIe: la clave privada nunca sale del chip de la tarjeta, igual que un `.p12`/`.pfx` nunca debería compartirse frente a un `.cer`.
[[B1 - T9.1 INSTRUMENTOS DE ACCESO]] — misma lógica detrás de por qué el certificado de sede electrónica de las AAPP no sirve para firmar: lo decisivo es qué clave privada custodia cada certificado.
[[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]] — el ENI codifica los certificados X.509 en estas mismas variantes (PEM/DER en Base64 o binario, PKCS#7 y PKCS#12) para la política de firma electrónica.
