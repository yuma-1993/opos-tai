Un comando ad-hoc es una tarea suelta que se lanza directamente desde la línea de comandos (`ansible all -m <módulo> -a "<args>"`), sin guardarla en ningún fichero. `-m` selecciona el módulo a usar (`ping`, `shell`, `apt`, `file`...); `-a` pasa argumentos a ese módulo. Si no se indica módulo con `-m`, Ansible usa por defecto el módulo `command`.

Es el equivalente a ejecutar una sola tarea de forma inmediata e imperativa — típico para comprobaciones rápidas (`ansible all -m ping`, `ansible all -a "uname -a"`) o cambios puntuales (`ansible all -m apt -a "name=vim"`), pero no pensado para configuraciones repetibles que se quieran versionar. Eso es justo lo que resuelve el [[Playbook (Ansible)|Playbook]]: mismo tipo de tareas, pero guardadas en un fichero declarativo y reejecutable.

[[B4 - T1.4 ADMON SSOO - ANSIBLE]]
