**Sobrecarga** (*overloading*): varios métodos con el mismo nombre que se diferencian entre sí por el número y/o el tipo de sus parámetros. Se resuelve en **tiempo de compilación** (*static binding*), según los parámetros con los que se hace la llamada.

**Sobreescritura** (*overriding*): una subclase redefine un método ya definido en su clase base. Es la base del polimorfismo por herencia y se resuelve en **tiempo de ejecución** (*late binding*/ligadura dinámica), según el tipo real del objeto — no según el tipo de la variable que lo referencia.

*(Ampliación, no viene literal de la fuente):* conviene no confundir ambos conceptos aunque a veces los dos se llamen "polimorfismo": solo la sobreescritura con *late binding* implica ligadura dinámica real; la sobrecarga se decide antes de ejecutar el programa.

[[Polimorfismo (POO)]]
[[B3 - T4.2 UML]]
