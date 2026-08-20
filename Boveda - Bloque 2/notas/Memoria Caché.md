La memoria caché es una memoria muy pequeña instalada dentro del propio microprocesador, de tipo **SRAM** (Static RAM). Es mucho más cara de fabricar que la RAM normal, pero no necesita refrescarse constantemente para conservar los datos — por eso es de acceso rapidísimo. Se encarga de almacenar temporalmente los datos e instrucciones que se utilizan con mayor frecuencia.

> [!note] Diferencia con las notas relacionadas
> Por qué la caché es SRAM (y no DRAM) está en [[Memoria RAM]]. Dónde vive físicamente (por núcleo, compartida) está también en [[Placa base]]. Las políticas de sustitución (FIFO/LRU/LFU) y de actualización (write-through/write-back) están en [[B2 - T1 INFORMATICA BASICA]] §12. Esta nota se centra en **cómo se decide qué va en la caché** (funciones de correspondencia) y en **los niveles y tipos de caché** que existen más allá de la CPU.

## Funciones de correspondencia: ¿dónde va cada bloque?

Cuando un bloque de la memoria principal (Mp) tiene que entrar en la caché (Mc), hace falta una regla que decida **en qué línea de la caché** se coloca. Hay tres:

| Función | Regla | Analogía |
|---|---|---|
| **Directa** | Un bloque de Mp solo puede ubicarse en **una** línea concreta de Mc: la que coincide al superponer Mc sobre Mp respetando las fronteras de Mc (es decir, sobre posiciones de Mp que son múltiplos del tamaño de Mc) | Taquillas numeradas: tu número de bloque decide, por resto de una división, en qué taquilla exacta te toca |
| **Asociativa** | Un bloque puede ubicarse en **cualquier** línea de Mc | Aparcas donde haya hueco libre; para encontrar el coche luego, hay que mirar plaza por plaza |
| **Asociativa por conjuntos** | Compromiso entre las dos anteriores: la caché se divide en conjuntos, un bloque va a un conjunto fijo (como en la directa) pero dentro de él puede ocupar cualquier línea (como en la asociativa) | Taquillas agrupadas por planta fija, pero libres dentro de su planta |

> [!tip] Por qué existe la versión "por conjuntos"
> La directa es rápida de buscar pero rígida (dos bloques que caen en la misma línea se pisan aunque el resto de la caché esté vacío). La asociativa es flexible pero cara de buscar (hay que comparar contra todas las líneas). La asociativa por conjuntos reparte la diferencia: suficiente flexibilidad, búsqueda razonable.

## Tipos de caché (no solo la de la CPU)

La caché es una técnica general (ver [[Caching]]), no exclusiva del procesador. Es un sistema especial de almacenamiento de alta velocidad, que puede ser tanto un área reservada de la memoria principal como un dispositivo independiente:

| Tipo | Qué hace |
|---|---|
| **Caché de disco** | Porción de RAM asociada a un disco ([[HDD (Hard Disk Drive)]] o [[SSD (Solid State Drive)]]) que guarda datos recientemente leídos, para agilizar la carga si se vuelven a pedir. Acceder a un byte en RAM puede ser miles de veces más rápido que acceder a un byte en disco. |
| **Caché de pista** | Memoria de estado sólido tipo RAM, de uso casi exclusivo en supercomputadoras por su coste elevado. |
| **Caché web** | Almacena documentos web para reducir ancho de banda, carga de servidores y retraso de descargas. Tres variantes: **privada** (un solo usuario), **compartida** (sirve a varios usuarios) y **pasarela** (a cargo del propio servidor original, transparente para los clientes). |

## Inclusivo vs exclusivo

Los datos se alojan en distintos niveles de caché según la frecuencia de uso, y pueden transferirse entre niveles de dos formas:

| Modo | Qué pasa con la copia de origen |
|---|---|
| **Inclusivo** | Se mantiene una copia en dos o más niveles a la vez |
| **Exclusivo** | Se elimina del nivel de origen en cuanto se transfiere al nuevo nivel |

## Niveles L1, L2 y L3

- **L1** (memoria interna): dentro del núcleo del microprocesador, el nivel con menor tiempo de respuesta. Se divide en dos subniveles: **Data Cache** (datos de uso frecuente) e **Instruction Cache** (instrucciones de uso frecuente) — la misma separación datos/instrucciones que la arquitectura Harvard.
- **L2**: mayor que L1 pero más lenta (aunque sigue siendo mucho más rápida que la RAM). Puede ser inclusiva (copia de L1 + información extra) o exclusiva (contenido totalmente distinto de L1), lo que en ese segundo caso da más capacidad total efectiva.
- **L3**: más rápida que la RAM pero más lenta que L1/L2; la de mayor capacidad de las tres. Agiliza el acceso a datos e instrucciones que no se encontraron en L1 ni L2. Igual que L2, puede ser inclusiva o exclusiva respecto al nivel anterior.

> [!important] Por núcleo vs compartida
> L1 y L2 existen **una por cada núcleo** del procesador. L3 es **compartida** por todos los núcleos — ver [[Placa base]] y [[CPU - Central Processing Unit]] para cómo encaja esto con el diseño multi-núcleo.

![[_attachments/cache-L1-L2-L3-pediaa.png]]
*Resumen visual de L1 vs L2 vs L3 (tabla comparativa externa, pediaa.com) — confirma en formato tabla lo ya descrito arriba: L1 más pequeña/rápida/interna al núcleo, L3 más grande/lenta/compartida.*

## 🔑 Resumen ultra-rápido

- Caché = SRAM, dentro/cerca de la CPU, sin refresco, cara pero rapidísima.
- Correspondencia: Directa (una línea fija, rápida pero rígida) / Asociativa (cualquier línea, flexible pero cara de buscar) / Por conjuntos (compromiso).
- No solo existe la caché de CPU: también de disco, de pista (supercomputadoras) y web (privada/compartida/pasarela).
- Inclusivo = copia en varios niveles a la vez. Exclusivo = se borra del nivel de origen al subir de nivel.
- L1 (por núcleo, dividida en datos/instrucciones) → L2 (por núcleo, mayor y más lenta) → L3 (compartida, la mayor y más lenta de las tres, pero sigue ganando a la RAM).

---

**Conexiones con otros conceptos TAI:**
- [[Jerarquía de memoria]] — dónde encaja la caché entre los registros y la RAM.
- [[Memoria RAM]] — por qué la caché es SRAM y no DRAM.
- [[Placa base]] y [[CPU - Central Processing Unit]] — ubicación física y relación con el diseño multi-núcleo.
- [[B2 - T1 INFORMATICA BASICA]] — políticas de sustitución y actualización (FIFO/LRU/LFU, write-through/write-back).
- [[Caching]] — la técnica general de la que la caché de CPU es un caso particular.
- [[HDD (Hard Disk Drive)]], [[SSD (Solid State Drive)]] — beneficiarios de la caché de disco.
- [[B2 - T5 NOSQL Y BIG DATA]] — REDIS se usa como caché de 1er nivel: la misma idea de acceso rapidísimo en memoria, llevada al modelo clave-valor de NoSQL.
- [[Redis]] — nota dedicada al producto NoSQL que ejemplifica este uso como caché de 1er nivel.

- [[B2 - T4.1 SISTEMAS OPERATIVOS]] — la TLB de la MMU aplica el mismo principio de caché a la tabla de páginas.
