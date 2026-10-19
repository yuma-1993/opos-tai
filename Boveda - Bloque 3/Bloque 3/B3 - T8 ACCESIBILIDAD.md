---
tags:
  - bloque3
  - tema8
  - accesibilidad
  - wcag
  - wai-aria
  - usabilidad
  - rd-1112-2018
  - seguridad-desarrollo
bloque: 3
tema: "8"
titulo: "Accesibilidad (WAI, WCAG 2.2, RD 1112/2018), usabilidad y seguridad en el desarrollo"
estado: por-repasar
---

# Tema 8 · Bloque 3 — Accesibilidad

> [!abstract] De qué va este tema
> La accesibilidad web se regula técnicamente con las normas WAI del W3C (UAAG, ATAG, ACT, EARL, ARIA, WCAG), de las que la WCAG 2.2 (4 principios, 13 pautas, 86 criterios, 3 niveles A/AA/AAA) es la central. En España, el Real Decreto 1112/2018 obliga al sector público a cumplir el nivel AA, con declaración de accesibilidad, mecanismos de quejas y seguimiento periódico ante la UE. El tema se completa con usabilidad (UX), herramientas de cifrado en puestos de usuario y conceptos de seguridad en el desarrollo.

> [!important] Actualización 20/05/2026
> El listado de actualizaciones de Velilla recoge **cuatro cambios** que afectan a este tema, aplicados en las secciones correspondientes: (1) WCAG 2.2 tiene **86 criterios** frente a los **78 de la 2.1**; (2) el RD 1112/2018 **no aplica a empresas con más de 100 empleados o que facturen más de 6 millones de euros**; (3) en Normativa → Contenidos → Documentos son **ofimáticos, no informáticos**; (4) **`article` no es un landmark**. Además, el 24/08/2024 se actualizaron las versiones: **ARIA 1.2** y **WCAG 2.2** (con su gráfico).

---

## 1. Normas WAI (Web Accessibility Initiative) del W3C

| Norma | Nombre | Qué regula |
|---|---|---|
| **UAAG 2.0** | User Agent Accessibility Guidelines | Normas que deben cumplir los **user agents**: cualquier agente que accede al contenido web (navegadores, extensiones del navegador, asistentes, etc.). **5 principios**: Perceptible, Operable, Comprensible, Acceso Programático, Especificaciones (admite otras especificaciones como la WCAG) |
| **ATAG 2.0** | Authoring Tool Accessibility Guidelines | Normas que deben seguir las **herramientas de autor**. Debe ser accesible tanto **la herramienta como el contenido generado**. Herramienta de autor: un editor HTML (WYSIWYG) de una web de gestión de foros, un CMS, blogs, wiki, foros, incluso un procesador de texto con opción "Guardar como HTML" o EPUB. **Dos partes, cada una con 4 principios** |
| **ACT** | Accessibility Conformance Testing | Especifica cómo deben ser las **reglas** a evaluar, el formato de las reglas de los sistemas de evaluación que realizan los test de conformidad. **Formato de entrada** |
| **EARL** | Evaluation And Report Language | Especifica el formato de los **resultados** de una evaluación (basado en **RDF**). **Formato de salida** |
| **ARIA 1.2** | Accessible Rich Internet Applications | Accesibilidad para páginas con una **interfaz compleja**, con muchos elementos gráficos de datos como árboles, elementos colapsables, widgets, AJAX, etc. |
| **WCAG 2.2** | Web Content Accessibility Guidelines | Accesibilidad referida al **contenido web en sí mismo** |

> [!tip] Entrada / salida
> **ACT** = reglas de **entrada** al evaluador; **EARL** = formato de **salida** (resultados, RDF).

> [!example] Esquema W3C ⊃ WAI (gráfico del PDF)
> **W3C** contiene a **WAI** (Guidelines and Techniques: WCAG 2.0, ATAG 2.0 (draft), UAAG 2.0 (draft), ARIA; y UAWG, *Working Groups*), que se relaciona con las **Technical Specs**: HTML, XML, CSS, SVG, SMIL, etc.

---

## 2. WAI-ARIA

Recursos mediante **roles** y **estados/propiedades**.

