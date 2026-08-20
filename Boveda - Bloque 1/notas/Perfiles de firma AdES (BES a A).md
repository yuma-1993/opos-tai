La **firma avanzada** (**AdES**, Advanced Electronic Signature) es una firma electrónica básica (hash + cifrado con la clave privada) a la que se añaden metadatos: el certificado del firmante, la fecha y hora de la firma, el resultado de la comprobación de revocación del certificado, etc. Existen varios perfiles según qué metadatos añaden, y **cada uno se construye sobre el anterior**:

| Perfil | Añade |
|---|---|
| AdES-BES | Firma básica; formato mínimo para satisfacer los requisitos de la firma electrónica avanzada. |
| AdES-EPES | BES + política de firma explícita (su identificador, OID). Es el **mínimo perfil admitido por la Administración** — no se admite una firma BES sola. |
| AdES-T | + sellado de tiempo (*TimeStamp*), para situar en el tiempo el instante en que se firma. |
| AdES-C | + referencias a los certificados de la cadena de certificación y su estado (C de Cadena), como base para una verificación longeva. |
| AdES-X | + sellos de tiempo sobre esas referencias (X de eXtendida), para asegurar que eran así en ese momento. |
| AdES-XL | + los propios certificados y su información de revocación, para validación a largo plazo (XL: eXtendido Largo plazo). |
| AdES-A | + sellos de tiempo periódicos, para garantizar la integridad de la firma archivada de cara a futuras verificaciones (A de Archivo). |

**¿Por qué hace falta esto?** Un certificado caduca y puede ser revocado, pero un documento firmado puede necesitar validez legal muchos años después. Los sellos de tiempo y la información de revocación embebida en los perfiles superiores permiten demostrar, años más tarde, que en el momento de la firma el certificado era válido — sin depender de que ese certificado siga existiendo o siendo consultable entonces.

Estos perfiles se aplican sobre cualquiera de los tres formatos de firma avanzada ([[CAdES, XAdES y PAdES (formatos de firma avanzada)]]): por ejemplo, un XAdES-BES al que se añade un sello de tiempo se convierte en un XAdES-T.

[[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]]
