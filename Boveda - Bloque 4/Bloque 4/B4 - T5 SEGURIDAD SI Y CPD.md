---
tags:
  - bloque4
  - tema5
  - seguridad
  - sgsi
  - ens
  - ccn
  - cpd
  - tier
  - malware
bloque: 4
tema: 5
titulo: Seguridad en sistemas de información y CPD
estado: por-repasar
---

# Tema 5 · Bloque 4 — Seguridad en SI y CPD

> [!abstract] De qué va este tema
> Cuatro partes: (1) seguridad de los sistemas de información: metodologías (SGSI, ENS, Common Criteria), tríada CIA, conceptos de riesgo, seguridad física y lógica (autenticación, MFA), actores, herramientas, malware y ataques, equipos Red/Blue/Purple; (2) las herramientas del CCN (Centro Criptológico Nacional); (3) el CPD: racks, climatización, energía, norma TIA-942 (Tier I a IV) y métricas de eficiencia (PUE, CUE, WUE, ERE, OCE); (4) herramientas de ticketing y de control remoto de puestos.

---

## 1. Seguridad en sistemas de información

**Proteger activos.** Activos: **información y servicio**. Guía **CCN-STIC-400** (ver [[CCN-STIC]]).

### 1.1 Metodologías

| Metodología | Contenido |
|---|---|
| **SGSI** (Sistemas de Gestión de la Seguridad de la Información) | **ISO/IEC 27001 y 27002**: basado en la estrategia de mejora continua **PDCA** (Plan → Do → Check → Act → ...) |
| **ENS** (Esquema Nacional de Seguridad) | De **obligado cumplimiento por la Admón Pública**. Análisis y gestión de riesgos. Métodos/herramientas: **MAGERIT** (herramienta de apoyo a Pilar y µPilar), OCTAVE, CRAMM, MEHARI, SP800-30, UNE 71504, EBIOS |
| **Common Criteria** (EAL 1-7) | Relacionados: ITSEC, CTCPSEC, TCSEC. Usado para la construcción del **eDNI** |
| Otras | ISM3, Cobit, SOGP, TLLJO, ITIL |

Ver el desarrollo legal del ENS en [[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]], [[NTI e ITS (desarrollo normativo del ENI y del ENS)]] y la herramienta [[Magerit, PILAR y µPILAR]]. Sobre el eDNI: [[DNI electrónico (DNIe)]].

#### Common Criteria: niveles EAL (tabla del PDF)

| Nivel | Requirements | Functional Specification | High-Level Design | Low-Level Design | Implementation |
|---|---|---|---|---|---|
| EAL 1 | Informal | Informal | Informal | Informal | Informal |
| EAL 2 | Informal | Informal | Informal | Informal | Informal |
| EAL 3 | Informal | Informal | Informal | Informal | Informal |
| EAL 4 | Informal | Informal | Informal | Informal | Informal |
| EAL 5 | Formal | Semiformal | Semiformal | Informal | Informal |
| EAL 6 | Formal | Semiformal | Semiformal | Semiformal | Informal |
| EAL 7 | Formal | Formal | Formal | Semiformal | Informal |
| Verified | Formal | Formal | Formal | Formal | Formal |

> [!tip] Cómo leer la tabla
> A medida que sube el EAL, la rigurosidad (informal → semiformal → formal) crece primero en los requisitos y luego en las especificaciones/diseños. En EAL 1-4 todo es informal; en la fila "Verified" todo es formal.

### 1.2 Atributos core a proteger: tríada CIA

| Atributo | Sobre qué recae | Descripción |
|---|---|---|
| **Confidencialidad** | Dato | Secreto, cifrado, encriptación |
| **Integridad** | Dato | Modificaciones no autorizadas |
| **Trazabilidad** | | |
| **Autenticidad** | | **No repudio**. Origen de la información (ver [[No repudio (irrenunciabilidad)]]) |
| **Disponibilidad** (Availability) | Servicio | |

> [!important] CIA
> Confidencialidad e Integridad se predican del **dato**; Disponibilidad, del **servicio**.

### 1.3 Conceptos de riesgo