| Función | Mecanismo | Detalle |
|---|---|---|
| Estructuración semántica del documento | Atributo `role` | Define zonas funcionales llamadas **LandMarks** (main, banner, navigation, search, etc.). Los roles son valores predefinidos para cada tipo y tienen correspondencia con los componentes de un framework como Bootstrap |
| Navegación mediante teclado | Atributo `tabindex` | — |
| Áreas que se actualizan dinámicamente | Atributo `aria-live` | Una región *live* o activa es aquella donde cambia el contenido sin que el usuario intervenga, como un anuncio |
| Informar sobre los widgets | `role` + `aria-*` de estado | Indica qué son y el estado que tienen |

```html
<div id="…" role="navigation"> … </div>
<div id="…" role="tabpanel" aria-expanded="false"> … </div>
```

> [!important] Actualización 20/05/2026 (entrada del 02/11/2025)
> Corrección: **`article` NO es un landmark.** Los landmarks son zonas funcionales como main, banner, navigation, search...

---

## 3. WCAG

**4 principios, 13 pautas, 86 criterios y más de 580 técnicas.** Los principios tienen pautas y éstas criterios de conformidad.

> [!important] Actualización 20/05/2026
> **WCAG 2.2: 86 criterios de conformidad**, frente a los **78 de la versión 2.1**.

- **Principios**: fundamentos de la accesibilidad web: **perceptible, operable, comprensible y robusto**.
- **Pautas**: objetivos básicos que los autores deben lograr para crear un contenido más accesible para los usuarios con discapacidad.

### 3.1 Principios y pautas

| Principio | Idea | Pauta (nº) | Qué exige |
|---|---|---|---|
| **Perceptible** | La información y los componentes deben mostrarse a los usuarios en formas que ellos puedan entender | **1.1** Texto alternativo (alternativas textuales) | Para el contenido que no sea textual, para poder ser transformado en otros formatos necesarios (braille, voz, símbolos, etc.) |
| | | **1.2** Contenido multimedia dependiente del tiempo (medios basados en el tiempo) | Alternativas sincronizadas para contenidos multimedia dependientes del tiempo |
| | | **1.3** Adaptable | Contenido que pueda presentarse de diferentes formas sin perder información ni estructura |
| | | **1.4** Distinguible | Facilitar a los usuarios ver y escuchar el contenido, incluyendo la distinción entre lo más y menos importante |
| **Operable** | Los componentes de la interfaz de usuario y la navegación deben ser manejables, permitiendo la interacción | **2.1** Teclado accesible | Poder controlar todas las funciones desde el teclado |
| | | **2.2** Tiempo suficiente | Tiempo suficiente para leer y utilizar el contenido |
| | | **2.3** Ataques epilépticos (convulsiones y reacciones físicas) | No diseñar contenido que pueda causar ataques epilépticos |
| | | **2.4** Navegación (navegable) | Formas de ayudar a navegar, a buscar contenido y a determinar dónde están |
| | | **2.5** Modalidades de entrada | Operar la funcionalidad a través de varios métodos de entrada además del teclado |
| **Comprensible** | La información y las operaciones de usuario deben ser comprensibles, entendibles | **3.1** Legible | Hacer el contenido de texto legible y comprensible |
| | | **3.2** Previsible | Hacer la apariencia y la forma de utilizar las páginas web previsibles |
| | | **3.3** Asistencia a la entrada de datos (ayuda para la entrada) | Los asistentes evitarán y corregirán errores |
| **Robusto** | El contenido debe ser robusto para que pueda ser bien interpretado por una gran variedad de user agents, incluyendo asistentes | **4.1** Compatible | Maximiza la compatibilidad con los user agents actuales y futuros, incluyendo tecnologías de asistencia |

> [!tip] Recuento de pautas
> 4 principios → 13 pautas: 4 (1.1–1.4) + 5 (2.1–2.5) + 3 (3.1–3.3) + 1 (4.1).

> [!note] Ampliación (conocimiento general, no viene del PDF)
> En inglés los cuatro principios forman el acrónimo POUR: Perceivable, Operable, Understandable, Robust.

### 3.2 Mapa de WCAG 2.2: criterios por pauta y nivel

El PDF incluye el "Mapa de WCAG 2.2" (Intopia, traducido por Carlos Muncharaz Rodríguez). **Clave**: ✱ = novedad en WCAG 2.2.

### Principio 1 — Perceptible

