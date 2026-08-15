Es una extensión del estándar de CD-ROM (el ISO 9660) que define **cómo un CD o DVD puede ser arrancable (booteable)**. Antes de esta especificación, los ordenadores solo sabían arrancar desde disquete o disco duro; El Torito le enseñó a la BIOS a arrancar también desde un disco óptico.

**¿Cómo lo consigue? El truco de la "emulación"**
La clave está justo en lo que dijiste: **simula** un dispositivo que la BIOS ya sabe manejar. La BIOS antigua no tenía ni idea de cómo arrancar desde un CD, pero sí sabía perfectamente arrancar desde un disquete o un disco duro. Entonces El Torito hace un pequeño engaño: le presenta a la BIOS una parte del CD **como si fuera** un disquete o un disco duro. La BIOS se lo cree, arranca de ahí tan contenta, y ni se entera de que en realidad está leyendo de un CD.

**El ejemplo Live CD de Linux**: metes el CD, arrancas el ordenador, y gracias a El Torito la [[BIOS]] es capaz de cargar el sistema operativo directamente desde el disco óptico sin necesidad de tener nada instalado en el disco duro.

Resumido en una frase:
> El Torito es la especificación que hace booteable un CD/DVD engañando a la BIOS para que crea que está arrancando desde un disquete o disco duro que ya sabe manejar (o, en su modo moderno, cargando directamente sin simular nada).