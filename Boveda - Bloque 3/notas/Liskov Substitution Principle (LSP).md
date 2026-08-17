Principio **L** de [[SOLID (principios)|SOLID]]: *derived classes must be substitutable for their base classes* — las clases hijas deben ser sustituibles por su clase base sin que el sistema deje de funcionar.

En una jerarquía donde `Clase B` y `Clase C` heredan de `Clase A` (redefiniendo sus métodos sin añadir otros nuevos), un subsistema que trabaja con objetos de esta jerarquía debería poder usar indistintamente cualquiera de las tres: el código "compilaría" y funcionaría igual, aunque el resultado concreto obtenido pudiera no ser el esperado en cada caso. Al subsistema le da igual la implementación concreta; implica tener una jerarquía robusta y un comportamiento por defecto (el de la clase base). Se basa en el polimorfismo.

Es la misma idea de fondo que el principio de [[Composición sobre herencia]]: si dos clases no cumplen una relación "es un/a" verdadera, no deben estar unidas por herencia.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
[[B3 - T4.2 UML]] (polimorfismo)
