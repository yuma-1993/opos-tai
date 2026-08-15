---
tags:
  - bloque2
  - tema2
  - entrada-salida
  - interrupciones
  - almacenamiento
  - raid
  - perifericos
  - conectividad
bloque: 2
tema: 2
titulo: Periféricos, almacenamiento y conectividad
estado: por-repasar
---

# Tema 2 · Bloque 2 — Periféricos, almacenamiento y conectividad

> [!abstract] De qué va este tema
> Cubre cómo la CPU se comunica con el resto del sistema: el mecanismo de interrupciones y las técnicas de entrada/salida (polling, interrupciones, DMA), las distintas tecnologías de almacenamiento secundario (óptico, HDD, SSD) y cómo se combinan en RAID, y finalmente los periféricos de visualización/impresión/escaneo y los buses de conectividad externa (USB, Thunderbolt, FireWire).

---

## Parte I — Interrupciones y Entrada/Salida

### 1. Contextualización: ¿por qué existen las interrupciones?

La [[CPU - Central Processing Unit]] es muy rápida; los periféricos (teclado, ratón, disco...) son lentísimos en comparación. Si la CPU tuviera que preguntar constantemente "¿hay algo nuevo?" (esto se llama **[[polling]]**), perdería un rendimiento brutal esperando.

> [!important] Solución
> Que sea el periférico el que avise a la CPU cuando tiene algo que decir. Eso es una **interrupción**. La CPU sigue haciendo su trabajo normal, y solo cuando le "tocan el hombro" deja lo que está haciendo para atender el aviso.

El ejemplo de pulsar una tecla es el caso de manual de este mecanismo. Se diseca pieza por pieza a continuación.

### 2. Conceptualización: pieza por pieza

#### 2.1 El [[controlador]] (Controller)

- **Qué es**: un chip físico soldado en la placa base (o en una tarjeta) que hace de intermediario entre el dispositivo físico y el bus del sistema.
- **Por dentro tiene**: registro de control, registro de estado, registro de datos, y **firmware** (lógica grabada en una ROM actualizable, no en un chip aparte de software).
- **Ejemplo**: cuando pulsas la "A", el teclado (dispositivo) no habla directamente con la CPU. Le pasa la señal eléctrica a su controlador, que la traduce a un código y la mete en su registro de datos.

#### 2.2 La [[IRQ - Interrupt Request]]

- **Qué es**: la señal concreta que el controlador lanza para decir "¡tengo algo!".
- **Ejemplo**: el controlador del teclado dispara la IRQ1 (en la numeración clásica de PC, el teclado suele ser IRQ1).

#### 2.3 La [[PIC - Programmable Interrupt Controller]]

- **Qué es**: un chip cuya única función es **centralizar y arbitrar** todas las IRQ que llegan de los distintos controladores, y decidir el orden si llegan varias a la vez (prioridades).
- **Por qué hace falta**: la CPU tiene muy pocas líneas físicas de interrupción; no puede tener un cable por cada periférico. La PIC agrupa todo eso.
- **Ejemplo**: si el teclado y el ratón interrumpen casi a la vez, la PIC decide a cuál atiende antes según su prioridad configurada.

#### 2.4 El [[offset]] de interrupción

- **Qué es**: un índice que apunta a una posición de una tabla en la [[Memoria RAM]] (la [[tabla de vectores de interrupción]]). En esa posición está la dirección de memoria donde arranca la **ISR** correspondiente.
- **Ejemplo**: el teclado usa el offset **09H**. La PIC no sabe "qué hacer" con la interrupción, solo sabe traducir la IRQ del teclado a ese número 09H, que sirve de índice para ir a buscar en la tabla.

> [!note] Dato importante
> Las interrupciones pueden llevar **parámetros** (por ejemplo, qué tecla concreta se pulsó); no es solo un aviso vacío.

#### 2.5 La [[ISR - Interrupt Service Rutine]]

- **Qué es**: el código —el **driver**— que realmente sabe qué hacer con esa interrupción concreta. Es software, vive en RAM (cargado desde el driver del dispositivo).
- **Ejemplo**: la ISR del teclado lee el código de la tecla desde el registro de datos del controlador, lo traduce a un carácter ASCII/Unicode y se lo pasa al sistema operativo para que lo muestre en pantalla.

### 3. El flujo completo, ya con las piezas identificadas

| Paso | Elemento | Acción |
|---|---|---|
| 1 | Controlador del teclado | Detecta la tecla, la pone en su registro de datos |
| 2 | Controlador → PIC | Lanza la IRQ |
| 3 | PIC | Traduce la IRQ a offset 09H (índice en tabla de RAM) |
| 4 | PIC → CPU | Le dice a la CPU: "para, hay algo urgente" |
| 5 | CPU | Guarda su estado actual, busca en RAM (usando el offset) la dirección de la ISR |
| 6 | CPU | Ejecuta la ISR (el driver) |
| 7 | CPU | Termina la ISR, recupera su estado anterior y sigue donde estaba |

### 4. El flujo, paso a paso (versión detallada con ejemplo)

