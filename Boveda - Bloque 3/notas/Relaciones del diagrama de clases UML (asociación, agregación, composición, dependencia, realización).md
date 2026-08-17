El [[Diagrama de clases (UML)|diagrama de clases]] de UML distingue cinco tipos de relación entre clases:

| Relación | Símbolo | Significado |
|---|---|---|
| **Asociación** | línea simple | relación general entre clases; una línea se traduce en un atributo |
| **Agregación** | ◇ (rombo hueco) | contención **lógica** — ojo: es un significado distinto al de la [[Agregación (E-R)|agregación del modelo E-R]] |
| **Composición** | ◆ (rombo relleno) | contención **física**, relación todo/parte |
| **Dependencia** | `- - - ->` (flecha discontinua) | tiene que ir estereotipada para tener sentido; especifica una semántica entre dos clases o entidades |
| **Realización** | `......▷` (flecha discontinua, punta hueca) | una clase implementa una interface |

Agregación y composición son ambas **tipos de asociación** (contención de un objeto dentro de otro), y se diferencian en si esa contención es solo lógica (agregación, la parte puede sobrevivir sin el todo) o física (composición, la parte no tiene sentido sin el todo). Una asociación en este diagrama tiene consecuencias directas en la implementación.

[[Diagrama de clases (UML)]]
[[B3 - T4.2 UML]]
