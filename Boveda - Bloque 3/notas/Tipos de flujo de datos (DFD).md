Un flujo de datos en un [[DFD - Diagrama de Flujo de Datos|DFD]] se puede clasificar por dos criterios independientes, más un tipo especial que no es un flujo de datos normal:

**Según qué operación hace sobre el almacén:**
- **Consulta**: solo lectura, no modifica datos.
- **Actualización**: solo escritura (crear/modificar/borrar), no necesita leer antes.
- **Diálogo**: lectura y escritura combinadas (lees el dato, lo procesas y lo vuelves a guardar).

**Según cómo se ejecuta en el tiempo:**
- **Síncrono**: ocurre directamente entre dos procesos, sin pasar por un almacén; un proceso le pasa el dato al siguiente de forma inmediata (como una llamada a función).
- **Asíncrono**: interviene un almacén de por medio; un proceso escribe y en algún momento posterior otro proceso lo lee. El almacén "desacopla" en el tiempo a los dos procesos.

**Proceso/Flujo de control (evento)**: un enlace especial entre dos procesos que actúa como disparador — cuando el proceso A termina (o se cumple una condición), se dispara automáticamente el proceso B, sin que medie un flujo de datos normal. Es la forma de modelar la asincronía por eventos, no por almacenamiento. Ej: al terminar "Confirmar Pedido" se dispara automáticamente "Enviar Notificación", pasando solo el "aviso", no un dato de negocio.

> [!note]
> No confundir Asíncrono (vía almacén) con Flujo de control (vía evento): ambos desacoplan procesos en el tiempo, pero el asíncrono mueve un dato real a través de un almacén, mientras que el flujo de control solo dispara la ejecución sin transportar un dato de negocio.

[[B3 - T1.1 ENTIDAD RELACION]]
