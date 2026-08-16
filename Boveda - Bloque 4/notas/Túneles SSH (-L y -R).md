SSH permite crear canales seguros para redirigir tráfico de red además de para abrir una sesión interactiva:

- **Túnel local (`ssh -L your_port:site_or_IP_to_access:site_port username@host`)**: el puerto que se abre queda **en tu máquina** (`your_port`); el tráfico que llega a ese puerto viaja, a través del túnel, hasta `site_port` en el host remoto. Útil para acceder tú a un servicio que solo es visible desde el servidor.
- **Túnel remoto (`ssh -R remote_port:site_or_IP_to_access:site_port username@host`)**: el puerto que se abre queda **en el servidor remoto** (`remote_port`); el tráfico que llega a ese puerto viaja hasta `site_port`, en tu propia máquina. Útil para exponer un servicio tuyo local a través de un servidor que sí es accesible desde fuera (por ejemplo, para saltarte un NAT).

En ambos casos se hace un túnel para ocultar/proteger un servicio: se crea un canal seguro que sustituye a una conexión directa, no protegida, al servicio real.

[[B4 - T1.2 ADMON SSOO - SSH]]
