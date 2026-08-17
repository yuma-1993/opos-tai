Patrón **creacional** que resuelve el problema de que una clase debe tener **un único objeto** compartido por todo el sistema (un objeto global) — por ejemplo, una configuración, un `DataSource`, etc.

La solución es hacer el **constructor privado** (para que nadie pueda hacer `new`) y exponer un **método estático** que crea el objeto la primera vez que se llama, y en el resto de llamadas devuelve siempre el mismo objeto ya creado.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
