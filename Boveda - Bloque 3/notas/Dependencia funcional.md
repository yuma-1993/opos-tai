**X → Y** ("X determina funcionalmente a Y"): a cada valor de X le corresponde un único valor de Y. X es el determinante, Y depende de X.

- La clave siempre determina funcionalmente al resto de atributos (por definición, no se repite).
- ¿Es buena o mala una DF?
  - Si el determinante es la clave → inevitable, no es un problema.
  - Si el determinante no es la clave → mala: indica redundancia, hay que [[Normalización|normalizar]] para eliminarla.

> [!example] Ejemplo práctico — R(a, b, c, d)
>
> | a | b | c | d |
> |---|---|---|---|
> | 1 | xx | 3 | 4 |
> | 1 | yy | 3 | a |
> | 1 | xx | 3 | b |
>
> - ¿a → b? No (a=1 aparece con b="xx" y b="yy": mismo valor de a, distinto b).
> - ¿a → c? Sí (a=1 siempre va con c=3).
> - ¿a → d? No (varios valores de d para a=1).
> - ¿c → d? No (c=3 siempre igual, pero d cambia: 4, a, b).

**Dependencia funcional completa**: G depende completamente de un grupo Z si depende de todo Z, pero no de ningún subconjunto propio de Z.

> [!example]
> R(A, B, C, E, F, G, H). Si A+B+C determinan G, pero C solo ya determina G → la dependencia no es completa (hay redundancia parcial: parte de la clave ya basta).

La [[Dependencia multivaluada (DMV)]] es una generalización de este mismo concepto.

[[B3 - T1.2 DISENO BBDD]]