1. Pulsas la tecla → el controlador del teclado guarda el código en su **registro de datos**.
2. El controlador manda la **IRQ** (solo el aviso, sin el dato) a la PIC.
3. La PIC traduce esa IRQ al offset (09H) y le dice a la CPU: "para y atiende".
4. La CPU busca en RAM la dirección de la ISR usando ese offset, y **ejecuta el driver**.
5. El driver (la ISR) es quien **va directamente al registro de datos del controlador** y **lee** el código de la tecla de ahí. La PIC ya no interviene en este paso.
6. Con dispositivos de salida (ej: enviar algo a la pantalla) pasa parecido: la CPU escribe el dato directamente en el registro del controlador correspondiente; la PIC no participa en enviar esos datos.

---

## Entrada/Salida: sincronización y transferencia CPU-dispositivos

### 5. Contexto general

Cuando la [[CPU - Central Processing Unit]] necesita comunicarse con un dispositivo (teclado, disco, tarjeta gráfica...) hay dos problemas distintos que resolver:

1. **¿Cómo sabe la CPU que el dispositivo está listo?** → Sincronización
2. **¿Cómo se mueven físicamente los datos?** → Transferencia

### 6. Sincronización CPU-dispositivo

#### 6.1 [[polling]] (sondeo)

La CPU pregunta activamente y en bucle si el dispositivo tiene datos listos ("busy waiting").

- **Ventaja**: simple de implementar.
- **Inconveniente**: desperdicia ciclos de CPU comprobando algo que la mayoría de veces no ha cambiado. Ineficiente si el dispositivo es lento (ej. impresora) frente a la CPU.
- Técnica **antigua**; hoy se usa solo en sistemas muy simples/embebidos o cuando la latencia de interrupción no compensa (dispositivos ultrarrápidos).

#### 6.2 [[Interrupciones]]

El dispositivo, cuando está listo, **avisa activamente** a la CPU mediante una señal eléctrica (IRQ) que interrumpe la ejecución normal.

- La CPU salta a una rutina de servicio de interrupción (**ISR**), gestionada por el controlador de interrupciones (antes PIC 8259, hoy **APIC**).
- Ventaja: la CPU no pierde tiempo esperando, puede hacer otras tareas.
- Ejemplo: al pulsar una tecla, el teclado genera IRQ1.

#### 6.3 [[DMA]] (Acceso Directo a Memoria)

El dispositivo (a través de su controlador DMA) transfiere datos **directamente a/desde memoria RAM sin pasar por la CPU**, salvo para iniciar y finalizar la operación.

- La CPU programa la transferencia (dirección origen, destino, tamaño) y queda libre para otras tareas; al terminar, el controlador DMA lanza una interrupción de finalización.
- **Problema de coherencia de caché**: si la CPU tiene en su caché una copia de un dato que el DMA modifica en RAM (o viceversa), la caché queda desactualizada. Se soluciona con *cache snooping* (el controlador de caché vigila el bus) o invalidando/forzando *flush* de caché antes/después de la transferencia.
- Lo usan dispositivos de alto volumen de datos: **disco duro, tarjeta gráfica, tarjeta de red**.

> [!important] Resumen comparativo
> Polling (CPU pregunta) → Interrupciones (dispositivo avisa) → DMA (dispositivo transfiere solo, CPU libre). Es una evolución en eficiencia.

### 7. Transferencia de datos: ¿por dónde viajan?

Independientemente del método de sincronización, los datos se mueven por uno de estos dos esquemas:

#### 7.1 [[E-S aislada]] (puertos, instrucciones IN/OUT)

El espacio de direcciones de E/S está **separado** del de memoria. La CPU usa instrucciones específicas del ensamblador (`IN`, `OUT` en x86) para leer/escribir en un **puerto** identificado por un número.

- Ejemplo clásico: **controlador de teclado**
  - Puerto **0x64**: registro de estado/control (¿hay dato disponible? ¿es una tecla o un comando?).
  - Puerto **0x60**: registro de datos (el código de la tecla, *scancode*).
- Requiere instrucciones de máquina dedicadas, no se puede acceder con instrucciones normales de acceso a memoria (`MOV`).

#### 7.2 [[E-S mapeada en memoria]] (Memory-Mapped I/O, MMIO)

Los registros del dispositivo se mapean dentro del **mismo espacio de direcciones** que la RAM. La CPU accede a ellos con instrucciones normales (`MOV`), no hace falta `IN`/`OUT`.

- Usado por dispositivos que mueven muchos datos, como tarjetas gráficas (framebuffer).
- Ventaja: más simple y rápido, se puede usar cualquier instrucción de acceso a memoria.

### 8. Técnicas de gestión de datos en [[memoria intermedia]]

| Técnica                                                         | Qué es                                                                                                                                  | Ejemplo                                                                                              |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **[[Caching]]**                                                 | Copia temporal de datos de uso frecuente en memoria más rápida, para evitar acceder repetidamente al dispositivo lento.                 | Caché de disco: guarda bloques leídos recientemente en RAM.                                          |
| **[[Buffering]]**                                               | Memoria intermedia que compensa diferencias de velocidad entre CPU y dispositivo, o entre productor y consumidor.                       | Buffer de teclado (se pueden pulsar teclas mientras la CPU está ocupada, y se procesan después).     |
| **[[Spooling]]** (*Simultaneous Peripheral Operations On-Line*) | Buffer especial para dispositivos que **no admiten multiplexación** (solo un trabajo a la vez), permitiendo encolar varias solicitudes. | Cola de impresión: varios usuarios envían documentos, se almacenan en disco y se imprimen uno a uno. |

