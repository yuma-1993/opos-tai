Clasifica cómo una herramienta de gestión de la configuración aplica los cambios a los equipos administrados.

- **Push**: es el servidor central el que inicia la conexión y envía (empuja) la configuración a cada equipo cuando el administrador lo decide. Así trabajan Ansible, WSUS y StackStorm.
- **Pull**: es cada equipo administrado, con un agente instalado, el que se conecta periódicamente al servidor central y descarga (tira de) su configuración. Así trabajan Chef, Puppet y SaltStack.
- SCCM combina los dos modelos (Pull y Push).

> [!note] Conocimiento general (no viene literal del tema)
> El tema de origen solo etiqueta cada herramienta como Push o Pull en una tabla, sin explicar qué significa cada término — esta definición de "quién inicia la conexión" es la lectura estándar de ambos modelos, no un dato literal de la fuente.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[IaC (Infrastructure as Code)]] y [[CCA (Continuous Configuration Automation)]] — el objetivo que persiguen ambos modelos; solo cambia el mecanismo de aplicación.
- [[DevOps]] — quien elige qué herramienta (y por tanto qué modelo) usar.
