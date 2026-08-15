El **polling** (sondeo o consulta) es el mecanismo en el que la CPU pregunta activa y repetidamente a los dispositivos periféricos si tienen datos listos o necesitan atención. En lugar de esperar a que el dispositivo avise, es la [[CPU - Central Processing Unit]] quien toma la iniciativa y va comprobando uno por uno: "¿tienes algo?, ¿y tú?, ¿y tú?".

Y sí, **supone un gasto de recursos**, por dos motivos principales:

- La CPU dedica ciclos a preguntar constantemente, incluso cuando el dispositivo no tiene nada que ofrecer. Ese tiempo podría emplearse en otras tareas útiles. Es lo que se llama _busy-waiting_ o espera activa.
- Hay que elegir la frecuencia del sondeo, y ninguna opción es ideal: si preguntas muy a menudo, malgastas CPU en consultas vacías; si preguntas poco, puedes tardar en atender al dispositivo y perder datos o reaccionar con retraso.

La alternativa es justamente el mecanismo de **[[interrupciones]]** que veníamos comentando: en vez de que la CPU pregunte, es el periférico quien avisa mediante una IRQ cuando realmente tiene algo. Así la CPU queda libre para otras tareas y solo se ocupa del dispositivo cuando hace falta.