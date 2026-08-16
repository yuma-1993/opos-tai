La **programación dinámica** es una técnica de diseño que combina las soluciones óptimas de subproblemas más pequeños para construir la solución del problema completo. Puede aplicarse de forma **Bottom-Up** o **Top-Down**, y en este segundo caso se apoya en la **memoización**: cachear los resultados de los subproblemas ya resueltos para no tener que recalcularlos.

**Ejemplo clásico (ampliación, no viene literalmente del tema)**: calcular Fibonacci de forma recursiva ingenua repite el cálculo de los mismos subproblemas una y otra vez — es el equivalente al "prueba todo" de **[[Backtracking]]**. Con memoización (guardar en una tabla cada resultado ya calculado) se evita recalcular, bajando la complejidad de exponencial a lineal. Ese mecanismo de fondo — guardar un resultado ya obtenido para no recalcularlo — es el mismo que el de [[Caching]].

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
