Es un **identificador único y mundial** que se le asigna a un dispositivo (un disco, un puerto SAS/Fibre Channel...). La idea es que sea **irrepetible en todo el planeta**: no hay dos dispositivos con el mismo WWN, igual que no hay dos tarjetas de red con la misma MAC, o dos coches con la misma matrícula a nivel mundial.

Es un número de **64 bits** (a veces 128), que suele escribirse en hexadecimal, tipo `50:06:01:60:...`. Una parte de ese número identifica al **fabricante** (hay un rango asignado a cada uno) y el resto identifica al **dispositivo concreto**. Así se garantiza que sea único.

**¿Por qué hace falta esto?**
Piensa en un servidor con cientos de discos conectados por SAS. Si los identificaras solo con números tipo "disco 1, disco 2..." (como el viejo ID de SCSI), esos números podrían **repetirse o cambiar** al reconectar cosas, y el sistema se liaría sobre cuál es cuál. Con el WWN, cada disco lleva su "matrícula mundial" grabada: da igual en qué puerto o cable lo enchufes, **el sistema siempre sabe que es exactamente ese disco**. Es imprescindible en entornos grandes (servidores, cabinas de almacenamiento) donde hay muchísimos dispositivos y no puedes permitirte confusiones.

En una frase: **el WWN es el "DNI mundial" irrepetible de un dispositivo de almacenamiento.**

---

**Conexiones con otros conceptos TAI:**
- [[SAS (Serial Attached SCSI)]] — sustituye aquí al viejo ID numérico de SCSI.
- [[B4 - T1.1 ADMON SSOO]] — en SAN, el HBA usa un WWN (WWNN de la cabina, WWPN del puerto), y el zoning entre switch FC y hosts se hace precisamente en base a estos WWN.