| Pauta | Nivel A | Nivel AA | Nivel AAA |
|---|---|---|---|
| **1.1 Alternativas textuales** | 1.1.1 Contenido no textual | — | — |
| **1.2 Medios basados en el tiempo** | 1.2.1 Audio solo o vídeo solo (grabado) · 1.2.2 Subtítulos (grabado) · 1.2.3 Audiodescripción o medios alternativos (grabado) | 1.2.4 Subtítulos (en directo) · 1.2.5 Audiodescripción (grabado) | 1.2.6 Lengua de signos (grabado) · 1.2.7 Audiodescripción extendida (grabado) · 1.2.8 Medios alternativos (grabado) · 1.2.9 Audio solo (en directo) |
| **1.3 Adaptable** | 1.3.1 Información y relaciones · 1.3.2 Secuencia significativa · 1.3.3 Características sensoriales | 1.3.4 Orientación · 1.3.5 Identificación del propósito de entrada | 1.3.6 Identificación del propósito |
| **1.4 Distinguible** | 1.4.1 Uso del color · 1.4.2 Control del audio | 1.4.3 Contraste (mínimo) · 1.4.4 Cambio de tamaño del texto · 1.4.5 Imágenes de texto · 1.4.10 Reajuste · 1.4.11 Contraste no textual · 1.4.12 Espaciado del texto · 1.4.13 Contenido en puntero o en foco | 1.4.6 Contraste (aumentado) · 1.4.7 Audio de fondo bajo o inexistente · 1.4.8 Presentación visual · 1.4.9 Imágenes de texto (sin excepción) |

### Principio 2 — Operable

| Pauta | Nivel A | Nivel AA | Nivel AAA |
|---|---|---|---|
| **2.1 Teclado accesible** | 2.1.1 Teclado · 2.1.2 Sin atrapamiento del teclado · 2.1.4 Teclas de atajo | — | 2.1.3 Teclado (sin excepción) |
| **2.2 Tiempo suficiente** | 2.2.1 Tiempo ajustable · 2.2.2 Pausar, detener, ocultar | — | 2.2.3 Sin límite de tiempo · 2.2.4 Interrupciones · 2.2.5 Reautentificación · 2.2.6 Expiración de tiempo |
| **2.3 Convulsiones y reacciones físicas** | 2.3.1 Umbral de tres destellos o menos | — | 2.3.2 Tres destellos · 2.3.3 Animaciones tras interacción |
| **2.4 Navegable** | 2.4.1 Salto de bloques · 2.4.2 Página titulada · 2.4.3 Orden del foco · 2.4.4 Propósito del enlace (en contexto) | 2.4.5 Múltiples vías · 2.4.6 Encabezados y etiquetas · 2.4.7 Foco visible · 2.4.11 Foco no oculto (mínimo) ✱ | 2.4.8 Localización · 2.4.9 Propósito del enlace (enlace solo) · 2.4.10 Encabezados de sección · 2.4.12 Foco no oculto (aumentado) ✱ · 2.4.13 Apariencia del foco ✱ |
| **2.5 Modalidades de entrada** | 2.5.1 Gestos del puntero · 2.5.2 Cancelación del puntero · 2.5.3 Etiqueta en el nombre · 2.5.4 Actuación del movimiento | 2.5.7 Movimientos de arrastre ✱ · 2.5.8 Tamaño del objetivo (mínimo) ✱ | 2.5.5 Tamaño del objetivo (aumentado) · 2.5.6 Mecanismos de entrada concurrentes |

### Principio 3 — Comprensible

| Pauta | Nivel A | Nivel AA | Nivel AAA |
|---|---|---|---|
| **3.1 Legible** | 3.1.1 Idioma de la página | 3.1.2 Idiomas de las partes | 3.1.3 Palabras inusuales · 3.1.4 Abreviaturas · 3.1.5 Nivel de lectura · 3.1.6 Pronunciación |
| **3.2 Predecible** | 3.2.1 En foco · 3.2.2 En entrada · 3.2.6 Ayuda consistente ✱ | 3.2.3 Navegación consistente · 3.2.4 Identificación consistente | 3.2.5 Cambio a petición |
| **3.3 Ayuda para la entrada** | 3.3.1 Identificación del error · 3.3.2 Etiquetas o instrucciones · 3.3.7 Entrada redundante ✱ | 3.3.3 Sugerencia para el error · 3.3.4 Prevención del error (legal, financiero, datos) · 3.3.8 Autentificación accesible (mínimo) ✱ | 3.3.5 Ayuda · 3.3.6 Prevención del error (todos) · 3.3.9 Autentificación accesible (aumentado) ✱ |

