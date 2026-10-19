---
tags:
  - bloque4
  - tema4
  - administracion-redes
  - snmp
  - mib
  - rmon
  - ldap
  - monitorizacion
bloque: 4
tema: 4
titulo: Administración de redes — funciones, monitorización (SNMP, RMON, CMIP) y gestión de usuarios (LDAP)
estado: por-repasar
---

# Tema 4 · Bloque 4 — Administración de redes

> [!abstract] De qué va este tema
> Primero se enumeran las funciones del administrador de redes (diseño, usuarios, dispositivos, seguridad, almacenamiento, backup, impresión, voz/vídeo y monitorización). Después se desarrollan las dos piezas que el temario detalla: la **monitorización y gestión con SNMP** (modelo Gestor-Agente, SMI, MIB, PDUs, versiones, RMON, herramientas NMS y alternativas OSI como CMIP/CMOT) y la **gestión de usuarios con LDAP** (directorio jerárquico basado en X.500, árbol, DN/RDN, LDIF, ObjectClass).

---

## 1. Funciones del administrador de redes

| Función | Contenido / ejemplos del PDF |
|---|---|
| Planificación y diseño | De la red |
| Gestión de usuarios y grupos | Ej: **LDAP** (ver sección 4) |
| Gestión de los dispositivos | Switch (VLAN), routers (subnetting), etc. |
| Gestión de la seguridad | Firewall (reglas), IDS/IPS, análisis de vulnerabilidades (ver [[B4 - T5 SEGURIDAD SI Y CPD]]) |
| Gestión de almacenamiento | Redes SAN (Zoning, LUN), NAS (CIFS/NFS) — ver [[SAN (Storage Area Network)]], [[Zoning (SAN)]], [[LUN y LUN Masking]], [[NAS (Network Attached Storage)]] |
| Gestión del backup | Enlaces dedicados, política, librerías LTO — ver [[Estrategias de backup (Completa, Incremental, Diferencial)]], [[LTO (Linear Tape-Open)]] |
| Gestión de la impresión | Configuración de impresoras **IPP** |
| Gestión de videoconferencia y VoIP | **Asterisk** (servicio de centralita o PBX) |
| Monitorización y supervisión | Configuración de agentes (alarmas) **SNMP**. Análisis de tráfico |

---

## 2. Monitorización y gestión: SNMP (Simple Network Management Protocol)

### 2.1 Características generales

- SNMP va sobre **UDP**. Deriva del protocolo **SGMP** (para Gateways). SNMP es de la **pila TCP/IP, no de OSI**.
- Modelo Cliente/Servidor denominado **Gestor-Agente**:
  - El **Gestor** es la estación central, el **NMS** (Network Management System).
  - El **Agente** es el software que se instala en cada dispositivo gestionable.

### 2.2 RFC de referencia

| RFC | Qué define |
|---|---|
| **RFC 1155** | **SMI**: árbol, tipos de datos y macro `OBJECT-TYPE` |
| **RFC 1156** | **MIB 1** |
| **RFC 1157** | **Protocolo**: PDUs |
| **RFC 1213** | **MIB 2** |
| RFC 2578 | **SMI v2** (versión 2c, ver 2.6) |

> [!tip] Truco para ordenar las RFC
> Van en orden de capa lógica: 1155 (estructura/SMI) → 1156 (datos/MIB 1) → 1157 (protocolo) → 1213 (MIB 2, la ampliación).

### 2.3 Versión 1: SMI, árbol y MIB

En la RFC 1155 se define la **SMI** (Estructura de Información de Gestión). Principalmente se define la estructura del árbol, los tipos de datos y la macro `OBJECT-TYPE` (≈ Estructura).

#### Árbol core de OBJECT-IDENTIFIERs

El número sirve para administrar la monitorización, para preguntar directamente por ese objeto. Ej: `1.3.6.1.4.1` → enterprises.

```
iso (1)
 └─ organization (3)
     └─ DoD (6)
         └─ internet (1)
             ├─ directory (1)
             ├─ management (2)
             │    └─ MIB-2 (1)
             ├─ experimental (3)
             └─ private (4)
                  └─ enterprises (1)
```

