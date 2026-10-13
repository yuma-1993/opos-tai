Quiero una sesión de machaque intensivo de datos duros (cifras,
artículos, plazos, mayorías, jerarquías, listas cerradas, pares
confundibles) sobre mi bóveda de estudio TAI.

Tema, temas, o alcance que quiero machacar hoy (déjalo vacío, o pon
"repaso"/"lo que toque", para que se calcule solo a partir de lo que
toca repasar y de mis dudas pendientes):

$ARGUMENTS

## Delegación

No ejecutes tú mismo la sesión. Usa el tool `Agent` con
`subagent_type: opos-memoriza`, pasándole en el prompt:
- El alcance exacto de `$ARGUMENTS` tal cual lo he escrito (si está
  vacío, dile explícitamente que estoy pidiendo modo AGENDA).
- Que es una invocación directa de `/memorizar` (no viene de `/opos`),
  así que si tras cerrar la sesión quiero además registrar el
  resultado en el repaso espaciado, pregúntamelo tú y si digo que sí,
  invoca a continuación `opos-repaso` en modo REGISTRAR con cada línea
  `RESULTADO` que entregue `opos-memoriza`.

No dupliques aquí la lógica del examen, el banco de ítems, ni las
reglas de corrección — todo eso vive en `opos-memoriza.md` para no
mantener dos copias de las mismas reglas. Tu único trabajo en este
comando es interpretar `$ARGUMENTS`, delegar, y encadenar el registro
final si se pide.