| Concepto | Definición |
|---|---|
| **Activo** | Recurso a proteger. Información y servicios |
| **Amenaza** | Evento que pueda darse aprovechando una vulnerabilidad |
| **Vulnerabilidad** | Probabilidad de ocurrencia/materialización de una amenaza. Debilidad del sistema. Riesgo según probabilidad e impacto |
| **Impacto** | Daño producido por la ocurrencia de una amenaza |
| **Impacto acumulado** | Impacto sobre el activo y sobre los dependientes |
| **Riesgo** | F (Probabilidad × Impacto). Lo probable que es una amenaza junto con el impacto que tendría |
| **Salvaguarda** | Medida prevista para evitar/reducir el riesgo |
| **Riesgo potencial** | Riesgo **antes** de aplicar salvaguardas |
| **Riesgo residual** | Riesgo que queda **después** de haber aplicado salvaguardas |

- Realizar una **evaluación del impacto**: **RGPD Art. 35**, Evaluación de Impacto en Protección de Datos (ver [[Evaluación de Impacto relativa a la Protección de Datos (EIPD)]]).

> [!example] Gráfico "Riesgo según probabilidad e impacto" (PDF)
> Plano con probabilidad en el eje X e impacto en el eje Y, con cuatro zonas numeradas:
>
> | Zona | Posición | Lectura |
> |---|---|---|
> | 1 | Arriba a la derecha | Alta probabilidad y alto impacto (zona roja, riesgo máximo) |
> | 2 | Centro | Riesgo intermedio |
> | 3 | Abajo a la izquierda | Baja probabilidad y bajo impacto (zona verde) |
> | 4 | Arriba a la izquierda | Alto impacto, baja probabilidad |

### 1.4 Seguridad física

- Control de acceso a edificios.
- Sistemas contra incendios (**NFPA 75**).
- Sistemas de energía eléctrica (**SAI**).
- Sistemas de vigilancia (**CCTV**).

### 1.5 Seguridad lógica

- Antivirus, Firewalls, IDS/IPS, Criptografía (VPN, SSL), Anti-spam, Políticas de seguridad, Backups (ver [[Estrategias de backup (Completa, Incremental, Diferencial)]], [[Regla 3-2-1]]).
- Sistemas de autenticación:

| Sistema | Nota |
|---|---|
| Radius / Kerberos | Tickets |
| OAuth / JWT | Token |
| OpenId | |
| **SAML** | **Cl@ve** (SSO) — ver [[Plataforma Cl@ve (incluye Cl@ve Firma)]] |
| Biométricos | |
| Sistemas **OTP** | One Time Password |

> [!important] MFA/2FA (Multifactor / 2 Factor Authentication)
> Consiste en combinar varios métodos:
>
> | Factor | Ejemplos |
> |---|---|
> | **Lo que sé** | PIN, clave, etc. |
> | **Lo que tengo** | USB, certificado, etc. |
> | **Lo que soy** | Biométrico |

### 1.6 Amenazas y vulnerabilidades

#### Actores

| Actor | Descripción |
|---|---|
| **Hacker** | Busca conocimiento para proteger |
| **Cracker** | Actividad ilícita |
| **Lamer** | Alardea pero usa sw de otros |
| **Phreaker** | Área de telefonía |
| **Newbie** | Novato |
| **CopyHacker** | Falsifica y crackea hw |
| **ScriptKiddie** | Aficionado que usa sw de otros |

| Siglas | Significado |
|---|---|
| **CVE** | Common Vulnerability Exposure. Publicados por el **MITRE**. Formato `CVE-YYYY-NNNN` |
| **CWE** | Common Weakness Enumeration |

#### Herramientas

| Herramienta | Para qué |
|---|---|
| **nmap** | Auditorías de seguridad. Escanea puertos |
| **nessus** | Detector de vulnerabilidades |
| **OpenVAS** | Detector de vulnerabilidades |
| **Metasploit** | Test de penetración |
| **Snort** | NIDS e IPS |
| **tcpdump** | Captura de paquetes |
| **ethreal/wireshark** | Sniffer |
| **Linux Kali** | Auditoría y seguridad informática |
| **John the Ripper** | Password cracker por fuerza bruta y diccionarios |
| **Hydra** | Password cracker por fuerza bruta y diccionarios |
| **Ncrack** | Password cracker por fuerza bruta y diccionarios |
| **Medusa** | Password cracker por fuerza bruta y diccionarios |
| **Cain y Abel** | Recuperación de password para Windows |
| **Shodan** | Motor de búsqueda de routers, servidores, webcams, etc. |
| **Nikto** | Vulnerabilidades web |
| **sqlmap** | Herramienta para probar SQL Injection |

#### Software malicioso (malware)

