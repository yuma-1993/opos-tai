---
tags:
  - bloque2
  - tema1
  - sistemas-informacion
  - business-intelligence
  - arquitectura-computadores
  - representacion-informacion
bloque: 2
tema: 1
titulo: Informática básica
estado: por-repasar
---

# Tema 1 · Bloque 2 — Informática básica

> [!abstract] De qué va este tema
> Tres bloques de contenido diferenciados: (1) sistemas de información empresariales y BI/OLAP, (2) representación de la información (sistemas de numeración, signo, coma flotante, errores, codificación de caracteres) y (3) arquitectura interna del computador (CPU, buses, memoria, placa base, rendimiento). No dependen unos de otros para entenderse, pero todos son muy preguntables por definiciones cruzadas (ej. "diferencia entre X e Y"). Contrastada con el PDF original de Carlos Velilla el 2026-10-19.

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

> [!note] Precisión del PDF sobre Slice/Dice
> Slice: selecciona **una** dimensión y da un nuevo subcubo. Dice: selecciona **2 o más** dimensiones de un cubo y da un nuevo subcubo.

### 6. ETL: cómo llegan los datos al DWH

- El **DWH** recibe y consolida los datos de los **TPS** mediante herramientas **ETL** (*Extract, Transform and Load*).
- En Java, **Kettle** es un ETL integrado en la suite **Pentaho Data Integration (PDI)**.
- En Microsoft: **SQL Server Integration Services (SSIS)**.
- Flujo completo: TPS → ETL → DWH → (cubos OLAP / Data Mining / BI) → informes.

> [!note] Clasificación de los sistemas según el PDF
> **DSS/OLAP** y **MIS** corresponden a la parte **analítica**, y eso lleva a Data Mining / BI. El PDF los caracteriza así: **EIS** estratégico (largo/medio plazo; usa ML, estadística, cuadros de mando); **DSS** táctico (corto plazo; también OLAP); **MIS** especializado en generar informes (Power BI); **TPS** procesos diarios de transacciones (sistemas transaccionales). Mediante redes neuronales, estadística, árboles de decisión, etc. se extrae información del Data Warehouse.

---

## Parte II — Representación de la información

> [!abstract] De qué va esta parte
> Cómo se codifica la información en binario: unidades, sistemas de numeración, signo, coma flotante, detección de errores, compresión y codificación de caracteres. Es la parte más "calculable" del tema y la más susceptible de ejercicios.

### 1. Sistema binario: unidades y códigos

| Unidad | Tamaño |
|---|---|
| **Bit** | Unidad mínima |
| **Crumb** | 2 bits |
| **Nibble** | 4 bits |
| **Byte** | 8 bits |

**Códigos para dígitos decimales:**

| Código | Cómo funciona | Ejemplo: decimal 16 |
|---|---|---|
| **BCD (8421)** | *Dígito decimal Codificado en Binario*: usa 4 bits para codificar cada dígito de forma independiente | `0001 0110` |
| **AIKEN (2421)** | Tiene una tabla propia de equivalencia | `0001 1100` |
| **Exceso a 3 (XS-3)** | Cada dígito se representa con 4 bits **más 3** (exceso) | 0 = 0000 + 0011 = `0011`; 8 = 1000 + 0011 = `1011` |

**Múltiplos: Sistema Internacional vs ISO/IEC 80000-13**

| Sistema Internacional (potencias de 10) | | ISO/IEC 80000-13 (potencias de 2) | |
|---|---|---|---|
| 10³ = 1000 | KB Kilobyte | 2¹⁰ = 1024 | KiB Kibibyte |
| 10⁶ | MB Megabyte | 2²⁰ | MiB Mebibyte |
| 10⁹ | GB Gigabyte | 2³⁰ | GiB Gibibyte |
| 10¹² | TB Terabyte | 2⁴⁰ | TiB Tebibyte |
| 10¹⁵ | PB Petabyte | 2⁵⁰ | PiB Pebibyte |
| 10¹⁸ | EB Exabyte | 2⁶⁰ | EiB Exbibyte |
| 10²¹ | ZB Zettabyte | 2⁷⁰ | ZiB Zebibyte |
| 10²⁴ | YB Yottabyte | 2⁸⁰ | YiB Yobibyte |
| 10²⁷ | RB Ronnabyte | 2⁹⁰ | RiB Robibyte |
| 10³⁰ | QB Quettabyte | 2¹⁰⁰ | QiB Quebibyte |

> [!important] KB ≠ KiB
> Un **KB ya no son 1024 B, sino 1000 B** en el Sistema Internacional. El **1024** se ha quedado en el estándar **ISO/IEC** (KiB).

