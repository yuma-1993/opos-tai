El modelo Standalone permite que un minion ejecute funciones localmente sin necesidad de contactar con el master en absoluto. Se activa configurando `file_client: local` en `/etc/salt/minion`, y se invoca con `salt-call --local`.

Es un modo pensado para ejecutar módulos de Salt en un minion aislado, sin depender de la [[Arquitectura Master-Minion (SaltStack)|arquitectura master/minion]] habitual.

[[B4 - T1.5 ADMON SSOO - SALTSTACK]]