> [!important] Diferencia clave caching vs buffering
> La caché guarda una **copia** de datos que ya existen en otro sitio (para no volver a leerlos); el buffer es un **paso intermedio obligatorio** para que la transferencia sea posible (no es una copia redundante, es parte del flujo).

---

## Parte II — Almacenamiento

> [!abstract]
> El almacenamiento secundario guarda información de forma persistente (a diferencia de la RAM, volátil). Hay tres grandes familias por tecnología: **óptico** (láser sobre disco), **magnético/mecánico** (HDD) y **electrónico/flash** (SSD). Cada una evoluciona hacia mayor velocidad y menor latencia, y cada una tiene sus propias interfaces de conexión.

### 1. Discos ópticos

Almacenan datos mediante variaciones ópticas (pits/lands) leídas con láser.

#### Formatos de sistema de archivos

- **ISO 9660**: formato estándar clásico para CD-ROM. Limitaciones: nombres de archivo cortos (8.3), sin soporte nativo de mayúsculas/minúsculas ni nombres largos.
- **UDF** (Universal Disk Format): sucesor pensado para DVD/Blu-ray, soporta archivos grandes, nombres largos y reescritura (packet writing).
- **Extensión Joliet**: extensión de ISO 9660 (creada por Microsoft) que añade soporte de **nombres largos** (hasta 64 caracteres, Unicode) manteniendo compatibilidad con el estándar base.

#### Tipos de disco (evolución por capacidad)

| Tipo                                 | Capacidad aprox.     | Láser                                                                        |
| ------------------------------------ | -------------------- | ---------------------------------------------------------------------------- |
| CD-ROM                               | ~700 MB              | infrarrojo                                                                   |
| DVD                                  | 4,7 GB (simple capa) | rojo                                                                         |
| Blu-ray                              | 25 GB (simple capa)  | azul                                                                         |
| **HVD** (Holographic Versatile Disc) | hasta 1 TB (teórico) | holográfico, tecnología experimental, no llegó a consolidarse comercialmente |

#### El [[Torito]]

Especificación que define cómo un CD/DVD puede ser **booteable** (arrancable), simulando un disquete o disco duro para que la BIOS pueda cargar el sistema desde él. Ejemplo: un Live CD de Linux.

### 2. [[HDD (Hard Disk Drive)]] — disco mecánico

#### Arquitectura física

El disco se compone de varios **platos** apilados, cada uno con dos caras. Sobre ellos:
- **Cilindro**: conjunto de pistas alineadas verticalmente en todos los platos (misma posición radial).
- **Pista (track)**: círculo concéntrico dentro de una cara del plato.
- **Cabeza L/E**: cabeza de lectura/escritura, una por cara.
- **Sector**: subdivisión de una pista, unidad mínima física de almacenamiento (tradicionalmente 512 bytes).
- **Cluster**: agrupación de varios sectores gestionada por el sistema de archivos (no por el hardware), es la unidad mínima que el SO asigna a un archivo.

#### [[Direccionamiento]]

- **CHS** (Cylinder-Head-Sector): direccionamiento "real", indica físicamente dónde está el dato (cilindro + cabeza + sector). Limitado en capacidad (por los bits reservados a cada campo) y complejo de gestionar.
- **LBA** (Logical Block Addressing): direccionamiento **lineal**, cada sector tiene un número secuencial único (0, 1, 2...). El controlador del disco traduce internamente a CHS. Es el estándar actual, permite discos de mayor capacidad.

#### [[Interfaces]] (evolución cronológica)

| Interfaz     | Transmisión | Características                                                                                                                                                                                                                                             |
| ------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **IDE/PATA** | Paralelo    | Cable ancho (40/80 hilos), máx. 2 dispositivos por cable (master/slave), obsoleta                                                                                                                                                                           |
| **SCSI**     | Paralelo    | Bus con **7 a 15 dispositivos**, cada uno con su **ID** único; usado históricamente en servidores                                                                                                                                                           |
| **SATA**     | Serie       | Sustituye a PATA. Un solo dispositivo por cable. Limitación de velocidad respecto a SAS/NVMe (pensado para consumo, no full-duplex)                                                                                                                         |
| **SAS**      | Serie       | Serial Attached **SCSI**: hereda el modelo lógico de SCSI pero con transmisión serie. Cada dispositivo tiene un **WWN** (World Wide Name, identificador único de 64 bits) en vez de ID numérico. Hasta **16.384 dispositivos** por dominio (vía expansores) |

**Velocidades SATA**: SATA-1 (1,5 Gbps) → SATA-2 (3 Gbps) → SATA-3 (6 Gbps, actual). Se duplica en cada generación.

**Velocidades SAS**: SAS-1 (3 Gbps) → SAS-2 (6 Gbps) → SAS-3 (12 Gbps) → SAS-4 (22,5 Gbps) → SAS-5 (45 Gbps, en desarrollo). También duplica aprox. cada generación.

> [!important] Idea clave para examen
> SAS es la evolución "profesional" de SCSI, pensada para servidores (múltiples discos, redundancia, hot-swap), mientras SATA es la evolución "doméstica" de PATA.

