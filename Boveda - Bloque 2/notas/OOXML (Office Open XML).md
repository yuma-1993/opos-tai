**OOXML (Office Open XML)** es el formato de los documentos de Microsoft Office desde la versión 2007 (`.docx`/`.docm`/`.dotx`/`.dotm`, `.xlsx`/`.xlsm`/`.xlsb`, `.pptx`/`.pptm`/`.potx`/`.potm`/`.ppsx`/`.ppsm` — la `t` indica plantilla/*template* y la `m` indica macros). Es el estándar **ECMA 376**, y por dentro es literalmente un **.zip** que contiene muchos ficheros **XML**.

**Cómo comprobarlo (ampliación, no viene literalmente del tema)**: renombrando cualquier `.docx` a `.zip` y abriéndolo con un descompresor normal, se ven las carpetas internas (`word/`, `_rels/`, etc.) con el XML del documento. Esto explica por qué OOXML se considera un formato **abierto**, frente al antiguo `.doc`/`.xls` (formato binario propietario **OLE**, anterior a 2007, no legible sin la especificación de Microsoft).

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
