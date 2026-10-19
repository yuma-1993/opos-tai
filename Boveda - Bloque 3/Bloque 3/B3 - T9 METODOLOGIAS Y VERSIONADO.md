---
tags:
  - bloque3
  - tema9
  - metodologias
  - metrica3
  - rup
  - scrum
  - xp
  - integracion-continua
  - pruebas
  - git
  - control-versiones
bloque: 3
tema: "9"
titulo: "Metodologías de desarrollo, pruebas y control de versiones (Git)"
estado: por-repasar
---

# Tema 9 · Bloque 3 — Metodologías y versionado

> [!abstract] De qué va este tema
> El tema clasifica las metodologías de desarrollo (estructuradas, orientadas a proceso, a objetos y ágiles) y desarrolla las más importantes: RUP, Métrica 3, Scrum y XP. Sigue con la integración/despliegue continuo (Jenkins, SonarQube, JUnit), la clasificación de las pruebas y sus herramientas, las herramientas CASE y, sobre todo, el control de versiones: sistemas centralizados frente a distribuidos y un repaso muy detallado de Git (estados, comandos, ramas, reset/revert), cerrando con plataformas colaborativas y de despliegue.

> [!important] Actualizaciones 20/05/2026 aplicadas a este tema
> Del listado de actualizaciones de Velilla: (1) **`git checkout feature`** sirve para cambiar a la rama `feature` (27/03/2026); (2) **Gitflow**: modelo alternativo de gestión de ramas en Git (04/11/2025); (3) **errata**: **Mockito** (y no "Mokito") (16/09/2025). Las tres están marcadas en su sección.

---

## 1. Metodologías de desarrollo

| Familia | Metodologías |
|---|---|
| **Estructuradas** | SSADM, Merise |
| **Orientadas a proceso** | **Métrica 3** |
| **Orientadas a objetos** | **Booch Method** (fase de **diseño**) · **OMT** (fase de **análisis**) · **OOSE (Jacobson)**: **casos de uso** → de estos tres nace **RUP** (Rational Unified Process) → **OpenUP** y **Agile UP**. Es **iterativo e incremental, no en cascada**. Un poquito de todo (análisis, diseño, etc.) referido a una funcionalidad |
| **Ágiles** | **XP**, **SCRUM**, **FDD**, **KANBAN** |

- **KANBAN**: pizarra con tareas: *To do; Doing; Done*. Ej.: **Trello**.
- **Manifiesto Ágil**: **12 principios**. Los recogidos en el PDF:
  - Satisfacer al cliente con **entregas continuas y tempranas**.
  - Bienvenidos los **requisitos cambiantes**.
  - Entregar con frecuencia software que funcione.
  - **Negocio y desarrollo** deben trabajar juntos.
  - Entorno con **individuos motivados**.
  - **Simplicidad**.
  - **Comunicación cara a cara**.
  - … (el PDF no lista los 12 completos)

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El PDF indica con "…" que hay más principios que los listados. El Manifiesto Ágil original (2001) enumera 12 principios en total; aquí solo constan los 7 que Velilla transcribe.

### 1.1 RUP (Rational Unified Process)

Proceso de desarrollo **dirigido por los casos de uso**. En cada iteración se toma un conjunto de casos de uso y se desarrollan **todas las fases**: diseño, implementación, pruebas, etc. **Centrado en la arquitectura** como elemento vital del desarrollo: al inicio del proyecto debe fijarse la arquitectura para poder implementar después los diferentes casos de uso elegidos.

**Fases**: **Inicio (Incepción)**, **Elaboración**, **Construcción** y **Transición**.

Nace el **Unified Process**, para independizarlo de RUP. Se crea **OpenUP** y **Agile Unified Process**.

> [!tip] Orden de las fases de RUP
> I – E – C – T: **I**nicio → **E**laboración → **C**onstrucción → **T**ransición.

Ver la nota suelta [[RUP (Rational Unified Process)]] (RUP como proceso frente a UML como notación) y [[Diagrama de casos de uso (UML)]], [[B3 - T4.2 UML]].

