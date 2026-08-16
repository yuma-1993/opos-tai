**UEFI** (Unified Extensible Firmware Interface) es el firmware que sustituye a la [[BIOS]] en los equipos modernos, resolviendo precisamente los dos límites que dejaron obsoleta a esta última: el número de particiones y el tamaño máximo de disco.

> [!note] Diferencia con `B2 - T1 INFORMATICA BASICA` y `Placa base`
> Esas notas traen la tabla comparativa BIOS vs UEFI. Esta nota se queda solo con UEFI: qué resuelve y qué características trae que la BIOS clásica no tenía.

## Particionamiento — GPT

UEFI trabaja con **GPT** (*GUID Partition Table*) en vez de MBR:

- **Sin el límite de 4 particiones**: permite muchas más particiones primarias.
- **Sin el límite de ~2 TiB**: soporta discos mucho más grandes, al usar direcciones más anchas para los sectores.
- **Redundancia**: a diferencia del MBR (una única copia de la tabla de particiones al principio del disco, un punto único de fallo), GPT guarda **una copia de respaldo** de la tabla de particiones al final del disco — si la primera se corrompe, hay una segunda de la que recuperarse.

## Otras diferencias frente a BIOS

- **Interfaz gráfica**: se navega con ratón, no solo con teclado.
- **Arranque más rápido**: el proceso de inicialización de hardware es más eficiente que el POST clásico de BIOS.
- **Secure Boot** (conocimiento general): UEFI puede verificar la **firma digital** del sistema operativo/bootloader antes de ejecutarlo, rechazando código no firmado o alterado. Es una defensa contra malware que intenta ejecutarse antes de que cargue el propio sistema operativo (rootkits de arranque). Es, por ejemplo, uno de los requisitos de Windows 11.
- **Compatibilidad con BIOS** (conocimiento general): muchas placas UEFI incluyen un modo **CSM** (*Compatibility Support Module*) que emula una BIOS clásica, para poder arrancar sistemas operativos o discos antiguos pensados solo para MBR/BIOS.

> [!important] Idea clave para examen
> UEFI no es "una BIOS con más botones": resuelve limitaciones estructurales concretas (4 particiones, 2 TiB) y añade una capa de seguridad (Secure Boot) que la BIOS clásica no podía ofrecer por diseño.

## 🔑 Resumen ultra-rápido

- UEFI = sucesor de BIOS, interfaz gráfica, arranque con GPT.
- GPT resuelve los dos límites de MBR: más de 4 particiones, discos de más de 2 TiB, y añade tabla de particiones redundante (copia de respaldo).
- Secure Boot: verifica firma digital del bootloader/SO antes de ejecutarlo.
- CSM: modo de compatibilidad para arrancar en modo BIOS/MBR cuando hace falta.

---

**Conexiones con otros conceptos TAI:**
- [[BIOS]] — el firmware al que sustituye, con el detalle de POST y MBR.
- [[Placa base]] — dónde vive físicamente el firmware.
- [[B2 - T1 INFORMATICA BASICA]] — tabla resumen de examen BIOS vs UEFI.
