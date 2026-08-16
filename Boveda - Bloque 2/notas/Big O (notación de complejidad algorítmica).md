**Big O** es la notación que representa la **cota superior asintótica** de la complejidad de un algoritmo — cuánto crecen su tiempo o su espacio necesarios a medida que crece el tamaño de la entrada (n).

De menor a mayor complejidad: **O(1)** (constante) < **O(log n)** (logarítmica) < **O(n)** (lineal) < **O(n log n)** < **O(n²)** (cuadrática) < **O(2ⁿ)** (exponencial) < **O(n!)** (factorial) < **O(nⁿ)** (potencial exponencial).

**Ampliación (conocimiento general, no viene del tema)**: para n=20, la diferencia de magnitud es brutal: O(log n) ≈ 4-5 pasos, O(n) = 20 pasos, O(n log n) ≈ 86 pasos, O(n²) = 400 pasos, O(2ⁿ) ≈ 1.048.576 pasos, O(n!) ≈ 2,4 × 10¹⁸ pasos. Es justo la diferencia entre los algoritmos de ordenación "buenos" (O(n log n), como [[MergeSort]] o [[QuickSort]]) y los "ingenuos" (O(n²), como [[Bubble Sort (Burbuja)|Burbuja]] o [[Selección (Selection Sort)|Selección]]).

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
