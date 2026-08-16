De más rápida/cara/pequeña a más lenta/barata/grande, todo lo que "recuerda algo" en un ordenador forma una única escalera. Cada nivel existe para tapar el hueco de velocidad entre el de arriba y el de abajo — el mismo patrón de [[Caching]] aplicado una y otra vez.

| Nivel | Velocidad | Coste/bit | Capacidad típica | Nota dedicada |
|---|---|---|---|---|
| **Registros** | Máxima | Máximo | Unas pocas decenas de valores | [[Registros clave]] |
| **Caché (L1→L2→L3)** | Muy alta → alta | Alto | KB → decenas de MB | [[Memoria Caché]] |
| **Memoria principal (RAM)** | Media | Medio | GB | [[Memoria RAM]] |
| **Almacenamiento secundario** | Baja | Bajo | TB | [[HDD (Hard Disk Drive)]], [[SSD (Solid State Drive)]] |

> [!important] La regla que explica toda la jerarquía
> A medida que bajas de nivel: **sube la capacidad, baja la velocidad, baja el coste por bit**. Ningún nivel podría hacer el trabajo de los demás — registros no dan para GB de datos, y un SSD no puede responder a la velocidad de un ciclo de reloj.

> [!tip] Por qué no hay un único nivel "que lo haga todo"
> Una memoria del tamaño/precio de la RAM pero a la velocidad de un registro sería inviable de fabricar a gran escala; y una memoria tan barata como un disco pero tan rápida como la caché, tampoco. Cada nivel es el mejor compromiso posible con la tecnología disponible en su rango de velocidad/coste — por eso conviven varios en cascada, cada uno tapando el hueco del siguiente.

---

**Conexiones con otros conceptos TAI:**
- [[Registros clave]], [[Memoria Caché]], [[Memoria RAM]] — desarrollo completo de cada nivel superior de la pirámide.
- [[HDD (Hard Disk Drive)]], [[SSD (Solid State Drive)]] — el escalón de almacenamiento secundario.
- [[Caching]] — el principio general que conecta cada nivel con el siguiente.
- [[B2 - T1 INFORMATICA BASICA]] — versión resumen de examen (§12).
