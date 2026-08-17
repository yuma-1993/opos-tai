**OCL** (Object Constraint Language) es una de las cuatro capas de la estructura de UML (junto a Infraestructura, Superestructura y XMI): el lenguaje que permite definir restricciones y reglas sobre un modelo — invariantes, precondiciones, postcondiciones, condiciones de estado, etc. — y que también sirve para definir casos de prueba. Un ejemplo típico es `{edad > 0}` sobre un atributo de una clase.

*(Ampliación, no viene literal de la fuente):* OCL es un lenguaje **declarativo y sin efectos secundarios**: solo consulta y restringe el modelo, nunca lo modifica. Una restricción OCL completa se escribe con la forma `context Clase inv: expresión` — por ejemplo, `context Persona inv: edad > 0` sería la versión completa del ejemplo `{edad > 0}` aplicado sobre una clase `Persona`.

[[B3 - T4.2 UML]]
