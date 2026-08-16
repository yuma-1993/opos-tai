La **criptografía asimétrica** se basa en generar un par de claves matemáticamente relacionadas: una **privada**, que se queda siempre en la máquina que la genera y nunca se comparte, y una **pública**, que se distribuye libremente y se copia en cada sitio donde se quiere poder demostrar identidad sin usar contraseña.

En SSH, la capacidad de securizar el canal se apoya en este mecanismo: al instalar SSH se generan `~/.ssh/id_rsa` (clave privada) e `~/.ssh/id_rsa.pub` (clave pública). Cuando el cliente intenta conectar, el servidor le reta a demostrar que posee la clave privada correspondiente a una de las públicas que tiene registradas — sin que la privada viaje nunca por la red.

`ssh-keygen` admite varios algoritmos para generar el par: **RSA** (el que usa SSH por defecto), **DSA** y **ECDSA**.

**¿Por qué hace falta esto?** Sin criptografía asimétrica, demostrar identidad de forma remota exigiría enviar un secreto (una contraseña) por la red en cada conexión, exponiéndolo a interceptación. Con un par de claves, el secreto (la clave privada) nunca se transmite: solo se demuestra que se posee, mediante un reto criptográfico que el servidor plantea al cliente.

[[B4 - T1.2 ADMON SSOO - SSH]]

**Conexiones con otros conceptos TAI:**
- [[Claves de host vs claves de usuario (SSH)]] — SSH aplica este mismo mecanismo dos veces, con roles distintos: para autenticar al servidor y para autenticar a la persona.