### Principio 4 — Robusto

| Pauta | Nivel A | Nivel AA | Nivel AAA |
|---|---|---|---|
| **4.1 Compatible** | 4.1.1 Validación (**eliminado en 2.2**) · 4.1.2 Nombre, rol, valor | 4.1.3 Mensajes de estado | — |

> [!important] Novedades de WCAG 2.2 (marcadas ✱ en el mapa)
> 2.4.11 Foco no oculto (mínimo) · 2.4.12 Foco no oculto (aumentado) · 2.4.13 Apariencia del foco · 2.5.7 Movimientos de arrastre · 2.5.8 Tamaño del objetivo (mínimo) · 3.2.6 Ayuda consistente · 3.3.7 Entrada redundante · 3.3.8 Autentificación accesible (mínimo) · 3.3.9 Autentificación accesible (aumentado). El criterio **4.1.1 Validación** se elimina en la 2.2.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Las siglas en inglés de los tres niveles son A (el más básico), AA y AAA (el más exigente). El nivel AA es el que exige la normativa española para el sector público (ver sección 5).

### 3.3 Requisitos / criterios de conformidad

- Alcanzar **uno de los 3 niveles** de conformidad (A, AA, AAA). Son **acumulativos**: para ser AA, debes cumplir A y AA.
- Aplicar a **páginas completas**.
- Aplicar a **procesos completos**, ya que un proceso puede implicar varias páginas.
- **No tener interferencias**: determinados contenidos no deben impedir el acceso al resto de la página.
- Usar **tecnologías compatibles con accesibilidad**, como PDF.

| Nivel | Debe satisfacer |
|---|---|
| **A** | Los criterios del Nivel A, o proporcionar una versión alternativa conforme A |
| **AA** | Los criterios de los Niveles A y AA, o proporcionar versión alternativa conforme AA |
| **AAA** | Los criterios de los Niveles A, AA y AAA, o versión alternativa AAA |

### 3.4 Declaración de conformidad y WCAG-EM

- **Declaración de conformidad**: usada para la **certificación**; contiene fecha, URI, título, tecnologías usadas, nivel de cumplimiento y versión.
- **WCAG-EM**: metodología para la **evaluación** de la accesibilidad, en 5 pasos: **1.** Definir el alcance · **2.** Explorar el sitio · **3.** Seleccionar muestra · **4.** Auditar la muestra · **5.** Elaborar el informe.
- **Servicio de diagnóstico en línea de la OAW**: la Oficina de Accesibilidad Web permite al personal de las AAPP solicitar una **revisión automática** de accesibilidad de sus sitios web conforme a la **Metodología para el Seguimiento Simplificado UNE-EN 301549:2022**, así como una revisión automática de la **Declaración de accesibilidad**. Disponible para los miembros de la Comunidad Accesibilidad.

### 3.5 Herramientas

| Evaluación / Testing | Magnificadores | Lectores de pantalla |
|---|---|---|
| Koa11y | LunarPlus | JAWS |
| AChecker | ZoomText | NVDA |
| Cynthia says | Magic | Windows Eyes |
| taw | | Orca (GNOME) |
| WAVE | | Voice Over (Mac OS) |
| tingtun | | Talk Back (Android) |
| eXaminator | | |
| validator.w3.org | | |
| Servicio online OAW | | |

**VINUX**: distribución Linux con este tipo de software. Especialmente diseñada para **ciegos** y personas con deficiencia visual.

---

## 4. Seguimiento y presentación de informes (esquema del PDF)

Basado en la **Decisión de Ejecución (UE) 2018/1524** (ver sección 5.6). Circuito del gráfico:

| Quién | Qué elabora | Cuándo / detalle |
|---|---|---|
| **Organismos del sector público** | **Informe de revisión de la accesibilidad**: TODOS los requisitos exigidos; revisión automática + revisión manual; debe cumplir las condiciones exigidas para las **Revisiones en profundidad** de la UE | **Fase de diseño**; antes de la puesta en funcionamiento; revisiones periódicas, **mínimo cada 3 años** |
| **Unidad responsable de accesibilidad** | (1) Informe de seguimiento sobre el cumplimiento de los requisitos de accesibilidad (incluye los informes de revisión realizados en ese año); (2) informe de seguimiento sobre la promoción, concienciación y formación; (3) informe sobre la atención de quejas y reclamaciones | **1 vez al año, antes del 1 de octubre** de cada año, hacia el Ministerio |
| **Ministerio (MAETD, Ministerio de Asuntos Económicos y Transformación Digital)** | Resultados del seguimiento anual + informe sobre el resultado del seguimiento (con información de cada uno de los periodos y de ambos métodos) | **Cada 3 años (2024, 2027, 2030…)** hacia la Unión Europea. **Periodo anual: 1 enero – 22 diciembre** |

