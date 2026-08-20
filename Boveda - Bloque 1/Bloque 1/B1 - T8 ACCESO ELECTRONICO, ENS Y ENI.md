---
tags:
  - bloque1
  - tema8
  - ens
  - eni
  - seguridad-de-la-informacion
  - firma-electronica
  - administracion-electronica
bloque: 1
tema: 8
titulo: Acceso electrónico, Esquema Nacional de Seguridad (ENS) y Esquema Nacional de Interoperabilidad (ENI)
estado: por-repasar
---

# Tema 8 · Bloque 1 — Acceso electrónico, ENS y ENI

> [!abstract] De qué va este tema
> El Esquema Nacional de Seguridad (ENS, RD 311/2022) regula cómo las Administraciones Públicas protegen la información y los servicios; el Esquema Nacional de Interoperabilidad (ENI, RD 4/2010) regula cómo esas mismas Administraciones consiguen que sus sistemas puedan compartir información entre sí. Ambos se completan con las notificaciones electrónicas a los ciudadanos, algunos registros y mecanismos de la Ley 39/2015, y los formatos y estándares de firma electrónica (CAdES, XAdES, PAdES, perfiles BES/EPES/T/C/X/XL/A) que dan soporte técnico a los dos esquemas.

---

## Esquema Nacional de Seguridad (ENS)

### Qué es y marco normativo

Determina la **política de seguridad** que se ha de aplicar en la utilización de los medios electrónicos. **El ENS será aplicado por las AAPP.** Está constituido por los **principios básicos y requisitos mínimos** necesarios para una protección adecuada.

Se pretende proteger la **información** y los **servicios**, asegurando el **acceso, confidencialidad, integridad, trazabilidad, autenticidad, disponibilidad y conservación** de datos y servicios.

Los pliegos de prescripciones administrativas o técnicas de los contratos que celebren las entidades del Sector público contemplarán todos los requisitos necesarios para asegurar la **conformidad con el ENS** (Declaraciones o Certificaciones de Conformidad).

> [!important] Regulación
> **Real Decreto 311/2022**, del ENS (también Ley 40/2015). También aplica a sistemas de información de **entidades privadas** cuando presten servicios a entidades públicas.