| Tipo | Descripción |
|---|---|
| **Virus** | |
| **Gusanos** | Se duplica en RAM/RED sin ficheros |
| **Troyanos** | Administración remota |
| **Rootkits** | Permanece oculto con permisos de root |
| **Backdoor** | Acceso sin autenticación |
| **Spyware** | Recopila datos para venderlos a agencias de publicidad |
| **Ransomware** | Cifran archivos para pedir rescate |
| **Keylogger o stealers** | Roban información sensible |
| **Adware** | Muestran publicidad |
| **Rogue** | Hacen creer que el PC está infectado. Antivirus falso |

#### Ataques y otras amenazas

| Amenaza | Descripción |
|---|---|
| **Hoaxes** | Bulo, mensaje que da falsas advertencias |
| **SQL Injection** | Ejecución de código SQL no autorizado por falta de validación en entradas de una app web. Herramienta para probarlo: sqlmap (ver [[B3 - T3 SQL]]) |
| **Eavesdropping** | Escuchar en secreto conversaciones privadas |
| **XSS** (Cross Site Scripting) | Permite a una tercera persona inyectar en páginas web código javascript malicioso. **CSP** (Content Security Policy) es una técnica de seguridad que evita XSS restringiendo los orígenes de los contenidos |
| **Hijacking** | Robo de una sesión ya iniciada |
| **Phishing** | Suplantación de identidad. Ej: al recibir un email supuestamente del banco. **QRishing** utiliza códigos QR |
| **Pharming** | Vulnerabilidad en servidores DNS. Tipo de phishing que redirige tráfico web, redirigiendo un dominio a otra IP |
| **Spoofing** | Suplantación de identidad |
| **DoS** | Denegación de Servicio. **Teardrop** (fragmentación IP). Técnicas de inundación o *flooding*: **SYN flood**, **ICMP Flood / Smurf**, **UDP Flood** |
| **DDoS** | Denegación de Servicio Distribuido. **Botnets**: redes de equipos infectados (bots/zombies) |

> [!tip] Pharming vs Phishing
> Phishing engaña al usuario (email, QR); pharming ataca la resolución DNS para que un dominio legítimo lleve a otra IP sin que el usuario haga nada raro.

#### Equipos

| Equipo | Función |
|---|---|
| **Red Team** | Especializados en ataques informáticos. Atacan empresas para detectar sus vulnerabilidades. **Seguridad ofensiva** |
| **Blue Team** | Especializados en analizar sistemas de seguridad, detectar fallos e implementar medidas de seguridad. **Seguridad defensiva** |
| **Purple Team** | Compartición de información entre los equipos rojo y azul |

---

## 2. Herramientas del CCN

Dentro de las funciones del **Centro Criptológico Nacional** está la coordinación, promoción y desarrollo de soluciones que garanticen la seguridad de los sistemas y contribuyan a una mejor gestión de la ciberseguridad en cualquier organización y permitan una mejor defensa frente a ciberataques. Contexto: [[CCN-CERT]], [[CCN-STIC]], [[CSIRT]].

