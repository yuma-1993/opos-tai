SSH usa dos parejas de claves asimétricas distintas, con roles distintos:

- **Claves de host** (`/etc/ssh/ssh_host_rsa_key`, `ssh_host_dsa_key`, `ssh_host_ecdsa_key`): identifican al **servidor** ante los clientes. Son las que generan el fingerprint que se muestra la primera vez que te conectas a una máquina ("The authenticity of host X can't be established...") y que queda registrado en `known_hosts` del cliente.
- **Claves de usuario** (`~/.ssh/id_rsa` / `id_rsa.pub`): identifican a la **persona** que se conecta. La clave pública es la que se copia con `ssh-copy-id` al fichero `authorized_keys` del servidor destino.

Son dos mecanismos de autenticación distintos, ambos basados en [[Criptografía asimétrica (clave pública y privada)]]: uno autentica el servidor frente a ti, el otro te autentica a ti frente al servidor.

[[B4 - T1.2 ADMON SSOO - SSH]]

**Conexiones con otros conceptos TAI:**
- [[authorized_keys vs known_hosts]] — los ficheros donde acaban registradas, respectivamente, las claves de usuario admitidas (servidor) y las claves de host ya vistas (cliente).
- [[Criptografía asimétrica (clave pública y privada)]] — el mecanismo criptográfico común a ambos tipos de clave.
