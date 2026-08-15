**BIOS** (Basic Input Output System) es el firmware clásico de la [[Placa base]]: el primer código que se ejecuta al pulsar el botón de encendido, guardado en un chip de memoria no volátil (ROM/EEPROM) de la propia placa, **antes** de que exista ningún sistema operativo cargado.

> [!note] Diferencia con `B2 - T1 INFORMATICA BASICA` y `Placa base`
> Esas notas traen la tabla comparativa BIOS vs [[UEFI]]. Esta nota se queda solo con BIOS: qué hace paso a paso y por qué se quedó obsoleta.

## Qué hace, en orden

1. **POST** (*Power-On Self-Test*): comprueba que el hardware básico funciona — memoria, teclado, controladoras de disco — antes de seguir. Si algo falla aquí, ni siquiera llegas a ver arrancar el sistema operativo (los famosos pitidos de la BIOS son códigos de error de esta fase).
2. Busca un dispositivo de arranque y lee su **MBR** (*Master Boot Record*): los primeros 512 bytes del disco, que contienen tanto el código de arranque como la tabla de particiones.
3. Entrega el control al **gestor de arranque** (bootloader) que encuentra ahí, y este ya carga el sistema operativo.

- **Interfaz**: modo carácter (texto), navegación con teclado, sin ratón.
- **Particionamiento — MBR**: soporta un máximo de **4 particiones primarias**. Al usar direcciones de 32 bits para los sectores (de 512 bytes cada uno), el límite teórico de tamaño de disco que puede direccionar son **2 TiB** — por encima de eso, MBR simplemente no puede direccionar el resto del disco.

> [!important] Por qué quedó obsoleta
> Dos límites duros de MBR/BIOS provocaron el salto a [[UEFI]]: el **tope de 4 particiones primarias** y el **tope de ~2 TiB por disco**. Cuando los discos empezaron a superar ese tamaño con normalidad, BIOS+MBR dejó de ser viable como estándar.

## Dónde vive la configuración

Los ajustes que se cambian desde el menú de la BIOS (orden de arranque, fecha/hora, voltajes...) se guardan en la **NVRAM/CMOS** de la placa, respaldada por una pila — la misma NVRAM que mantiene el **RTC** descrito en [[Reloj]]. Sin esa pila, la BIOS "olvida" su configuración y la fecha/hora al desenchufar el equipo.

## 🔑 Resumen ultra-rápido

- BIOS = firmware en ROM/EEPROM de la placa, primer código ejecutado al encender.
- Orden: POST (autodiagnóstico) → lee MBR → entrega el control al bootloader.
- Interfaz de texto, sin ratón. Particionamiento MBR: máx. 4 particiones primarias, máx. ~2 TiB por disco.
- Configuración guardada en la NVRAM/CMOS de la placa, con pila de respaldo (mismo sitio que el RTC).
- Sustituida por UEFI precisamente por los límites de MBR (particiones y tamaño de disco).

---

**Conexiones con otros conceptos TAI:**
- [[UEFI]] — su sucesor directo, con tabla comparativa completa.
- [[Placa base]] — dónde vive físicamente el chip de firmware y la NVRAM/CMOS.
- [[Reloj]] — el RTC que comparte NVRAM con la configuración de la BIOS.
- [[B2 - T1 INFORMATICA BASICA]] — tabla resumen de examen BIOS vs UEFI.
