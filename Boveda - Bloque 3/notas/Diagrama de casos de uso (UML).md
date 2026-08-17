El **diagrama de casos de uso** representa los **requisitos funcionales** de la aplicación: cada caso de uso es una funcionalidad identificable de cara al usuario. No todos los casos de uso tienen el mismo "tamaño", no existen casos de uso "abstractos" (del tipo genérico "Gestionar…"), y a diferencia de los [[DFD - Diagrama de Flujo de Datos|DFD]] los casos de uso **no "explotan"** en subniveles — capturan un nivel de granularidad medio-bajo y se organizan, como mucho, en paquetes/subsistemas. Es importante tener claro que un diagrama de casos de uso **no refleja flujo**: dice qué ocurre, no cuándo ocurre (para eso hace falta acompañarlo de una especificación **SRS**, especificación de requisitos de software).

Puede existir relación de herencia entre actores y entre casos de uso (poco habitual). Si el actor se dibuja a la **izquierda** del caso de uso es el **actor principal**; si se dibuja a la **derecha**, es un **actor secundario**.

Dos relaciones especiales conectan casos de uso entre sí:

| Relación | Notación | Significado |
|---|---|---|
| Inclusión | `<<include>>` | comportamiento **obligatorio**; funcionalidad común a varios casos de uso |
| Extensión | `<<extend>>` | comportamiento **opcional**, activado desde un **punto de extensión** que especifica bajo qué condiciones se produce o no |

Ej.: el caso de uso `Place Order` incluye obligatoriamente (`<<include>>`) los casos `Supply Customer Data`, `Order Product` y `Arrange Payment`; y tiene un punto de extensión que activa opcionalmente (`<<extend>>`) el caso `Request Catalog`.

[[B3 - T4.2 UML]]
