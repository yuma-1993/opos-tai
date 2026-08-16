Tres formas de decidir qué copiar en cada backup, según el **bit de modificado** de cada fichero (se activa cuando el fichero se modifica):

| Estrategia | Qué copia | ¿Desactiva el bit? | Espacio | Restauración | Qué hace falta para restaurar |
|---|---|---|---|---|---|
| **Completa** | Todos los archivos | Sí | Mayor | Menor | Solo la copia completa |
| **Incremental** | Ficheros modificados desde el último backup (de cualquier tipo) | Sí | Menor | Mayor | Última completa + **todos** los incrementales, en orden |
| **Diferencial** | Ficheros modificados desde la última completa (va acumulando) | No | Intermedio | Intermedio | Última completa + **última** diferencial |

**¿Por qué hace falta esto?**
La incremental copia poco cada vez (rápida, ocupa poco), pero para restaurar hay que aplicar la completa y luego cada incremental en orden — si se pierde uno de la cadena, se pierde la restauración desde ese punto. La diferencial siempre copia "todo lo cambiado desde la completa", así que cada copia crece, pero para restaurar solo hacen falta dos copias (completa + última diferencial), lo que la hace más robusta ante el fallo de un solo archivo de backup.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[RPO vs RTO]] — la estrategia y frecuencia elegidas determinan directamente el RPO real del sistema.
- [[Regla 3-2-1]] y [[Política GFS (Abuelo-Padre-Hijo)]] — las políticas de dónde guardar y cuánto tiempo retener estas copias.
- [[RAID (Redundant Array of Independent Disks)]] — RAID protege del fallo físico de un disco, no de un borrado accidental o corrupción lógica; estas estrategias de backup son las que cubren ese hueco.
