---
tags:
  - bloque2
  - tema1
  - sistemas-informacion
  - business-intelligence
  - arquitectura-computadores
bloque: 2
tema: 1
titulo: Informática básica
estado: por-repasar
---

# Tema 1 · Bloque 2 — Informática básica

> [!abstract] De qué va este tema
> Dos bloques de contenido bien diferenciados: (1) sistemas de información empresariales y BI/OLAP, y (2) arquitectura interna del computador (CPU, buses, memoria, placa base). No dependen el uno del otro para entenderse, pero ambos son muy preguntables por definiciones cruzadas (ej. "diferencia entre X e Y").

---

## Parte I — Sistemas de información empresariales y BI

### 1. La pirámide de sistemas de información

Clásica pirámide según el nivel de la organización al que sirven. Se explica de abajo a arriba, que es como tiene más sentido lógico: los datos van subiendo y agregándose.

**1. TPS (Transaction Processing System)** — base de la pirámide
- Nivel operativo, el día a día.
- Registra transacciones: ventas, nóminas, pedidos, entradas/salidas de almacén.
- Volumen alto, datos muy detallados y en tiempo real.
- Ejemplo: el TPC de un supermercado registrando cada venta en caja.

**2. MIS (Management Information System)** — mandos intermedios
- Coge los datos del TPS y los convierte en **informes periódicos y estructurados** (ventas del mes, stock semanal...).
- Ayuda a controlar que todo funciona bien, pero con preguntas ya predefinidas ("dame el informe de ventas").
- Power BI encaja aquí como herramienta típica de reporting.

**3. DSS (Decision Support System)** — nivel táctico
- Decisiones no tan estructuradas ni repetitivas.
- Aquí entra **OLAP**: analizar datos desde múltiples dimensiones (producto, región, tiempo...) haciendo drill-down, roll-up, etc.
- Responde a preguntas tipo "¿qué pasaría si...?" (simulaciones).
- Corto plazo, pero ya con capacidad de análisis, no solo informes fijos.

**4. EIS (Executive Information System)** — cúspide, alta dirección
- Datos muy resumidos: cuadros de mando (dashboards), KPIs.
- Aquí puede entrar Machine Learning para predicciones a largo plazo.
- Preguntas tipo "¿hacia dónde va la empresa?".

> [!important] Idea clave para el examen
> A medida que subes en la pirámide (TPS → MIS → DSS → EIS): **baja el volumen de datos** pero **sube el nivel de agregación y abstracción**, y pasas de operaciones repetitivas (TPS) a decisiones estratégicas poco estructuradas (EIS).

### 2. BI y Data Mining

- **BI (Business Intelligence)**: conjunto de estrategias/herramientas para transformar datos en conocimiento útil para la toma de decisiones. Es el "paraguas" que engloba todo lo demás.
- **Data Mining (minería de datos)**: técnica concreta para extraer patrones y conocimiento oculto de grandes volúmenes de datos, usando redes neuronales, árboles de decisión, clustering, estadística...
- **Data Warehouse (DWH)**: el origen habitual de los datos. Almacén de datos históricos, integrados y orientados a análisis — a diferencia de las BBDD transaccionales, orientadas a operación.
- Power BI se conecta al DWH, entiende su estructura (normalmente modelo en estrella o copo de nieve) y genera los informes/cuadros de mando.

### 3. Cubos OLAP

Forma de representar datos multidimensionalmente para análisis rápido.

- **Tabla de hechos**: los datos numéricos/medibles (ventas, importes) → la "foto" resumen.
- **Tablas de dimensión**: los ejes por los que puedes cortar esa foto (tiempo, geografía, cliente, producto...).

**Variantes de OLAP:**

| Tipo | Significado |
|---|---|
| MOLAP | Multidimensional (cubos precalculados, muy rápido) |
| ROLAP | Relacional (usa BBDD relacional por debajo) |
| HOLAP | Híbrido (mezcla de los dos anteriores) |
| WOLAP | Web (acceso vía navegador) |
| RTOLAP | Real Time |
| SOLAP | Espacial (datos geográficos) |
| DOLAP | Desktop (local, para un usuario) |

### 4. MDX

Lenguaje para consultar cubos OLAP, igual que SQL consulta tablas relacionales, pero pensado para moverte en varias dimensiones a la vez.

### 5. Operaciones OLAP

