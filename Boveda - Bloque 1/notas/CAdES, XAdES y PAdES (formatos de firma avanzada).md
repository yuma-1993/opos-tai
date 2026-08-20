Son los tres formatos concretos en los que se puede materializar una firma electrónica avanzada ([[Perfiles de firma AdES (BES a A)|AdES]]), según el tipo de contenedor:

| Formato | Nombre completo | Cuándo usarlo |
|---|---|---|
| **CAdES** | CMS Avanzado | Evolución del primer formato de firma estandarizado. Adecuado para ficheros grandes, especialmente si la firma contiene el documento original, porque optimiza el espacio. Tras firmar, la información firmada no se puede ver directamente porque se guarda de forma **binaria**. |
| **XAdES** | XML Avanzado | El resultado es un fichero de texto **XML**, con etiquetas, similar al HTML. Suele ser más grande que en CAdES, así que no es adecuado si el fichero original es muy grande. Aplicaciones como eCoFirma (Ministerio de Industria y Comercio) solo firman en XAdES. |
| **PAdES** | PDF Avanzado | El más adecuado cuando el documento original es un **PDF**: el destinatario puede comprobar fácilmente la firma y el documento firmado, cosa que con los otros dos formatos no es posible sin herramientas externas. |

Existen también formatos de firma propios de las suites ofimáticas: **OOXML** (Microsoft Office) y **ODF** (Open Office).

[[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]]