| Herramienta | Función |
|---|---|
| **ADA** | Plataforma de análisis avanzado de malware. Integra **MARIA** (multiantivirus) y **MARTA** (multisandboxing) |
| **AMPARO** | Implantación de seguridad y conformidad del ENS |
| **ANA** | Automatización y normalización de auditorías. Detección de vulnerabilidades, capacidad de vigilancia y saber superficie de exposición. Versiones: **ANA On Premise** (instalación independiente del resto de organismos) y **ANA Central** (nube privada) |
| **ANGELES** | Portal de formación en ciberseguridad |
| **ATENEA** | Web con desafíos de seguridad. Jugar y aprender |
| **CARLA** | Protección y trazabilidad del dato |
| **CARMEN** | Defensa de ataques avanzados/APT. Dispositivo situado en la **DMZ** que analiza el tráfico de red ([[DMZ (zona desmilitarizada)]]). Centro de Análisis de Registros y Minería de Eventos, destinada a los analistas de seguridad. Facilita la toma de decisiones e identifica amenazas en la organización. **IPS** |
| **CCNDroid** | Seguridad para Android |
| **CLARA** | Auditoría de cumplimiento ENS/STIC en sistemas Windows. Analiza las características de seguridad técnicas |
| **CLAUDIA** | Detección de amenazas complejas en el puesto de usuario |
| **microCLAUDIA** | Centro de vacunación |
| **ELENA** | Simulador de técnicas de cibervigilancia |
| **ELSA** | Exposición Local y Superficie de Ataque. Detecta vectores de ataque y analiza vulnerabilidades para reducir ciberataques |
| **EMMA** | Visibilidad y control sobre la red |
| **GLORIA** | Gestor de logs para responder ante incidentes y amenazas. **SIEM**. Se integra con CARMEN, REYES y LUCIA |
| **INES** | Informe Nacional del Estado de Seguridad. Portal que ofrece un conocimiento más rápido e intuitivo de su nivel de adecuación al ENS |
| **IRIS** | Muestra en tiempo real el estado de la ciberseguridad del sector público y a nivel nacional. Usa mapas interactivos |
| **LORETO** | Almacenamiento en la nube |
| **LUCIA** | Listado Unificado de Coordinación de Incidentes y Amenazas. Sistemas de Gestión Federada de Tickets. Tipos de ciberincidentes: propios del Organismo; del Sistema de Alerta Temprana de Red SARA (**SAT-SARA**, ver [[Red SARA]]); del Sistema de Alerta Temprana de Internet (**SAT-INET**) |
| **MÓNICA** | Gestión de eventos e información de seguridad. **NG SIEM** (Next Generation). Se integra con CARMEN, REYES y LUCIA |
| **OLVIDO** | Borrado seguro de datos |
| **metaOLVIDO** | Previene fugas de información y limpia metadatos e información sensible oculta en los ficheros ofimáticos publicados |
| **PILAR** | Análisis y Gestión de Riesgos siguiendo metodología de **Magerit** ([[Magerit, PILAR y µPILAR]]). Variantes: PILAR, PILAR Basic, µPILAR, **RMAT** (herramienta de configuración para consultores y grandes organizaciones). **EAR** (Entorno de Análisis de Riesgos) |
| **REYES** | Intercambio de información de ciberamenazas. Análisis de ciberincidentes y compartir información de ciberamenazas |
| **ROCIO** | Inspección de Operación. Auditoría de configuraciones de dispositivos de red |
| **VANESA** | Grabaciones y emisiones de vídeo en streaming. Formación y sensibilización |

> [!tip] Agrupar las herramientas del CCN
> - SIEM / gestión de eventos y logs: **GLORIA**, **MÓNICA** (ambos se integran con CARMEN, REYES y LUCIA).
> - Malware / amenazas: **ADA** (MARIA + MARTA), **CARMEN** (APT, en la DMZ), **CLAUDIA** / **microCLAUDIA** (puesto de usuario).
> - Auditoría / cumplimiento ENS: **AMPARO**, **ANA**, **CLARA** (Windows), **INES**, **ROCIO** (dispositivos de red), **ELSA** (superficie de ataque).
> - Riesgos: **PILAR** (Magerit).
> - Formación: **ANGELES**, **ATENEA**, **ELENA**, **VANESA**.
> - Datos: **CARLA** (protección y trazabilidad), **OLVIDO** (borrado seguro), **metaOLVIDO** (metadatos), **LORETO** (nube).
> - Incidentes: **LUCIA** (tickets federados), **REYES** (ciberamenazas), **IRIS** (estado nacional), **EMMA** (visibilidad de red), **CCNDroid** (Android).

---

## 3. CPD — Centro de Procesamiento de Datos

### 3.1 Elementos de un CPD

| Elemento | Descripción |
|---|---|
| **Racks / bastidores** | Servidores, switches, etc. organizados en racks. Anchura normalizada de **19 pulgadas**. Medida de altura (**u**) de **1,75 pulgadas** |
| **Pasillos fríos y calientes** | Alternancia para circulación de aire (**TIA 942**). Técnica de refrigeración. Armarios enfrentados. Suelo técnico perforado |
| **Climatización** | Temperatura y humedad constantes. **HVAC**. (**21 ºC con 50 % HR**) |
| **Iluminación** | Luz artificial, no natural |
| **Detección y control de incendios** | **NFPA 75** |
| **Energía eléctrica** | **SAI**s (apagado controlado) y **grupos electrógenos**. Cuadros eléctricos separados por salas/zonas |
| **Cableado estructurado** | Técnica para el cableado de un CPD. Suelos y techos falsos/técnicos (**TIA 568**) |
| **Control de acceso y videovigilancia** | |
| **Ubicación física** | Plantas intermedias, sin interferencias, sin canales de agua cerca |
| **CPD de respaldo** | Implica **réplica de datos**. **Sala blanca**: igual que el CPD principal. **Sala de backup**: similar pero ofrece menos servicio |

