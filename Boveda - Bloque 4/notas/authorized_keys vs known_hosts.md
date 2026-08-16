- **`~/.ssh/authorized_keys`**: fichero en el **servidor**, con las claves públicas de los clientes autorizados a conectarse sin contraseña.
- **`~/.ssh/known_hosts`**: fichero en el **cliente**, con los fingerprints de las claves públicas de los servidores a los que ya se ha conectado alguna vez.

`ssh-copy-id` es el comando que puebla `authorized_keys`: copia la clave pública del cliente (`id_rsa.pub`) al servidor destino. A partir de ahí, `ssh usuario@servidor` no vuelve a pedir contraseña — este acceso sin contraseña es precisamente el prerrequisito que usa una herramienta *agentless* como Ansible.

[[B4 - T1.2 ADMON SSOO - SSH]]

**Conexiones con otros conceptos TAI:**
- [[Claves de host vs claves de usuario (SSH)]] — `authorized_keys` guarda claves de usuario; `known_hosts` guarda fingerprints derivados de claves de host.
- [[Comandos de gestión de claves SSH (ssh-keygen, ssh-copy-id, ssh-agent, ssh-add, ssh-keyscan)]] — `ssh-copy-id` es el comando que puebla `authorized_keys`.
