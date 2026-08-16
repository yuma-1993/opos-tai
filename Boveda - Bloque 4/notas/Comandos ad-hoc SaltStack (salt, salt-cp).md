Los comandos `salt '*' <módulo>` ejecutan una función puntual e inmediata en los minions indicados, sin guardarla en ningún fichero — el equivalente imperativo del [[Salt State (.sls)|Salt State]] declarativo. El `'*'` selecciona a qué minions se dirige el comando (aquí, todos); se puede filtrar por [[Grains (SaltStack)|grain]] con `-G`. Ejemplos: `salt '*' test.version`, `salt '*' disk.usage`, `salt '*' cmd.run 'ls -l /etc'`, `salt '*' pkg.install vim` (instala un paquete sin pasar por un `.sls`), `salt '*' network.interfaces`, `salt '*' grains.get 'cpu_model'`.

`salt-cp` copia ficheros del master a los minions: `salt-cp '*' salt.doc /usr/local/` lo envía a todos, y `salt-cp -G 'os:centos' irq.py /usr/local/` solo a los que tienen ese grain.

Es el paralelo directo de los [[Comandos ad-hoc (Ansible)|comandos ad-hoc de Ansible]]: la misma idea de tarea suelta e imperativa, salvo que aquí se lanzan desde el master hacia minions ya conectados, en vez de por SSH.

**Conexiones con otros conceptos TAI:**
- [[Comandos ad-hoc (Ansible)]] — el mismo concepto (tarea imperativa puntual) en la otra herramienta.
- [[Salt State (.sls)]] — el modo declarativo con el que se contrastan estos comandos.
- [[Grains (SaltStack)]] — la información que se consulta y se usa para filtrar minions con `-G`.

[[B4 - T1.5 ADMON SSOO - SALTSTACK]]