- **Drill down** ↓ más detalle (ej: de año → trimestre → mes).
- **Drill up / Roll up** ↑ menos detalle (agregas hacia arriba).
- **Slice**: fijas un valor de **una** dimensión → obtienes un subcubo (una "loncha").
- **Dice**: filtras por **varias** dimensiones a la vez → subcubo más pequeño y específico.
- **Pivot (rotar)**: cambias qué dimensiones van en filas/columnas para ver el informe desde otro ángulo.

> [!tip] Truco mnemotécnico
> Slice = 1 corte (una dimensión). Dice = varios cortes, como dados, varias caras/dimensiones.

---

## Parte II — Arquitectura de computadores

### 1. Componentes principales de la CPU

- **Unidad de Control (UC)**: el "director de orquesta". Busca instrucciones, las decodifica y coordina qué hace cada parte de la CPU. No calcula nada, solo gobierna.
- **ALU (Unidad Aritmético-Lógica)**: la "calculadora". Suma, resta, AND, OR, desplazamientos de bits... Ejecuta lo que la UC le manda.
- **Decodificador**: traduce el código máquina (binario) a una señal que la CPU entiende como "qué operación hay que hacer".
- **Secuenciador**: el que dispara la ejecución paso a paso de la instrucción ya decodificada.

> [!note] Orden lógico
> Fetch → Decodificador → Secuenciador → (ALU si hace falta)

### 2. [[Reloj]]

- Todo va **síncrono**, a golpe de reloj.
- **Reloj externo**: sincroniza la CPU con la placa base (bus, RAM...).
- **Reloj interno**: más rápido, es un múltiplo del externo (factor multiplicador).
- **Overclocking**: subir ese factor multiplicador → la CPU va más rápido, pero genera más calor/inestabilidad.

### 3. [[Buses]] (las "carreteras" de datos)

| Bus         | Función                                             |
| ----------- | --------------------------------------------------- |
| Control     | Dice si es lectura o escritura                      |
| Direcciones | Dice **dónde** (qué dirección de RAM)               |
| Datos       | Transporta **qué** (la instrucción o el dato en sí) |

> [!tip] Truco
> Direcciones = dónde. Datos = qué.

### 4. [[Registros clave]]

- **MAR** (Memory Address Register): guarda la dirección de memoria a la que se va a acceder.
- **MDR** (Memory Data Register): guarda el dato que se lee/escribe de esa dirección.
- **AC** (Acumulador): guarda resultados intermedios de operaciones.
- **PC** (Program Counter) / Instruction Pointer en Intel: dirección de la **siguiente** instrucción.
- **IR / CIR** (Instruction Register): la instrucción **actual**, ya traída de memoria.
- **Flags**: banderas de estado (cero, acarreo, paridad...) que indican el resultado de la última operación.

> [!important] Diferencia PC vs IR
> PC apunta a lo que viene. IR contiene lo que se está ejecutando ahora mismo.

### 5. Ciclo de ejecución: Fetch – Decode – Execute – (Store)

1. **Fetch**: la UC pide a la RAM la instrucción señalada por el PC → llega y se guarda en el **IR**.
2. **Decode**: el IR pasa por el decodificador, que interpreta qué operación es.
3. **Execute**: el secuenciador la ejecuta, usando la ALU si la operación lo requiere.
4. **Store** (opcional): si hay resultado, se guarda (en registro o memoria).

Después de esto, el PC se actualiza para apuntar a la siguiente instrucción, y el ciclo se repite.

### 6. [[CISC vs RISC]]

La CPU puede seguir dos enfoques de diseño:

- **CISC**: instrucciones complejas, varios ciclos de reloj, lógica programada (microcódigo), típico de Intel.
- **RISC**: instrucciones simples de un solo ciclo, tamaño fijo, pocos modos de direccionamiento, lógica cableada, menor consumo, típico de ARM.

Para ganar velocidad — especialmente en RISC, por tener instrucciones simples y de tamaño fijo — se recurre a la técnica de **pipeline** (ver sección 8).

| | CISC | RISC |
|---|---|---|
| Instrucciones | Complejas, varios ciclos de reloj | Simples, 1 ciclo de reloj |
| Lógica | Programada (microcódigo) | Cableada (hardware) |
| Modos direccionamiento | Muchos | Pocos |
| Tamaño instrucción | Variable | Fijo |
| Consumo/temperatura | Mayor | Menor |
| Ejemplo | Intel (x86) | ARM |

- **RISC-V**: estándar RISC **abierto** → cualquiera puede diseñar su propio procesador sin pagar licencias.
- **Arduino**: hardware y software libre (licencia GPL) para democratizar el acceso a la computación. No es lo mismo que RISC-V, pero comparte la filosofía de "abierto/libre".