### 2. Sistemas de numeración

| Sistema | Dígitos | Ejemplo |
|---|---|---|
| Decimal | 0–9 | 429₁₀ |
| Binario | 0–1 | 010010₂ |
| Hexadecimal | 0–9, A–F | AF30101ₕ |
| Octal | 0–7 | 73010₈ |

**Fórmula para pasar cualquier número de cualquier base a decimal:**

> Decimal = Σ dᵢ × bⁱ (para i = 0 hasta N−1), donde **i** = posición del dígito (desde la derecha, empezando en 0), **d** = dígito, **b** = base. Es decir: *dígito × base elevada al índice*.

> [!example] Ejemplos de conversión a decimal
> - 101₂ = 1×2⁰ + 0×2¹ + 1×2² = 1 + 0 + 4 = **5**
> - 238₈ → **Error**: no existe el dígito 8 en octal.
> - 231₈ = 1×8⁰ + 3×8¹ + 2×8² = 1 + 24 + 128 = **153**

**Conversiones entre bases:**

- **Binario → Hexadecimal**: separar en bloques de **4** bits. `00011001` → `0001-1001` = 1-9 = **19**.
- **Binario → Octal**: separar en bloques de **3** bits.
- **Decimal → Hexadecimal**: dividir entre 16, o pasar a binario y de binario a hexadecimal.
- **Decimal → Binario**: dividir entre 2 (o a mano usando los pesos, "la cuenta de la vieja"). Se divide entre 2 hasta el final y se ordena **desde el último cociente hasta el primer resto**. Ejemplo: 100₁₀ = 1100100₂.

### 3. Base64

- Es más un **sistema de codificación** que de números. **Ocupa un 33 % más.**
- **PEM** es un formato de exportación de datos codificado en Base64.
- Hacen falta **6 bits** para codificar 64 caracteres: `A-Z`, `a-z`, `0-9`, `+`, `/`.
- Se cogen grupos de 6 en 6 bits **empezando por la izquierda**.
- `=` es el relleno o *pad*: 1 o 2 como máximo, para rellenar el grupo de la derecha. `=` ≈ `00`.

> [!example] Ejemplo del PDF: "Ma" en Base64
> Octetos: M = 77 (0x4d), a = 97 (0x61) → bits `01001101 01100001` → grupos de 6 bits: `010011` `010110` `0001` + `00` de relleno → sextetos **19, 22, 4** + padding → caracteres **T, W, E, =**.

### 4. Representación del signo

- **Signo-módulo**: bit de signo + valor absoluto del número. **0 = +; 1 = −**.
- **CA1 (complemento a 1)**: para obtener el negativo se intercambian los 0 por 1 y los 1 por 0. Rango de **7 a −7** (4 bits). **Doble valor del 0**: `0000` y `1111`.
- **CA2 (complemento a 2)**: se calcula el CA1 y se **suma 1**. Rango de **7 a −8**. **Los números en Java se representan internamente con CA2.**

| | Rango (4 bits) | Ceros |
|---|---|---|
| CA1 | 7 a −7 | Dos (`0000` y `1111`) |
| CA2 | 7 a −8 | Uno |

### 5. Coma flotante: IEEE 754

| Precisión | Total | Signo | Exponente | Mantisa |
|---|---|---|---|---|
| Simple | 32 bits | 1 | 8 | 23 |
| Doble | 64 bits | 1 | 11 | 52 |

> [!example] Ejemplo resuelto del PDF: 263,3 en precisión simple
> 1. **Parte entera**: 263 → dividiendo entre 2 = `100000111`.
> 2. **Parte decimal**: 0,3 → se multiplica por 2 repetidamente (0,3×2 = 0,6; 0,6×2 = 1,2; 0,2×2 = 0,4; 0,4×2 = 0,8; 0,8×2 = 1,6; 0,6×2 = 1,2…) hasta llegar a decimal 0 o detectar un periodo → `01001` (con periodo `1001`).
> 3. `100000111,01001…` → notación científica → `1,0000011101001… × 2⁸`.
> 4. **Signo**: 0. **Exponente**: exponente + 127 = 8 + 127 = 135 = `10000111`.
> 5. **Resultado**: `0 10000111 00000111010011001100110`.

> [!important] Sesgo
> En precisión simple el exponente se almacena **sesgado (+127)**.

### 6. Detección (y corrección) de errores

