Patrón de **comportamiento** que define el flujo de ejecución de un proceso, pero solo **parcialmente**: a nivel de *framework* se definen algunos métodos ya resueltos (`m()`, final) y otros abstractos, sin implementar todavía (`g()`, `h()`), aunque con el esqueleto/flujo del proceso ya fijado — el "método plantilla". A nivel de aplicación, cada caso concreto implementa esos métodos abstractos a su manera, sin poder alterar el orden del flujo general.

**Strategy vs. State vs. Template Method**: ver [[Strategy (patrón GoF)]].

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