### 3. [[SSD (Solid State Drive)]] — disco de estado sólido

Sin partes móviles, basado en memoria **Flash NAND**: almacena datos en celdas de transistores mediante carga eléctrica.

#### Tecnologías de fabricación (bits por celda)

| Tipo | Bits/celda | Velocidad/durabilidad | Coste |
|---|---|---|---|
| **SLC** (Single) | 1 bit | Máxima velocidad y ciclos de escritura (más duradera) | Más cara |
| **MLC** (Multi) | 2 bits | Intermedia | Media |
| **TLC** (Triple) | 3 bits | Más lenta, menos ciclos | Barata (uso doméstico habitual) |
| **QLC** (Quad) | 4 bits | La más lenta y menos duradera | La más barata |

> [!important]
> A más bits por celda → mayor capacidad por el mismo espacio físico, pero menor velocidad y vida útil (más desgaste por escritura).

#### Interfaces específicas de SSD

- **M.2**: formato físico tipo "tarjeta de memoria" que reemplaza a **mSATA**. No define un único protocolo: puede llevar señal **SATA** (M.2 SATA, más lento, limitado a ~6 Gbps) o **PCIe/NVMe** (M.2 NVMe, mucho más rápido).
  - Nomenclatura de tamaño: **M2 2280** = 22 mm de ancho × 80 mm de largo.
- **NVMe** (Non-Volatile Memory Express): protocolo diseñado específicamente para SSD (no usa SATA), se conecta directamente al bus **PCIe**, usando típicamente **4 lanes/carriles**. Mucho menor latencia que AHCI/SATA porque está diseñado desde cero para flash.
- **PCIe** (bus subyacente que usa NVMe): bus de datos serie, hasta **16 lanes**. Velocidad por generación (por lane, en GT/s = giga-transferencias/segundo):
  - PCIe 6: 64 GT/s
  - PCIe 7: 128 GT/s
  - (Patrón: cada generación duplica, potencia de 2: 2⁶=64, 2⁷=128)
- **U.2**: interfaz orientada a **servidores**, permite conectar SSD NVMe con conector similar a SAS/SATA. Ventaja clave: **hot-swapping** (sustitución en caliente sin apagar el equipo), típico en entornos de alta disponibilidad.

> [!note] Cuadro resumen mental (incompleto en la fuente original)
> ```
> Óptico:  CD/DVD (ISO9660+Joliet) → UDF → Blu-ray → HVD
> ```
> La fuente original solo incluía la línea de ópticos; si tienes las líneas equivalentes para HDD y SSD, se pueden añadir aquí.

---

## Parte III — [[RAID (Redundant Array of Independent Disks)]]

> [!abstract]
> RAID combina varios discos físicos para que el sistema operativo los vea como **una única unidad lógica**. El objetivo es mejorar **rendimiento** (velocidad), **seguridad** (tolerancia a fallos) o ambos, a costa de capacidad útil o coste. Puede implementarse por **hardware** (controladora RAID dedicada) o por **software** (el propio SO, ej. Windows Storage Spaces, mdadm en Linux).

### Regla general de capacidad

Si mezclas discos de distinto tamaño, RAID trata a todos como si tuvieran el tamaño del **más pequeño** (el resto de espacio de los discos mayores se desperdicia).

> [!example]
> Discos de 120 GB y 320 GB → el sistema los trata como si ambos fueran de 120 GB. En RAID 0 (sin redundancia): capacidad = 2 × 120 GB = **240 GB** (se pierden 200 GB del disco grande).

### Spare (disco de repuesto)

Disco extra, sin usar, conectado a la controladora. Si un disco activo falla, el *spare* **entra automáticamente** a sustituirlo y el RAID reconstruye (*rebuild*) la información redundante sobre él, sin intervención manual inmediata.

### RAID 0 — Striping (división)

- **Qué hace**: divide los datos en **tiras (stripes)** repartidas entre todos los discos.
- **Redundancia**: ninguna. Si falla un disco, se pierde **todo** el conjunto de datos.
- **Rendimiento**: excelente en lectura y escritura, porque las operaciones se paralelizan entre discos.
- **Mínimo**: 2 discos.
- **Capacidad neta** = nº discos × capacidad del disco más pequeño (100% aprovechado).
- **Uso típico**: edición de vídeo, escenarios donde importa la velocidad y los datos están respaldados en otro sitio.

### RAID 1 — Mirroring (espejo)

- **Qué hace**: cada bloque se **duplica** en dos (o más) discos: uno primario, otro espejo.
- **Redundancia**: total, no usa paridad, usa copia exacta.
- **Rendimiento**: buena lectura (puede leer de cualquier copia), escritura normal (hay que escribir dos veces).
- **Mínimo**: 2 discos.
- **Desventaja**: solo aprovechas el 50% de la capacidad total.
- **Capacidad neta** = (nº discos × capacidad del más pequeño) / 2.
- **Uso típico**: sistemas críticos donde no puedes permitirte perder datos (ej. servidores de bases de datos pequeños).

### RAID 2 y 3 — Acceso en paralelo (tiras muy pequeñas: bit/byte)

Característica común: **todos los discos participan a la vez en cada operación de E/S** (una petición usa todos los discos simultáneamente).

#### RAID 2

