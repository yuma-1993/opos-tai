Consiste en definir y configurar la infraestructura (servidores, redes, servicios) igual que si fuera **código fuente**: en vez de ejecutar pasos manuales uno a uno, se escriben archivos de definición (con un lenguaje de programación) que describen las acciones a realizar, y son esos archivos los que se ejecutan para dejar el sistema configurado.

**¿Por qué hace falta esto?**
Como cualquier código, esos archivos se pueden versionar en un repositorio (ej. Git), revisar antes de aplicarlos y repetir tantas veces como haga falta con el mismo resultado — a diferencia de una serie de comandos manuales, difícil de auditar o de reproducir exactamente igual en otro servidor.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[CCA (Continuous Configuration Automation)]] — la capa que se encarga de que ese estado definido por IaC se mantenga en el tiempo, no solo en el despliegue inicial.
- [[DevOps]] — la figura que usa IaC para automatizar su trabajo.
- [[Modelo Push vs Pull (gestión de configuración)]] — las herramientas concretas que implementan IaC (Ansible, SaltStack...) se clasifican según cómo aplican esos archivos de definición.