| Rama | OID |
|---|---|
| iso | 1 |
| organization | 3 |
| DoD | 6 |
| internet | 1 |
| directory | 1 |
| management (mgt) | 2 |
| experimental | 3 |
| private | 4 |
| MIB-2 (bajo management) | 1 |
| enterprises (bajo private) | 1 → `1.3.6.1.4.1` |

- En el árbol se definen todos los parámetros monitorizables, todos los OBJECTs, los OIDs.
- **Enterprises**: aquí los fabricantes crean su propia rama y cuelgan sus productos monitorizables. `enterprises OBJECT IDENTIFIER ::= {private 1}`.
- Mediante sintaxis **ASN.1** se definen las bases para definir los MIB.

> [!important] Qué es un MIB
> Un **MIB** es una serie de parámetros agrupados para que un cierto Agente pueda responder ante ellos. Es la **BD de gestión de un Agente**. Ej: conjunto de parámetros monitorizables del switch 2960 de Cisco. Cada aparato tiene su propio MIB, aunque hay una parte general, común, que cuelga de **management (mgt)**. En la RFC 1156 se define el MIB 1; en la RFC 1213, el MIB 2.
>
> El MIB (RFC 1156) es un *module*, donde se importa la definición de la RFC 1155, se definen nuevas ramas del árbol SMI y objetos gestionables.

#### Tipos de datos (SMI)

Counter, TimeTicks, IpAddress, Gauge (escrito "Guage" en el PDF), Opaque, Network Address, Number, String, **OID** (Object Identifier, para definir ramas del árbol), **Sequence** (para crear tablas).

#### Macro OBJECT-TYPE (transcripción del PDF)

```
OBJECT-TYPE MACRO ::=
  BEGIN
    TYPE NOTATION ::= "SYNTAX" type (TYPE ObjectSyntax)
                      "ACCESS" Access
                      "STATUS" Status
    VALUE NOTATION ::= value (VALUE ObjectName)

    Access ::= "read-only"
             | "read-write"
             | "write-only"
             | "not-accessible"
    Status ::= "mandatory"
             | "optional"
             | "obsolete"
  END
```

| Campo | Valores posibles |
|---|---|
| `ACCESS` | read-only, read-write, write-only, not-accessible |
| `STATUS` | mandatory, optional, obsolete |

Ejemplo del PDF (tabla `atTable` y objeto `AtIndex`):

```
atTable OBJECT-TYPE
  SYNTAX SEQUENCE OF AtEntry
  ACCESS read-write
  STATUS mandatory
  ::= { at 1 }

AtEntry ::= SEQUENCE {
  atIndex        INTEGER,
  atPhysAddress  OCTET STRING,
  atNetAddress   NetworkAddress
}
```

| Ejemplo de objeto | Valor |
|---|---|
| OBJECT | `AtIndex { atEntry 1 }` |
| Syntax | INTEGER |
| Definition | The interface number for the physical address |
| Access | read-write |
| Status | mandatory |

> [!note] Producto
> **MIB Browser**: producto para monitorizar máquinas (navegar el MIB de un agente).

### 2.4 El protocolo (RFC 1157): PDUs

Estructura del mensaje SNMP (diagrama del PDF): `IP header | UDP header | Versión | Community name | SNMP PDU`.

- **Community**: cadena de seguridad (≈ contraseña).
- **Variable Bindings**: pares OID + valor | OID + valor…

Formato de cada PDU (campos tras `PDU type`):

| PDU | Campos |
|---|---|
| Get / GetNext | PDU type, Request ID, 0, 0, Variable bindings |
| GetBulk | PDU type, Request ID, Non repeaters, Max repetitions, Variable bindings |
| Response | PDU type, Request ID, Error status, Error index, Variable bindings |
| Set | PDU type, Request ID, 0, 0, Variable bindings |
| Trap (SNMPv1) | PDU type, Enterprise, Agent addr, Generic trap, Specific trap, Time stamp, Variable bindings |
| Trap / Inform (SNMPv2c) | PDU type, Request ID, 0, 0, Variable bindings |

#### Tipos de PDU y sentido