> [!important] Normas citadas
> TIA 942 (pasillos fríos/calientes y Tiers), TIA 568 (cableado estructurado), NFPA 75 (incendios; también citada en seguridad física).

Para la continuidad con un CPD de respaldo, ver también [[RPO vs RTO]].

### 3.2 Norma TIA 942 (Tier I a Tier IV)

La diferencia entre Tiers está en la **redundancia de componentes**. Hay **áreas funcionales (zonas)** y **4 subsistemas** para un datacenter: telecomunicaciones, arquitectura, sistema eléctrico y sistema mecánico.

| | Tier I | Tier II | Tier III | Tier IV |
|---|---|---|---|---|
| **Disponibilidad** | 99,671 % | 99,741 % | 99,982 % | 99,995 % |
| **Tº inactividad anual** | 28,8 h | 22 h | 1,6 h | 0,4 h |
| **Paradas por mantenimiento** | 2 al año de 12 h | 3 cada 2 años de 12 h | Ninguna | Ninguna |
| **Distribución de energía** | Única | Única | 1 activa y 1 pasiva (backup) | 2 activas |
| **Componentes redundantes** | Ninguno | N+1 | N+1 | 2 (N+1): todo está duplicado |

> [!tip] Resumen mnemotécnico de los Tiers
> I = sin redundancia; II = redundancia de componentes (N+1) pero energía única; III = N+1, energía con 1 activa + 1 pasiva y sin paradas por mantenimiento; IV = todo duplicado (2 (N+1)) con 2 distribuciones de energía activas.

### 3.3 Eficiencia y energía

| Sigla | Significado |
|---|---|
| **EPO** | Emergency Power Off. Para activar la interrupción del sistema de energía de emergencia |
| **PUE** | Power Usage Effectiveness. `PUE = 1/DCiE`. Valores de **1 a 2**; **1 es lo mejor** |
| **DCiE** | Eficiencia del CPD. `DCiE = Consumo de la parte informática / Potencia` |
| **CUE** | Carbon Usage Effectiveness. Debe tender a **0** |
| **WUE** | Water Usage Effectiveness |
| **ERE** | Energy Reuse Effectiveness |
| **OCE** | Overall Consumption Effectiveness. Eficiencia de los consumos |
| **Green Computing** | Concepto asociado a la eficiencia |

> [!note] Erratas / actualizaciones (Actualizaciones 20_05_2026)
> El documento de actualizaciones recoge para este tema solo tres cambios, todos ya incorporados en el PDF: (1) 26/08/2024: añadidas dos herramientas del CCN, **ELSA** y **metaOLVIDO**; (2) 17/01/2025: ampliación de la descripción de la herramienta **ANA**; (3) 08/02/2025: nuevas medidas de eficiencia del CPD, **CUE, ERE y WUE**. No hay erratas que corregir en este tema.

> [!note] Ampliación (conocimiento general, no viene del PDF)
> En la práctica, PUE se define como (energía total que consume el CPD) / (energía consumida por los equipos informáticos), por eso su valor mínimo teórico es 1: toda la energía llegaría a los equipos TI sin pérdidas de refrigeración ni distribución. Es consistente con lo que dice el PDF (`PUE = 1/DCiE`, con DCiE como fracción útil).

---

## 4. Herramientas de gestión de incidencias / ticketing

| | | | |
|---|---|---|---|
| GLPI | Bugzilla | Trac | SpiceWorks help desk |
| Request Tracker (RT) | Redmine | OTRS | Remedy (soporte al **SLA**) |
| MANTIS Bug Tracker | JIRA | OSTicket | |

---

## 5. Herramientas de control remoto de puestos

| Herramienta | Nota |
|---|---|
| **VNC** | Cliente/Servidor. **Puerto 5900** |
| **RDP** | Cliente/Servidor. Servidor: MS Terminal Server. **Puerto 3389** |
| **SSH** | Ver [[B4 - T1.2 ADMON SSOO - SSH]] |
| TeamViewer | Nube |
| AnyDesk | |
| Chrome Remote Desktop | |
| LogMeIn | |
| Citrix | |
| Ammyy Admin | |
| BeAnywhere | |

---

## 6. Conexiones con otros temas

