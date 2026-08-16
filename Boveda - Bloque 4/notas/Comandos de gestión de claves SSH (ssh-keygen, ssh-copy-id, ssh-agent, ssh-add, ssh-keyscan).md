Conjunto de comandos del ecosistema SSH para generar y gestionar claves:

- **`ssh-keygen -t rsa/dsa/ecdsa -b numero_bits_clave`**: genera un par de claves (privada + pública).
- **`ssh-keygen -l -f fichero.pub`**: muestra el fingerprint de una clave.
- **`ssh-copy-id username@remote_host`**: copia la clave pública propia al fichero `authorized_keys` del servidor destino, para poder entrar sin contraseña a partir de entonces.
- **`ssh-agent`**: agente de autenticación que mantiene la clave privada descifrada en memoria durante la sesión, para no tener que teclear la passphrase en cada conexión.
- **`ssh-add`**: añade una clave privada al agente en ejecución.
- **`ssh-keyscan`**: recopila claves públicas de uno o varios hosts.

**¿Por qué hace falta `ssh-agent`?** La passphrase de `ssh-agent`/`ssh-add` no es la contraseña del usuario remoto: es la contraseña opcional con la que se puede cifrar la propia clave privada (`id_rsa`) en el disco local. Sin `ssh-agent`, si la clave privada tiene passphrase, se pediría en cada conexión SSH aunque la autenticación por clave ya esté configurada; `ssh-agent` la pide una única vez y la mantiene disponible mientras dura la sesión.

[[B4 - T1.2 ADMON SSOO - SSH]]

**Conexiones con otros conceptos TAI:**
- [[authorized_keys vs known_hosts]] — `ssh-copy-id` es el comando que puebla `authorized_keys`.
- [[Criptografía asimétrica (clave pública y privada)]] — el par de claves que genera `ssh-keygen`.
- El acceso sin contraseña que deja configurado `ssh-copy-id` es el prerrequisito que usa Ansible como herramienta *agentless* (ver [[B4 - T1.4 ADMON SSOO - ANSIBLE]]).
