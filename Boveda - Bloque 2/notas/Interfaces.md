**¿Qué es una interfaz aquí?**  
Es el **sistema de conexión** entre el disco y el ordenador: el conjunto de **cable + conector + reglas** (protocolo) que define cómo viajan los datos entre ambos. Es literalmente **el idioma y el camino físico** por el que el disco habla con la [[Placa base]]. 

**Paralelo vs Serie (la clave de toda la evolución)**

- **Paralelo:** manda **muchos bits a la vez**, cada uno por su propio hilo (por eso los cables son anchos, con muchos hilos). Suena mejor, pero a alta velocidad los bits de los distintos hilos se **desincronizan** y se estorban entre sí. Es un callejón sin salida.
- **Serie:** manda los bits **de uno en uno**, pero **rapidísimo**, por muy pocos hilos. Al no tener que sincronizar varios hilos, puede ir a frecuencias mucho más altas. Gana el serie, y por eso toda la evolución va de paralelo → serie.

Con eso, la tabla se lee sola:

**[[PATA (Parallel ATA)]] — paralelo, obsoleta**  
La vieja escuela. Cable ancho y plano (40 u 80 hilos), y solo **2 dispositivos por cable**, que tenían que repartirse los papeles de **master y slave** (uno mandaba, otro secundario). Lenta y aparatosa. Ya no se usa.

**[[SCSI (Small Computer System Interface)]] ("escasi") — paralelo, para servidores**  
Más ambiciosa: un **bus** al que se conectaban de **7 a 15 dispositivos**, cada uno identificado por un **ID único** (como un DNI dentro del bus). Era cara y robusta, típica de **servidores** de la época. Piensa en ella como la versión "profesional" del paralelo.

**[[SATA (Serial ATA)]] — serie, el estándar de consumo**  
La sucesora de PATA, ya en **serie**. Cable finito, **un dispositivo por cable** (adiós al lío de master/slave), más rápida y ordenada. Es la que llevan los PCs y portátiles normales. Su techo de velocidad es más bajo que SAS/NVMe porque está **pensada para consumo doméstico**, no para exprimir al máximo.

**[[SAS (Serial Attached SCSI)]] — serie, la evolución profesional**  
Aquí está el truco elegante: coge el **cerebro lógico de SCSI** (su forma de gestionar muchos dispositivos) pero le pone **transmisión serie** moderna. Lo mejor de los dos mundos. Cambia el ID numérico por un **[[WWN (World Wide Name)]]**, un identificador único de 64 bits (como una matrícula mundial irrepetible), y con **expansores** puede manejar una barbaridad de dispositivos (**hasta 16.384** por dominio). Es la interfaz de **servidores y centros de datos** actuales.

> [!note] Detalle a fondo de cada una
> Esta nota es la narrativa que las conecta. Los datos duros (tablas de velocidades, cifras exactas) están en la nota dedicada de cada interfaz: [[PATA (Parallel ATA)]], [[SATA (Serial ATA)]], [[SCSI (Small Computer System Interface)]], [[SAS (Serial Attached SCSI)]].

**El hilo conductor para retenerlo:**

> Todo evoluciona de **paralelo → serie**. En consumo: **PATA → SATA**. En profesional/servidor: **SCSI → SAS**. Y SAS es especial porque conserva la "inteligencia" de SCSI pero con la velocidad del serie.

**[[NVMe (Non-Volatile Memory Express)]]**, que es el escalón siguiente (pensado para SSDs, conecta directo por PCIe y deja atrás en velocidad a todas estas). Pero eso ya es otro capítulo si te interesa.