Patrón **estructural** (también llamado *Wrapper*) que actúa de intermediario ofreciendo al cliente una interfaz más fácil de utilizar que la ya desarrollada. La clase cliente necesita un servicio (`methodX()`) que le resulta demasiado complejo o que no sabe usar directamente; la clase `Adapter` le ofrece un servicio que el cliente sí sabe usar, y es ella la que se encarga de llamar/"adaptar" al objeto original (`Adaptee`). Puede implementarse **por herencia** (Adapter hereda tanto de Target como de Adaptee) o **por asociación** (Adapter implementa Target y guarda una referencia interna a Adaptee).

**Proxy vs. Facade vs. Adapter**: ver [[Proxy (patrón GoF)]].

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