| Método de seguimiento (gráfico) | Alcance | Detalle |
|---|---|---|
| **Seguimiento Simplificado** | **1008 sitios web en 2022** y **1475 sitios web a partir de 2023** | Subconjunto de requisitos; pruebas automatizadas; realizado por el MAETD |
| **Seguimiento en Profundidad** | **84 sitios web y 53 apps** | TODOS los requisitos; se usarán los informes de revisión de accesibilidad facilitados por los organismos, que serán verificados y agregados por el MAETD |

---

## 5. Normativa referente a la accesibilidad

### 5.1 Qué es el RD 1112/2018

El **Real Decreto 1112/2018** es una transposición de la **Directiva Europea 2016/2102** (normativa técnica) y de la **Decisión de Ejecución 2018/1524** (metodología de seguimiento). La normativa técnica viene recogida en la **EN 301 549 (UNE-EN 301 549)**, donde se hace referencia a la **WCAG 2.1**.

Determina la accesibilidad de los **sitios web y aplicaciones para dispositivos móviles**, debiendo cumplir el **nivel de conformidad AA**.

| Ámbito | En vigor desde |
|---|---|
| Webs | **20/09/2018** |
| Intranets y extranets | **23/09/2019** |
| Apps (móviles) | **23/06/2021** |

> [!important] Actualización 20/05/2026 (entrada del 03/04/2026)
> **El RD 1112/2018 no aplica a empresas con más de 100 empleados o que facturen más de 6 millones de euros.** (Se transcribe literalmente el enunciado del listado de actualizaciones; el sentido exacto del umbral conviene contrastarlo con la norma antes del examen.)

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Una Directiva europea no se aplica directamente a los ciudadanos: obliga a los Estados a "transponerla" a su derecho interno, que aquí se hace mediante un Real Decreto. Ver [[Instrumentos jurídicos de la Unión Europea (Reglamento, Directiva, Decisión, Recomendación)]].

### 5.2 ¿A qué contenidos aplica?

| Tipo de contenido | Detalle |
|---|---|
| Textuales y no textuales | Imágenes, etc. |
| **Documentos** y formularios descargables | **Ofimáticos**, PDF, etc. |
| Contenidos multimedia pregrabados | De **base temporal**, independiente de la plataforma de difusión (YouTube, Twitter, etc.), con **excepción del servicio público de radiodifusión** |
| Formas de interacción (persona-sitio) | Formularios digitales, procesos de firma, procesos de pago, etc. |

> [!important] Actualización 20/05/2026 (entrada del 04/11/2025)
> Corrección en Normativa → Contenidos → Documentos: son **ofimáticos, no informáticos**.

### 5.3 Excepción por carga desproporcionada

Aquella que impone a la entidad obligada una **carga financiera y organizativa excesiva**, o que compromete su capacidad para cumplir su cometido o para publicar la información necesaria y pertinente para sus tareas y servicios, teniendo en cuenta al mismo tiempo el posible beneficio o perjuicio para los ciudadanos, en particular para las personas con discapacidad y personas mayores.

- **Debe motivarse.**
- Debe ser **excepcional** y **limitada a contenidos concretos**.
- **No se consideran motivos** que permitan apreciarla: la **falta de prioridad, de tiempo o de conocimientos**.

### 5.4 ¿A quién obliga?

- AGE / CCAA / EELL / Sector público institucional.
- Asociaciones constituidas por la Administración, entes y organismos que forman el sector público.
- Congreso / Senado / Consejo de Estado / CGPJ / TC / Defensor del Pueblo / Banco de España / Asambleas Legislativas de las CCAA.
- Administración de Justicia.
- **Entidades si reciben financiación pública.**
- Sitios web vinculados a la prestación de servicios públicos.
- Centros privados educativos sostenidos total o parcialmente con fondos públicos.