> [!note] Ver también [[B1 - T6.1 SOCIEDAD DE LA INFORMACION#Marco normativo de la Administración Electrónica|Tema 6.1, "Marco normativo de la Administración Electrónica"]], donde la tabla de jerarquía de normas señala que es el **artículo 156 de la Ley 40/2015** el que crea tanto el ENI como el ENS como los dos instrumentos gemelos de la Administración Electrónica.

### Principios básicos (7)

| Principio | En qué consiste |
|---|---|
| Seguridad como proceso integral | Máxima atención a concienciar a las personas que intervienen en el proceso y a los responsables jerárquicos, para evitar que la ignorancia, la falta de organización y de coordinación o de instrucciones adecuadas constituyan fuentes de riesgo. |
| Gestión de la seguridad basada en los riesgos | El análisis y la gestión de riesgos es esencial en el proceso de seguridad. |
| Prevención, detección, respuesta y conservación | Para que las amenazas no se materialicen o no afecten gravemente a datos o servicios. |
| Existencia de líneas de defensa | Estrategia de protección constituida por múltiples capas de seguridad, que permite reducir la probabilidad de que el sistema sea comprometido en su conjunto y minimizar el impacto final. |
| Vigilancia continua | Permite la detección de actividades o comportamientos anómalos y su oportuna respuesta. |
| Reevaluación periódica | Permite medir la evolución del sistema, detectando vulnerabilidades e identificando deficiencias de configuración. |
| Diferenciación de responsabilidades | Responsable de la información, responsable del servicio, responsable de la seguridad y responsable del sistema. La responsabilidad de la seguridad de los sistemas estará diferenciada de la responsabilidad sobre los recursos. |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> La "existencia de líneas de defensa" es el principio de **defensa en profundidad**: como un castillo con varias murallas concéntricas, si un atacante supera una capa (por ejemplo el perímetro de red) todavía se encuentra con más capas (control de acceso, cifrado, monitorización...), en vez de que todo dependa de un único punto de fallo.

### Política de seguridad y requisitos mínimos

**Política de seguridad**: conjunto de directrices que rigen la forma en que una organización gestiona y protege la información que trata y los servicios que presta. Deberá incluir como mínimo:

- Los objetivos de la organización.
- El marco regulatorio en el que se desarrollarán las actividades.
- Los roles o funciones de seguridad, definiendo deberes y responsabilidades, así como el procedimiento para su designación y renovación.
- La estructura y composición del comité para la gestión y coordinación de la seguridad, detallando responsabilidades y relaciones.
- Las directrices para la estructuración de la documentación de seguridad del sistema, su gestión y acceso.
- Los riesgos que se derivan del tratamiento de los datos personales.

La política de seguridad se establecerá de acuerdo con los principios básicos y se desarrollará aplicando los siguientes **requisitos mínimos**:

1. Organización e implantación del proceso de seguridad.
2. Análisis y gestión de los riesgos.
3. Gestión de personal.
4. Profesionalidad.
5. Autorización y control de los accesos.
6. Protección de las instalaciones.
7. Adquisición de productos de seguridad y contratación de servicios.
8. Mínimo privilegio.
9. Integridad y actualización del sistema.
10. Protección de la información almacenada y en tránsito.
11. Prevención ante otros sistemas de información interconectados.
12. Registro de la actividad y detección de código dañino.
13. Incidentes de seguridad.
14. Continuidad de la actividad.
15. Mejora continua del proceso de seguridad.

### Organización e implantación del proceso de seguridad

| Responsable | Función |
|---|---|
| Responsable de la información | Determina los requisitos de la información tratada. |
| Responsable del servicio | Determina los requisitos de los servicios prestados. |
| Responsable de la seguridad | Determina las decisiones para satisfacer los requisitos de seguridad de información y servicios, y las supervisa. |
| Responsable del sistema | Implementa la seguridad en el sistema y supervisa la operación diaria del mismo. |

> [!important] El responsable de la seguridad debe ser **distinto** del responsable del sistema — no debe existir dependencia jerárquica entre ambos.

En servicios externalizados, el prestatario designará un **[[POC (Punto de Contacto)|POC]]** (Punto o Persona de Contacto), Responsable de Seguridad de la organización.

Desarrollo de otros requisitos mínimos:

- **Análisis y gestión de riesgos**: cada organización realizará su propia gestión de riesgos.
- **Gestión de personal**: el personal propio o ajeno será formado e informado de deberes, obligaciones y responsabilidades en materia de seguridad.
- **Profesionalidad**: la seguridad estará atendida y será revisada y auditada por personal cualificado.
- **Autorización y control de los accesos**: acceso controlado a los sistemas de información.
- **Protección de instalaciones**: los sistemas de información estarán en áreas controladas, con mecanismos de acceso adecuados al análisis de riesgos.
- **Mínimo privilegio**: los sistemas de información deben diseñarse y configurarse otorgando los mínimos privilegios necesarios.
- **Integridad y actualización del sistema**: incluir un elemento físico o lógico en el sistema requerirá autorización formal previa.
- **Protección de la información almacenada y en tránsito**: la información deberá estar encriptada cuando sale de las instalaciones.
- **Registro de actividad y detección de código dañino**.
- **Incidentes de seguridad**: procedimientos de gestión de incidentes de seguridad y de comunicación a las partes interesadas.
- **Continuidad de la actividad**: los sistemas dispondrán de copias de seguridad y mecanismos para garantizar la continuidad de las operaciones.
- **Mejora continua del proceso de seguridad**: el proceso integral de seguridad implantado deberá ser actualizado y mejorado de forma continua.

### Cumplimiento de los requisitos mínimos

Las entidades adoptarán las medidas y refuerzos de seguridad correspondientes, teniendo en cuenta:

- Los **activos**.
- La **categoría** del sistema.
- Las **decisiones** para gestionar los riesgos identificados.

**Infraestructuras y servicios comunes**: el uso de infraestructuras y servicios comunes de las AAPP facilitará el cumplimiento del ENS.

**[[Perfil de cumplimiento específico|Perfiles de cumplimiento específicos]] y acreditación de entidades de implementación de configuraciones seguras**: conjunto de medidas de seguridad idóneas para una concreta categoría de seguridad. El **CCN** validará y publicará los perfiles de cumplimiento específicos.

### Auditoría de la seguridad

> [!important] Auditoría
> Al menos cada **dos años**. Podrá extenderse durante **tres meses**. De forma extraordinaria si hay cambios sustanciales en los sistemas de información que afecten a las medidas de seguridad. El resultado se presenta al **responsable del sistema** y al **de seguridad**. La auditoría la analiza el responsable de seguridad y presenta sus conclusiones al responsable del sistema para que adopte las medidas adecuadas.
>
> En el caso de los sistemas de **categoría ALTA**, si hay deficiencias graves, el **responsable del sistema** podrá suspender temporalmente el tratamiento de informaciones, la prestación de servicios o la total operación del sistema, hasta su adecuada subsanación o mitigación.

**Informe del estado de la seguridad**: la Comisión Sectorial de Administración Electrónica recogerá la información del estado de las principales variables de la seguridad en los sistemas de información para elaborar un perfil general del estado de la seguridad.

### Capacidad de respuesta a incidentes: CCN-CERT y CSIRT

El **CCN** articulará la respuesta a los incidentes de seguridad en torno a la estructura denominada **[[CCN-CERT]]** (Computer Emergency Response Team). Los **[[CSIRT]]** (Computer Security Incident Response Team) se coordinarán con el Ministerio del Interior, a través de su Oficina de Coordinación de Ciberseguridad.

Funciones del CSIRT:
- Responder urgente y coordinadamente a ataques.
- Detener el impacto de ataques en curso.
- Coordinar acciones legales.
- Facilitar indicaciones sobre la seguridad a corto y medio plazo.

**Prestación de servicios de respuesta a incidentes de seguridad a las entidades del sector público**:
- Soporte y coordinación para el tratamiento de vulnerabilidades y la resolución de incidentes de seguridad.
- Investigación y divulgación de las mejores prácticas sobre seguridad de la información. Documentos **[[CCN-STIC]]**.
- Formación destinada al personal del sector público especialista en el campo de la seguridad de las tecnologías de la información.
- Información sobre vulnerabilidades, alertas y avisos de nuevas amenazas a los sistemas de información.

**Administración digital**: el CCN es el órgano competente para garantizar la debida interoperabilidad en materia de ciberseguridad y criptografía.
**Ciclo de vida de servicios y sistemas**: las especificaciones de seguridad se incluirán en el ciclo de vida de los servicios y sistemas, para garantizar de forma real y efectiva el cumplimiento del ENS.
**Mecanismos de control**: actualización permanente.
**Formación**: el CCN y el Instituto Nacional de Administración Pública desarrollarán programas de formación.

### Procedimientos de determinación de la conformidad

Los sistemas de información serán objeto de un proceso para determinar su **conformidad con el ENS**.

| Categoría del sistema | Procedimiento de conformidad |
|---|---|
| MEDIA o ALTA | Auditoría para la **certificación** de su conformidad. |
| BÁSICA | **Autoevaluación** para su declaración de la conformidad. |

Las entidades certificadoras son las que otorgan el certificado de conformidad (Media, Alta) o la declaración de conformidad (Básica). La **[[ENAC]]** es quien autoriza a las entidades certificadoras a certificar la conformidad con el ENS.

### Categorías de seguridad

**Categorías de seguridad**: equilibrio entre la importancia de la información que maneja y servicios que presta, y el esfuerzo de seguridad requerido, en función de los riesgos a los que está expuesto. Se determina en función de la valoración del impacto sobre el **[[CITAD]]**.

**Fundamentos para la determinación de la categoría de seguridad de un sistema de información**: se basará en la valoración del impacto que tendría sobre la organización un incidente que afectase a la seguridad de la información tratada o de los servicios prestados para:

- Alcanzar sus objetivos.
- Proteger los activos a su cargo.
- Garantizar la conformidad con el ordenamiento jurídico.

Anualmente, o si se producen modificaciones significativas, deberá **re-evaluarse** la categoría de seguridad de los sistemas de información.

**Dimensiones de la seguridad** (para determinar el impacto de un incidente y así establecer la categoría de seguridad del sistema):

| Dimensión | Sigla |
|---|---|
| Confidencialidad | C |
| Integridad | I |
| Trazabilidad | T |
| Autenticidad | A |
| Disponibilidad | D |

**Determinación del nivel de seguridad requerido en una dimensión** (será el mayor para cada función, activo o individuo afectado):

| Nivel | Consecuencias de un incidente |
|---|---|
| BAJO | Perjuicio **limitado** sobre las funciones, activos o individuos afectados. |
| MEDIO | Perjuicio **grave** sobre las funciones, activos o individuos afectados. |
| ALTO | Perjuicio **muy grave** sobre las funciones, activos o individuos afectados. |

**Determinación de la categoría de seguridad de un sistema de información**:

| Categoría | Condición |
|---|---|
| BÁSICA | Alguna dimensión alcanza el nivel BAJO, y ninguna alcanza un nivel superior. |
| MEDIA | Alguna dimensión alcanza el nivel MEDIO, y ninguna alcanza un nivel superior. |
| ALTA | Alguna dimensión alcanza el nivel ALTO. |

Las guías **CCN-STIC** precisarán los criterios de categorización (secuencia de actuaciones para determinar la categoría de seguridad de un sistema).

### Medidas de seguridad

Se aplicarán a las dimensiones de seguridad y la categoría de seguridad del sistema. Se dividen en tres grupos:

| Marco | Descripción | Nº de medidas |
|---|---|---|
| Marco organizativo [org] | Conjunto de medidas relacionadas con la organización global de la seguridad. | 4 |
| Marco operacional [op] | Medidas a tomar para proteger la operación del sistema. | 33 |
| Medidas de protección [mp] | Se centran en proteger activos concretos. | 36 |

> [!important] Total: **73 medidas de seguridad** (4 + 33 + 36).

### Desarrollo, certificación y herramientas del ENS

**Desarrollo del ENS**: los Secretarios de Estado firman los Reales Decretos. La Secretaría de Estado de Digitalización e IA del MAETD aprobará las **[[NTI e ITS (desarrollo normativo del ENI y del ENS)|Instrucciones Técnicas de Seguridad (ITS)]]**. El CCN elaborará y difundirá guías **CCN-STIC**, particularmente de la serie 800.

> [!note] Simetría ENS / ENI
> Si el **ENI** se desarrolla con **NTI** (Normas Técnicas de Interoperabilidad), el **ENS** se desarrolla con **ITS** (Instrucciones Técnicas de Seguridad).

Herramientas: guías **CCN-STIC-8xx** + herramientas **INES** (estado de cumplimiento del ENS) y **CLARA** (auditoría).

Reglamento (UE) **2019/881** relativo a **ENISA** (Agencia de la Unión Europea para la Ciberseguridad) y a la certificación de la ciberseguridad.

### Metodología del ENS

Ciclo (cíclico, vuelve al primer paso tras "Mejorar la seguridad"):

1. **Preparar y aprobar la política de seguridad** — CCN-STIC-805.
2. **Definir roles y asignar personas** — CCN-STIC-801.
3. **Valorar/categorizar el sistema** (información/servicios) — CCN-STIC-803.
4. **Realizar análisis de riesgos** — herramientas [[Magerit, PILAR y µPILAR|Magerit, Pilar, µPILAR]].
5. **Preparar y aprobar la declaración de aplicabilidad** — CCN-STIC-804.
6. **Implantar, operar y monitorizar el sistema** — CCN-STIC-806, 807, 811, 812, 813, 814...
7. **Auditar cada dos años (A/M)** — CCN-STIC-802, CCN-STIC-808. Sistemas básicos: autoevaluación. Guías de bajo nivel, concretas.
8. **Mejorar la seguridad** — CCN-STIC-809, CCN-STIC-815 → vuelve al paso 1.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> **Magerit** es la metodología de análisis y gestión de riesgos de los sistemas de información promovida por las Administraciones Públicas españolas; **PILAR** y **µPILAR** son las herramientas software (desarrolladas con el CCN) que la implementan — µPILAR es la versión simplificada, pensada para organizaciones pequeñas o análisis rápidos.

Detalle de algunas guías:

| Guía | Contenido |
|---|---|
| CCN-STIC-801 | Responsable de seguridad (delegados), Responsable del Sistema/Información/Servicio, Administrador de seguridad. |
| CCN-STIC-803 | Por cada activo se pide la valoración de su nivel (bajo, medio o alto) en cada dimensión de seguridad: Servicios → Disponibilidad (D); Información → C (Confidencialidad), I (Integridad), T (Trazabilidad) y A (Autenticidad). |
| CCN-STIC-807 | Mecanismos criptográficos autorizados por el ENS. |
| CCN-STIC-808 | Itinerario de auditoría para la evaluación de la conformidad con el ENS. |
| CCN-STIC-883B | Perfil de Cumplimiento Específico para Ayuntamientos < 20.000 habitantes. |

**Perfil de cumplimiento específico**: conjunto de medidas de seguridad que, como consecuencia del preceptivo análisis de riesgos, resulten de aplicación a una entidad o sector de actividad concreta y para una determinada categoría de seguridad.

> [!note] Tabla de valoración de activos (fuente)
> El PDF incluye una plantilla ilustrativa de tabla de valoración con columnas "Denominación del activo esencial", "Tipo", C, I, T, A, D, y una fila de "Valor máximo del nivel registrado en las dimensiones de seguridad", sin datos rellenados — se referencia aquí su estructura, sin inventar valores.

### Adecuación de sistemas preexistentes

Los sistemas preexistentes tendrán **24 meses** para adecuarse al ENS. Se obtendrá el **Distintivo de Conformidad**. Para los sistemas que ya tuviesen el Distintivo de Conformidad, podrán mantener su vigencia procediendo a su renovación de conformidad.

### Ejemplos de medidas de seguridad

| Medida | Por categoría o dimensión | BAJO / BÁSICA | MEDIO / MEDIA | ALTO / ALTA |
|---|---|---|---|---|
| org — Marco organizativo | — | Todos los `org` aplican a todas las categorías | | |
| org.1 Política de seguridad | Categoría | aplica | aplica | aplica |
| op — Marco operacional | — | | | |
| op.nub Servicios en la nube | — | | | |
| op.nub.1 Protección de servicios en la nube | Categoría | aplica | + R1 | + R1 + R2 |
| op.exp.8 Registro de actividad | T | aplica | + R1+R2+R3+R4 | + R1+R2+R3+R4+R5 |
| mp — Medidas de protección | — | | | |
| mp.com Protección de las comunicaciones | — | | | |
| mp.com.1 Perímetro seguro | Categoría | aplica | aplica | aplica |
| mp.com.2 Protección de la confidencialidad | C | aplica | + R1 | + R1+R2+R3 |
| mp.si Protección de los soportes de información | — | | | |
| mp.si.5 Borrado y destrucción | C | aplica | + R1 | + R1 |
| mp.info Protección de la información | — | | | |
| mp.info.1 Datos personales | Categoría | aplica | aplica | aplica |
| mp.s Protección de los servicios | — | | | |
| mp.s.1 Protección del correo electrónico | Categoría | aplica | aplica | aplica |
| mp.s.2 Protección de servicios y aplicaciones web | Categoría | + [R1 o R2] | + [R1 o R2] | + R2+R3 |

> [!note] "R1", "R2"... son **refuerzos** — ver más abajo, en los cambios del ENS 2022, el nuevo sistema de referencias que divide las medidas entre requisitos generales y refuerzos.

### ENS 2010 → ENS 2022: principales cambios

**Cambios en el número de medidas** (tal y como aparecen en el diagrama comparativo de la fuente):

| Bloque | RD 2010 | Detalle 2010 | Nuevo RD (2022) | Detalle 2022 |
|---|---|---|---|---|
| Marco organizativo | 4 | (1) Política de seguridad, (1) Normativa de seguridad, (1) Procedimiento de seguridad, (1) Proceso de autorización | 4 | (1) Política de seguridad, (1) Normativa de seguridad, (1) Procedimiento de seguridad, (1) Proceso de autorización |
| Marco operacional | 31 | (5) Planificación, (7) Control de acceso, (10) Explotación, (3) Servicios externos, (4) Continuidad del servicio, (2) Monitorización del sistema | 33 | (5) Planificación, (6) Control de acceso, (4) Explotación, (4) Servicio en la nube, (3) Servicios externos, (4) Continuidad del servicio, (2) Monitorización del sistema |
| Medidas de protección | 40 | (8) Instalaciones e infraestructuras, (5) Gestión del personal, (4) Protección de los equipos, (4) Protección de las comunicaciones, (5) Protección de los soportes de información, (2) Protección de aplicaciones informáticas, (7) Protección de la información, (4) Protección de los servicios | 36 | (7) Instalaciones e infraestructuras, (4) Gestión del personal, (4) Protección de los equipos, (4) Protección de las comunicaciones, (5) Protección de los soportes de información, (2) Protección de aplicaciones informáticas, (6) Protección de la información, (4) Protección de los servicios |

> [!note] Estos desgloses son la transcripción literal del diagrama de la fuente; sus subtotales no siempre cuadran de forma exacta con el total indicado (31/33/40/36) en la propia imagen — se mantiene tal cual figura en el documento original, sin corregir ni inventar la discrepancia.

**Cambios en principios básicos**: ENS 2010 tenía "Prevención, reacción y recuperación" → ENS 2022 lo cambia a "**Prevención, detección, respuesta y conservación**". Se introduce el principio básico de **Vigilancia continua**.

**Cambios en requisitos mínimos**: ENS 2010 tenía "Seguridad por defecto" → ENS 2022 lo renombra a "**Mínimo privilegio**" (modificación de terminología).

**Resumen de modificaciones a las medidas de seguridad**:
- Aumentan considerablemente su nivel de exigencia (9): Identificación, Configuración de seguridad, Gestión de la configuración de seguridad, Protección frente a código dañino, Registro de actividad, Gestión de la capacidad, Detección de intrusión, Sistema de métricas, Aceptación y puesta en servicio.
- Nuevas medidas (6): Servicios en la nube, Interconexión de sistemas, Protección de la cadena de suministro, Medios alternativos, Vigilancia, Otros dispositivos conectados a la red.

**Otros cambios recogidos por el ENS 2022** (texto de la fuente):
- **Ámbito de aplicación**: se detalla el ámbito de aplicación de la norma, haciendo mención expresa a los sistemas de información clasificada y las entidades privadas que presten servicios a las Administraciones Públicas para el ejercicio de sus competencias y potestades.
- **Diferenciación de responsabilidades**: además del responsable de la información, del servicio y de la seguridad, también habrá que designar un **responsable del sistema**. En el artículo 13 se recogen las obligaciones de cada uno de los responsables.
- **Política de seguridad**: se amplía el contenido mínimo, debiendo incluir los riesgos que derivan del tratamiento de los datos personales.
- **Persona de contacto**: las entidades jurídicas privadas que presten servicios dentro del alcance del ENS deberán nombrar a una **Persona de Contacto (POC)**, responsable de la seguridad de la organización contratada.
- **Comunicaciones electrónicas**: se elimina el Capítulo IV, relativo a comunicaciones electrónicas, en el que se regulaban aspectos como la firma electrónica o los requerimientos técnicos de notificaciones y publicaciones electrónicas.
- **Perfiles de cumplimiento**: para agilizar la implementación del ENS, se promoverá la implementación de perfiles de cumplimiento — conjunto de medidas de seguridad destinadas a una concreta categoría de seguridad (ámbito), que permitirán una adaptación al ENS más eficaz y eficiente.
- **Respuesta a incidentes de seguridad**: se regula más en profundidad las obligaciones en relación a la notificación de incidentes de seguridad, así como las actuaciones a llevar a cabo por parte del CCN-CERT. Se recoge la obligación de las organizaciones privadas (relacionadas con el ámbito de la Administración) de notificar al **INCIBE-CERT**. Para temas militares está el **ESPDEF-CERT**.
- **Categoría del sistema**: obligación de reevaluar de forma **anual** la categoría del sistema.
- **Medidas de seguridad**: de forma general, el rango de alcance de las medidas ha sido ampliado y son sustancialmente más estrictas. La principal novedad es el **nuevo sistema de referencias**, dividiendo las medidas de seguridad entre **requisitos generales** y **refuerzos**. En función del nivel de exigencia, estos refuerzos podrán resultar tanto obligatorios como preceptivos.

---

## Notificaciones electrónicas

Preferentemente por medios electrónicos. Serán válidas siempre que permitan tener constancia de su **envío**, **recepción** por interesado o representante, **fechas y horas**, **contenido íntegro** e **identidad fidedigna** del remitente y destinatario. La acreditación se incorporará al expediente.

**Práctica de las notificaciones a través de medios electrónicos**: comparecencia en la sede electrónica es el acceso por interesado o representante al contenido de la notificación.

> [!important] Notificación rechazada
> Se considera **rechazada** cuando pasen **10 días naturales** desde la puesta a disposición sin que se acceda a su contenido. Podrá accederse a las notificaciones desde la sede electrónica del organismo, el **PAG** y la **DEHú**.

**[[DEHú|Dirección Electrónica Habilitada única (DEHú)]]**: buzón seguro asociado a una DEHú, en la que se pueden recibir comunicaciones y notificaciones electrónicas administrativas. Requiere certificado digital o DNIe. Vigencia indefinida. Se podrá inhabilitar si pasan **3 años** sin notificaciones.

**Notificación mediante recepción en dirección de correo electrónico**: si genera automáticamente acuse de recibo en el momento del acceso.

**Notificación por comparecencia electrónica**: para que la comparecencia electrónica produzca los efectos de notificación debe cumplir:
- Con carácter previo al acceso a su contenido, el interesado deberá visualizar un aviso del carácter de dicho acceso.
- El sistema de información correspondiente dejará constancia de dicho acceso con indicación de fecha y hora.

**NOTIFIC@**: sistema de gestión de notificaciones que concentra peticiones de emisión de notificaciones a ciudadanos y empresas. Actúa de intermediario.

> [!note] Ver también [[B1 - T9.2 SERVICIOS COMUNES#Comunicaciones y notificaciones al ciudadano|Tema 9.2, "Comunicaciones y notificaciones al ciudadano"]], donde la Dirección Electrónica Habilitada única y "Notifica" (el mismo servicio que aquí aparece como NOTIFIC@) se catalogan junto con SIM, el servicio de avisos por SMS/correo.

---

## Esquema Nacional de Interoperabilidad (ENI)

### Qué es y ámbito de aplicación

Regulado en el **RD 4/2010** y la **Ley 40/2015**. El objetivo del ENI es poder **compartir información**. Formato y Semántica.

**Ámbito de aplicación**: AGE, CCAA, EELL y Sector Público Institucional.

> [!note] Al igual que el ENS (ver más arriba), el ENI nace del **artículo 156 de la Ley 40/2015** — ver [[B1 - T6.1 SOCIEDAD DE LA INFORMACION#Marco normativo de la Administración Electrónica|Tema 6.1, "Marco normativo de la Administración Electrónica"]].

> [!important] ENS vs ENI
> El **ENS** protege la información y los servicios (confidencialidad, integridad, disponibilidad...). El **ENI** existe para que esa información se pueda **compartir** entre sistemas de distintas Administraciones (formato y semántica comunes). Son complementarios, no alternativos: uno protege, el otro hace interoperable.

### Principios básicos

- La **interoperabilidad como cualidad integral**.
- Enfoque de **soluciones multilaterales**. Multiplataforma. Escalado. Reutilización.
- **Carácter multidimensional** de la interoperabilidad. Tres dimensiones:

| Dimensión | Contenido |
|---|---|
| Organizativa | Convenios, condiciones de acceso, etc. Inventarios de información administrativa (SIA, DIR3). |
| Semántica | Modelos de datos. El **CISE** (Centro de Interoperabilidad Semántica) es quien define los modelos de datos. |
| Técnica | Estándares abiertos. Relacionado con el **Catálogo de Estándares**. |

> [!note] Ver también [[B1 - T9.2 SERVICIOS COMUNES#Sistemas de información transversales|Tema 9.2, "Sistemas de información transversales"]] (SIA y DIR3 como servicios concretos) y [[B1 - T9.2 SERVICIOS COMUNES#Reutilización|Tema 9.2, "Reutilización"]] (CISE, en el catálogo de servicios comunes de la SGAD).

**Catálogo de Estándares**: no es completo ni existe procedimiento de homologación formal. Debe revisarse al menos **1 vez al año**. Son abiertos y de uso generalizado. Contenido: Autenticación, Codificación, Formatos de ficheros, Cifrado, Integridad, Protocolos, Métricas, Semántica, etc.

### Documento electrónico

**Documento electrónico**: agrupación lógica, un contenedor. XSD. **INSIDE**: gestión de documentos y expedientes electrónicos que cumple con el ENI.

Estructura de un documento (que forma parte de un expediente):

- **Contenido**: Datos XML (CDATA) / Valor Binario / Referencia. Nombre Formato (según Catálogo de Estándares). Identificador (opcional).
- **Metadatos**:
  - Versión NTI.
  - Identificador normalizado, con estructura determinada: `ES-<DIR3>-<YYYY>-<ID>`.
  - Órgano: código DIR3.
  - Fecha de la captura.
  - Origen: 0 = Ciudadano, 1 = Administración.
  - Estado de elaboración: Original, Copia auténtica con cambio de formato, Copia auténtica de documento en papel, Copia parcial auténtica.
  - Tipo documental: Resolución, Acuerdo, Contrato, Alegación, Notificación, Recurso, Acta, etc.
- **Firma**:
  - Tipo de firma:
    - **CSV**: solo usable por la Administración. Cada organismo debe publicar su algoritmo de generación del CSV. Ver [[B1 - T9.1 INSTRUMENTOS DE ACCESO#3.5 Sistemas de código seguro de verificación (CSV)|Tema 9.1, apartado 3.5]] para su regulación legal completa (Ley 40/2015: unicidad, vinculación al documento y al firmante, verificación en sede).
    - Firmas avanzadas: **[[CAdES, XAdES y PAdES (formatos de firma avanzada)|XAdES, PAdES, CAdES]]**.
  - Contenido de la firma.

### Expediente electrónico

**Expediente electrónico**: agrupa documentos. Un expediente puede tener subexpedientes. La información que tal está en el documento.

Contenido de un expediente electrónico:

- **Documentos**: pueden ser independientes, dentro de una carpeta o dentro de un subexpediente.
- **Índice**: estructura que gobierna los documentos del expediente y su fecha de incorporación. Contiene el ID del documento, la **huella del documento (hash)** y la fecha de incorporación.
- **Firma del índice**: lo que se firma del expediente es su índice.
- **Metadatos**: versión NTI, Identificador, Órgano (DIR3), Fecha de apertura, Clasificación (SIA), Estado (Abierto, Cerrado, Índice para remisión cerrado), Interesado (NIF, NIE, DIR3).

**Ciclo de vida de un expediente electrónico**:

1. **Apertura**.
2. **Tramitación**: existe el cierre lógico, no real, no administrativo. Se puede reactivar.
3. **Conservación y Selección**: finalizado su periodo de validez administrativa. Puede mandarse a ARCHIVE.

> [!note] Ver también [[B1 - T9.2 SERVICIOS COMUNES#Expediente, documento y archivo electrónico|Tema 9.2, "Expediente, documento y archivo electrónico"]], donde INSIDE (aquí, gestor de documentos/expedientes conforme al ENI) y ARCHIVE aparecen como servicios comunes concretos de la SGAD: **InSiDe** (genera y custodia), **G-InSiDe** (genera, no almacena) y **Archive** (archivo definitivo de expedientes cerrados).

### Normas técnicas de interoperabilidad

**Digitalización de documentos**:
- Requisitos de la imagen: en b/n, color o grises, y con una resolución mínima de **200 ppp**.
- Formatos admitidos: Catálogo de Estándares.

**Política de firma** (basada en certificados):
- Identificación: PDF con el nombre del documento, versión, identificador (OID: Object ID), URI, fecha de expedición y ámbito de aplicación.
- Usos: Transmisiones y Contenido.
- Formatos de firma: **XAdES** (XML), **PAdES** (PDF), **CAdES** (Binario).
- Certificados reconocidos: Reglamento **[[Reglamento eIDAS (UE) 910-2014|eIDAS (910/2014)]]**. Nodo eIDAS utilizado en la plataforma **Cl@ve**.
  - De firma: persona física.
  - De sello: persona jurídica.
  - De autenticación web.
  - No cualificado.

> [!example] Firma avanzada pero no cualificada
> Si firmo un documento con un certificado cualificado (DNIe, FNMT) pero lo hago con un dispositivo o software no cualificado, tendríamos una firma **avanzada pero no cualificada**.

> [!important] AdES-EPES
> AdES-EPES es un AdES-BES al que se le añade el identificador de la política de firma (OID) que se ha utilizado. **No añade seguridad criptográfica**, pero sí **seguridad jurídico-administrativa**. En la Administración **no se admite una firma BES**: el mínimo es EPES.

> [!note] Un sello es una firma con marca de tiempos que hace una **TSA** (Time Stamping Authority). Ver [[B1 - T9.2 SERVICIOS COMUNES#Hora oficial|Tema 9.2, "Hora oficial"]] (la TS@, Autoridad de Sellado de Tiempo, dando fe de la hora oficial en un documento) y [[B1 - T6.1 SOCIEDAD DE LA INFORMACION#Sistemas de firma e identificación de la Administración|Tema 6.1]] (la fila "TSA", donde se detalla que la FNMT pide la hora al ROA y genera la firma con el hash del documento).

> [!note] Ampliación (conocimiento general, no viene del PDF)
> **eIDAS** (Reglamento UE 910/2014) es la norma europea que da **reconocimiento legal transfronterizo** a la identificación electrónica y a los servicios de confianza (firma, sello, sellado de tiempo...): un certificado cualificado emitido en España tiene el mismo valor jurídico en cualquier otro Estado miembro de la UE, lo que evita que cada país tenga que reconocer certificados extranjeros caso a caso.
>
> Desarrollo legal completo (Ley 6/2020, tipos de servicios cualificados, niveles de seguridad de identificación qaa/LoA, tipos de firma eIDAS) en [[B1 - T6.1 SOCIEDAD DE LA INFORMACION#Ley 6/2020, de servicios electrónicos de confianza|Tema 6.1]].

**Protocolos de Intermediación de datos**: App Web + WS SOAP.
- **Plataforma de Intermediación de Datos (PID-SVD)**: servicios de verificación y consulta. Residencia, desempleo, títulos oficiales, TGSS, AEAT, etc.
- **SCSP**: Sustitución de Certificados en Soporte Papel. Es un envoltorio común: Formato XML común + Formato XML específico. Conjunto de especificaciones orientadas al intercambio de datos.

> [!note] Ver también [[B1 - T9.2 SERVICIOS COMUNES#Intercambio de información entre Administraciones Públicas|Tema 9.2, "Intercambio de información entre Administraciones Públicas"]], donde PID y Portfolio SCSPv3 (los mismos PID-SVD y SCSP de aquí) aparecen junto a Corinto, el servicio de comunicaciones electrónicas seguras con anexos.
- **Modelos de datos**: XSD publicadas a través de **CISE**.
- **Política de gestión de documentos**: metadatos **e-EMGDE** (Esquema de Metadatos para la Gestión de Documentos Electrónicos). Son más metadatos de negocio normalizados. e-EMGDE define Agentes (Quién), Actividades (Cómo), Documentos (Qué) y Regulaciones (Por qué). Los XSD son comunes para todos los organismos: todos deben usar los mismos XSD.
- **Modelo de datos para intercambio de asientos registrales**: **SICRES v4.0** (XML).
- **Reutilización de recursos de información**: datos.gob.es. **[[DCAT (Data Catalog Vocabulary)|DCAT]]** proporciona un vocabulario **RDF** (conjunto de clases y propiedades) para describir el contenido de los datos en la web (añade información semántica a la información). **[[RISP (Reutilización de la información del sector público)|RISP]]**: uso por personas físicas o jurídicas, de datos generados y custodiados por organismos del sector público, con fines comerciales o no.

### Auditoría sobre la conformidad del ENI

Marco **organizativo** [org], marco **operacional** [op] y **medidas técnicas** [tec].

---

## Ley 39/2015 — mecanismos de identificación y registro

Ley 39/2015, del Procedimiento Administrativo Común de las Administraciones Públicas:

| Mecanismo | Definición |
|---|---|
| **REA** | Registro Electrónico de Apoderamientos a terceros para actuar en su nombre ante la AGE y OOPP. Validez máxima de **5 años**. Implementado por el servicio **Apodera** — ver [[B1 - T9.2 SERVICIOS COMUNES#Registros y representación del ciudadano ante las AAPP|Tema 9.2]]. |
| **RFH** | Registro de Funcionarios Habilitados a prestar un servicio de asistencia a ciudadanos sin medios para relacionarse con las AAPP. Implementado por el servicio **Habilita** — ver [[B1 - T9.2 SERVICIOS COMUNES#Registros y representación del ciudadano ante las AAPP|Tema 9.2]]. |
| **PAG** | Punto de Acceso General. Portal de la AGE (administracion.gob.es). Punto único de acceso a todas las AAPP: AGE, CCAA, EELL y UE. Desarrollo legal completo (titularidad, dominios, canales) en [[B1 - T9.1 INSTRUMENTOS DE ACCESO#9. Punto de Acceso General de la AGE (PAG)|Tema 9.1, apartado 9]]. |
| **Archivo Único Electrónico** | Permite almacenar por medios electrónicos todos los documentos utilizados en las actuaciones administrativas. |
| **Registro Electrónico Común** | Registro genérico donde presentar cualquier solicitud, escrito y comunicación dirigida a la AGE y OOPP. |

---

## Firma electrónica

### Fundamentos criptográficos: hash y cifrado asimétrico

Proceso de la **firma "básica"**:

```
Documento (xml o binario) → Hash → residuo/message digest (01001...110110)
                                   → Cifrado asimétrico con la clave privada (X.509 v3)
                                   → Firma "básica" (0011100110001100...)
```

- Algoritmos de **[[Función hash criptográfica|hash]]**: SHA-256/384/512, SHA-1 (160 bits), MD5 (128 bits).
- Algoritmos de **cifrado asimétrico**: El-Gamal, RSA / DSA / DH / EC — el mismo mecanismo de par de claves pública/privada que se explica en detalle (con el ejemplo de SSH) en [[Criptografía asimétrica (clave pública y privada)]].

**Cl@ve** ha facilitado la firma en la nube mediante la generación y custodia de certificados [[Certificado TLS-SSL (X.509)|X.509]].

> [!note] Ampliación (conocimiento general, no viene del PDF)
> Una función **hash** criptográfica es determinista (el mismo documento siempre produce el mismo resumen), no reversible (no se puede reconstruir el documento a partir del resumen) y sensible a cualquier cambio mínimo (cambiar un solo carácter del documento produce un resumen completamente distinto — "efecto avalancha"). Por eso sirve para comprobar la **integridad**: si el documento se altera después de firmarlo, su hash ya no coincide con el que se firmó.

### Firma electrónica avanzada (AdES) y sus perfiles

**Firma avanzada** (AdES: Advanced digital Electronic Signature) = Firma "básica" + Metadatos (certificado firmante, fecha y hora de la firma, resultado de la revocación, etc.).

Versiones en función de los metadatos: **[[Perfiles de firma AdES (BES a A)|BES, T, C, X, XL y A]]**. (XAdES: XML — CAdES: Binario — PAdES: PDF).

| Perfil | Añade |
|---|---|
| **AdES-BES** | Firma Básica. Formato básico para satisfacer los requisitos de la firma electrónica avanzada. |
| **AdES-EPES** | Firma Básica BES + política de firma explícita. Mínimo perfil admitido por la Administración. |
| **AdES-T** | Sellado de tiempo (T de *TimeStamp*), para situar en el tiempo el instante en que se firma un documento. |
| **AdES-C** | Referencias a los certificados de la cadena de certificación y su estado, como base para una verificación longeva (C: Cadena). |
| **AdES-X** | Sellos de tiempo a las referencias creadas en el paso anterior (X: eXtendida). Asegura que fue así en ese momento del tiempo. |
| **AdES-XL** | Los certificados y la información de revocación de los mismos, para su validación a largo plazo (XL: eXtendido Largo plazo). |
| **AdES-A** | Sellos de tiempo periódicos para garantizar la integridad de la firma archivada para futuras verificaciones (A: Archivo). |

> [!tip] Cada perfil se construye sobre el anterior
> Sobre la firma anterior se añade algo nuevo. Ejemplo: sobre un XAdES-BES se añade un sello de tiempo y se obtiene un **XAdES-T**. La secuencia completa es BES → T → C → X → XL → A, cada uno añadiendo la pieza del anterior más la suya propia.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El sentido práctico de ir subiendo de perfil es la **validación a largo plazo**: un certificado tiene fecha de caducidad y puede ser revocado, pero un documento firmado puede necesitar tener validez legal muchos años después. Los sellos de tiempo (T) y la información de revocación embebida (C, X, XL, A) permiten demostrar, años más tarde, que en el momento de la firma el certificado era válido — sin depender de que ese certificado siga existiendo o siendo consultable entonces.

### Formatos de firma: CAdES, XAdES, PAdES, OOXML, ODF

| Formato | Nombre completo | Cuándo usarlo |
|---|---|---|
| **CAdES** | CMS Avanzado | Evolución del primer formato de firma estandarizado. Apropiado para firmar ficheros grandes, especialmente si la firma contiene el documento original, porque optimiza el espacio de la información. Tras firmar, no se puede ver la información firmada porque se guarda de forma **binaria**. |
| **XAdES** | XML Avanzado | El resultado es un fichero de texto **XML**, similar al HTML, que utiliza etiquetas. Los documentos obtenidos suelen ser más grandes que en CAdES, por lo que no es adecuado si el fichero original es muy grande. Aplicaciones como eCoFirma del Ministerio de Industria y Comercio solo firman en XAdES. |
| **PAdES** | PDF Avanzado | El formato más adecuado cuando el documento original es un **PDF**. El destinatario puede comprobar fácilmente la firma y el documento firmado; con los otros formatos esto no es posible sin herramientas externas. |
| **OOXML / ODF** | — | Formatos de firma que utilizan Microsoft Office y Open Office, respectivamente. |

### Firma XML (XMLDSIG)

Estándar **[[XMLDSIG]]** de la W3C. Es el precursor de XAdES (es una extensión). Tiene **3 versiones**: Enveloping, Enveloped y Detached.

Aunque su formato es XML, se puede firmar cualquier tipo de documento. Se usó mucho en la cabecera SOAP para firmar las peticiones (**WS-Security**).

Datos / etiquetas básicas:
- `<DigestValue>` + `<DigestMethod>` → MD5, SHA1, etc.
- `<SignatureValue>` + `<SignatureMethod>`
- `<X509Certificate>` → RSA, DSA, DH, etc.

| Versión | Estructura |
|---|---|
| Enveloping signature | La firma envuelve al documento firmado (*signed data* contiene *document* + *signature*). |
| Enveloped signature | El documento contiene sus datos y la firma dentro de sí mismo. |
| Detached signature | El documento y la firma van en ficheros/elementos separados. |

### Certificados X.509: estructura y codificaciones

Los certificados **[[Certificado TLS-SSL (X.509)|X.509]]** definen su estructura de datos apoyándose en **ASN.1**. Esa estructura de datos se [[Codificaciones de certificados X.509 (PEM, DER, PKCS7, PKCS12)|codifica de dos formas posibles]]:

| Codificación | Tipo | Extensiones |
|---|---|---|
| Base64/ASCII | PEM | `.pem`, `.crt`, `.cer`, `.key` |
| Base64/ASCII | PKCS#7 | `.p7b`, `.p7c` |
| Binario | DER | `.der`, `.cer` |
| Binario | PKCS#12 | `.pfx`, `.p12` |

> [!note] `.p12`/`.pfx` **incluyen la clave privada** del certificado (por eso son ficheros sensibles a proteger), mientras que `.cer`/`.der` son solo la parte pública, compartible sin riesgo — ver [[p12-pfx vs cer (certificado con-sin clave privada)]] para el detalle de esta distinción, aplicable a cualquier certificado X.509 (incluido el del DNIe, ver [[B1 - T6.1 SOCIEDAD DE LA INFORMACION#Custodia de las claves privadas y PIN|Tema 6.1]]).

---

## 🔑 Resumen ultra-rápido

- **ENS** (RD 311/2022, Ley 40/2015): protege información y servicios de las AAPP. Aplica también a privadas que dan servicio a AAPP. Se desarrolla con ITS.
- Principios ENS (7): proceso integral, gestión basada en riesgos, prevención/detección/respuesta/conservación, líneas de defensa, vigilancia continua (nuevo en 2022), reevaluación periódica, diferenciación de responsabilidades.
- Requisitos mínimos ENS: 15, entre ellos mínimo privilegio (antes "seguridad por defecto" en 2010).
- 4 responsables ENS: información, servicio, seguridad, sistema — seguridad y sistema no pueden coincidir.
- Auditoría ENS: cada 2 años (+3 meses), certificación (MEDIA/ALTA) o autoevaluación (BÁSICA); ENAC autoriza a las certificadoras.
- CCN-CERT coordina la respuesta a incidentes; CSIRT se coordina con Interior; INCIBE-CERT para privadas relacionadas con AAPP; ESPDEF-CERT para lo militar.
- Categoría de seguridad = mayor nivel (BAJO/MEDIO/ALTO) entre las dimensiones CITAD (Confidencialidad, Integridad, Trazabilidad, Autenticidad, Disponibilidad).
- Medidas de seguridad ENS: 73 = 4 org + 33 op + 36 mp. Sistemas preexistentes: 24 meses para adecuarse (Distintivo de Conformidad).
- Metodología ENS cíclica: política → roles → categorizar → análisis de riesgos (Magerit/Pilar) → declaración de aplicabilidad → implantar/operar/monitorizar → auditar → mejorar.
- Notificaciones electrónicas: rechazadas a los 10 días naturales sin acceso. DEHú: buzón único, vigencia indefinida, se inhabilita a los 3 años sin uso. PAG y DEHú dan acceso.
- **ENI** (RD 4/2010, Ley 40/2015): objetivo = compartir información (formato + semántica). Se desarrolla con NTI. Ámbito: AGE, CCAA, EELL, Sector Público Institucional.
- 3 dimensiones ENI: organizativa (SIA, DIR3), semántica (CISE), técnica (Catálogo de Estándares, revisión anual).
- Documento electrónico ENI: contenido + metadatos (identificador ES-DIR3-YYYY-ID) + firma (CSV solo AAPP, o avanzadas XAdES/PAdES/CAdES).
- Expediente electrónico: documentos + índice (con hash) + firma del índice + metadatos. Ciclo: apertura → tramitación (cierre lógico, reactivable) → conservación/selección (ARCHIVE).
- Digitalización ENI: mínimo 200 ppp. Política de firma: eIDAS (910/2014), mínimo EPES (BES no se admite en la Administración).
- Intermediación de datos: PID-SVD, SCSP; gestión documental e-EMGDE; intercambio de asientos SICRES v4.0; reutilización vía datos.gob.es (DCAT/RDF, RISP).
- Ley 39/2015: REA (apoderamientos, 5 años), RFH (funcionarios habilitados), PAG (punto único de acceso), Archivo Único Electrónico, Registro Electrónico Común.
- Firma electrónica: hash (SHA-256/384/512, SHA-1, MD5) + cifrado asimétrico con clave privada (RSA/DSA/DH/EC/El-Gamal) = firma básica.
- Perfiles AdES (se construyen unos sobre otros): BES → EPES (+política de firma, mínimo admitido en AAPP) → T (+sellado de tiempo) → C (+referencias a cadena de certificación) → X (+sellos de tiempo sobre esas referencias) → XL (+certificados y revocación) → A (+sellos de tiempo periódicos).
- Formatos de firma: CAdES (binario, ficheros grandes), XAdES (XML, eCoFirma), PAdES (PDF, verificable sin herramientas externas), OOXML/ODF (Office).
- XMLDSIG (W3C): precursor de XAdES, 3 versiones (Enveloping, Enveloped, Detached), muy usado en cabeceras SOAP (WS-Security).
- X.509 + ASN.1: codificación Base64/ASCII → PEM (.pem/.crt/.cer/.key) o PKCS#7 (.p7b/.p7c); codificación binaria → DER (.der/.cer) o PKCS#12 (.pfx/.p12).
