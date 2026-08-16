El bus de datos es la línea (o conjunto de líneas) por la que viaja **el dato en sí**: la instrucción o el valor que la CPU lee o escribe. Es, junto al [[Bus de dirección]] y el [[Bus de control]], uno de los tres buses internos que forman el modelo clásico de comunicación de la CPU (ver [[Buses]]).

> [!tip] Truco para no confundirlo con el bus de dirección
> **Dirección = dónde. Datos = qué.** El bus de direcciones dice en qué casilla de memoria hay que mirar; el bus de datos es lo que realmente entra o sale de esa casilla.

- **Bidireccional**: a diferencia del bus de direcciones (que normalmente solo viaja en un sentido, de la CPU hacia la memoria/periférico, indicando dónde), el bus de datos transporta información **en ambos sentidos**: la CPU puede escribir en memoria (dato sale de la CPU) o leer de ella (dato entra a la CPU).
- **Anchura = tamaño de palabra**: el número de líneas físicas del bus de datos determina cuántos bits se mueven **a la vez**, en un mismo ciclo. Esa anchura coincide con el tamaño de palabra de la arquitectura: una CPU de 64 bits tiene un bus de datos de 64 bits (ver arquitectura de 64 bits en [[B2 - T1 INFORMATICA BASICA]]).
- Cuanto más ancho el bus, más datos por ciclo, pero también más líneas físicas y circuitería necesaria — la misma tensión entre paralelo y serie que aparece en [[Bus de comunicación]].

> [!example] El bus de datos también decide la velocidad de la RAM
> El cálculo de DDR-400/PC-3200 en [[Memoria RAM]] multiplica la frecuencia por el ancho del canal en bytes (8 B = 64 bits): el ancho del bus de datos es, literalmente, uno de los tres factores de esa cuenta.

---

**Conexiones con otros conceptos TAI:**
- [[Bus de dirección]] y [[Bus de control]] — los otros dos buses del trío clásico.
- [[Buses]] — nota índice de todos los buses del temario.
- [[B2 - T1 INFORMATICA BASICA]] — arquitectura de 64 bits, tamaño de palabra.
- [[Memoria RAM]] — el ancho del bus de datos como factor en la velocidad de transferencia (DDR-400/PC-3200).