### 1.2 Métrica 3

```
 PSI  Planificación de Sistemas de Información
 ─────────────────────────────────────────────
 DESARROLLO
   EVS  Estudio de Viabilidad del Sistema
   ASI  Análisis del Sistema de Información
   DSI  Diseño del Sistema de Información
   CSI  Construcción del Sistema de Información
   IAS  Implantación y Aceptación del Sistema
 ─────────────────────────────────────────────
 MSI  Mantenimiento de Sistemas de Información

 INTERFACES (procesos transversales, afectan a todo el ciclo de los procesos):
   Aseguramiento de Calidad · Gestión de Proyectos · Gestión de Configuración · Seguridad
```

| Proceso principal | Siglas |
|---|---|
| **Planificación** de Sistemas de Información | **PSI** |
| **Desarrollo** | **EVS**, **ASI**, **DSI**, **CSI**, **IAS** |
| **Mantenimiento** de Sistemas de Información | **MSI** |

- Métrica 3 tiene **3 grandes procesos**: Planificación, Desarrollo, Mantenimiento.
- **Guía de técnicas**: manual técnico donde explica los casos de uso. Te guía dependiendo de si tu enfoque es **orientado a objetos** o **estructurado**.
- Un **proceso** se divide en **actividades** y una actividad se divide en **tareas**.
- **Elementos de Métrica 3**: Procesos · Actividades · Tareas · Interfaces · Guía de técnicas.
- **Interfaces** (procesos transversales): **Aseguramiento de Calidad**, **Gestión de Proyectos**, **Gestión de Configuración**, **Seguridad**. Afectan a todo el ciclo de los procesos.

| Sesiones de trabajo en Métrica 3 | Para qué | Tipo |
|---|---|---|
| **Entrevistas** | Obtener información **individualmente** | Práctica |
| **Reuniones** | Extraer y depurar información **global** | Práctica |
| **JAD** | Se involucra al **usuario** | Sesión técnica |
| **JRP** | Se involucra a la **alta dirección** | Sesión técnica |

| Participantes en Métrica 3 | Incluye |
|---|---|
| **Directivo** | Comités, Directivos, Usuarios expertos |
| **Jefe de Proyecto** | Jefe de proyecto, Responsable de XX |
| **Consultor** | Consultor XX, Técnico XX, Especialista |
| **Analista** | DBA, Equipo de XX, Grupo de Aseguramiento de Calidad |
| **Programador** | — |

Para las tareas DSI 4.1–4.7 de diseño orientado a objetos, ver [[B3 - T4.1 PATRONES DE DISENO Y SOLID]].

### 1.3 SCRUM

- **Iterativo e incremental. Inteligencia colectiva. Pensamiento Lean.**
- **Artefactos** Scrum (trabajo o valor): **Product Goal**, **Definition of Done** (además de Product Backlog, Sprint Backlog, etc.).

| Roles | Rol | Qué es |
|---|---|---|
| **Principales** (más involucrados) | **Product Owner** | Representa la **voz del cliente**. Es como el **director del proyecto**. Marca las prioridades |
| | **Scrum Master** | **Facilitador**. Hace que Scrum se cumpla |
| | **Scrum Team** | PO, SM y desarrolladores. **< 10** con habilidades transversales |
| **Secundarios** (más tangenciales) | **Stakeholders** | Interesados externos o internos. Usuarios. Participan en las **revisiones del sprint** |

**Eventos Scrum**: Sprint Planning, Sprint, Daily, Sprint Review, Sprint Retrospective.

| Práctica / producto | Qué es | Duración |
|---|---|---|
| **Product Backlog** | Catálogo de requisitos **priorizado** que alimenta y gestiona el Product Owner. El PO marca las prioridades | — |
| **Sprint** | Periodo de **tiempo fijo** en el que el Scrum Team trabaja para completar el Sprint Backlog | **7 a 30 días** |
| **Sprint Backlog** | **Subconjunto** del Product Backlog | — |
| **Sprint Planning Meeting** | Reunión de planificación del sprint | — |
| **Daily Scrum** | Reunión diaria | **máximo 15 minutos** |
| **Sprint Review** | Revisión del sprint con alguna **demo** | **1 h** |
| **Sprint Retrospective** | Revisión del sprint para **buscar mejoras** | **1 h** |