> [!important] Idea clave
> CISC hace más "en una sola instrucción" (más trabajo para el hardware). RISC simplifica cada instrucción pero se apoya en ejecutar muchas más, muy rápido — por eso combina tan bien con pipeline.

### 7. SoC vs APU

- **SoC** (System on a Chip): todo integrado en un solo chip → CPU, GPU, RAM, controladores... (típico en móviles).
- **APU**: caso más concreto, solo **CPU + GPU** en el mismo chip (típico AMD).

> [!important]
> SoC es más amplio que APU.

### 8. [[Pipeline]] (segmentación)

- El Fetch (ir a buscar a memoria) es el paso más lento del ciclo.
- Solución: mientras se hace el Fetch de una instrucción, ya se puede estar Decodificando la anterior, Ejecutando la anterior a esa, etc. → trabajo en cadena, como una fábrica.
- Muy típico en RISC porque, al tener instrucciones de tamaño fijo y simples, es más fácil solapar las fases.

### 9. [[Modos de direccionamiento]]

Formas que tiene una instrucción de máquina de indicarle a la CPU dónde se encuentra el operando (el dato) con el que tiene que trabajar: cómo se calcula o se obtiene la dirección de memoria (o el valor) que va a usar la operación.

No todas las instrucciones necesitan el dato de la misma manera: a veces el propio código de operación ya deja claro implícitamente de dónde sacarlo (implícito), otras veces el dato viaja incluido en la propia instrucción sin necesidad de ir a buscarlo a ningún sitio (inmediato), otras veces la instrucción indica directamente la dirección de memoria donde está el dato (directo o absoluto), y en los casos más complejos la instrucción apunta a una dirección que a su vez contiene otra dirección, siendo esta última la que finalmente señala dónde está el dato real (indirecto).

Cuantos más modos de direccionamiento soporta un procesador, más flexible es a la hora de acceder a memoria, pero también más compleja resulta su circuitería — por eso CISC suele tener muchos modos y RISC muy pocos, priorizando la simplicidad y velocidad.

| Modo                 | ¿Dónde está el dato?                                                                               | Ejemplo       |
| -------------------- | -------------------------------------------------------------------------------------------------- | ------------- |
| **Implícito**        | Ya se sabe por la propia operación (ej: pop de una pila)                                           | `top()`       |
| **Inmediato**        | El dato viene **dentro** de la instrucción, no hay que ir a buscarlo                               | `MOV AX, 12`  |
| **Directo/Absoluto** | La instrucción da la **dirección de memoria** donde está el dato                                   | `MOV A, 17H`  |
| **Indirecto**        | La instrucción da una dirección, y **en esa dirección hay otra dirección** donde está el dato real | (doble salto) |

> [!tip] Truco para recordarlo
> Cada modo añade un "salto" más hasta llegar al dato real: Inmediato = 0 saltos (el dato ya está ahí). Directo = 1 salto (voy a la dirección y ahí está el dato). Indirecto = 2 saltos (voy a la dirección, ahí hay otra dirección, y ahí sí está el dato).

### 10. Arquitectura de 64 bits

- El tamaño/ancho de la palabra es lo que marca la arquitectura. El tamaño de la palabra es de 64 bits.
- 64 bits es el tamaño de los registros de la [[CPU - Central Processing Unit]]. El [[Bus de datos]] de datos es de 64 bits.
- La memoria se divide en posiciones, y en cada posición se almacena una palabra.
- Las instrucciones de código máquina son de 64 bits: por eso no funciona un Windows de 64 bits en un procesador de 32 bits, pero sí al revés.
- El bus de direcciones es de 48 bits. Con 48 bits podemos direccionar 256 TB.

### 11. [[Placa base]]

**Placa base**: vía de comunicación entre los componentes (microprocesador, tarjetas de expansión, memoria, etc.), proporcionando las líneas eléctricas necesarias y las señales de control para que todas las transferencias de datos se lleven a cabo de manera rápida y fiable.

- El **chipset** es un ayudante de la CPU: circuitería auxiliar.
  - **Northbridge** (Chipset Norte): cosas rápidas, como acceder a la memoria.
  - **Southbridge** (Chipset Sur): cosas lentas, como la E/S.
- **FSB** (Front-Side Bus): el bus principal, hasta hace unos años. La velocidad se la da el reloj del sistema. Es la manera de llegar a la memoria principal; principalmente lleva datos. Ahora se elimina y se sustituye por:
  - Intel: **QPI** (QuickPath Interconnect) y **DMI** (Direct Media Interface, conexión entre Chipset Norte y Sur).
  - AMD: **HyperTransport**.
