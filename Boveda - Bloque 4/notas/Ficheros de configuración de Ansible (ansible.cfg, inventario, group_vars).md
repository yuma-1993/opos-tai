Ansible reparte su configuración en tres ficheros que trabajan juntos:

- **`ansible.cfg`**: configuración global. Con `[defaults] inventory = /etc/ansible/hosts` le dice a Ansible dónde está el fichero de inventario por defecto (esa misma ruta ya es la que asume Ansible aunque no se declare explícitamente).
- **Inventario de hosts** (`/etc/ansible/hosts`): define los grupos y los hosts que los componen, con el formato `[group_name]` + `alias ansible_ssh_host=ip`. El `alias` es el nombre corto que se usa luego en los playbooks; `ansible_ssh_host` es la IP/hostname real al que Ansible se conecta.
- **`group_vars/<grupo>`**: fichero YAML (ej. `/etc/ansible/group_vars/labservers`) con variables que se aplican automáticamente a todos los hosts de ese grupo, sin repetirlas host a host. El nombre del fichero debe coincidir con el nombre del grupo del inventario. Ejemplo: `ansible_ssh_user: root` hace que Ansible se conecte como `root` por SSH a todo el grupo.

`ansible.cfg` apunta al inventario, el inventario define grupos y hosts, y `group_vars/<grupo>` añade variables por grupo — los tres encajan en cadena antes de que se ejecute ningún comando o playbook.

[[B4 - T1.4 ADMON SSOO - ANSIBLE]]