| Sentido | Puerto UDP | PDU | Función |
|---|---|---|---|
| Gestor → Agente | **161** | **Get** + **Response** (van de la mano) | Consulta de un valor y su respuesta |
| Gestor → Agente | **161** | **GetNext** | Da la información del siguiente OID. Ej: para navegar por una tabla. Usado por `snmpwalk` |
| Gestor → Agente | **161** | **Set** | Modificar un valor |
| Agente → Gestor | **162** | **Trap** | Alarma. Ej: si reinicias `snmpd` en la máquina monitorizada, manda un trap al gestor |

> [!important] Puertos
> El Gestor pregunta al **161** del Agente; el Agente avisa (trap) al **162** del Gestor. Truco: 161 = "consulta" (el agente escucha), 162 = "alarma" (el gestor escucha).

#### Comandos

| Comando | Qué hace |
|---|---|
| `snmpget` | Usa consultas de recuperación simples, para obtener un objeto específico (OID – Object Identifier) |
| `snmpwalk` | Dado un primer OID, va recuperando lo que devuelve *GetNext Request* y con esa información podemos movernos por la tabla. Es como un recorrido en profundidad del árbol |

### 2.5 Agentes

- **Agente**: software que gestiona una determinada MIB.
- **Protocolo AgentX**: para poder extender el agente principal con nuevos módulos MIB, para tener **subagentes**. Es una especie de plugin que resulta transparente.
- En el Agente corre **`snmpd`**, demonio de SNMP. Producto: **net-snmp** para Linux.
- Fichero `/etc/snmp/snmp.conf` para definir la Community y la IP del equipo Gestor. Ejemplo del PDF: `rocommunity tai 192.168.0.1/24`.

### 2.6 Versiones de SNMP

| Versión | Características |
|---|---|
| **v1** | RFC 1155 (SMI), 1156 (MIB 1), 1157 (protocolo), 1213 (MIB 2). PDU Trap con formato propio |
| **v2c** | *Community based*. **Es la usada hoy día**. **Incompatible con la v1**. Amplía el modelo con la **RFC 2578** (SMI v2): nuevos tipos de datos, macro `NOTIFICATION-TYPE` y árbol core más completo con la rama MIB-2. Nuevas primitivas: GetBulk, SNMPv2-Trap, Inform, Report |
| **v3** | Añade **seguridad SSH** (según el PDF). No muy extendida porque da problemas de compatibilidad al ser tan reciente |

Nuevas primitivas de la v2c:

| Primitiva | Qué hace |
|---|---|
| **GetBulk** | Obtiene todo lo que cuelga de la rama. No hace GetNext, sino que es masivo |
| **SNMPv2-Trap** | Tramas tipo trap en la versión 2c |
| **Inform** | **Gestor-Gestor**. Sirve para comunicación entre Gestores |
| **Report** | No está definido aún su uso |

> [!note] Ampliación (conocimiento general, no viene del PDF)
> El PDF dice que SNMPv3 "añade seguridad SSH". Conviene saber que, en general, lo que añade SNMPv3 es autenticación y cifrado propios del protocolo (modelo de seguridad basado en usuario, USM), no el protocolo SSH de [[B4 - T1.2 ADMON SSOO - SSH]]. Para el examen, tener presente el enunciado del temario ("seguridad") y no confundir con la community de v1/v2c, que viaja en claro.

### 2.7 RMON MIB

- Caso muy particular de MIB en el que se encuentra información muy completa, con **estadísticas históricas** sobre una determinada **zona de la red**.
- Al software se le llama **Sonda** en lugar de Agente. Ofrece información **de la red**, no de un equipo concreto como hace el Agente.
- Suele instalarse en un **router troncal**, en un **switch** o en **hardware específico**.

| Versión | Qué monitoriza |
|---|---|
| **RMON v1** | Solo tráfico a **nivel 1 y 2** (Física y Enlace) |
| **RMON v2** | Tráfico de **nivel 3 a 7** |

Diagrama del PDF ("Versiones de RMON"): sobre el modelo de capas (Application, Presentation, Session, Transport, Network, Data Link, Physical), **RMON** abarca las capas física y de enlace y **RMON2** cubre de la capa de red hasta la de aplicación.

### 2.8 Herramientas NMS

Instaladas en el Gestor. Funcionan con todo tipo de Agentes, ya que SNMP es un estándar.

