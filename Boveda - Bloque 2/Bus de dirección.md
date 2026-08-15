El Bus de dirección es una línea de comunicación en los sistemas digitales que conecta varios dispositivos. Esta línea contiene información sobre la dirección de memoria que se necesita para acceder a los datos o instrucciones almacenados en la memoria. Es uno de los principales buses del sistema, junto al [[Bus de datos]] y el [[Bus de control]] (ver [[Buses]]). Su función principal es permitir que el procesador ([[CPU - Central Processing Unit]]) indique qué dirección de memoria desea leer o escribir. Es un mapa de memoria que selecciona los dispositivos de E/S conectados como [[Periféricos]].

## Dos formas de que la CPU hable con un dispositivo

[[E-S mapeada en memoria]] y [[E-S aislada]] (o independiente) son dos métodos de implementar entradas/salidas entre los periféricos y la CPU. Otro método, que no pasa por ninguno de los dos, es [[DMA]].

| Método | Espacio de direcciones | Instrucción de acceso |
|---|---|---|
| **E/S mapeada en memoria** | Mismo bus de direcciones para memoria y dispositivos | `MOV` normal, la misma que para acceder a memoria |
| **E/S aislada** | Espacio separado de la memoria (puertos) | Instrucciones especiales (`IN`/`OUT` en Intel) |
| **DMA** | No aplica — el dispositivo transfiere directamente con la RAM | La CPU no interviene en el movimiento de datos |

- La **E/S mapeada en memoria** usa el mismo bus de direcciones para memoria y dispositivos de E/S: las instrucciones de la CPU usadas para acceder a la memoria son también usadas para acceder a los dispositivos. Para tener espacio para los dispositivos de E/S, las áreas del espacio direccionable por la CPU deben reservarse para E/S en vez de para memoria. Esta reserva puede ser temporal (el Commodore 64 podía conmutar entre el banco de dispositivos de E/S y un banco de memoria) o permanente. Cada dispositivo de E/S monitoriza el bus de direcciones de la CPU y responde a cualquier acceso de esta al espacio de direcciones del dispositivo, conectando el bus de datos con la localización en memoria física del dispositivo deseado.
- La **E/S aislada o independiente** usa un tipo especial de instrucciones de la CPU para implementar E/S. Principalmente en microprocesadores Intel encontramos las instrucciones `IN` y `OUT`, que pueden leer y escribir un único byte en un dispositivo de E/S. Tienen un espacio de direcciones separado de la memoria, llevado a cabo o bien por un "pin de E/S" extra en la CPU o bien por un bus entero dedicado a E/S.
- Un dispositivo de acceso directo a memoria ([[DMA]]) no se ve afectado por estos dos métodos de comunicación CPU-dispositivo, especialmente por la E/S mapeada en memoria: por definición, DMA es un método de comunicación memoria-dispositivo que evita a la CPU.

> [!important] Trade-off entre los dos métodos
> El uso de **E/S independiente** facilita la protección de E/S y los programas son más rápidos, al tener una decodificación más sencilla y un tamaño menor las instrucciones de E/S. La ventaja de la **E/S mapeada** es la menor complejidad a la hora de diseñar el procesador, ya que no distingue entre accesos a memoria y accesos a dispositivos de E/S — con el coste de "robarle" espacio de direcciones a la memoria.

## Y las interrupciones, ¿por qué no cuentan aquí?

Las [[Interrupciones]] hardware son otro método de comunicación entre CPU y [[Periféricos]], pero se tratan siempre por separado por dos razones: es un mecanismo **iniciado por el dispositivo** (en oposición a los tres de arriba, iniciados por la CPU), y es **unidireccional** — la información fluye solo del dispositivo hacia la CPU, y cada interrupción lleva consigo solo un bit de información, con la única intención de notificar el aviso.

---

**Conexiones con otros conceptos TAI:**
- [[Bus de datos]] y [[Bus de control]] — los otros dos buses del trío clásico.
- [[E-S mapeada en memoria]] y [[E-S aislada]] — desarrollo completo de cada método, con ejemplos (teclado, framebuffer de la tarjeta gráfica).
- [[DMA]] e [[Interrupciones]] — los métodos que no dependen del bus de direcciones de la misma forma.
- [[CPU - Central Processing Unit]] y [[Periféricos]] — los dos extremos que este bus conecta.