- **Burn down chart**: gráfica que mide la cantidad de **requisitos pendientes** en el backlog del proyecto **al comienzo de cada sprint**.

### 1.4 XP (Extreme Programming)

- Potenciar las **relaciones interpersonales**. **Retroalimentación continua** [Cliente–Equipo de desarrollo].
- Técnica para especificar requisitos: **Historias de Usuario**, para definir funcionalidad. Las **épicas** se desgranan en historias de usuario y éstas en **tareas**. Las historias de usuario se agrupan en épicas.
- **Roles**: Programador · Cliente · Encargado de pruebas (**tester**) · Encargado de seguimiento (**tracker**) · Entrenador (**coach**) · Consultor · Gestor (**Big Boss**).
- **Prácticas**:
  - **Programación en parejas** (pair programming).
  - **Refactoring** (rehacer, mejorar código).
  - **Técnicos estiman y Clientes priorizan.**
  - **Integración continua.**
  - **Cliente in-situ.**
  - **40 h/semana.**
  - **Pruebas unitarias primero** (TDD: Test Driven Design).
  - **Entregas pequeñas.**

> [!important] Scrum vs XP (confusiones típicas)
> **Scrum** = roles PO / SM / Team, sprints de 7–30 días, backlogs, eventos. **XP** = prácticas técnicas (pair programming, TDD, refactoring, integración continua, 40 h/semana) y requisitos en historias de usuario agrupadas en épicas.

---

## 2. Integración continua (CI/CD)

Ejemplo de integración continua de un proyecto **Java**. **Jenkins** es un motor de integración continua. Jenkins incluye **Maven**.

```
   [SonarQube]        [JUnit]         [JBoss]
   Análisis código    Test unitarios  Runtime
        ↑ 3               ↑ 4            ↑ 5
              [ JENKINS (Maven) ]
        ↑ 1                       ↑ 2
   [GIT / SVN / TFS]       [Artifactory / Nexus / Archiva / JFrog]
   Repositorios de código   Repositorios de artefactos JAR/WAR/etc
```

Se define un **pipeline** de tareas, un circuito (1, 2, 3, 4 y 5):

| Sigla | Qué es | Alcance en el circuito |
|---|---|---|
| **CI** | Integración Continua | Hasta los test (**1–4**) |
| **CD** | Despliegue Continuo | Hasta el deploy (**1–5**) |

**Herramientas de CI/CD**: Jenkins, Travis CI, Circle CI, TeamCity, Code Ship, Bamboo.

| Paso | Qué ocurre |
|---|---|
| **1** | Pieza que lee todo el código que se sube a un repositorio (Git/SVN/TFS). Esas lecturas/consolidaciones pueden planificarse: **manual, planificado y de escucha** |
| **2** | **Jenkins** coge el código fuente y todos los **artefactos** (dependencias externas) necesarios (repositorio Artifactory/Nexus/Archiva/JFrog) y lo **compila** |
| **3** | **SonarQube** indica si el código no cumple el estándar de calidad, **rechazándolo**. Pruebas de calidad de **código estático**. Análisis de sintaxis |
| **4** | **Pruebas unitarias**: pruebas de **código dinámico** (código en ejecución). **JUnit** prueba la funcionalidad del proyecto |
| **5** | Se **despliega** el desarrollo. Por ejemplo, cualquier servidor de JEE: **JBoss, WildFly, WebSphere**, etc. Puede integrarse con **Ansible** para desplegar (ver [[B4 - T1.4 ADMON SSOO - ANSIBLE]] y [[Playbook (Ansible)]]) |

Jenkins también aparece como imagen Docker en [[B4 - T3.2.2 VIRTUALIZACION - DOCKER]].

---

## 3. Pruebas

