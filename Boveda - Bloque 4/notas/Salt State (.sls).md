Un Salt State es un fichero en formato YAML, con extensión `.sls`, que describe el estado final deseado de un minion en vez de los pasos para llegar a él. Por ejemplo, `mc: pkg.installed` significa "quiero que el paquete `mc` esté instalado", sin especificar cómo — es SaltStack quien decide si hace falta actuar. Se aplica con `salt '*' state.apply <nombre>`, que busca el fichero `<nombre>.sls` correspondiente y lo aplica a los minions indicados.

Es el equivalente conceptual del [[Playbook (Ansible)|playbook]] de Ansible: la misma idea de definición declarativa y reejecutable ([[Idempotencia]]), frente al modo imperativo de los [[Comandos ad-hoc SaltStack (salt, salt-cp)|comandos ad-hoc]]. A diferencia de un playbook, un Salt State puede procesarse tanto en modo push (`state.apply`, el master empuja la orden) como en modo pull (el minion pregunta al master si hay algo pendiente) — ver [[Modelo Push vs Pull (gestión de configuración)]].

**Conexiones con otros conceptos TAI:**
- [[Playbook (Ansible)]] — el equivalente declarativo en Ansible.
- [[Idempotencia]] — la propiedad que hace seguro reejecutar un Salt State.
- [[Modelo Push vs Pull (gestión de configuración)]] — un `.sls` admite ambos modos según cómo se invoque.
- [[IaC (Infrastructure as Code)]] — el fichero `.sls` es el fichero de definición con el que SaltStack implementa IaC.

[[B4 - T1.5 ADMON SSOO - SALTSTACK]]
