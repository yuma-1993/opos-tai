Patrón **creacional** que resuelve la creación de objetos cuando existen **varios tipos** de un mismo concepto, apoyándose en el **polimorfismo**: la complejidad está en la jerarquía de clases (muchos tipos posibles de un mismo objeto). La "fábrica" declara un método que crea el objeto en su forma **abstracta**, pero cada implementación concreta del creador devuelve el tipo **concreto** correspondiente.

Está directamente ligado al principio de inversión de dependencias de [[SOLID (principios)]]: el código cliente que llama al método de fábrica depende de la abstracción, nunca de la implementación concreta que se instancia por debajo.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