### 3.1 Clasificación A (según se conozca o no el interior)

| Tipo | Qué es |
|---|---|
| **Caja blanca** | Se conoce el detalle del algoritmo. Interesa lo que ocurre **dentro**. Pruebas de **flujo de control**, de **bifurcación**, **caminos básicos**... |
| **Caja negra** | Solo interesan las **entradas y las salidas**, es decir, la **interfaz** |

### 3.2 Clasificación B

| Categoría | Prueba | Qué es |
|---|---|---|
| **Funcionales** | **Unitarias** | De cada componente |
| | **Integración** | Varios componentes/subsistemas |
| | **Aceptación** | Orientadas al usuario desde el punto de vista funcional |
| | **Regresión** | Comprobar que ante un cambio todo sigue funcionando |
| | **Alpha** | Hechas por el usuario con el **desarrollador de observador** en **entorno controlado** |
| | **Beta** | Realizadas por el usuario en **su entorno de trabajo** y **sin observadores** |
| **No funcionales** | Compatibilidad · Rendimiento · Seguridad · Usabilidad · Etc. | — |

### 3.3 Pruebas en Métrica 3

| Prueba | Qué es |
|---|---|
| **Unitarias** | De cada componente individualmente |
| **Integración** | Ensamblaje entre componentes. **Incremental**: top-down; bottom-up; combinada. **No incremental**: **Big-Bang**, todo de golpe |
| **Sistema** | Interfaces entre los subsistemas |
| **Implantación** | Sistema integrado de hw y sw en el entorno de operación |
| **Aceptación** | Funcionamiento esperado |
| **Regresión** | No se crean errores en otros componentes no modificados |
| Etc. | — |

### 3.4 Herramientas de pruebas

| Tipo | Descripción | Ejemplos |
|---|---|---|
| **Funcionales** | Simulan lo que hace el usuario | **Selenium**, **SoapUI**, **Watir** (Ruby), **WatiN** (.NET) |
| **Unitarias** | La prueba es de un componente **de forma aislada**. **Mockito** se usa para **mockear** datos | **JUnit**, **NUnit**, **TestNG** |
| **De carga** | — | **JMeter**, **HP LoadRunner**, **LoadUI** |
| **Análisis de código estático** | — | **SonarQube**, **PMD**, **CheckStyle**, **FindBugs** |

> [!important] Actualización 20/05/2026 (entrada del 16/09/2025)
> Errata corregida: es **Mockito** (no "Mokito").

---

## 4. Herramientas CASE

Nos ayudan al **desarrollo de software**, principalmente en las fases de **análisis y diseño**. **Entornos i-CASE**: varias CASE integradas cubren todo el ciclo de desarrollo. Se comunican mediante **XMI** (lenguaje de intercambio) — ver [[XMI (XML Metadata Interchange)]].

---

## 5. Control de versiones

### 5.1 Formatos / sistemas

| Tipo | Características | Ejemplos |
|---|---|---|
| **Centralizados** | **Repositorio único**. El desarrollador está permanentemente conectado al repositorio (**online**) | **CVS**, **Subversion (SVN)** (TortoiseSVN es el cliente), **TFS / SourceSafe** (Team Foundation Server). Comandos de SVN ≈ Git, comienzan por `# svn …` |
| **Distribuidos** | **Repositorio local** y luego se suben los cambios al servidor central | **Git**, **Mercurial**, **Bazaar**, **Darcs**, **BitKeeper**. Comandos de Mercurial ≈ Git: `# hg …`; Bazaar: `# bzr …` |

También se **versionan los elementos de gestión de la configuración**. Ej.: los *playbooks* de Ansible.

### 5.2 Git: características

Creado por **Linus Torvalds**, creador del kernel de Linux.