- Distribuye los **bits** entre M discos de datos + N discos de paridad, calculada con **código Hamming** (detecta y corrige errores, no solo detecta).
- Nivel **teórico**, nunca se implementó comercialmente (los discos modernos ya tienen su propia corrección de errores interna, hace innecesario RAID 2).
- 3 o más discos. Capacidad según configuración (3+2, 7+3, 15+4...): el número de discos de paridad depende del número de bits de datos (a más discos de datos, proporcionalmente menos discos de paridad necesarios, según Hamming).

#### RAID 3

- Distribuye **tiras de información** (bytes) entre M discos + **1 disco dedicado a paridad**.
- 3 o más discos.
- **Capacidad neta** = (nº discos − 1) × capacidad del disco más pequeño.
- Problema práctico: como cada operación usa todos los discos a la vez, no se pueden paralelizar varias peticiones distintas simultáneamente → mal rendimiento con muchas peticiones pequeñas concurrentes. Poco usado hoy.

### RAID 4, 5 y 6 — Acceso independiente (tiras grandes: bloques)

Característica común: cada disco puede atender **peticiones distintas de forma independiente** (mejor para muchos accesos concurrentes pequeños, típico de servidores).

#### RAID 4

- Igual que RAID 3, pero con tiras de **bloques** en vez de bytes: M discos de datos + **1 disco fijo de paridad**.
- 3 o más discos.
- **Capacidad neta** = (nº discos − 1) × capacidad del disco más pequeño.
- **Problema**: el disco de paridad es un **cuello de botella**, porque cada escritura implica escribir también en ese único disco → se satura. Por eso RAID 5 lo mejora.

#### RAID 5

- Igual concepto, pero la paridad se **distribuye rotando entre todos los discos** (no hay un disco fijo de paridad) → elimina el cuello de botella de RAID 4.
- 3 o más discos.
- Tolera **1 fallo** de disco (con la paridad se reconstruye el disco perdido).
- **Capacidad neta** = (nº discos − 1) × capacidad del disco más pequeño.
- **El más usado** en la práctica: buen equilibrio capacidad/seguridad/rendimiento. Ejemplo: 4 discos de 1 TB en RAID 5 → 3 TB útiles, tolera 1 fallo.

#### RAID 6

- Como RAID 5, pero con **doble paridad distribuida** (dos bloques de paridad distintos, **P** y **Q**, calculados con algoritmos diferentes).
- Necesita **N+2 discos**, mínimo 4.
- Tolera **2 fallos simultáneos**.
- **Capacidad neta** = (nº discos − 2) × capacidad del disco más pequeño.
- Uso típico: almacenamiento grande donde durante la reconstrucción (rebuild) tras un fallo, un segundo fallo sería catastrófico (discos muy grandes tardan mucho en reconstruirse).

### Niveles anidados (Nested/Hybrid RAID)

Combinan dos niveles RAID en dos capas.

#### RAID 0+1 ("espejo de divisiones")

1. Se crean **dos grupos RAID 0** (cada uno con striping internamente).
2. Se hace un **RAID 1 (espejo)** entre esos dos grupos.

Si falla un disco, **todo su grupo RAID 0 queda inutilizado** (aunque el otro grupo entero sigue funcionando como respaldo).

#### RAID 1+0 / RAID 10 ("división de espejos")

1. Se crean varios **pares RAID 1** (espejos) independientes.
2. Se aplica **RAID 0 (striping)** sobre esos pares.

Si falla un disco, solo se pierde la redundancia de **su pareja concreta**, el resto de pares no se ven afectados. Es más resistente a fallos múltiples que RAID 0+1.

> [!important] Diferencia clave para el examen
> En RAID 10, puedes perder hasta la mitad de los discos (uno de cada pareja) sin perder datos. En RAID 01, perder un disco en cada grupo (2 discos totales, uno por cada mitad) destruye todo el array. **RAID 10 es más robusto**, por eso se prefiere en la práctica.

### JBOD (Just a Bunch Of Disks)

- **No es RAID real** (no aplica ni striping ni redundancia): simplemente concatena varios discos para que el SO los vea como uno solo (como una partición extendida).
- Aprovecha el **100%** de la capacidad de todos los discos, incluso si son de tamaños distintos (no está limitado por el disco más pequeño, a diferencia de RAID).
- **Sin redundancia**: si falla un disco, se pierden solo los datos almacenados físicamente en ese disco (los demás siguen accesibles), a diferencia de RAID 0 donde falla todo el conjunto.

### Cuadro resumen comparativo

| RAID | Mínimo discos | Tolera fallos         | Capacidad neta      | Rendimiento                              |
| ---- | ------------- | --------------------- | ------------------- | ---------------------------------------- |
| 0    | 2             | 0                     | N × menor           | Máximo (lectura/escritura)               |
| 1    | 2             | 1 (por réplica)       | (N × menor)/2       | Buena lectura                            |
| 3    | 3             | 1                     | (N−1) × menor       | Malo con concurrencia                    |
| 4    | 3             | 1                     | (N−1) × menor       | Cuello de botella en paridad             |
| 5    | 3             | 1                     | (N−1) × menor       | Buen equilibrio (el más usado)           |
| 6    | 4             | 2                     | (N−2) × menor       | Como RAID 5, algo más lento en escritura |
| 10   | 4             | varios (1 por pareja) | (N × menor)/2       | Excelente + seguro                       |
| JBOD | 2             | 0 (parcial)           | Suma total de todos | Ninguna mejora                           |