| | | | | |
|---|---|---|---|---|
| Nagios | Cacti | OpenView | Pandora FMS | SolarWinds |
| Zabbix | Patrol | Zennos | Icinga | OpenNMS |

---

## 3. Otros protocolos de monitorización y gestión

| Protocolo | Descripción |
|---|---|
| **TMN** | Usado en grandes redes de telecomunicaciones (redes WAN gigantes) |
| **CMIP/CMIS** | Propuesta de la **pila OSI** similar a SNMP |
| **CMOT** | Cuando CMIP va sobre la pila TCP/IP en lugar de sobre OSI |

### SNMP vs CMIP/CMIS

| Aspecto | SNMP | CMIP/CMIS |
|---|---|---|
| Pila | TCP/IP | OSI |
| Crear y borrar objetos | **No lo permite** (la estructura ya está definida por el estándar y por el fabricante) | **Permite borrar y crear** |
| Conexión | **No orientado a conexión** (UDP) | **Orientado a conexión** |
| Alarmas | Trap | *Event driven* (es como el Trap de SNMP) |

---

## 4. Gestión de usuarios: LDAP (Lightweight Directory Access Protocol)

### 4.1 Características

- Usado no solo para usuarios, sino también para **máquinas**.
- **Base de datos jerárquica**.
- Versión actual **LDAP v3**.
- **LDAP es binario**.
- Basado en las recomendaciones **X.500** (OSI) de directorio (estructura del árbol).
- Utiliza **TCP puerto 389**. En **LDAP + SSL** utiliza el puerto **636** (LDAPS).

| Servicio | Transporte | Puerto |
|---|---|---|
| LDAP | TCP | 389 |
| LDAPS (LDAP + SSL) | TCP | 636 |

> [!important] Autentica, no autoriza
> De cara a la seguridad, podemos **autenticar** contra LDAP. **No autorizamos, solo autenticamos.** Ej: si la máquina que intenta acceder no está registrada en LDAP, no podrá entrar; igual con los usuarios. LDAP almacena los datos de autenticación (user/pass o certificado X.509).

### 4.2 Operaciones

| Operación | Qué hace |
|---|---|
| **StartTLS** | Cambia a modo seguro |
| **Bind** | Conectarse y autenticarse |
| **Search** | Buscar |
| **Add** | Añadir |
| **Delete** | Borrar |
| **Modify** | Modificar |

> [!note] StartTLS
> Usado en LDAP, IMAP, POP3, SMTP (ESMTP), FTP, HTTP, etc. Es una extensión a los protocolos de comunicación de texto plano. Relacionado con TLS: ver [[Certificado TLS-SSL (X.509)]].

### 4.3 URL del servicio

`ldap://host:port/DN?atributes?scope?filter?extensions`

| Componente | Significado |
|---|---|
| **DN** | Distinguished Name: es la **PK** de cualquier entrada del árbol |
| **atributes** | Lista separada por comas de atributos a devolver |
| **scope** | Profundidad de búsqueda: **base** (por defecto) / **one** (1 nivel) / **sub** (árbol) |
| **filter** | Ej: `ObjectClass = *`, person, group, ou, etc. |
| **extensions** | Extensiones |

### 4.4 Estructura del árbol

- Una **entrada** es un conjunto de atributos (Nombre: valor).
- Cada entrada tiene un identificador único llamado **Distinguished Name**: **DN = RDN + DN padre**.

| Abreviatura | Significado |
|---|---|
| dn | distinguished name |
| dc | domain component |
| ou | organizational unit |
| cn | common name |
| rdn | relative dn |

#### Formato LDIF (LDAP Data Interchange Format)

- LDIF es un **formato de fichero**. Puede usarse para **poblar de forma masiva** el árbol de LDAP: generas el fichero y lo subes. Se usa para **importación y exportación**.

Ejemplo del PDF:

```
dn: cn = Jhon Doe, dc = ibm, dc = com        <- RDN (cn = Jhon Doe) + DN padre (dc = ibm, dc = com: Domain Component)
cn: Jon Doe
givenName: Jhon                              \
sn: Doe                                       > Metadatos
telephoneNumber: +34666555444                /
ObjectClass: top                             \ Jerarquía de clases. Te quedas con la última
ObjectClass: person                          / Tipos definidos en X.521, con sus atributos predefinidos
changeType: add                              <- añadir al árbol una nueva entrada (como llamar a la primitiva Add)
```

