El Bus de comunicación es una línea o conjunto de líneas en los sistemas digitales que conecta varios dispositivos entre sí para permitir el intercambio de información. Estas líneas transportan los datos, junto con las señales necesarias para coordinar la transferencia, siguiendo un protocolo que define cómo emisor y receptor deben entenderse. Es uno de los elementos fundamentales del sistema y también en la conexión con el exterior: permite que los distintos componentes (procesador, memoria, periféricos) se transmitan información de forma ordenada y sincronizada. Es una vía **compartida** que interconecta y da servicio a múltiples dispositivos.

> [!note] Esta es la nota "teoría general" de los buses
> El índice de qué bus concreto corresponde a cada caso está en **[[Buses]]**.

## Los tres ejes de clasificación

Un mismo bus se puede describir por tres clasificaciones independientes entre sí:

| Eje | Opciones |
|---|---|
| Nº de bits a la vez | **Serie** (uno a uno) vs **Paralelo** (varios a la vez) |
| Coordinación temporal | **Síncrono** (reloj común) vs **Asíncrono** (marcas de inicio/fin, sin reloj compartido) |
| Alcance | **Interno** (dentro del equipo) vs **Externo** (conecta dispositivos fuera del equipo) |

### Serie vs Paralelo

La **comunicación en serie** envía los bits uno tras otro por una sola línea de datos, lo que reduce el número de conductores y las interferencias, permitiendo mayores distancias y velocidades a frecuencias altas. Las instrucciones y señales de control gestionan el flujo para que los datos lleguen en el orden correcto.

La **comunicación en paralelo** usa varias líneas simultáneas para enviar varios bits a la vez, transfiriendo un conjunto completo de bits en un solo ciclo mediante un bus ancho dedicado. Principalmente en buses internos antiguos como PCI o el bus ISA (ver [[Buses de expansión internos (ISA, PCI, AGP)]]) se usaba este método.

> [!important] Por qué gana el serie a alta velocidad
> El paralelo tiene mayor velocidad de transferencia en distancias cortas (varios bits por ciclo), y sistemas serie son más simples al necesitar menos conductores. Pero a frecuencias altas los hilos de un bus paralelo se **desincronizan** entre sí y se interfieren — un callejón sin salida. El serie, al no tener que sincronizar varios hilos, puede subir mucho más la frecuencia. Por eso casi toda la evolución de interfaces va de paralelo a serie.

- **[[PATA (Parallel ATA)]]**, también conocido como IDE, es un bus de comunicación **paralelo** e interno. Fue el estándar dominante durante muchos años para conectar discos duros y lectores de CD/DVD. Transmite varios bits simultáneamente a través de un cable ancho y plano (de 40 u 80 hilos). Su principal limitación es que la transmisión paralela genera interferencias a altas velocidades y en cables largos, lo que acabó frenando su desarrollo. Hoy está prácticamente obsoleto.
- **[[SATA (Serial ATA)]]** es el sucesor de PATA y es un bus de comunicación **serie** e interno. Sustituyó al PATA precisamente porque la transmisión serie permite mayores velocidades, cables más finos y largos, y mejor ventilación dentro del equipo. Es bidireccional, admite conexión y desconexión en caliente (*hot-plug*) y es el estándar más común hoy en día para conectar discos duros y SSD en computadoras de consumo.
- **[[SAS (Serial Attached SCSI)]]** es también un bus de comunicación **serie**, pero orientado al ámbito **profesional y empresarial** (servidores, centros de datos). Es compatible físicamente con SATA (un controlador SAS puede usar discos SATA, pero no al revés), y ofrece mayor fiabilidad, velocidad, y la posibilidad de conectar muchos más dispositivos. Está diseñado para entornos que requieren alto rendimiento y funcionamiento continuo.

### Síncrono vs Asíncrono

Para poder coordinar a los dispositivos, el bus debe reservar líneas o tiempos para las señales de control y sincronización, no solo para los datos. Esta gestión puede ser controlada por un reloj común (**comunicación síncrona**, como en I2C o SPI) o basada en marcas de inicio y fin sin reloj compartido (**comunicación asíncrona**, como en UART). Cada dispositivo conectado al bus monitoriza las líneas y responde solo cuando reconoce que la transmisión va dirigida a él, mediante una dirección o identificador propio.

### Interno vs Externo

Un dispositivo de acceso directo a memoria (DMA) también hace uso del bus de comunicación, especialmente para la transferencia masiva de datos. Esto es porque, por definición, [[DMA]] aprovecha el bus para mover información entre memoria y dispositivo evitando la intervención continua de la CPU.

Los **buses externos** como [[USB]] son otro tipo de comunicación entre [[CPU - Central Processing Unit]] y [[Periféricos]]. No obstante, se tratan separadamente por múltiples razones: permiten la conexión de dispositivos externos, en oposición a los buses internos; suelen ser bidireccionales, pues la información puede fluir en ambos sentidos entre el dispositivo y la CPU; y cada bus externo lleva consigo su propio protocolo con la intención de gestionar la conexión, identificación y transferencia de los dispositivos conectados.

## 🔑 Resumen ultra-rápido

- Bus = vía compartida que interconecta varios dispositivos, con protocolo propio de coordinación.
- Serie (un hilo, rápido a alta frecuencia) vs Paralelo (varios hilos, se desincronizan a alta frecuencia) → el serie gana la carrera histórica.
- Síncrono (reloj común, ej. I2C/SPI) vs Asíncrono (marcas de inicio/fin, ej. UART).
- Interno (CPU-placa) vs Externo (USB y similares, con su propio protocolo de conexión/identificación).
- PATA (paralelo) → SATA (serie); SCSI (paralelo) → SAS (serie): mismo patrón repetido en las dos familias de almacenamiento.

---

**Conexiones con otros conceptos TAI:**
- [[Buses]] — índice general de todos los buses del temario.
- [[Bus de dirección]], [[Bus de datos]], [[Bus de control]] — el trío interno de la CPU.
- [[PATA (Parallel ATA)]], [[SATA (Serial ATA)]], [[SCSI (Small Computer System Interface)]], [[SAS (Serial Attached SCSI)]] — ejemplos concretos de esta clasificación aplicados al almacenamiento.
- [[USB]], [[Thunderbolt]], [[FireWire (IEEE 1394)]] — ejemplos de buses externos.
- [[DMA]] — usuario intensivo del bus de comunicación para transferencias masivas.