| Técnica | Qué hace |
|---|---|
| **Bit de paridad** | Estrategia par o impar. Pasa de 7 a 8 bits añadiendo 1 bit al final. Busca que el conjunto final tenga un nº par o impar de 1s |
| **CRC** | Verificación por redundancia cíclica |
| **Golay** | Detección y corrección de errores |
| **Gray** | Detección y corrección de errores. Se basa en que dos datos consecutivos solo se diferencian en **1 bit** |
| **Reed-Solomon** | Detección y corrección de errores |
| **Hadamard** | Detección y corrección de errores |
| **Hamming** | Detección y corrección de errores |
| **Checksum** | Suma de verificación. Función matemática de redundancia para detectar errores en una transmisión. **Asegura la integridad** |
| **Hash** | Algoritmo matemático que transforma un bloque de datos en una nueva serie de caracteres de **longitud fija**. **Asegura la integridad** |

### 7. Compresión de datos sin pérdida

- **Código Huffman**: usado en la creación de ficheros **gzip**.

### 8. Codificación de caracteres

**ISO 10646** es el Conjunto de Caracteres Universal (**UCS**). En Windows, Latin-1 es el **Windows-1252**.

| Código | Características |
|---|---|
| **ASCII** | 7 bits + 1 de paridad. 32–126: imprimibles; 0–31 y 127: no imprimibles. No tiene €, ni Ñ, ni letras con tilde. **A = 65** |
| **EBCDIC** | 8 bits. Mainframe de IBM. Cada país tenía su tabla; cada tabla de caracteres se llama **Codepage** |
| **ISO 8859-1** (Latin-1) | 8 bits de verdad. Tiene Ñ y tildes, pero **no tiene €**. **ISO-8859-15** incorpora el €. A = 65 |
| **UTF-8** | *8-bit Unicode Transformation Format*. Mínimo 8 bits. **Longitud variable 1–4 bytes**. Los de 1 byte coinciden con ASCII; el resto son los más raros |
| **UTF-16** | Mínimo 16 bits. **Longitud variable de 2–4 bytes**: 1 o 2 palabras de 16 bits (cada palabra son 2 bytes) |

### 9. Operaciones lógicas

| A | B | AND (A ∧ B) | OR (A ∨ B) | XOR (A ⊕ B) |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

### 10. ISO 8601: fecha y hora

Formato internacional para representar el tiempo en **horas-minutos-segundos** o las fechas en **año-mes-día**.

- **Hora UTC** (Tiempo Universal Coordinado): carácter **"Z"**.
- **Hora local**: carácter **"T"** (según el PDF).
- **Semana**: carácter **"W"**.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> En un formato como `2026-10-19T14:30:00Z`, la **T** separa la fecha de la hora y la **Z** indica que la hora es UTC.

---

## Parte III — Arquitectura de computadores

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

### 13. Von Neumann vs Harvard (y el cúbit)

- **Bit**: unidad básica de información en la computación **clásica**. **Cúbit** (bit cuántico): unidad básica de información en la computación **cuántica**.

| Arquitectura | Memoria |
|---|---|
| **Von Neumann** | **Una única memoria** para instrucciones y datos |
| **Harvard** | **Memoria separada** para instrucciones y datos. Mejor seguridad y rendimiento |

### 14. Medidas de rendimiento de una computadora

| Medida | Significado | Qué indica |
|---|---|---|
| **MIPS** | Millones de Instrucciones Por Segundo | **Potencia** de un procesador |
| **MFLOPS** | Millones de Operaciones en Coma Flotante Por Segundo | **Rendimiento** del procesador |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> MIPS cuenta cualquier instrucción, y no todas hacen el mismo trabajo, así que no es comparable entre arquitecturas distintas (CISC frente a RISC). MFLOPS solo cuenta operaciones en coma flotante: más comparable, pero válido solo para cargas de cálculo. Múltiplos: GFLOPS (10⁹), TFLOPS (10¹²), PFLOPS (10¹⁵). Ninguna de las dos es la frecuencia de reloj (GHz).

### 15. Taxonomía de Flinn

Clasificación de la arquitectura de computadores en función de las **instrucciones (I)** y los **datos (D)**: **SISD, SIMD, MISD, MIMD**.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> S = *Single*, M = *Multiple*. SISD: una instrucción sobre un dato (CPU secuencial clásica). SIMD: una instrucción sobre muchos datos (vectorial, GPU). MISD: varias instrucciones sobre un mismo dato (rara). MIMD: varias instrucciones sobre varios datos (multinúcleo, clústeres).

### 16. Direcciones lógicas (virtuales) vs físicas

- La **MMU** (gestor de memoria) traduce las **direcciones virtuales** en **direcciones físicas**.
- La **TLB** es la tabla de traducción que usa la MMU.

