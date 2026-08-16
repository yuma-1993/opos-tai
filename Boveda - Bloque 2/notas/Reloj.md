El reloj es una señal eléctrica periódica (una alternancia constante entre dos niveles de voltaje, 0/1) que marca el ritmo al que se ejecuta todo dentro del ordenador. **Todo va síncrono**: cada componente da un paso cuando el reloj se lo marca, no cuando le apetece.

> [!note] Por qué hace falta ir síncrono (conocimiento general, no literal de la fuente)
> Si cada componente trabajara a su propio ritmo, dos piezas podrían intentar leer/escribir el mismo dato a la vez y producir resultados inconsistentes (una condición de carrera). Sincronizar todo contra la misma señal de reloj garantiza que cuando un componente vaya a leer un dato, el que lo escribe ya ha tenido tiempo de dejarlo listo.
>
> La velocidad del reloj se mide en **Hz** (ciclos por segundo); un reloj de 3 GHz da 3.000 millones de "golpes" por segundo, y en cada uno la CPU puede avanzar un paso de su ciclo de ejecución.

## Reloj externo vs reloj interno

- **Reloj externo**: sincroniza la CPU con el resto de la placa base (bus, RAM...). Es la señal que llega desde fuera del procesador.
- **Reloj interno**: el que usa el propio núcleo de la CPU para funcionar, **más rápido** que el externo — es un **múltiplo** de él (el llamado *factor multiplicador*).

> [!example] Cómo se relacionan
> Si el reloj externo va a 100 MHz y el multiplicador es ×36, el reloj interno de la CPU corre a 3.600 MHz (3,6 GHz). El componente que impone ese reloj externo históricamente era el **FSB** (Front-Side Bus, ver [[B2 - T1 INFORMATICA BASICA]]), hoy sustituido por enlaces como QPI/DMI (Intel) o HyperTransport (AMD).

## Overclocking

Subir el factor multiplicador (o directamente el reloj base) **por encima** de lo que especifica el fabricante → la CPU ejecuta más ciclos por segundo → va más rápido.

> [!important] El precio del overclocking
> Un transistor consume y disipa más calor cuantas más veces conmuta por segundo. Subir la frecuencia por encima de spec dispara ese calor y puede llevar a la CPU a una zona donde el fabricante ya no garantiza que cada conmutación sea fiable → de ahí el riesgo de **inestabilidad** (cuelgues, cálculos erróneos) si no se compensa con mejor refrigeración.

> [!note] Overclocking vs Turbo Boost — no confundir (conocimiento general)
> El **Turbo Boost/Turbo Core** de las CPU modernas también sube la frecuencia por encima del reloj base, pero lo hace el propio procesador de forma **automática y dentro de los márgenes que el fabricante sí garantiza** (cuando hay margen térmico y pocos núcleos activos). El **overclocking** es manual y va **más allá** de esos márgenes garantizados, por eso conlleva riesgo y puede anular la garantía.

## Reloj del sistema vs reloj de tiempo real (RTC)

> [!important] Dos "relojes" distintos, trampa clásica de examen
> El reloj de esta nota (el que marca ciclos por segundo) **no es el mismo** que el reloj que mantiene la **fecha y hora** del equipo. Ese segundo reloj es el **RTC** (Real-Time Clock), alojado en la [[Placa base]] junto a la **NVRAM/CMOS**, alimentado por una pila para seguir funcionando aunque el equipo esté apagado (ver la NVRAM de placa en [[B2 - T1 INFORMATICA BASICA]]). Uno cuenta ciclos de ejecución a miles de millones por segundo; el otro cuenta segundos de calendario.

## Conexión con la memoria: por qué DDR existe gracias al reloj

El reloj no solo marca el ritmo de la CPU: la [[Memoria RAM]] aprovecha directamente su forma de onda. La DDR hace **dos** operaciones por cada ciclo (una en el flanco de subida, otra en el de bajada) precisamente porque el reloj no es un pulso instantáneo, sino una señal con dos transiciones aprovechables por ciclo.

## 🔑 Resumen ultra-rápido

- Reloj = señal periódica que sincroniza todo el sistema; evita que los componentes pisen datos a destiempo.
- Reloj externo (sincroniza CPU-placa) vs reloj interno (más rápido, múltiplo del externo vía el factor multiplicador).
- Overclocking = subir el multiplicador/reloj base por encima de spec → más velocidad, más calor, riesgo de inestabilidad.
- Turbo Boost ≠ overclocking: el primero es automático y dentro de spec; el segundo es manual y fuera de spec.
- Reloj del sistema (ciclos/segundo) ≠ RTC (fecha/hora, vive en la NVRAM/CMOS de la placa con pila propia).
- La DDR de la RAM existe porque aprovecha los dos flancos (subida y bajada) del mismo ciclo de reloj.

---

**Conexiones con otros conceptos TAI:**
- [[B2 - T1 INFORMATICA BASICA]] — FSB/QPI/DMI/HyperTransport como el bus que transporta la señal de reloj externo, y la NVRAM de placa que respalda el RTC.
- [[Memoria RAM]] — SDR vs DDR se explica directamente por los flancos de la señal de reloj.
- [[CPU - Central Processing Unit]] — el multiplicador de reloj y el overclocking afectan directamente al consumo/calor que el diseño multi-núcleo ya tiene que arbitrar.