### 5.5 Comunicaciones, quejas y sugerencias; declaración; unidad responsable; certificación

**Mecanismos sobre comunicaciones, quejas y sugerencias sobre accesibilidad**: email habilitado o formulario · teléfono y oficina física de atención · Oficina de Atención a la Discapacidad · Defensor del Pueblo.

### Declaración de accesibilidad

- Acceso disponible **en todas las páginas** mediante el enlace "Accesibilidad" o equivalente en su idioma.
- Será revisada y actualizada **como mínimo anualmente**.
- Contenido mínimo:
  - Explicación sobre las partes del contenido que no sean accesibles, razones y alternativas.
  - Enlace y descripción del mecanismo de comunicación.
  - Enlace al procedimiento de reclamación en caso de respuesta insatisfactoria.

**Revisión de accesibilidad** mediante orden del MPTFP, determinando el modelo y las condiciones.

**Certificación de accesibilidad**: es **opcional** y la hace una entidad reconocida por la **[[ENAC]]**.

**Unidad responsable de accesibilidad** (hay que designarla). Funciones: coordinación de revisiones periódicas · atención de quejas, consultas, etc. · promoción y concienciación · informes.

### 5.6 Seguimiento y presentación de informes

- **Decisión de Ejecución 2018/1524 de la UE.**
- Reporte periódico **anual** de las unidades al Ministerio.
- Reporte periódico **cada 3 años** del Ministerio a Europa.
- Metodologías:

| Metodología | Aplica a |
|---|---|
| **Método Simplificado** | **Solo a sitios web** |
| **Metodología en Profundidad** | **Sitios web y apps.** Hay una para webs y otra para aplicaciones móviles |

Para el marco de la discapacidad y accesibilidad universal en el empleo y la igualdad, ver [[B1 - T5 IGUALDAD, DISCAPACIDAD, DEPENDENCIA Y LGTBI]] y [[Discapacidad]]; para el ENS, la certificación y la ENAC, [[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]].

---

## 6. Usabilidad web (UX)

- **10 principios heurísticos de Jakob Nielsen.**
- Métodos de evaluación de la usabilidad: **Sirius, WUEP (Web Usability Evaluation Process), User focus, HHS**.
- Una web es usable si es:

| Criterio | Significado |
|---|---|
| **Rápido** | Se encuentra lo buscado en menos de 4 segundos |
| **Simple** | Navegación sencilla |
| **Investigable** | Por los buscadores |
| **Compatible** | Para la mayoría |
| **Actualizada** | — |

- **Fundación SIDAR**: promueve el **Diseño Centrado en el Usuario (DCU)**: el usuario debe estar involucrado **desde el inicio** del proceso de diseño.
- **Grado de usabilidad**: pruebas empíricas; pruebas relativas (comparación con otros sistemas).

---

## 7. Confidencialidad en puestos de usuario

Herramientas para cifrar documentos y/o discos:

| Herramienta | Detalle |
|---|---|
| **BitLocker** (Windows) | Cifra discos. Por defecto usa **AES-CBC de 128 bits** de clave. También funciona con USB. Ver [[B2 - T4.2 WINDOWS Y SISTEMAS OPERATIVOS MOVILES]] |
| **EFS** | Trabaja sobre **NTFS** y permite cifrado de **archivos** |
| **TrueCrypt / VeraCrypt** | Cifran discos / particiones |
| **FileVault 2** | Cifra discos en **Mac** |
| **Cipher Shed**, **DiskCryptor**, **LUKS**, **GNU-PG** | Otras herramientas de cifrado |

---

## 8. Seguridad en el desarrollo de aplicaciones

Concepto: **la seguridad desde el inicio de la aplicación**. Herramienta de ayuda: **JFrog Xray**.

- **Proyecto OWASP**: principios **Security by Design**.
- **Ciclos de vida con la seguridad incluida (SSDLC)**: **MS SDL, NIST 800-64, OWASP CLASP**.

---

## 🔑 Resumen ultra-rápido

