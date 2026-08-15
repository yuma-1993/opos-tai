Es un dispositivo de almacenamiento que guarda los datos de forma magnética sobre uno o varios **platos** circulares que giran a gran velocidad (por ejemplo, 5.400 o 7.200 revoluciones por minuto). Un **cabezal** de lectura/escritura se desplaza sobre la superficie de esos platos para acceder a la información, moviéndose hasta la posición exacta donde están los datos. Al depender de piezas que se mueven físicamente, es más lento que un disco de estado sólido (SSD) y más sensible a golpes, pero ofrece **mucha capacidad a bajo coste**, lo que lo hace ideal para almacenar grandes cantidades de datos. Su naturaleza mecánica es justo lo que lo distingue: mientras un SSD no tiene partes móviles, el HDD funciona como un pequeño tocadiscos de alta precisión.

## Arquitectura

**Imagina una pila de CDs atravesados por un lápiz por el centro.** Eso es el disco duro por dentro: varios **platos** apilados, girando todos juntos alrededor de ese eje central. Cada plato tiene **dos caras** útiles (arriba y abajo), como una moneda.

**Pista (track):** en una cara, imagina los círculos de una diana. Cada aro de la diana es una pista: un círculo perfecto por el que pasan los datos. Una cara tiene miles de estos aros, uno dentro de otro.

**Sector:** ahora coge uno de esos aros y córtalo como si fuera una **pizza**, en porciones. Cada trocito del aro es un sector. Es la casilla más pequeña donde el hardware guarda datos (tradicionalmente 512 bytes). Pista = el aro entero; sector = una porción de ese aro.

**Cabeza L/E:** encima de cada cara hay una aguja, como la de un tocadiscos. Es la **cabeza** que lee y escribe. Hay una por cada cara, así que si tienes 3 platos → 6 caras → 6 cabezas, todas moviéndose a la vez hacia dentro y hacia fuera.

**Cilindro:** esta es la que más cuesta. Vuelve a la pila de CDs. Coge el aro número 20 del plato de arriba, el aro número 20 del de en medio y el número 20 del de abajo... todos a la misma distancia del centro. Si los unieras verticalmente, forman **un tubo hueco**, un cilindro invisible que atraviesa toda la pila. Eso es el cilindro: **todas las pistas que quedan justo una encima de otra**. Importa porque, como todas las cabezas se mueven juntas, cuando una está sobre la pista 20, _todas_ están sobre su pista 20 → puedes leer un cilindro entero sin mover las cabezas (rápido).

**Cluster:** los sectores (las porciones de pizza) son diminutos, y al sistema operativo le sale caro ir de uno en uno. Así que **agrupa varios sectores en un paquete** y trabaja con paquetes. Ese paquete es el cluster. Es la unidad mínima que el SO le da a un archivo. Ojo: esto lo inventa el **software**, no el hardware. El hardware solo conoce sectores; el cluster es una agrupación que hace el sistema para ir más cómodo.

Para fijarlo, quédate con esta jerarquía de tamaño:

> **Cluster** (paquete que usa el SO) ⊃ **Sector** (casilla física mínima) ⊂ **Pista** (aro completo) → apila las pistas de todos los platos y tienes el **Cilindro** (tubo vertical).

Y la frase resumen: **diana** (pistas) cortada en **porciones de pizza** (sectores), repetida en varios **CDs apilados** (platos), leída por **agujas de tocadiscos** (cabezas), donde los aros alineados en vertical forman un **tubo** (cilindro) y el sistema agrupa porciones en **paquetes** (clusters).