---

## Parte IV — Visualización y digitalización

> [!abstract]
> Cubre el ciclo completo: **entrada de imagen** (escáner), **salida visual** (pantallas) y **salida física** (impresoras), más los buses y estándares de resolución que las conectan al equipo.

### 1. Pantallas

#### CRT (Cathode Ray Tube) — tecnología antigua

Un cañón dispara un **haz de electrones** que golpea una capa de **fósforo**, haciéndola brillar. El haz "barre" la pantalla línea a línea.

**Modos de barrido (Raster Scan)**:

- **Progresivo (p)**: dibuja todas las líneas en orden, de arriba a abajo, en un solo pase. Imagen más nítida y estable (ej. 1080p).
- **Entrelazado (i)**: primero dibuja las líneas **impares**, luego las **pares**, en dos pases. Ahorra ancho de banda pero puede provocar parpadeo (ej. 1080i, formato heredado de la TV analógica).

**Vectorial**: en vez de barrer toda la pantalla, el haz dibuja directamente **líneas/formas** (como un plotter). Se usaba en osciloscopios y algunos arcades antiguos (ej. *Asteroids*), no en TV/monitores comerciales.

#### LCD (Liquid Crystal Display)

Cristal líquido que, al aplicarle voltaje, **bloquea o deja pasar la luz** de una fuente de iluminación trasera. El cristal líquido no emite luz propia → necesita **retroiluminación** (backlight).

#### LED

En rigor, es un LCD cuya retroiluminación usa **diodos LED** en vez de tubos fluorescentes (CCFL, tecnología anterior). Mejor contraste, menor consumo, más delgado. **No es una tecnología de panel distinta a LCD**, sino de iluminación.

#### OLED (Organic LED)

Cada **píxel es su propio diodo emisor de luz** — no necesita retroiluminación. Ventajas: negros perfectos (píxel apagado = negro absoluto), mayor contraste, ángulos de visión mejores. Desventaja: riesgo de *burn-in* (desgaste desigual de píxeles).

> [!tip] Progresión conceptual
> CRT (haz+fósforo) → LCD (cristal líquido + luz externa) → LED (LCD con mejor luz externa) → OLED (cada píxel emite su propia luz, sin luz externa).

#### Interfaces de vídeo

| Interfaz | Detalle |
|---|---|
| **DVI-D** | Solo señal Digital |
| **DVI-I** | Digital + analógica (Integrada) |
| **DVI-A** | Solo Analógica (compatibilidad con VGA) |
| **DisplayPort** (estándar VESA) | Transmite **audio + vídeo** simultáneamente. **v2.0**: soporta hasta **10K** y **60 fps** |

### 2. Escáner

Convierte una imagen física en digital.

- **Fotosensor CCD** (Charge-Coupled Device): sensor que convierte luz en señal eléctrica, línea a línea, según el escáner se desplaza sobre el documento (misma tecnología base usada en cámaras).
- **Resolución**: se mide en **DPI** (Dots Per Inch, puntos por pulgada) — a mayor DPI, más detalle capturado.
- **Profundidad de color/bit depth**: cuántos bits se usan para representar el color de cada punto (ej. 24 bits = ~16,7 millones de colores).
- **OCR** (Optical Character Recognition): software que analiza la imagen escaneada de texto y la convierte en **texto editable**. Ejemplo: escanear un contrato en papel y obtener un .docx editable.
- **Interfaces/protocolos de comunicación escáner-SO**:
  - **TWAIN**: estándar multiplataforma clásico.
  - **ISIS**: alternativa orientada a escáneres profesionales/alto volumen.
  - **WIA** (Windows Image Acquisition): propio de Microsoft.
  - **SANE** (Scanner Access Now Easy): estándar en entornos Linux/Unix.

### 3. Impresión

#### Tecnologías físicas

| Tipo | Mecanismo |
|---|---|
| **Láser** | Un **tambor fotosensible** se carga eléctricamente con el patrón de la imagen (mediante láser); atrae **tóner** (polvo) que luego se funde sobre el papel con calor. Rápida, buena para grandes volúmenes. |
| **Inyección de tinta** | Diminutos inyectores lanzan gotas de tinta líquida directamente sobre el papel. |
| **Impacto** | La imagen se forma por presión física sobre una cinta entintada. Dos variantes: **matricial** (agujas que forman puntos) y **margarita** (rueda con caracteres en relieve, como una máquina de escribir electrónica; obsoleta). |
| **Térmica** | Papel especial sensible al calor que se oscurece al contacto con un cabezal caliente (sin tinta). Ejemplo: tickets de compra. |
| **Sublimación** | Calor transfiere tinta desde una cinta de **4 colores** directamente al papel en estado gaseoso, dando gradientes muy suaves. Usada en impresión fotográfica de alta calidad. |

#### Modelo de color: [[CMYK]]

**C**yan, **M**agenta, **Y**ellow (amarillo), **K**ey/blacK. Modelo **sustractivo** (a diferencia de RGB, que es **aditivo**): parte de un lienzo **blanco** y cada tinta **resta** luz reflejada; mezclar todos los colores tiende al negro (en teoría), por eso se añade K (negro) para negros puros y ahorro de tinta.