- WAI (W3C): **UAAG 2.0** (user agents; 5 principios) · **ATAG 2.0** (herramientas de autor; 2 partes × 4 principios) · **ACT** (formato de **entrada**, reglas) · **EARL** (formato de **salida**, RDF) · **ARIA 1.2** (interfaces complejas, widgets, AJAX) · **WCAG 2.2** (contenido web).
- WAI-ARIA: `role` (landmarks: main, banner, navigation, search; **article NO**), `tabindex` (teclado), `aria-live` (regiones dinámicas), `aria-*` de estado para widgets.
- WCAG: **4 principios** (perceptible, operable, comprensible, robusto), **13 pautas**, **86 criterios** (la 2.1 tenía 78) y +580 técnicas.
- Pautas: 1.1 alternativas textuales, 1.2 medios temporales, 1.3 adaptable, 1.4 distinguible · 2.1 teclado, 2.2 tiempo, 2.3 convulsiones, 2.4 navegable, 2.5 modalidades de entrada · 3.1 legible, 3.2 previsible, 3.3 ayuda a la entrada · 4.1 compatible.
- Niveles **A, AA, AAA acumulativos**; conformidad sobre páginas completas, procesos completos, sin interferencias, tecnologías accesibles.
- Novedades 2.2: 2.4.11, 2.4.12, 2.4.13, 2.5.7, 2.5.8, 3.2.6, 3.3.7, 3.3.8, 3.3.9; eliminado 4.1.1.
- WCAG-EM en 5 pasos: alcance, explorar, muestra, auditar, informe. OAW: revisión automática (UNE-EN 301549:2022) + declaración de accesibilidad.
- Herramientas: evaluación (Koa11y, AChecker, Cynthia says, taw, WAVE, tingtun, eXaminator, validator.w3.org, OAW) · magnificadores (LunarPlus, ZoomText, Magic) · lectores (JAWS, NVDA, Windows Eyes, Orca, VoiceOver, TalkBack) · VINUX (Linux para ciegos).
- **RD 1112/2018** = transposición de Directiva **2016/2102** + Decisión de Ejecución **2018/1524**; técnica: **EN 301 549** (→ WCAG 2.1); nivel **AA**; vigencia **webs 20/09/2018, intranets/extranets 23/09/2019, apps 23/06/2021**. No aplica a empresas >100 empleados o >6 M€ facturación (actualización 03/04/2026).
- Contenidos: textuales/no textuales, documentos **ofimáticos**/PDF y formularios descargables, multimedia pregrabado (excepto radiodifusión pública), formas de interacción (formularios, firma, pago).
- Carga desproporcionada: debe motivarse, excepcional y limitada; **no** valen falta de prioridad, tiempo o conocimientos.
- Declaración de accesibilidad: enlace "Accesibilidad" en todas las páginas, revisión **anual**, contenido mínimo (partes no accesibles + mecanismo + reclamación). Certificación **opcional** (entidad reconocida por **ENAC**). Unidad responsable de accesibilidad.
- Informes: unidades → Ministerio **anual** (antes del **1 de octubre**); Ministerio → UE **cada 3 años** (2024, 2027, 2030…). Simplificado (solo webs; 1008 sitios en 2022, 1475 desde 2023) vs Profundidad (webs y apps; 84 webs y 53 apps). Periodo anual 1 enero – 22 diciembre.
- UX: **10 heurísticos de Nielsen**; métodos Sirius, WUEP, User focus, HHS; usable = rápido (<4 s), simple, investigable, compatible, actualizada; **SIDAR** → Diseño Centrado en el Usuario.
- Cifrado en puesto de usuario: **BitLocker** (AES-CBC 128 por defecto, también USB), **EFS** (archivos sobre NTFS), TrueCrypt/VeraCrypt, **FileVault 2** (Mac), Cipher Shed, DiskCryptor, LUKS, GNU-PG.
- Seguridad en desarrollo: JFrog Xray; **OWASP** Security by Design; SSDLC: **MS SDL, NIST 800-64, OWASP CLASP**.

**Conexiones con otros conceptos TAI:**
- [[B1 - T5 IGUALDAD, DISCAPACIDAD, DEPENDENCIA Y LGTBI]] y [[Discapacidad]] — accesibilidad universal y diseño para todos como derecho de las personas con discapacidad.
- [[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]] y [[ENAC]] — certificación (ENAC) y marco de administración electrónica.
- [[Instrumentos jurídicos de la Unión Europea (Reglamento, Directiva, Decisión, Recomendación)]] — Directiva 2016/2102 y Decisión de Ejecución 2018/1524.
- [[B2 - T4.2 WINDOWS Y SISTEMAS OPERATIVOS MOVILES]] — BitLocker y EFS en Windows.
