**¿Qué es direccionamiento aquí?**  
Es simplemente **la forma de decirle al disco dónde está un dato**: el sistema de "direcciones" que usas para señalar una casilla concreta entre los millones que hay. Como una dirección postal, pero para sectores del disco. Y hay dos formas de escribir esa dirección: CHS y LBA.

> [!note] No confundir con [[Modos de direccionamiento]]
> Esta nota va de direccionar **sectores de un disco** (CHS/LBA). La otra nota, con nombre parecido, va de cómo una **instrucción de máquina** localiza su operando (inmediato, directo, indirecto...). Comparten palabra, no nivel.

**CHS — la dirección "física" (las coordenadas reales)**

Con lo que ya sabes de la arquitectura, esto encaja solo. CHS localiza un dato dando sus **tres coordenadas físicas**:

- **C**ylinder → ¿en qué cilindro? (a qué distancia del centro)
- **H**ead → ¿en qué cabeza/cara? (en qué plato, arriba o abajo)
- **S**ector → ¿en qué porción de pizza?

Es como decir: "el dato está en el aro 20, cara 3, porción 7". Una dirección que apunta al **lugar físico exacto**.

El problema: cada coordenada tiene un número **limitado de dígitos** reservados (unos pocos bits). Es como una matrícula con pocas casillas: en cuanto los discos crecieron, los números disponibles no alcanzaban para nombrar todos los sectores → **límite de capacidad** (el famoso tope histórico de ~8 GB). Además es engorroso: cualquier programa que quiera un dato tiene que pensar en tres coordenadas físicas a la vez.

**LBA — la dirección "lógica" (numerar todo del tirón)**

LBA hace algo mucho más simple: **olvídate de la geometría física y numera todos los sectores en fila**, del primero al último: 0, 1, 2, 3... hasta el final. Un solo número por sector. Punto.

Es como pasar de decir "aro 20, cara 3, porción 7" a decir simplemente "**la casilla número 5.842.113**". Mucho más fácil de manejar: un número y ya.

¿Y qué pasa con la geometría física real? No desaparece; simplemente **el controlador del disco la esconde**. Tú le pides el bloque nº 5.842.113 y él, por dentro, traduce ese número a su cilindro-cabeza-sector real y va a buscarlo. Tú no te enteras de la geometría; es cosa suya.

Ventajas: al usar un número largo y lineal, **caben muchísimos más sectores** (adiós al límite de capacidad) y es **mucho más simple** de gestionar. Por eso LBA es **el estándar actual** y CHS quedó como una reliquia histórica.

**Resumen del contraste:**

- **CHS:** dirección física con 3 coordenadas (cilindro, cabeza, sector). Real pero limitada y engorrosa. → _"aro 20, cara 3, porción 7"_
- **LBA:** dirección lógica, un número secuencial único por sector. Simple y sin límite práctico; el controlador traduce a CHS por dentro. → _"la casilla nº 5.842.113"_

La idea clave para retenerlo: **LBA es una capa de simplicidad por encima del caos físico**. Le pones un número ordenado a cada casilla y dejas que el disco se encargue de saber dónde está de verdad.

[[Bus de dirección]]
[[Modos de direccionamiento]]