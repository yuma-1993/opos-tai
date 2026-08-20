**XMLDSIG** es el estándar de firma XML de la **W3C**, precursor de XAdES (XAdES es una extensión suya) — ver [[CAdES, XAdES y PAdES (formatos de firma avanzada)]]. Aunque su formato de salida es XML, permite firmar cualquier tipo de documento, no solo XML. Se usó mucho en la cabecera SOAP para firmar las peticiones (**WS-Security**).

Tiene tres formas de relacionar la firma con el documento firmado:

| Versión | Estructura |
|---|---|
| Enveloping | La firma envuelve al documento firmado (*signed data* contiene *document* + *signature*). |
| Enveloped | El documento contiene sus datos y la firma dentro de sí mismo. |
| Detached | El documento y la firma van en ficheros o elementos separados. |

Sus etiquetas básicas son `<DigestValue>` + `<DigestMethod>` (el algoritmo de hash usado, MD5, SHA1...), `<SignatureValue>` + `<SignatureMethod>`, y `<X509Certificate>` (con el algoritmo de cifrado asimétrico usado: RSA, DSA, DH...).

[[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]]
