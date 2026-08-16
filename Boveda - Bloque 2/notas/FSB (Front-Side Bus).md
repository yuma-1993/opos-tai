El **FSB** (Front-Side Bus) fue, durante años, el bus principal que conectaba la CPU con el resto del sistema: memoria y chipset. Es el ejemplo físico y real de lo que en [[Reloj]] se llama **reloj externo** — la velocidad del FSB la marca el reloj del sistema, y sobre ella la CPU aplica su factor multiplicador para obtener su reloj interno.

> [!example] Recordatorio del cálculo
> Reloj externo (FSB) 100 MHz × multiplicador ×36 = reloj interno de la CPU a 3,6 GHz. Ver [[Reloj]].

## Por qué se abandonó

El FSB era un **bus compartido**: memoria, chipset y CPU se repartían el mismo camino. A medida que las CPU se hicieron más rápidas y con más núcleos, ese bus único se convirtió en un **cuello de botella** — demasiado tráfico peleando por la misma vía.

La solución fue sustituirlo por enlaces **punto a punto** dedicados, cada uno con su propio ancho de banda, sin compartir camino con los demás:

| Fabricante | Sucesor del FSB | Función |
|---|---|---|
| **Intel** | **QPI** (QuickPath Interconnect) | Enlace de alta velocidad CPU ↔ chipset/otras CPU |
| **Intel** | **DMI** (Direct Media Interface) | Conexión específica entre **Northbridge** (Chipset Norte) y **Southbridge** (Chipset Sur) |
| **AMD** | **HyperTransport** | Equivalente de AMD a QPI |

> [!note] Encaja con la arquitectura Norte/Sur
> Northbridge (rápido: memoria) y Southbridge (lento: E/S) — ver [[B2 - T1 INFORMATICA BASICA]] — son precisamente los dos extremos que el FSB unía en un solo bus compartido, y que QPI/DMI/HyperTransport separan en enlaces dedicados independientes.

---

**Conexiones con otros conceptos TAI:**
- [[Reloj]] — el FSB es el "reloj externo" en la práctica.
- [[B2 - T1 INFORMATICA BASICA]] — Northbridge/Southbridge, chipset.
- [[Bus de comunicación]] — el FSB como caso concreto de bus compartido, frente a los enlaces punto a punto que lo sustituyen.
- [[CPU - Central Processing Unit]] — el multiplicador de reloj que parte del reloj externo del FSB.
