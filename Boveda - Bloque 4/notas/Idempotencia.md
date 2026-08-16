Una operación es idempotente cuando aplicarla varias veces produce el mismo resultado que aplicarla una sola vez: si el sistema ya está en el estado que describe, repetir la operación no cambia nada ni duplica el efecto. Aplicado a la gestión de configuración, esto significa que ejecutar dos veces el mismo fichero de definición (un [[Playbook (Ansible)|playbook]], por ejemplo) deja el sistema en el mismo estado, en vez de reinstalar, duplicar o dar error.

Es la propiedad que hace segura la automatización declarativa: con [[IaC (Infrastructure as Code)|IaC]] se puede reejecutar el mismo fichero de definición las veces que haga falta (tras un fallo, para comprobar que nada ha cambiado, o de forma periódica) sin preocuparse de si ya se había aplicado antes. Por ejemplo, un playbook que instala `apache2` con `state: present` no vuelve a instalarlo si ya está presente — simplemente no hace nada.

**Conexiones con otros conceptos TAI:**
- [[IaC (Infrastructure as Code)]] — la idempotencia es la idea central que permite tratar la infraestructura como código reejecutable.
- [[Playbook (Ansible)]] — ejemplo concreto de fichero declarativo pensado para ser idempotente.
- [[CCA (Continuous Configuration Automation)]] — depende de la idempotencia para poder reaplicar la configuración en el tiempo sin efectos acumulativos indeseados.

[[B4 - T1.1 ADMON SSOO]]
[[B4 - T1.4 ADMON SSOO - ANSIBLE]]
