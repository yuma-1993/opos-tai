Patrón de **comportamiento** que convierte los estados de un objeto en clases propias. Punto de partida típico: una clase con ciclo de vida (por ejemplo, `Factura`) cuyo método principal (`abonar()`) acumula un "super if" difícil de mantener (si se abona el total se marca como pagada y se contabiliza, si está bloqueada se avisa a jurídico...). La solución saca esa lógica de negocio asociada a cada estado a una clase propia que implementa una interfaz común (`Estado`, con un método `execute()`), y el objeto principal solo delega en el estado actual, eliminando el "super if".

**Strategy vs. State vs. Template Method**: ver [[Strategy (patrón GoF)]].

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
