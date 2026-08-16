Un Playbook es un fichero YAML donde se define lo que se quiere que Ansible haga en los nodos, y se ejecuta con `ansible-playbook fichero.yml`. Su estructura básica incluye `name` (descripción), `hosts` (grupo del inventario sobre el que actúa), `become`/`user` (con qué privilegios se ejecuta en el nodo remoto) y `tasks` (la lista de tareas, cada una con su `name` y el módulo que usa).

Frente a los [[Comandos ad-hoc (Ansible)|comandos ad-hoc]] (imperativos: "haz esto ahora"), un playbook es **declarativo**: describe el estado final que quieres (ej. `apache2` presente) y es Ansible quien decide si hace falta actuar o no — si el paquete ya está instalado, volver a ejecutar el playbook no cambia nada ([[Idempotencia]]). Es la misma distinción abstracta "qué quieres" (declarativo) vs "cómo obtenerlo" (procedimental/imperativo) que aparece en [[Álgebra relacional vs Cálculo relacional]], aplicada aquí a la gestión de configuración en vez de a consultas de bases de datos.

**Conexiones con otros conceptos TAI:**
- [[Idempotencia]] — la propiedad que hace útil reejecutar un playbook sin miedo a duplicar cambios.
- [[Comandos ad-hoc (Ansible)]] — el modo imperativo con el que se contrasta el playbook.
- [[IaC (Infrastructure as Code)]] — el playbook es, en concreto, el fichero de definición con el que Ansible implementa IaC.

[[B4 - T1.4 ADMON SSOO - ANSIBLE]]
[[B4 - T1.1 ADMON SSOO]]
