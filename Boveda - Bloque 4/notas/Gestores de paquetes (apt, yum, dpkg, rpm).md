En Linux hay dos niveles de herramientas para instalar software, con el mismo patrón en las dos grandes familias de distribuciones:

| | Debian | Red Hat |
|---|---|---|
| Instalar con resolución de dependencias | `apt install` | `yum install` |
| Actualizar índice de paquetes | `apt update` | `yum update` |
| Buscar | `apt cache search` (`axi-cache search`) | `yum search` |
| Directorio de repositorios | `/etc/apt/sources.list` | `/etc/yum.repos.d` |
| Instalación offline de un paquete individual | `dpkg` (`.deb`) | `rpm` (`.rpm`) |

> [!important] Idea clave
> `apt`/`yum` gestionan dependencias y descargan de repositorios remotos; `dpkg`/`rpm` instalan un paquete individual ya descargado, en modo offline, **sin resolver dependencias por sí solos**.

[[B4 - T1.1 ADMON SSOO]]
[[B2 - T4.2 WINDOWS Y SISTEMAS OPERATIVOS MOVILES]] — el mismo concepto en Windows (WinGet, Chocolatey, Scoop) y macOS (HomeBrew).
