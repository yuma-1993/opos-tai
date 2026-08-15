**Entidad fuerte (o regular)**: tiene existencia e identidad propia, no depende de ninguna otra entidad para "tener sentido". Ej: `Autor`, `Pedido`.

**Entidad débil**: no tiene sentido por sí sola; necesita apoyarse en otra entidad (fuerte) para existir o para identificarse. Hay dos matices que hay que separar bien:

- **Débil en existencia**: necesita que exista otra entidad para poder existir ella, pero sí tiene un atributo propio que la identifica de forma única. Ej: `Factura` no tiene sentido sin un `Pedido` asociado, pero sí tiene su propio `número de factura` que la identifica sin ambigüedad.
- **Débil en identidad** (y por tanto también en existencia): ni existe sin la otra, ni tiene ningún atributo propio que la distinga por sí sola; necesita "tomar prestada" la clave de la entidad fuerte de la que depende. Ej: `Ejemplar` de un libro no tiene un identificador propio con sentido aislado — necesita la clave del `Libro` al que pertenece (debilidad "en cascada").

> [!tip] Truco para memorizarlo
> Pregúntate dos cosas por separado: ¿puede existir sin la otra entidad? (existencia) y ¿tiene un atributo propio que la identifique sin ayuda? (identidad). Si falla solo la 1 → débil en existencia. Si fallan las dos → débil en existencia e identidad.

En la notación de Chen, la entidad débil se dibuja con rectángulo de doble línea, y su clave parcial (discriminante) con el nombre subrayado en línea discontinua, para distinguirla de una clave primaria "normal". Ver [[Notación de Chen]].

Al transformar al modelo relacional (Tema 1.2), la entidad débil se traduce en una tabla cuya clave primaria incluye la FK de la entidad fuerte de la que depende. Ej: `Factura(ID_Factura)` → `LineaFactura(ID_Factura, NumLinea)`, donde `ID_Factura` es FK y forma parte de la PK de `LineaFactura`. Es el mismo concepto de debilidad, ya aplicado a tablas.

[[B3 - T1.1 ENTIDAD RELACION]]
[[B3 - T1.2 DISENO BBDD]]