> [!important]
> RGB (aditivo, para pantallas que emiten luz) vs CMYK (sustractivo, para impresión sobre superficie que refleja luz) — pregunta clásica de examen.

#### PDL (Page Description Language)

Lenguaje que describe una página completa (texto, gráficos, formato) en comandos que la **impresora interpreta directamente**, en vez de recibir un simple mapa de bits.

| PDL | Fabricante/origen |
|---|---|
| **PostScript** | Adobe |
| **PCL** (Printer Command Language) | HP |
| **XPS** (Open XML Paper Specification) | Microsoft, estandarizado como **ECMA-388** |
| **PDF** | Estandarizado como **ISO 32000-1** |
| **DVI** (DeVice Independent) | Vinculado al sistema de composición de textos **TeX**, usado en ámbito académico/científico |

#### Impresión 3D

- **Formatos de archivo**: **STL** (el más extendido, malla de triángulos), **3MF** (formato moderno de Microsoft, más completo que STL), **VRML** (formato 3D más antiguo, orientado también a realidad virtual).
- **Tecnología más usada**: **extrusión** — **FDM** (Fused Deposition Modeling) / **FFF** (Fused Filament Fabrication), son términos prácticamente equivalentes (FFF es el término "libre de marca" de FDM, que originalmente era una marca registrada de Stratasys).
- **Materiales típicos**:
  - **PLA**: biodegradable, fácil de imprimir, rígido.
  - **ABS**: más resistente y flexible, requiere mayor temperatura, emite gases al fundir.
  - **TPU**: material flexible tipo goma.

### 4. Buses gráficos (evolución cronológica)

| Bus | Estado |
|---|---|
| **PCI** | Obsoleto, bus paralelo genérico compartido |
| **AGP** (Accelerated Graphics Port) | Obsoleto, bus dedicado en exclusiva a la tarjeta gráfica, sucesor de PCI para gráficos |
| **PCI Express (PCIe)** | Actual, bus serie por lanes, el mismo que usan hoy las tarjetas gráficas y SSD NVMe (ver Parte II — Almacenamiento) |

### 5. Resoluciones de pantalla

| Nombre | Resolución |
|---|---|
| SVGA | 800×600 |
| XVGA | 1024×768 |
| 720p (HD) | 1280×720 |
| 1080p (FHD) | 1920×1080 |
| 2K | 2048×1080 |
| QHD | 2560×1440 |
| 4K (UHD) | 3840×2160 |
| 8K (UHD) | 7680×4320 |

> [!tip] Regla mnemotécnica de multiplicadores
> Útil para deducir en examen si no recuerdas el número exacto:
> - 720p × 1,5 = 1080p
> - 720p × 2 = QHD
> - 1080p × 2 = 4K
> - 4K × 2 = 8K
>
> Truco: cada "salto grande" (720p→4K→8K) es una **duplicación de cada dimensión** (ancho y alto), lo que significa **4 veces más píxeles totales**, no el doble.

---

## Parte V — Conectividad

> [!abstract]
> Los buses de conectividad conectan dispositivos externos al equipo. La tendencia histórica es clara: de puertos **especializados y lentos** (FireWire) hacia **buses universales, rápidos y multipropósito** que combinan datos, vídeo y energía en un mismo cable (USB-C, Thunderbolt).

### 1. FireWire (IEEE 1394)

- **Estado**: obsoleto.
- Bus de alta velocidad diseñado para conectar dispositivos digitales que generan mucho flujo de datos continuo: **cámaras y videocámaras** (edición de vídeo en los años 2000).
- Se diferenciaba de USB de su época porque no necesitaba pasar por la CPU para transferir (similar a DMA), y soportaba conexión entre dos dispositivos sin PC intermedio (peer-to-peer).
- Desplazado por USB al hacerse este más rápido y universal.

### 2. Thunderbolt (Light Peak)

Desarrollado originalmente por Intel (con Apple), con el nombre en clave **Light Peak** (pensado inicialmente para fibra óptica, aunque se acabó implementando sobre cobre).

#### Idea clave

Es la **combinación de dos buses en un mismo conector físico**: **PCIe** (para datos de alta velocidad) + **DisplayPort** (para vídeo), transmitidos como **2 señales serie independientes** por el mismo cable. Esto permite enviar datos y vídeo simultáneamente por un solo cable.

#### Características

- **Múltiples protocolos**: soporta encapsular DisplayPort, HDMI y Ethernet dentro de la misma conexión.
- **QoS** (Quality of Service): prioriza tráfico según el tipo (ej. vídeo en tiempo real frente a transferencia de archivo).
- **Bidireccional**: transmite y recibe simultáneamente por el mismo canal.
- **Múltiples dispositivos**: permite encadenar (*daisy-chain*) varios periféricos desde un solo puerto.

#### Versiones

| Versión | Velocidad | Conector |
|---|---|---|
| Thunderbolt 1 | 10 Gbps | mini DisplayPort |
| Thunderbolt 2 | 20 Gbps | mini DisplayPort |
| Thunderbolt 3 | 40 Gbps | **USB Type-C** → compatible con USB 3.1 y superiores |
| Thunderbolt 4 | 40 Gbps | USB Type-C |

