**Buffering simple:** se usa un único buffer. Mientras se llena con datos nuevos, no se puede vaciar a la vez, así que hay que esperar a que se procese antes de volver a llenarlo. Es lo más sencillo, pero puede generar esperas.

**Buffering doble (double buffering):** se usan dos buffers alternándolos. Mientras uno se está vaciando (procesando), el otro se va llenando con datos nuevos. Cuando terminan, intercambian los papeles. Así casi nunca hay que esperar y el flujo es más continuo (es la técnica típica en gráficos para evitar parpadeos en pantalla).

**Buffer circular (circular/ring buffer):** un buffer tratado como si fuera un anillo: cuando se llega al final, se vuelve al principio. Tiene un puntero que indica dónde se escribe y otro dónde se lee, persiguiéndose el uno al otro. Es muy útil para flujos continuos de datos (audio, streaming, teclado), porque permite escribir y leer al mismo tiempo sin reorganizar nada.

[[Técnicas de gestión de datos en memoria intermedia]]
[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]] (la función Hash usa buffers circulares)