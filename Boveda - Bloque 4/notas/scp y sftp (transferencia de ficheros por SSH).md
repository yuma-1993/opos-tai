**`scp`** (*secure copy*) copia ficheros entre dos máquinas a través de SSH, sin abrir una sesión interactiva:

```
scp [opciones] [origen usuario@IP]:/ruta/fichero [destino usuario@IP]:/ruta/destino
scp usuario@remotehost.edu:foobar.txt /directorio/local
scp foobar.txt usuario@remotehost.edu:/directorio/remoto
```

Opciones principales: `-r` (copia recursiva de directorios), `-p` (conserva tiempos de modificación y atributos del fichero original), `-l` (limita el ancho de banda usado, en Kbit/s).

**`sftp`** es un cliente de copia remota similar a `scp`, también sobre el canal cifrado de SSH.

[[B4 - T1.2 ADMON SSOO - SSH]]
