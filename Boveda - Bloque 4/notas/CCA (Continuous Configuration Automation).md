Es el proceso que automatiza la implementación y configuración de los equipos de forma continua: no se limita a aplicar la configuración una sola vez, sino que va comprobando y ajustando el estado del sistema a medida que pasa el tiempo.

**¿Por qué hace falta esto?**
Un despliegue inicial (lo que resuelve [[IaC (Infrastructure as Code)|IaC]]) no basta por sí solo: los sistemas se van desviando de su configuración original (alguien cambia algo a mano, falla un servicio, se instala un paquete de más). CCA es la capa que detecta y corrige esas desviaciones de forma continuada, para que el sistema no se aleje del estado que se definió.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[IaC (Infrastructure as Code)]] — define el estado deseado; CCA se encarga de mantenerlo en el tiempo.
- [[Modelo Push vs Pull (gestión de configuración)]] — las herramientas de CCA aplican sus cambios según uno de estos dos modelos.