> [!important] ObjectClass
> **ObjectClass** es un **esquema**: las distintas entradas para definir las propiedades de los atributos. Una definición objectclass determina qué atributos se requieren y cuáles no para cada entrada. Tipos definidos en **X.521**, con sus atributos predefinidos: `person` (usuarios), `device`, `organizationalUnit`, `group`, etc. Las clases forman una jerarquía (top → person): te quedas con la última.

### 4.5 Productos y API

| Producto | Notas |
|---|---|
| **Active Directory** | Windows |
| **OpenLDAP** | |
| **Apache Directory Server** | |
| **Red Hat Directory Server** | |
| **JNDI** | API de Java para gestionar consultas LDAP. Viene con la propia JRE |

---

## 5. Conexiones con otros temas

- Gestión de la seguridad (firewall, IDS/IPS, vulnerabilidades): [[B4 - T5 SEGURIDAD SI Y CPD]].
- Almacenamiento y backup (funciones del administrador): [[SAN (Storage Area Network)]], [[NAS (Network Attached Storage)]], [[LUN y LUN Masking]], [[Zoning (SAN)]], [[Estrategias de backup (Completa, Incremental, Diferencial)]], [[LTO (Linear Tape-Open)]].
- Administración remota y automatización de equipos: [[B4 - T1.2 ADMON SSOO - SSH]] (SSH), [[B4 - T1.1 ADMON SSOO]].
- Autenticación con certificados X.509 en LDAP: [[Certificado TLS-SSL (X.509)]].

---

## 🔑 Resumen ultra-rápido

- Funciones: diseño, usuarios (LDAP), dispositivos (VLAN, subnetting), seguridad, almacenamiento (SAN/NAS), backup (LTO), impresión (IPP), VoIP/videoconferencia (Asterisk), monitorización (SNMP).
- SNMP: sobre **UDP**, pila **TCP/IP** (no OSI), deriva de **SGMP**; modelo **Gestor (NMS) - Agente**.
- RFC: **1155** SMI (árbol, tipos, OBJECT-TYPE), **1156** MIB 1, **1157** protocolo/PDUs, **1213** MIB 2, **2578** SMI v2.
- Árbol: iso(1).org(3).DoD(6).internet(1); `management(2)` → MIB-2; `private(4)` → `enterprises(1)` = `1.3.6.1.4.1` (ramas de fabricantes).
- MIB = BD de gestión de un Agente; sintaxis ASN.1; parte común bajo `mgt`.
- Puertos UDP: Gestor→Agente **161** (Get/Response, GetNext, Set); Agente→Gestor **162** (Trap).
- `snmpget` = un OID concreto; `snmpwalk` = recorrido con GetNext (profundidad).
- v1 / **v2c** (community, usada hoy, incompatible con v1; GetBulk, SNMPv2-Trap, Inform = Gestor-Gestor, Report) / **v3** (seguridad, poco extendida).
- Agente: `snmpd`, net-snmp, AgentX (subagentes), `/etc/snmp/snmp.conf` (`rocommunity tai 192.168.0.1/24`).
- RMON: sonda, estadísticas históricas de una zona de red; v1 niveles 1-2, v2 niveles 3-7.
- NMS: Nagios, Cacti, OpenView, Pandora FMS, SolarWinds, Zabbix, Patrol, Zennos, Icinga, OpenNMS.
- Otros: TMN (WAN gigantes), CMIP/CMIS (OSI; crea/borra; orientado a conexión; event driven), CMOT (CMIP sobre TCP/IP).
- LDAP: directorio jerárquico, v3, binario, basado en X.500; TCP **389**, LDAPS **636**; autentica pero no autoriza.
- LDAP operaciones: StartTLS, Bind, Search, Add, Delete, Modify. URL `ldap://host:port/DN?atributes?scope?filter?extensions`; scope base/one/sub.
- DN = RDN + DN padre; LDIF para importar/exportar masivamente; ObjectClass = esquema (X.521: person, device, organizationalUnit, group).
- Productos: Active Directory, OpenLDAP, Apache Directory Server, Red Hat Directory Server; JNDI (API Java).