- Gestión de la seguridad como función del administrador de redes: [[B4 - T4 ADMON REDES]].
- Marco legal del ENS y la respuesta a incidentes: [[B1 - T8 ACCESO ELECTRONICO, ENS Y ENI]], [[CCN-CERT]], [[CSIRT]].
- Protección de datos y evaluación de impacto: [[B1 - T7 PROTECCION DE DATOS]], [[Evaluación de Impacto relativa a la Protección de Datos (EIPD)]].
- Criptografía y certificados: [[Criptografía asimétrica (clave pública y privada)]], [[Certificado TLS-SSL (X.509)]].
- Backup y recuperación: [[Estrategias de backup (Completa, Incremental, Diferencial)]], [[RPO vs RTO]].

---

## 🔑 Resumen ultra-rápido

- Proteger activos (información y servicio). Guía **CCN-STIC-400**.
- **SGSI**: ISO/IEC 27001 y 27002, ciclo **PDCA**. **ENS**: obligatorio en Admón Pública; análisis de riesgos con **MAGERIT** (+ Pilar/µPilar), OCTAVE, CRAMM, MEHARI, SP800-30, UNE 71504, EBIOS. **Common Criteria** EAL 1-7 (eDNI). Otras: ISM3, Cobit, SOGP, TLLJO, ITIL.
- **Tríada CIA**: Confidencialidad y Integridad (dato), Disponibilidad (servicio). Más: trazabilidad, autenticidad (no repudio, origen).
- Riesgo = Probabilidad × Impacto; riesgo **potencial** (antes de salvaguardas) vs **residual** (después). EIPD: **RGPD art. 35**.
- Seguridad física: acceso, incendios (NFPA 75), SAI, CCTV. Lógica: antivirus, firewall, IDS/IPS, VPN/SSL, antispam, políticas, backups, autenticación (Radius/Kerberos, OAuth/JWT, OpenId, SAML/Cl@ve, biométricos, OTP).
- **MFA**: lo que sé / lo que tengo / lo que soy.
- Actores: Hacker (protege), Cracker (ilícito), Lamer, Phreaker (telefonía), Newbie, CopyHacker, ScriptKiddie. **CVE-YYYY-NNNN** (MITRE), CWE.
- Herramientas: nmap (puertos), nessus/OpenVAS (vulnerabilidades), Metasploit (pentest), Snort (NIDS/IPS), tcpdump, wireshark, Kali; crackers John, Hydra, Ncrack, Medusa; Cain y Abel; Shodan; Nikto; sqlmap.
- Malware: virus, gusano (RAM/red), troyano (admin remota), rootkit, backdoor, spyware, ransomware, keylogger, adware, rogue.
- Ataques: SQL injection, XSS (defensa CSP), hijacking, phishing (QRishing), pharming (DNS), spoofing, DoS (teardrop, SYN flood, ICMP/Smurf, UDP flood), DDoS (botnets).
- Red Team (ofensivo), Blue Team (defensivo), Purple Team (compartir).
- CCN: ADA (MARIA + MARTA), AMPARO, ANA (On Premise/Central), ANGELES, ATENEA, CARLA, CARMEN (DMZ, APT, IPS), CCNDroid, CLARA, CLAUDIA, microCLAUDIA, ELENA, ELSA, EMMA, GLORIA (SIEM), INES, IRIS, LORETO, LUCIA (SAT-SARA, SAT-INET), MÓNICA (NG SIEM), OLVIDO, metaOLVIDO, PILAR (Magerit), REYES, ROCIO, VANESA.
- CPD: rack 19", 1u = 1,75"; pasillos fríos/calientes (TIA 942); 21 ºC con 50 % HR; luz artificial; NFPA 75; SAI + grupos electrógenos; cableado TIA 568; CPD de respaldo (sala blanca = igual; sala de backup = menos servicio).
- **Tiers**: I 99,671 % (28,8 h/año, sin redundancia); II 99,741 % (22 h, N+1); III 99,982 % (1,6 h, N+1, energía 1 activa + 1 pasiva); IV 99,995 % (0,4 h, 2 activas, 2 (N+1)).
- EPO (corte de emergencia); PUE = 1/DCiE (1 a 2, 1 mejor); CUE tiende a 0; WUE (agua); ERE (reutilización de energía); OCE (consumos).
- Ticketing: GLPI, RT, Mantis, Bugzilla, Redmine, JIRA, Trac, OTRS, OSTicket, SpiceWorks, Remedy (SLA).
- Control remoto: VNC (5900), RDP (3389), TeamViewer, AnyDesk, Chrome Remote Desktop, LogMeIn, Citrix, Ammyy Admin, SSH, BeAnywhere.