- **Distribuido**: la mayor parte del trabajo se hace en local.
- **Soporte avanzado de ramas y mezclas** de código. Se crean ramas para ir desarrollando correctivos y evolutivos. Creas una rama para que el resto no te moleste, pero luego hay que integrarlo, mezclarlo. Te sales temporalmente de la línea de desarrollo.
- Compatible con **HTTP(S) y SSH**. También existe el **local protocol** (≈ NFS) y el **Git Protocol (puerto 9418)**. Ver [[B4 - T1.2 ADMON SSOO - SSH]].
- **Uso de criptografía**: hace un **hash del contenido del commit**, realizando un **SHA-1** sobre objetos (ver [[Función hash criptográfica]]):

| Objeto | Qué es |
|---|---|
| **Tree** | ≈ directorio |
| **Blob** | ≈ fichero |
| **Commit** | Una **foto** de cierto trozo de código, un conjunto de ficheros y directorios que subo al control de versiones |
| **Tag** | Descripción del commit. Sirve para localizar una **release**, por ejemplo |

Cuando haces un commit estás subiendo un **tree** y ese tree puede llevar otros trees (subdirectorios) y blobs (ficheros). Un commit apunta a su tree de contenido y al commit anterior.

### 5.3 Repositorio local: creación, clonación y configuración

- **Creación del repositorio local**: `# git init`.
- **Directorio `.git`**: directorio oculto donde está la metainformación del repositorio. Contiene **Index** (staging area), **objects** (commits, etc.), **refs** (branches, tags, etc.). El Working area, Staging area y Local repo representan todo mi directorio `.git` de mi repositorio local. Mantiene la estructura de todo el sistema de ficheros interno. **No se crean las ramas (directorios) físicamente, sino internamente.**
- **Clonación**: pasa el repositorio de la nube a local. `# git clone uri` ≈ `# svn checkout svn+ssh://svn@ibm.com/svn/trunk`. Podemos crearnos un repositorio local a partir de un repositorio ya existente en la nube.
- **Configuración básica**:

```bash
# Credenciales
git config --global user.name "carlos"
git config --global user.email "carlos@inap.es"
```

- **Fichero `.gitignore`**: se definen los archivos que se **ignorarán** al hacer commit y no se subirán. Ej. Java: `*.class`, ya que el resto de desarrolladores solo necesitan los fuentes (`.java`).

### 5.4 Ramas, historial y remotos

- Todo repositorio tiene una **rama inicial llamada "master"**. Puede cambiarse. Otros nombres comunes: **"main"** (GitHub) y **"trunk"** (SVN). Es una convención, no obligación: `# git branch -m old_name new_name`.
- **History**: Git lleva un control de todos los commits del proyecto: `# git log`.
- Comprobar si un repositorio local está conectado a otro remoto: `# git remote -v`. **Git permite tener varios repositorios remotos** y subir los cambios a todos ellos.

### 5.5 Los 4 estados en un repositorio local

| Estado | Qué es | Analogía del PDF |
|---|---|---|
| **Working directory** | Local directory. Aquí tengo el fichero con el que trabajo. Para que sea susceptible de ir en el commit antes debo hacer `# git add fich`, `# git add .` o `# git add --all` para subir todo al staging area | Los estantes del supermercado |
| **Staging area** | Index area | El carro de la compra |
| **Local repo** | Mi repositorio local | La compra ya está en mi coche |
| **Remote repo** | **origin** es el nombre del repositorio remoto: `origin/main`. Ej.: GitHub / Bitbucket / GitLab | — |

```
 Working directory --git add--> Staging area --git commit--> Local repo --git push--> Remote repo
 Working directory <--git checkout-- (deshace)          Local repo <--git pull-- Remote repo
 (git merge: dentro del Local repo / working)
```

### 5.6 Comandos de Git