> [!important] Dato para examen
> A partir de Thunderbolt 3, el conector pasa a ser físicamente **USB-C**, lo que permite que un mismo puerto USB-C acepte tanto periféricos Thunderbolt como USB normales (aunque no todo puerto USB-C es Thunderbolt).

### 3. [[USB]] (Universal Serial Bus)

No es un único estándar sino una **familia de estándares** gestionada por el **USB-IF** (USB Implementers Forum), el organismo que certifica y define las especificaciones.

- **Tunneling**: capacidad de USB de transportar **otro protocolo** encapsulado dentro de la señal USB (ej. DisplayPort o PCIe), similar en concepto a lo que hace Thunderbolt.
- **Longitud máxima de cable**: 3 metros (limitación física de la señal antes de degradarse).

#### Versiones y velocidades

| Versión | Alias técnico | Velocidad | Energía |
|---|---|---|---|
| USB 3.0 | USB 3.1 Gen 1 | 5 Gbps | 4,5 W |
| USB 3.1 | USB 3.1 Gen 2 | 10 Gbps | hasta 100 W |
| USB 3.2 | — | 20 Gbps | conector Type-C |
| USB 4.0 | — | 40 Gbps (simétrico); **80 Gbps** (generación simétrica mejorada); **120 Gbps** (modo asimétrico) | — |

#### Suministro de energía

- **USB Power Delivery (PD)**: estándar de USB-IF para negociar y entregar más potencia eléctrica a través del cable USB (no solo datos).
- **Quick Charge (QC)**: tecnología equivalente pero propietaria de **Qualcomm**, con función similar a PD.

| Versión PD | Potencia máx. | Conector |
|---|---|---|
| PD 3.0 | hasta 100 W | Type-C |
| PD 3.1 | hasta 240 W | Type-C, mediante **EPR** (Extended Power Range) |

#### USB OTG (On The Go)

Permite que un dispositivo normalmente **esclavo** (ej. un smartphone) actúe como **host/maestro** y controle otro periférico conectado a él.

- **Ejemplo**: conectar un ratón o un pendrive directamente a un móvil Android mediante un adaptador OTG, sin necesidad de un PC de por medio.

### Cuadro comparativo Thunderbolt vs USB

| | Thunderbolt | USB |
|---|---|---|
| Origen | Intel/Apple | USB-IF (consorcio) |
| Combina vídeo+datos | Sí (PCIe + DisplayPort nativo) | Vía tunneling |
| Velocidad máx. actual | 40 Gbps (TB3/4) | 120 Gbps (USB4 asimétrico) |
| Conector actual | USB-C | USB-C |
| Encadenamiento (daisy-chain) | Sí | No (típicamente en estrella vía hubs) |

---

## 🔑 Resumen ultra-rápido (para repaso)

- Interrupción = el periférico avisa a la CPU (vs. polling = la CPU pregunta constantemente).
- Cadena: Controlador (detecta) → IRQ (avisa) → PIC (arbitra y traduce a offset) → CPU (busca ISR en tabla de vectores) → ISR/driver (ejecuta, lee del controlador directamente).
- Offset del teclado = 09H. La PIC no ejecuta nada, solo enruta.
- Sincronización E/S: Polling (CPU pregunta) → Interrupciones (dispositivo avisa) → DMA (transferencia sin pasar por CPU).
- DMA: riesgo de caché desactualizada → cache snooping o flush.
- E/S aislada (puertos IN/OUT, ej. teclado 0x60/0x64) vs MMIO (registros en el espacio de memoria, `MOV` normal).
- Caching = copia para no releer. Buffering = paso intermedio obligatorio. Spooling = cola para dispositivos sin multiplexación (impresoras).
- Almacenamiento óptico: ISO 9660 (+Joliet para nombres largos) → UDF (DVD/Blu-ray). El Torito = especificación de arranque.
- HDD: CHS (físico) vs LBA (lineal, actual). Interfaces: IDE/PATA → SATA (doméstico) / SCSI → SAS (profesional).
- SSD: SLC > MLC > TLC > QLC (a más bits/celda, más barato pero más lento y menos duradero). NVMe va sobre PCIe, mucho más rápido que SATA.
- RAID 0 = velocidad, sin redundancia. RAID 1 = espejo, 50% capacidad. RAID 5 = paridad rotada, el más usado. RAID 6 = doble paridad, tolera 2 fallos. RAID 10 > RAID 01 en resistencia a fallos. JBOD ≠ RAID (sin redundancia ni límite por disco pequeño).
- CRT (haz+fósforo) → LCD (cristal líquido) → LED (LCD con luz LED) → OLED (píxel = su propia luz).
- CMYK (sustractivo, impresión) vs RGB (aditivo, pantallas).
- PDL: PostScript (Adobe), PCL (HP), XPS (Microsoft/ECMA-388), PDF (ISO 32000-1).
- Resoluciones: 720p ×1,5 = 1080p; ×2 = QHD; 1080p ×2 = 4K; 4K ×2 = 8K.
- Conectividad: FireWire (obsoleto) → Thunderbolt (PCIe+DisplayPort combinados, USB-C desde TB3) → USB (universal, con tunneling, PD para energía).