> [!note] Más detalle
> Memoria virtual, paginación y fallos de página están en [[B2 - T4.1 SISTEMAS OPERATIVOS]].

### 17. Virtualización a nivel de CPU

Soporte hardware a nivel de CPU para dar capacidad de virtualización: **Intel VT-x** y **AMD-V**.

### 18. Ejercicios resueltos del PDF

> [!example] Ejercicio 1: capacidad de una memoria
> *¿Capacidad en KB de una memoria con 1024 posiciones y palabras de 16 bits?*
> - 1024 posiciones → bus de direcciones de **10 bits**.
> - En cada posición se almacena una **palabra**.
> - 1024 × 2 bytes = 2048 bytes = **2 KB**.

> [!example] Ejercicio 2: caracteres que caben en la memoria
> *Computadora con 36 Kpalabras de memoria principal, palabras de 32 bits. ¿Cuántos caracteres de 8 bits caben?*
> - Tamaño de memoria = 36 Kpalabras × 32 bits/palabra.
> - Nº de caracteres = (36K × 32) / 8.
> - (Cálculo final, no resuelto en el PDF: 36K × 4 = 144K caracteres = 147 456, tomando K = 1024.)

> [!example] Ejercicio 3: tamaño máximo de fichero con inodos
> *Dispositivo dividido en bloques de 4 KB, dirección de bloque de 64 bits. Cada inodo tiene 12 punteros directos, 1 indirecto simple y 1 indirecto doble. Tamaño máximo aproximado de los ficheros.*
> - Bloque (de datos o de índices) = 4 KB. Dirección de un bloque = 64 bits = 8 bytes.
> - Entradas por bloque de índices = 4 KB / 8 B = 2¹² / 2³ = 2⁹ = **512**.
> - Tamaño máximo = 12 × 4 KB + 512 × 4 KB + 512 × 512 × 4 KB = 12 × 2¹² + 2⁹ × 2¹² + 2⁹ × 2⁹ × 2¹² = 12 × 4 KB + 2²¹ + 2³⁰ ≈ **1 GB**.

> [!example] Ejercicio 4: memoria virtual
> *Computador de 32 bits, páginas de 16 KB, memoria principal de 1 GB.* (1 KB = 2¹⁰, 1 MB = 2²⁰, 1 GB = 2³⁰). Página = 16 KB = 2¹⁴ → **14 bits** de desplazamiento.
> - a) **Formato de la dirección virtual**: nº de página (**18** bits) + desplazamiento (**14** bits).
> - b) **Nº máximo de páginas**: 2¹⁸.
> - c) **Nº de marcos de página**: 2³⁰ / 2¹⁴ = 2¹⁶.
> - d) **Bloque transferido** entre disco y memoria principal en un fallo de página: **16 KB** (una página).
> - e) **Genera el fallo de página y quién lo trata**: la **MMU**.

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
- ETL (Extract, Transform, Load) lleva los datos de los TPS al DWH. Kettle/PDI (Java), SSIS (Microsoft).
- Unidades: crumb 2 bits, nibble 4, byte 8. KB = 1000 B (SI); KiB = 1024 B (ISO/IEC 80000-13).
- BCD (8421), Aiken (2421), Exceso a 3 (+3). Octal: 0–7 (el 8 no existe). Bin→Hex bloques de 4; Bin→Oct bloques de 3.
- Base64: 6 bits por carácter, +33 % de tamaño, `=` = padding (1 o 2). PEM usa Base64.
- CA1: 7 a −7, doble cero. CA2: 7 a −8 (CA1 + 1); Java usa CA2.
- IEEE 754: simple 1+8+23 bits (sesgo +127), doble 1+11+52.
- Detectan/corrigen: Hamming, Golay, Reed-Solomon, Hadamard, Gray (1 bit de diferencia). Integridad: checksum y hash. Huffman → gzip.
- ASCII 7 bits (A = 65). ISO 8859-1 sin €, 8859-15 con €. UTF-8 1–4 bytes, UTF-16 2–4 bytes. EBCDIC = IBM.
- ISO 8601: Z = UTC, T = hora local (según el PDF), W = semana.
- Von Neumann = memoria única. Harvard = datos e instrucciones separados. Cúbit = bit cuántico.
- MIPS = millones de instrucciones/s (potencia). MFLOPS = millones de operaciones en coma flotante/s (rendimiento).
- Flinn: SISD, SIMD, MISD, MIMD. MMU traduce virtual→física (TLB). Virtualización CPU: Intel VT-x, AMD-V.