| Comando | Qué hace |
|---|---|
| `# git status` | Indica en qué rama estás, si tienes algún fichero del que hacer `add` y si tienes algún fichero del que hacer `commit` |
| `# git diff` | Lista diferencias, por ejemplo, entre commits |
| `# git blame` | Detalle (líneas) sobre los cambios en ficheros (autor, …) |
| `# git merge` | Te sitúas en la rama en la que quieres hacer el merge. Si en la rama `hotfix` tenía `f4.java` y en `master` también, tendríamos un **conflicto** a resolver. **Linealiza la historia** con respecto a `--no-ff`. **Fast Forward** es avanzar la master. `[--no-ff]`: mismo resultado, cambia la vista mostrando el branch. Puede hacerse si los ficheros no han cambiado en master |
| `# git tag` | Creación de etiquetas |
| `# git branch rama` | Crea una nueva rama, **pero no se mueve a ella**. ≈ `# svn copy rama_origen rama_destino` |
| `# git checkout` | Cambia el working directory, para **moverse de rama**. ≈ `# svn switch uri` |
| `# git checkout -b hotfix` | **Crea la rama y se mueve a ella.** No crea el directorio físicamente como hace SVN; la crea internamente (`.git`) |
| `# git checkout f2.txt` | **Deshace los cambios** realizados sobre `f2.txt` y lo deja como en el último commit |
| `# git checkout feature` | Sirve para **cambiar a la rama `feature`** (actualización 27/03/2026) |
| `# git fetch` | **No trae los ficheros** de remoto a local, pero sí **actualiza el estado** de tu repositorio local para saber si está o no actualizado. Solo hace el fetch de la rama en la que te encuentras posicionado. **No es necesario hacer un fetch para poder hacer un pull** |
| `# git fetch --all` | Hace el fetch de **todas las ramas** del repositorio |
| `# git pull` | **Trae a local los ficheros** del repo remoto para dejarlos sincronizados. Puedes especificar la rama: `# git pull origin/main/hotfix` |
| `# git commit` | Guarda los cambios en **local repo**: `# git commit -m "descripción"` |
| `# git commit --amend` | Para no generar commits que no aportan. Se acumulan sobre el último commit. ≈ Salvaguardas |
| `# git log --graph --online --all` | Formato del commit más resumido, intuitivo y visual (tal cual aparece en el PDF) |
| `# git log` | Muestra la historia de commits. `HEAD → master`. **HEAD** es como un **puntero al último commit**. Ese commit apunta al anterior commit y así sucesivamente hasta llegar al primer commit. Un commit apunta a su tree de contenido y al commit anterior |
| `# git push` | Sube los commits de local a remoto. "Tu rama está adelantada": local tiene más commits que remoto. Formato: `# git push <remote> <branch>`. Ejemplo: `# git push origin master` |
| `# git rebase master` | Sirve para **reescribir la historia** |
| `# git rebase -i HEAD~3` | **Consolida los 3 últimos commits en un único commit.** `-i` = interactivo: solicita confirmación y permite modificar la descripción del commit al aglutinar muchos en uno solo |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> En el comando `git log --graph --online --all` la opción real de Git para el formato resumido de una línea por commit es `--oneline` (el PDF escribe `--online`). Se deja tal cual el PDF en la tabla, pero conviene recordar la forma correcta.

> [!important] Actualización 20/05/2026 (entrada del 27/03/2026)
> `# git checkout feature` sirve para **cambiar a la rama `feature`**. Ojo con los tres usos de `checkout` en el tema: `git checkout rama` (moverse), `git checkout -b rama` (crear y moverse), `git checkout fichero` (deshacer cambios del fichero).

### 5.7 Los 3 tipos de reset y revert

Hay **3 tipos de reset**: se puede hacer sobre el **HEAD** o sobre un **commit concreto** indicando el hash del propio commit.

| Comando | Efecto |
|---|---|
| `# git reset --soft HEAD` | Deshace el **último commit**. Saca el cambio de local repo y lo deja de nuevo en **Staging area**, pendiente de commit |
| `# git reset --mixed HEAD` | Deshace el commit y el cambio lo lleva al **Working directory**, deshaciendo también el `add`. **Por defecto es `--mixed`** |
| `# git reset --hard HEAD` | Deshace el commit, deshace el add y **borra físicamente** los cambios y/o ficheros asociados al commit (**destructivo**) |
| `# git revert` | Es **el patrón SAGA de Git**. Introduce un **commit nuevo que anula** lo hecho en el último commit. **No borra nada de la historia, no borra ningún commit.** En microservicios, el patrón SAGA es para deshacer a base del negativo (transacción compensatoria) |