- La **caché de nivel 1** está dentro de la CPU, dividida en dos (datos e instrucciones) — similar a la arquitectura Harvard con la memoria principal.
  - Caché L1 y L2: por cada núcleo/core del procesador.
  - Caché L3: compartida por todos los núcleos.
- **PCI** y **PCI-Express**: tarjetas de expansión (gráficas, de red, etc.).
- **NVRAM** (de la placa): necesita una pila para mantener fecha, hora y configuración.

|                  | [[BIOS]]                  | [[UEFI]]                              |
| ---------------- | ------------------------- | ------------------------------------- |
| Nombre           | Basic Input Output System | Unified Extensible Firmware Interface |
| Interfaz         | Modo carácter             | Gráfica                               |
| Particionamiento | MBR (hasta 4 particiones) | GPT (más de 4 particiones)            |

### 12. Memoria

**Jerarquía de memorias según velocidad (de más a menos rápida):**

Registros → Caché → Memoria Principal → Resto

- **Memoria caché**: es de tipo SRAM. Trabaja a nivel de **bloque**, no de celda. Estructura: etiqueta, bloque y metadatos.
- **Asignación**: directa (función mod), asociativa (recorre el bloque preguntando) o mixta.
- **Política de sustitución**: FIFO, LRU, LFU, etc.
- **Política de actualización**:
  - *Write through* (escritura directa): al modificar la caché se modifica también la memoria principal.
  - *Write back* (escritura diferida): se escribe en memoria principal solo cuando ese bloque va a salir de caché, para no perder la información.

**Tipos de memoria:**

| Tipo | Descripción |
|---|---|
| ROM | Solo lectura |
| EPROM | Se puede actualizar con luz UV |
| EEPROM | Se puede borrar eléctricamente |
| SRAM | No necesita refresco de voltaje → más rápida (ahorra ciclos de reloj en refrescos) |
| DRAM | Dinámica. Necesita refresco de voltaje |
| SDRAM | DRAM síncrona. Es la habitual |
| DDR SDRAM | Double Data Rate: escribe en ciclos de subida y de bajada, doblando la velocidad |
| NVRAM | RAM no volátil, alimentada por una batería |
| GDDR | Memoria para la tarjeta gráfica |
| LPDDR | Memoria para dispositivos móviles (Low Power) |

- **Encapsulado DIMM**: contactos separados a ambos lados.
- **SO-DIMM**: para ordenadores portátiles.

> [!example] Cálculo DDR-400
> Bus de 200 MHz. 200 × 2 × 8 B (64 bits) = 3200 MB/s → de ahí el nombre comercial **PC-3200** (máxima capacidad de transferencia).

**Latencias en memorias RAM**: hay varios tipos, según la fase de acceso. Lo importante para el examen es el total, hasta obtener el dato.

| Latencia  | Qué mide                                      |
| --------- | --------------------------------------------- |
| RAS       | Tiempo en colocarse sobre una fila            |
| CAS       | Tiempo en colocarse sobre una columna o celda |
| ACTIVE    | Tiempo en activar un tablero                  |
| PRECHARGE | Tiempo en desactivar un tablero               |

> [!important]
> El tiempo que tarda la memoria en proporcionar el dato es la suma de **ACTIVE + RAS + CAS**.

---

## 🔑 Resumen ultra-rápido (para repaso)

- Pirámide SI: TPS (operativo) → MIS (informes) → DSS (OLAP, análisis) → EIS (dashboards, ML). Sube abstracción, baja volumen.
- BI = paraguas. Data Mining = técnica de extracción de patrones. DWH = origen de los datos.
- OLAP: tabla de hechos + tablas de dimensión. Slice = 1 dimensión, Dice = varias.
- CPU: UC gobierna, ALU calcula, Decodificador traduce, Secuenciador ejecuta paso a paso.
- Ciclo: Fetch (a IR) → Decode → Execute → Store.
- PC = siguiente instrucción. IR = instrucción actual.
- CISC = complejo/microcódigo/Intel. RISC = simple/cableado/ARM/pipeline.
- Modos direccionamiento = nº de "saltos" hasta el dato: inmediato (0) → directo (1) → indirecto (2).
- Northbridge = rápido (memoria). Southbridge = lento (E/S).
- Jerarquía memoria: Registros > Caché > Memoria Principal > Resto.
- Write through = inmediato. Write back = diferido (al salir de caché).
- BIOS = MBR/carácter. UEFI = GPT/gráfico.
- Latencia total RAM = ACTIVE + RAS + CAS.
