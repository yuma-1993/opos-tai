**La idea central: hay dos "mundos" separados**

Imagina que la [[CPU - Central Processing Unit]] tiene dos libretas de direcciones distintas:
- Una para la **memoria** (la [[Memoria RAM]]).
- Otra para los **dispositivos** (teclado, ratón, etc.).

Son mundos separados. La dirección número 0x60 de la memoria **no** es lo mismo que el puerto número 0x60 de los dispositivos. Aunque el número sea igual, apuntan a sitios diferentes, como si tuvieras la casa "nº 60 de la Calle Memoria" y la casa "nº 60 de la Calle Dispositivos": mismo número, calles distintas.

**¿Cómo habla la CPU con cada mundo?**
Aquí está la clave: la CPU usa **palabras distintas** para dirigirse a cada uno.
- Para hablar con la memoria usa la instrucción normal: `MOV`.
- Para hablar con los dispositivos usa instrucciones especiales: `IN` (para leer) y `OUT` (para escribir).

Si la CPU intenta usar `MOV` para hablar con un dispositivo, no funciona. Es como intentar abrir una puerta con la llave equivocada. Para los dispositivos, **sí o sí** tienes que usar `IN` y `OUT`.

**¿Qué es un "puerto"?**
Un puerto es simplemente un **número que identifica una ventanilla** por la que hablas con un dispositivo. Cada dispositivo tiene sus ventanillas con su número.

**El ejemplo del teclado (así lo entiendes de golpe)**
El teclado tiene dos ventanillas:

- **Puerto 0x60 → la ventanilla de datos.** Por aquí sale el código de la tecla que has pulsado (el famoso _scancode_, un número que representa esa tecla).
- **Puerto 0x64 → la ventanilla de estado.** Por aquí la CPU pregunta cosas como "¿hay alguna tecla lista para recoger?" o "¿esto es una tecla o es un comando?".

**Cómo funciona en la práctica, paso a paso:**
1. La CPU mira por la ventanilla de estado (`IN` desde el puerto 0x64) y pregunta: "¿hay algo?".
2. Si la respuesta es "sí, hay una tecla lista", entonces la CPU va a la ventanilla de datos (`IN` desde el puerto 0x60) y recoge el código de la tecla.
3. Ya tiene el dato y puede procesarlo.

Y eso es todo. Resumido en una frase:
> Los datos del teclado viajan por unos **puertos numerados** (0x60 y 0x64), que son ventanillas de un mundo aparte de la memoria, y la CPU solo puede asomarse a ellas usando las instrucciones especiales `IN` y `OUT`, nunca con el `MOV` de siempre.