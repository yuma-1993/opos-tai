**`apache2ctl`** (y su alias **`apachectl`**, el mismo binario con nombre distinto según la distribución/paquete) es el comando de control del servicio Apache HTTP Server:

- `apache2ctl status` / `fullstatus` — estado del servicio.
- `apache2ctl start` / `stop` / `restart` — arrancar, parar o reiniciar.
- `apache2ctl -M` — ver los módulos activos.
- `apache2ctl -t` — probar la sintaxis del fichero de configuración.

**¿Por qué hace falta `-t`?** Conviene ejecutarlo siempre antes de un `restart` en producción: si el fichero de configuración tiene un error de sintaxis, un `restart` directo puede dejar el servicio caído sin volver a arrancar; `-t` valida la sintaxis sin llegar a recargar nada.

[[B4 - T1.3 ADMON SSOO - APACHE]]
