---
description: Simulacro del examen oficial TAI de acceso libre en PDF (o corregir uno ya hecho). Úsalo SIEMPRE que el usuario diga algo como "vamos a hacer un examen real", "hazme un examen real", "examen como el oficial", "simulacro", "examen de verdad", "examen en PDF" o "corrige mi simulacro" — no confundir con opos-examen (50 preguntas de un tema en el chat).
---

Quiero un simulacro del examen oficial de TAI (acceso libre) en PDF,
o corregir uno que ya he hecho.

Argumentos (vacío, temas, o `corregir <id|último> <respuestas> [supuesto I|II] [impugno la N porque …]`):

$ARGUMENTS

## Paso 1 — ¿Generar o corregir?

- Si `$ARGUMENTS` empieza por `corregir`, ve al paso 3.
- Si no, es GENERAR.

## Paso 2 — GENERAR: preguntar los temas nada más empezar

Si `$ARGUMENTS` está vacío o no identifica temas concretos, **lo
primero** es preguntarme sobre qué temas quiero el examen:

1. Lista los temas disponibles. Son los `.md` de
   `C:\Users\PC\Desktop\Opos tai\Boveda - Bloque N\Bloque N\` para
   N = 1–4, agrupados por bloque, con su código (`B1-T1 CONSTITUCION`,
   `B3-T3 SQL`, …).
2. Pregúntame cuáles quiero. Valen:
   - códigos sueltos;
   - bloques enteros («Bloque 1»);
   - «todo» (simulacro completo con 80 + supuesto);
   - una descripción aproximada.
3. Recuérdame en una línea:
   - que el tamaño se ajusta solo al peso real de cada tema en los
     exámenes;
   - que si elijo temas del Bloque 3 y/o 4 habrá supuesto práctico (si
     hay de los dos, dos supuestos para elegir uno).

Con los temas ya claros, usa el tool `Agent` con
`subagent_type: opos-simulacro`. En el prompt pásale `MODO GENERAR` y
la lista exacta de notas resuelta: códigos y rutas de los `.md`.

Cuando termine, enséñame su informe tal cual: rutas de los PDF,
composición, tiempo y cómo pedir la corrección. **No me muestres
preguntas ni respuestas.**

## Paso 3 — CORREGIR

1. Extrae de `$ARGUMENTS` estos datos:
   - el `id` (o «último»);
   - las respuestas;
   - el supuesto elegido;
   - las impugnaciones, si hay.
2. Si falta algo imprescindible, pregúntamelo antes de delegar:
   - si no hay respuestas;
   - si el examen tiene dos supuestos y no he dicho cuál elegí (sin
     elección, la 2ª parte no se corrige, como en el examen real).
3. Usa `Agent` con `subagent_type: opos-simulacro`, `MODO CORREGIR`, y
   todo lo anterior literal.
4. Muéstrame la corrección completa.
5. Después pregúntame si quiero:
   - (a) registrar cada línea `RESULTADO` en el repaso espaciado. Si
     digo que sí, invoca `opos-repaso` en modo REGISTRAR, una vez por
     tema;
   - (b) apuntar los fallos como dudas nuevas en `_dudas.md`. Si digo
     que sí, añade tú las filas con el formato de esa tabla.

No dupliques aquí la lógica de generación ni de corrección: vive en
`.claude/agents/opos-simulacro.md` y en `.claude/scripts/simulacro.py`.
