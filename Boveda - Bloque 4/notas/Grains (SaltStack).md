Los grains son información consultable de cada minion — sistema operativo, CPU, red...— por la que se puede preguntar o filtrar. `salt '*' grains.items` muestra todos los grains disponibles y `salt '*' grains.item <nombre>` muestra el valor de uno concreto (ej. `dns`). También se pueden crear grains propios en los minions.

Además de consultarse, sirven para dirigir una acción solo a un subconjunto de minions, como en `salt-cp -G 'os:centos' irq.py /usr/local/`, que copia un fichero solo a los minions cuyo grain `os` valga `centos`.

> [!note] Conocimiento general (no viene literal del tema)
> Los grains son el equivalente conceptual de los "facts" de Ansible: datos estáticos o semi-estáticos del nodo que sirven tanto para consultar su estado como para filtrar sobre qué equipos actuar.

**Conexiones con otros conceptos TAI:**
- [[Salt State (.sls)]] — el filtrado por grain permite dirigir un `.sls` solo a un subconjunto de minions.
- [[Comandos ad-hoc SaltStack (salt, salt-cp)]] — los grains se consultan y se usan como filtro (`-G`) con estos mismos comandos.

[[B4 - T1.5 ADMON SSOO - SALTSTACK]]