```
 Working directory <---- reset --mixed (default) ---- Staging area <---- reset --soft ---- Local repo
 reset --hard (destructive): deshace hasta el Working directory y borra los cambios
```

> [!important] reset vs revert
> `reset` **mueve el puntero** y (según el tipo) deshace commit/add/cambios; `revert` **añade** un commit nuevo que anula el anterior y no reescribe la historia. Ver el patrón SAGA con transacción compensatoria en [[B4 - T3.3 MICROSERVICIOS]].

> [!important] Actualización 20/05/2026 (entrada del 04/11/2025)
> **Gitflow**: modelo **alternativo** de gestión de ramas en Git.

**Source Tree**: herramienta gráfica de **Atlassian**, los creadores de **Jira**.

---

## 6. Plataformas colaborativas de software

- **Forja (Forge)**: concepto de **FOSS** (Free and Open Source Software). Ej.: SourceForge, Gforge, GitHub, GitLab, Bitbucket, Redmine, Google Code.
- **Flujos colaborativos en GitHub**:

| Flujo | Qué es |
|---|---|
| **Fork** | Haces una **copia del proyecto en tu cuenta de GitHub** (no sale de la nube) y de ahí puedes clonarla en tu local y trabajar sobre ella |
| **Pull Request** | Al creador del repositorio original le llegan tus modificaciones y, si quiere, podrá hacer un **merge** de tu código |

- **Plataformas de despliegue**:

| Plataforma | Modelo |
|---|---|
| **Heroku** | PaaS |
| **Digital Ocean** | IaaS |
| **AWS Elastic Beanstalk** | PaaS |
| **IBM Cloud Foundry** | PaaS |
| **Google App Engine** | PaaS |
| **OpenShift** | PaaS |
| **Windows Azure** | — (sin etiqueta en el PDF) |

Ver PaaS/IaaS en [[B4 - T3.2.1 VIRTUALIZACION]].

---

## 🔑 Resumen ultra-rápido

