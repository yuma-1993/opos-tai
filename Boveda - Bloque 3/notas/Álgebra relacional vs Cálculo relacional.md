Ambos son formas equivalentes de expresar consultas sobre el modelo relacional. El álgebra dice **cómo** obtener el resultado (procedimental); el cálculo dice **qué** resultado quieres (declarativo). SQL, en su ejecución interna, se traduce a álgebra relacional; en su sintaxis, se parece más al cálculo.

| | Álgebra relacional | Cálculo relacional |
|---|---|---|
| **Enfoque** | Procedimental/imperativo: describes cómo obtener el resultado (secuencia de operaciones) | Declarativo: describes qué resultado quieres, sin decir cómo obtenerlo |
| **Analogía** | Como una receta paso a paso | Como especificar una condición matemática que deben cumplir los resultados |
| **Relación con SQL** | SQL se ejecuta internamente traduciéndose a álgebra relacional | SQL, en su forma de escribirlo, se parece más al cálculo relacional (dices el qué, no el cómo) |

> [!important]
> Ambos formalismos son equivalentes en potencia expresiva (teorema de Codd): todo lo expresable en uno se puede expresar en el otro.

[[Operaciones básicas del álgebra relacional]]
[[Operaciones derivadas del álgebra relacional]]
[[Cálculo relacional (tuplas y dominios)]]
[[B3 - T1.2 DISENO BBDD]]
