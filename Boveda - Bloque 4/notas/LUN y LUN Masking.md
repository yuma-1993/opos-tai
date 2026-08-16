Un **LUN (Logical Unit Number)** es una unidad lógica de almacenamiento, un trozo recortado de una cabina de discos ([[SAN (Storage Area Network)|SAN]]).

El **LUN Masking** es el mecanismo que define qué equipos pueden ver determinados LUN: aunque un host esté conectado a la misma cabina (e incluso a la misma zona del switch, ver [[Zoning (SAN)|Zoning]]), el LUN Masking es lo que decide, a nivel de la propia cabina, qué LUN concreto puede ver cada host.

> [!note] Conocimiento general (no viene literal del tema)
> Zoning y LUN Masking se suelen combinar y operan a distinto nivel: primero el zoning segmenta la red a nivel del switch FC (qué puertos "se ven"), y después el LUN Masking afina el acceso a discos concretos dentro de esa zona, a nivel de la cabina/array.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[Zoning (SAN)]] — el otro mecanismo de control de acceso en una SAN, a nivel de switch en vez de a nivel de cabina.
- [[SAN (Storage Area Network)]] — el entorno donde existen LUN y LUN Masking.
