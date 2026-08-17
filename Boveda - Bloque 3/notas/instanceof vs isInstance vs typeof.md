Tres formas de comprobar en tiempo de ejecución el tipo real de un objeto, que se prestan a confusión entre lenguajes:

- **`typeof`**: operador de .NET.
- **`instanceof`** (Java): similar a `typeof`, pero en Java también da `true` con tipos compatibles por herencia, no solo con el tipo exacto — por ejemplo, `p instanceof PolizaVida` solo admite tipos compatibles por herencia hacia abajo (`Poliza`, `PolizaVida`, `PolizaAuto`).
- **`isInstance`** (Java, método de `Class`): este sí se comporta como el `typeof` de .NET.

Ambos operadores de Java (`instanceof` e `isInstance()`) devuelven un booleano y son muy parecidos, pero se recomienda usar `isInstance()` en lugar de `instanceof` para comprobar la clase de un objeto: `isInstance()` funciona tal y como se espera en cualquier escenario, algo que no siempre ocurre con `instanceof`.

[[Polimorfismo (POO)]]
[[B3 - T4.2 UML]]
