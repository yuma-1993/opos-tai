En SaltStack el **master** es el servidor central de administración y el **minion** es el agente que hay que instalar en cada equipo administrado, con una conexión ya establecida con el master. A diferencia del modelo agentless de Ansible (que solo necesita SSH ya configurado), SaltStack necesita mantener este agente activo — pero a cambio permite un modelo de comunicación pub/sub más eficiente en parques grandes: el master publica órdenes a todos los minions a la vez, en vez de abrir una conexión nueva por cada host en cada ejecución.

En la configuración del master (`/etc/salt/master`) esto se refleja en dos puertos distintos: `publish_port: 4505`, por el que el master publica órdenes, y `ret_port: 4506`, por el que los minions devuelven resultados. `file_roots` indica además dónde sirve el master los ficheros de estado (`.sls`) que reparte a los minions.

Es la misma distinción agent-based (SaltStack, Puppet, Chef) frente a agentless (Ansible) que aparece al comparar herramientas de gestión de configuración, y que condiciona también si el modo por defecto de la herramienta es push o pull.

**Conexiones con otros conceptos TAI:**
- [[Modelo Push vs Pull (gestión de configuración)]] — tener un agente instalado en cada minion es lo que permite a SaltStack trabajar en modo pull.
- [[IaC (Infrastructure as Code)]] — el conjunto master/minion es la infraestructura sobre la que SaltStack aplica la configuración como código.
- [[Modelo Standalone (SaltStack)]] — modo en el que un minion se ejecuta sin depender de esta arquitectura.

[[B4 - T1.1 ADMON SSOO]]
[[B4 - T1.4 ADMON SSOO - ANSIBLE]]
[[B4 - T1.5 ADMON SSOO - SALTSTACK]]
