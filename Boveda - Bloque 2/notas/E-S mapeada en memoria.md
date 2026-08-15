**La idea central: aquí hay un solo "mundo"**
Los dispositivos se meten dentro del mismo mapa de direcciones que la [[Memoria RAM]]. Es como si al dispositivo le dieras una casa **en la misma calle** que la memoria. Ya no hay "Calle Memoria" y "Calle Dispositivos" por separado: todo está en la misma calle, con números que no se repiten.

**¿Cómo habla la CPU con el dispositivo ahora?**
Como el dispositivo ya vive en la calle de la memoria, la CPU le habla **igual que a la memoria**. Con la instrucción normal de siempre: `MOV`.

Ya no hacen falta las instrucciones especiales `IN` y `OUT`. La CPU no nota la diferencia: para ella, escribir en un dispositivo es como escribir en una casilla de RAM cualquiera. Escribe en una dirección y, sin saberlo, en realidad le está mandando datos al dispositivo.

**El ejemplo de la tarjeta gráfica**
Este es el caso típico. La tarjeta gráfica tiene una zona de memoria llamada _framebuffer_, que es básicamente **la imagen que se ve en la pantalla, guardada como datos**. Cada posición corresponde a un punto (píxel) de la pantalla.

Con el mapeo en memoria, esa zona aparece como si fuera un trozo más de la RAM. Entonces, para dibujar en pantalla, la CPU solo tiene que hacer `MOV` a esas direcciones, como si estuviera escribiendo en memoria normal. Escribe ahí un color → aparece ese color en el píxel correspondiente de la pantalla.

**¿Por qué se usa esto para mover muchos datos?**
Porque es **más simple y más rápido**, por dos razones:
- Puedes usar **cualquier** instrucción de acceso a memoria, no solo `IN`/`OUT`. Y la CPU tiene un montón de instrucciones potentes para trabajar con memoria (copiar bloques enteros de golpe, por ejemplo). Todo ese arsenal queda disponible para hablar con el dispositivo.
- No tienes que ir dato a dato por una ventanilla estrecha; puedes tratar la zona del dispositivo como una gran extensión de memoria y volcar datos en cantidad.

Por eso es ideal para dispositivos que mueven **muchísima** información, como una tarjeta gráfica que tiene que refrescar millones de píxeles constantemente.

**Resumido en una frase:**
> En el mapeo en memoria, el dispositivo se coloca dentro del mismo mapa que la RAM, así que la CPU le escribe y le lee con el `MOV` de siempre, sin instrucciones especiales; es más simple y rápido, y por eso se usa en cosas que mueven muchos datos, como la tarjeta gráfica.

**El contraste con la [[E-S aislada]], en una línea:**
- **Puertos de E/S (lo de antes):** mundo aparte, ventanillas numeradas, instrucciones especiales `IN`/`OUT`.
- **Mapeado en memoria (esto):** mismo mundo que la RAM, se accede con el `MOV` normal.