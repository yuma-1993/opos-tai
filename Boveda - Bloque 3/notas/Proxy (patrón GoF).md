Patrón **estructural** que controla el acceso a un objeto real, interponiéndose entre el cliente y ese objeto. Es una relación **uno a uno**: hay un Proxy para un tipo de dato concreto, y solo para ese. El Proxy va siempre por delante de la clase real, actuando como una capa que aísla; para el cliente es transparente gracias al polimorfismo (ambos implementan la misma interfaz).

**Proxy vs. Facade vs. Adapter**: Proxy usa la **misma interfaz** que el objeto real y controla el acceso a **un único** objeto; [[Facade (patrón GoF)|Facade]] ofrece una interfaz **nueva** de alto nivel para simplificar el acceso a **varias** clases/subsistemas; [[Adapter (patrón GoF)|Adapter]] ofrece una interfaz **nueva** para hacer compatible una interfaz **ya existente** con la que espera el cliente (traduce, no simplifica).

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
