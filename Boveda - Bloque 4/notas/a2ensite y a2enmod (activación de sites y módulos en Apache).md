En Apache (Debian/Ubuntu), **`a2ensite`** activa la configuración de un site y **`a2enmod`** activa un módulo — por ejemplo, `a2ensite 100-ruinosa.conf` o `a2enmod ssl`. En ambos casos, "activar" no significa instalar ni escribir configuración nueva: es crear un **enlace simbólico** dentro de `/etc/apache2`, entre el directorio donde está *disponible* (`sites-available`, `mods-available`) y el directorio donde queda *activo* (`sites-enabled`, `mods-enabled`).

`*-available` contiene **todas** las configuraciones o módulos instalados, estén activos o no; `*-enabled` contiene solo enlaces simbólicos a los que están realmente en uso. Los comandos complementarios `a2dissite`/`a2dismod` desactivan borrando ese enlace, sin tocar el fichero original.

**¿Por qué hace falta esto?** Permite tener una configuración o un módulo guardado pero apagado, listo para reactivar sin volver a escribirlo — y probar o depurar activando/desactivando sin perder nada.

[[B4 - T1.3 ADMON SSOO - APACHE]]