- Metodologías: **estructuradas** (SSADM, Merise) · **proceso** (Métrica 3) · **objetos** (Booch = diseño, OMT = análisis, OOSE/Jacobson = casos de uso → **RUP** → OpenUP, Agile UP) · **ágiles** (XP, SCRUM, FDD, KANBAN). Manifiesto Ágil = 12 principios. Kanban = To do / Doing / Done (Trello).
- **RUP**: dirigido por casos de uso, centrado en la arquitectura, iterativo e incremental (no cascada). Fases: **Inicio, Elaboración, Construcción, Transición**.
- **Métrica 3**: 3 procesos (**PSI**, **Desarrollo** = EVS/ASI/DSI/CSI/IAS, **MSI**); interfaces transversales: Calidad, Proyectos, Configuración, Seguridad. Proceso → actividades → tareas. Sesiones: entrevistas (individual), reuniones (global), **JAD** (usuario), **JRP** (alta dirección). Participantes: directivo, jefe de proyecto, consultor, analista, programador.
- **Scrum**: iterativo e incremental, Lean. Roles: **Product Owner** (voz del cliente, prioriza el backlog), **Scrum Master** (facilitador), **Scrum Team** (<10); secundarios: stakeholders. **Sprint 7–30 días**, Daily **≤15 min**, Review **1 h**, Retrospective **1 h**. Product Backlog ⊃ Sprint Backlog. Burn down chart = requisitos pendientes.
- **XP**: historias de usuario (épicas → historias → tareas); roles (programador, cliente, tester, tracker, coach, consultor, Big Boss); prácticas: pair programming, refactoring, TDD, integración continua, cliente in-situ, **40 h/semana**, entregas pequeñas.
- **CI/CD** con Jenkins (incluye Maven): 1 repo (Git/SVN/TFS) → 2 compila con artefactos → 3 **SonarQube** (estático) → 4 **JUnit** (dinámico) → 5 deploy (JBoss/WildFly/WebSphere; Ansible). **CI = pasos 1–4; CD = 1–5**. Herramientas: Jenkins, Travis CI, Circle CI, TeamCity, Code Ship, Bamboo.
- Pruebas: caja **blanca** (interior: flujo de control, bifurcación, caminos básicos) vs **negra** (entradas/salidas). Funcionales (unitarias, integración, aceptación, regresión, **alpha** = con observador y entorno controlado, **beta** = entorno del usuario sin observadores) y no funcionales (compatibilidad, rendimiento, seguridad, usabilidad). Integración: incremental (top-down, bottom-up, combinada) vs Big-Bang.
- Herramientas de prueba: Selenium/SoapUI/Watir/WatiN (funcionales) · JUnit/NUnit/TestNG + **Mockito** (unitarias) · JMeter/HP LoadRunner/LoadUI (carga) · SonarQube/PMD/CheckStyle/FindBugs (estático).
- **CASE**: análisis y diseño; **i-CASE** integradas vía **XMI**.
- Versionado: **centralizado** (CVS, SVN/TortoiseSVN, TFS/SourceSafe; online) vs **distribuido** (Git, Mercurial `hg`, Bazaar `bzr`, Darcs, BitKeeper).
- **Git**: Linus Torvalds; SHA-1 sobre **tree, blob, commit, tag**; protocolos HTTP(S), SSH, local, Git (puerto **9418**); `.git` (index, objects, refs); `.gitignore`; rama inicial **master** (main en GitHub, trunk en SVN).
- 4 estados: **Working directory → Staging area (add) → Local repo (commit) → Remote repo (push)**; `pull` trae; `fetch` solo actualiza el estado (no hace falta para `pull`); `fetch --all`.
- `checkout` rama / `checkout -b` crea y mueve / `checkout fichero` deshace; `branch` crea sin moverse; `merge` (conflictos; fast forward vs `--no-ff`); `rebase -i HEAD~3` consolida 3 commits; `commit --amend`; HEAD = puntero al último commit.
- **reset**: `--soft` (vuelve a staging), `--mixed` (por defecto; vuelve al working directory), `--hard` (borra físicamente). **revert** = SAGA de Git: nuevo commit que anula, sin borrar historia. **Gitflow** = modelo alternativo de ramas. **Source Tree** = Atlassian (Jira).
- Forjas (FOSS): SourceForge, Gforge, GitHub, GitLab, Bitbucket, Redmine, Google Code. GitHub: **Fork** (copia en tu cuenta) y **Pull Request**. Despliegue: Heroku (PaaS), Digital Ocean (IaaS), AWS Elastic Beanstalk, IBM Cloud Foundry, Google App Engine, OpenShift (PaaS), Windows Azure.

**Conexiones con otros conceptos TAI:**
- [[RUP (Rational Unified Process)]], [[Diagrama de casos de uso (UML)]] y [[B3 - T4.2 UML]] — RUP como proceso dirigido por casos de uso y UML como notación.
- [[B3 - T4.1 PATRONES DE DISENO Y SOLID]] — tareas DSI de Métrica 3 en el diseño orientado a objetos.
- [[XMI (XML Metadata Interchange)]] — lenguaje de intercambio entre herramientas CASE.
- [[B4 - T1.4 ADMON SSOO - ANSIBLE]] y [[Playbook (Ansible)]] — despliegue desde el pipeline y versionado de playbooks.
- [[B4 - T3.2.2 VIRTUALIZACION - DOCKER]] — Jenkins como imagen Docker.
- [[B4 - T3.3 MICROSERVICIOS]] — patrón SAGA (transacción compensatoria), equivalente conceptual de `git revert`.
- [[B4 - T3.2.1 VIRTUALIZACION]] — PaaS/IaaS de las plataformas de despliegue.
- [[Función hash criptográfica]] — SHA-1 en los objetos de Git.
- [[B4 - T1.2 ADMON SSOO - SSH]] — SSH como protocolo de acceso a repositorios Git.
