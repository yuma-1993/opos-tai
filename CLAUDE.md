# Opos TAI — Bóveda de estudio

Este proyecto es una bóveda de Obsidian (`opostai/`) con el temario de
las oposiciones de **TAI (Técnico Auxiliar de Informática)**, abierta
en VS Code para poder editarla y trabajar sobre ella con Claude Code.
El objetivo no es solo tener el temario transcrito, sino **fijarlo a
largo plazo**: notas bien conceptualizadas, no solo bien resumidas.

## Estructura

```
opostai/                    ← raíz de la bóveda de Obsidian
  Bloque 2/
    B2 - T1 INFORMATICA BASICA.md
  ...
.claude/
  commands/
    socratico.md            ← comando de estudio activo (ver abajo)
```

Convención de carpetas: una carpeta por **Bloque** del temario, y
dentro un archivo `.md` por **Tema** (nombrado `B<bloque> - T<tema>
<TÍTULO>.md`).

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

### `/opos`

Orquestador del sistema de estudio: repasar, testear, examen tipo
test, auditar la bóveda, completar/crear un tema a partir de recuerdo
activo (`opos-sintesis`), importar un PDF externo de golpe
ampliándolo y enlazándolo con el resto de la bóveda (`opos-importar`),
o trocear un tema ya escrito en conceptos sueltos enlazables dentro de
`notas/` (`opos-conceptos`). Ver `.claude/commands/opos.md` y los
agentes en `.claude/agents/`.

## Pendiente / próximos pasos

- Extender `opos-importar` a un directorio completo de PDFs (una nota
  por PDF en lote), en vez de un PDF a la vez.
