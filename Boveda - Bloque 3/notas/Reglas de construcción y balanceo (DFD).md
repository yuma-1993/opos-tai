Reglas de construcción de un [[DFD - Diagrama de Flujo de Datos|DFD]], muy preguntadas en examen:

1. **Los flujos son direccionales**: siempre llevan flecha, indicando el sentido en el que viaja el dato.
2. **Flujos permitidos** — solo estas tres combinaciones:
   - Proceso ↔ Proceso
   - Proceso ↔ Almacén
   - Proceso ↔ Entidad externa
3. **Descomponibilidad**: tanto los flujos de datos como los almacenes se pueden descomponer en niveles más bajos, igual que los procesos (un almacén "Clientes" en nivel 1 puede abrirse en varios almacenes más específicos en nivel 2).
4. **Balanceo entre niveles**: todos los niveles del DFD deben ser coherentes entre sí. Todo lo que aparece en el nivel N debe tener su origen en el nivel N-1; no se puede inventar una flecha nueva hacia una entidad externa en el nivel N si esa relación no existía ya anunciada en el nivel N-1. Al hacer zoom-in solo se puede detallar lo que ya estaba, nunca añadir relaciones externas nuevas.

> [!important] Flujo prohibido
> Almacén ↔ Almacén directamente. Nunca puede haber una flecha entre dos almacenes sin que medie un proceso. Un almacén es pasivo, no tiene "vida propia". Si los datos tienen que moverse de un almacén a otro, hace falta un proceso que los lea, los procese (aunque sea mínimamente) y los vuelva a escribir.

[[B3 - T1.1 ENTIDAD RELACION]]
