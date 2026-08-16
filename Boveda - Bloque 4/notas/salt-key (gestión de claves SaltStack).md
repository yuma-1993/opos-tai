`salt-key` gestiona el mecanismo de confianza entre minions y master: cada minion genera su propio par de claves y envía la pública al master al arrancar, pero el master no le hace caso hasta que un administrador la acepta explícitamente. `salt-key -L` lista todas las claves que maneja el master (aceptadas y pendientes) y `salt-key -A` acepta las pendientes.

Es el mismo problema de fondo que resuelve `ssh-copy-id` para SSH — establecer confianza antes de poder ejecutar nada remotamente —, pero aquí SaltStack lo resuelve con un intercambio de claves propio en vez de con el mecanismo de SSH.

**Conexiones con otros conceptos TAI:**
- [[Criptografía asimétrica (clave pública y privada)]] — el mismo principio de par de claves pública/privada en el que se basa esta confianza.
- [[Comandos de gestión de claves SSH (ssh-keygen, ssh-copy-id, ssh-agent, ssh-add, ssh-keyscan)]] — el equivalente en SSH: establecer confianza antes de ejecutar nada remotamente.

[[B4 - T1.5 ADMON SSOO - SALTSTACK]]
