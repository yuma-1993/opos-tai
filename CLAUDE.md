# Opos TAI — Bóveda de estudio

Este proyecto es el temario de las oposiciones de **TAI (Técnico
Auxiliar de Informática)**, abierto en VS Code para poder editarlo y
trabajar sobre él con Claude Code. El objetivo no es solo tener el
temario transcrito, sino **fijarlo a largo plazo**: notas bien
conceptualizadas, no solo bien resumidas.

## Estructura

La raíz del proyecto **no** es un único vault de Obsidian: contiene
**4 vaults de Obsidian independientes**, uno por Bloque del temario
(cada uno con su propia carpeta `.obsidian/`), más la configuración de
Claude Code:

```
Boveda - Bloque 1/           ← vault de Obsidian independiente
  .obsidian/
  Bloque 1/
    B1 - T1 <TÍTULO>.md
  notas/
  Ejercicios/
Boveda - Bloque 2/           ← vault de Obsidian independiente
  .obsidian/
  Bloque 2/
    B2 - T1 INFORMATICA BASICA.md
  notas/
  _repasos.md                ← registro de repaso espaciado (compartido
  _calibracion.md              entre los 4 bloques, vive aquí por ahora
  _examenes.md                  aunque no es específico del Bloque 2)
  _dudas.md                  ← registro de dudas/puntos flojos (mismo caso)
Boveda - Bloque 3/            ← vault de Obsidian independiente
  ...
Boveda - Bloque 4/            ← vault de Obsidian independiente
  ...
.claude/
  commands/
    socratico.md            ← comando de estudio activo (ver abajo)
  agents/                    ← subagentes de /opos
CLAUDE.md                    ← este archivo, en la raíz
```

Convención de carpetas dentro de cada `Boveda - Bloque N/`: la carpeta
`Bloque N/` tiene un archivo `.md` por **Tema** (nombrado `B<bloque> -
T<tema> <TÍTULO>.md`), y `notas/` tiene los conceptos sueltos
enlazables trocados de esos temas (ver `opos-conceptos`).

> Los registros compartidos del sistema de repaso (`_repasos.md`,
> `_calibracion.md`, `_examenes.md`, `_dudas.md`) están hoy dentro de
> `Boveda - Bloque 2/` por herencia histórica, no porque sean del
> Bloque 2 — son el registro único para los 4 bloques. Si en el futuro
> se mueven a la raíz del proyecto, hay que actualizar las rutas
> hardcodeadas en `.claude/agents/*.md` (`opos-dia`, `opos-repaso`,
> `opos-test`, `opos-examen`, `opos-memoriza`, `opos-metacognicion`,
> `opos-simulacro`)
> que hoy apuntan a esa ruta.

## Convención de cada nota de tema

Toda nota de tema sigue este esquema:

1. **Frontmatter YAML** al principio:
   ```yaml
   ---
   tags:
     - bloque<N>
     - tema<N>
     - <tags temáticos específicos, ej. arquitectura-computadores>
   bloque: <N>
   tema: <N>
   titulo: <título del tema>
   estado: por-repasar   # o: en-progreso / dominado
   ---
   ```
2. **Callout de apertura** (`> [!abstract]`) con un resumen de una o
   dos frases de qué contiene el tema y cómo se relacionan sus partes.
3. Contenido organizado en `##` (bloques temáticos grandes) y `###`
   (subtemas), nunca negrita usada como si fuera un encabezado.
4. **Callouts de Obsidian** para resaltar lo que hay que memorizar de
   forma distinta al resto:
   - `> [!important]` — idea clave para el examen, diferencia crítica
     entre dos conceptos que se prestan a confusión.
   - `> [!tip]` — truco mnemotécnico.
   - `> [!example]` — ejemplo resuelto o cálculo.
   - `> [!note]` — aclaración menor.
5. Tablas de Markdown siempre que el contenido sea comparativo o tipo
   glosario (mejor que listas largas de bullets).
6. Sección final **"🔑 Resumen ultra-rápido"**: lista compacta de todas
   las ideas clave del tema, pensada para repasos rápidos por
   repetición espaciada, no para primera lectura.

**Regla de oro al editar o generar notas: nunca se pierde información
del contenido original** (apuntes propios, fuente, PDF). Se puede
reestructurar, reordenar, convertir prosa en tabla/lista o completar
una frase cortada a partir de contenido que ya aparece en el propio
documento — pero no se inventan datos, cifras ni definiciones que no
estén ya en la fuente. Si hace falta un dato externo para que algo
tenga sentido, se dice explícitamente que es conocimiento general y no
parte del temario/fuente.

## Comandos disponibles

