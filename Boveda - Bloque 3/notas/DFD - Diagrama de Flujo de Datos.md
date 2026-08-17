Mientras el modelo [[Tipo de Entidad y Entidad|Entidad-Relación]] hace **análisis estructural** (qué datos existen y cómo se relacionan), el DFD hace **análisis funcional**: se centra en qué procesos transforman esos datos y cómo fluye la información entre ellos. Es la vista de "procesos de negocio", complementaria a la del E-R, no una alternativa a ella — un sistema real se modela con ambas vistas a la vez.

> [!note] Equivalencia en UML
> El DFD es un lenguaje pre-UML/estructurado; su equivalente conceptual en UML es el diagrama de actividad, que también representa flujos de proceso, aunque con notación distinta.

**Descomposición funcional Top-Down (por niveles)**: la idea es ir haciendo zoom progresivamente, empezando por el sistema como caja negra y abriéndolo en subcajas cada vez más detalladas.

- **Nivel 0 (Diagrama de Contexto)**: una única burbuja que representa todo el sistema, mostrando solo sus relaciones con el exterior (qué entidades externas le mandan datos y qué les devuelve). Sin procesos internos visibles.
- **Nivel 1**: se "explosiona" esa burbuja única en subsistemas o módulos más concretos.
- **Nivel N**: se sigue bajando hasta funciones concretas, ya con detalle suficiente para definir almacenes de datos. Un almacén no tiene por qué corresponder 1:1 con una tabla física de la base de datos; es un concepto lógico, la implementación real se decide después en el modelo físico.
- Al llegar a niveles muy bajos, donde cada burbuja ya se podría programar directamente, se usa un [[Flujograma]] para describir el algoritmo interno de esa función.

> [!tip] Truco para recordar la jerarquía
> Contexto (0) → Subsistemas (1) → Funciones (N) → Algoritmo (flujograma). Cada nivel es un "zoom-in" del anterior, nunca información nueva de la nada.

[[Tipos de flujo de datos (DFD)]]
[[Reglas de construcción y balanceo (DFD)]]
[[B3 - T1.1 ENTIDAD RELACION]]
[[B3 - T4.2 UML]] (contraste con el diagrama de casos de uso: los casos de uso no "explotan" en niveles como el DFD)
