**Sistemas de Aplicaciones y Redes para las Administraciones (SARA)**: conjunto de infraestructuras de comunicaciones y servicios básicos que conecta las redes de las AAPP españolas e instituciones europeas, facilitando el intercambio de información y el acceso a los servicios prestados desde ella.

Cada organismo se conecta a través de un **Punto de Presencia (PdP)**, la sede con conexión directa a SARA, a la que se accede mediante un **Proveedor de Acceso a la Red SARA (PAS)**: un intermediario que instala en sus dependencias un **Área de Conexión (AC)**, una [[DMZ (zona desmilitarizada)|DMZ]] con DNS, Proxy, Switch, SMTP, IDS, IPS, Firewall y Proxy Inverso, con todo lo necesario para que un departamento se integre en la red. Hacia el resto de sedes de SARA se establece **VPN**, cifrando las comunicaciones con túneles.

La conexión con las instituciones europeas se hace a través de la **red s-TESTA** (servicios transeuropeos seguros de telemática entre administraciones), mientras que las **universidades públicas** se conectan a SARA a través de la **red IRIS** como salto intermedio. Sus características principales son fiabilidad, seguridad, capacidad, calidad de servicio e interoperabilidad.

SARA también es la infraestructura que distribuye la **Hora Oficial Española** a las AAPP conectadas mediante el protocolo [[NTP (Network Time Protocol)|NTP]].

[[B1 - T9.2 SERVICIOS COMUNES]]

**Conexiones con otros conceptos TAI:**
- [[DMZ (zona desmilitarizada)]] — el Área de Conexión que da acceso a SARA es una DMZ.
- [[NTP (Network Time Protocol)]] — protocolo con el que SARA distribuye la hora oficial.