### `/socratico <tema o concepto>`

Sesión de estudio por diálogo socrático sobre un concepto ya existente
en la bóveda. Busca las notas relevantes (por contenido, título y
enlaces `[[...]]`), y luego hace preguntas una a una, exigiendo
comprensión real (no memorización de vocabulario), contrastando mis
respuestas contra el contenido literal de mis notas. No cierra la
sesión ni escribe nada en la bóveda por su cuenta — solo lo hace si yo
lo pido explícitamente.

Ver `.claude/commands/socratico.md` para el detalle completo de reglas.

### `/memorizar [tema(s) o vacío]`

Sesión de machaque intensivo de datos duros: cifras, artículos,
plazos, mayorías, jerarquías, listas cerradas y pares confundibles.
Mezcla modos de pregunta (recall en blanco, respuesta exacta,
enumeración, test tipo oposición con distractores reales) con
corrección inmediata y reintento dentro de la misma sesión — a
diferencia de `/socratico` (comprensión, no memorización literal) y de
`opos-test`/`opos-examen` (un único tema fijo). Si se invoca sin tema,
calcula el alcance solo cruzando `_repasos.md` (lo que toca repasar
hoy) y `_dudas.md` (dudas sin resolver), y lo propone antes de
empezar. Por defecto no modifica la bóveda: solo si se pide, registra
dudas nuevas/resueltas en `_dudas.md` o exporta a Anki.

Es un comando delegador: `.claude/commands/memorizar.md` invoca al
subagente `opos-memoriza` (`.claude/agents/opos-memoriza.md`), donde
vive toda la lógica real, para no duplicarla entre comando y agente.

### `/simulacro [temas | corregir <id> <respuestas>]`

Simulacro del examen oficial de TAI por **acceso libre**, con el
formato de la convocatoria del 22-12-2025 y los criterios de la CPS del
18-05-2026. Se genera en PDF.

- **Disparadores**: se activa (vía `/simulacro`) cuando digo algo como
  «vamos a hacer un examen real», «examen real», «examen de verdad»,
  «simulacro» o «examen en PDF». No confundir con `opos-examen` (50
  preguntas de un solo tema en el chat).
- **Arranque**: lo primero que hace es preguntar los temas de la bóveda.
- **Tamaño**: proporcional al peso real de cada epígrafe en los
  exámenes de 2024–2025, con un mínimo de 8 preguntas por tema y un
  máximo de 80 + 5 de reserva.
- **Supuesto práctico**: se añade si entran temas del Bloque 3
  (Supuesto I) o del Bloque 4 (Supuesto II). Si entran los dos, hay que
  elegir uno, como en el examen real.
- **Preguntas**: son nuevas y salen solo de las notas, con el estilo
  INAP.
- **Entrega**: dos PDF en `examenes/simulacros/<fecha>_<temas>/`.
  `cuestionario.pdf` incluye la hoja de respuestas. `plantilla.pdf`
  lleva las respuestas justificadas con su cita de la nota.
- **Corrección**: `/simulacro corregir <id> 1a 2c 3- … S1b …`. Aplica
  A − E/3, el corte del 50 % y la escala 0–50, admite impugnaciones
  (que anulan la pregunta y entra la reserva) y registra el resultado
  en `_examenes.md`.

Es un comando delegador: la lógica vive en el agente `opos-simulacro`
(`.claude/agents/opos-simulacro.md`), y la maquetación y las cuentas en
`.claude/scripts/simulacro.py` (HTML → PDF con Edge en modo headless).

El material de referencia está en `examenes/_banco/`:
- texto de los exámenes 2018–2025, con OCR de los escaneados;
- plantillas de 2025;
- criterios y bases;
- un `README.md` con la guía de estilo, el peso por epígrafe y la
  correspondencia entre programa y bóveda. Hay que actualizar esa tabla
  si se añaden temas o exámenes.

### `/opos`

Orquestador del sistema de estudio: repasar, testear, examen tipo
test, simulacro oficial en PDF (`opos-simulacro`), machacar datos duros (`opos-memoriza`), auditar la bóveda,
completar/crear un tema a partir de recuerdo activo (`opos-sintesis`),
importar un PDF externo de golpe ampliándolo y enlazándolo con el
resto de la bóveda (`opos-importar`), o trocear un tema ya escrito en
conceptos sueltos enlazables dentro de `notas/` (`opos-conceptos`).
Ver `.claude/commands/opos.md` y los agentes en `.claude/agents/`.

## Pendiente / próximos pasos

- Extender `opos-importar` a un directorio completo de PDFs (una nota
  por PDF en lote), en vez de un PDF a la vez.
