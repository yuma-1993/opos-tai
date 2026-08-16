Es la unidad básica de comando en PowerShell, organizada en **módulos** (gestionables con `Get-Module –ListAvailable`/`–All` e `Import-Module`). A diferencia de los comandos tradicionales de Linux, los cmdlets están escritos en **.NET** y **retornan objetos**, no texto plano — por eso se pueden encadenar con `| Where-Object`, `| Sort-Object`, `| ForEach-Object` filtrando por propiedades reales del objeto. Tienen alias (ej. `Get-Alias ls`). Se descubren con `Get-Command` y `Get-Help` (`–full`, `–examples`, `–online`), y sus propiedades con `Get-ChildItem | Get-Member`.

> [!note] Conocimiento general (no viene literal del tema)
> Los cmdlets siguen siempre el patrón de nombre **Verbo-Sustantivo** (`Get-ChildItem`, `Import-Module`, `Sort-Object`): si existe `Get-Process`, es razonable esperar que también exista `Stop-Process`.

> [!important] Diferencia clave frente a Bash
> En Linux, la tubería (`|`) pasa **texto**. En PowerShell, la tubería pasa **objetos**, con sus propiedades y métodos.

[[B4 - T1.1 ADMON SSOO]]
