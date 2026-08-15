El bus de control no transporta datos ni direcciones: transporta **órdenes** sobre qué hacer con lo que ya circula por el [[Bus de datos]] y el [[Bus de dirección]]. Es el tercer bus del trío clásico (ver [[Buses]]).

> [!important] Sin bus de control, los otros dos buses son ambiguos
> Si la CPU pone una dirección en el bus de direcciones y un valor en el bus de datos, **nadie sabe si eso es una lectura o una escritura** sin una señal aparte que lo indique. Esa señal —y otras como ella— es el trabajo del bus de control.

Señales típicas que viajan por él:

- **Lectura/Escritura (R/W)**: indica si la operación en curso es leer de memoria/dispositivo o escribir en él.
- **Sincronismo**: señales ligadas al [[Reloj]] que marcan cuándo es válido el dato que hay en el bus.
- **Petición de interrupción**: la vía por la que un controlador dispara una IRQ hacia la CPU (ver [[IRQ - Interrupt Request]], [[PIC - Programmable Interrupt Controller]]).
- **Petición/concesión de bus (bus request/grant)**: mecanismo de arbitraje que decide quién tiene el control del bus en cada momento — lo usa un controlador [[DMA]] para "pedir prestado" el bus y transferir datos sin la CPU, y es el mismo tipo de problema que resuelve el arbitraje entre núcleos descrito en [[CPU - Central Processing Unit]].

> [!tip] Un bus, tres preguntas
> Dirección = **dónde**. Datos = **qué**. Control = **qué hacer con ello y quién manda ahora mismo**.

---

**Conexiones con otros conceptos TAI:**
- [[Bus de dirección]] y [[Bus de datos]] — los otros dos buses del trío clásico.
- [[Reloj]] — el sincronismo que viaja por el bus de control depende directamente de la señal de reloj.
- [[DMA]] y [[PIC - Programmable Interrupt Controller]] — ambos dependen de señales del bus de control (petición de bus, petición de interrupción).
- [[CPU - Central Processing Unit]] — el arbitraje de bus entre núcleos es el mismo problema de fondo que el arbitraje de IRQ.
