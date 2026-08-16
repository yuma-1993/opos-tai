**LVM (Logical Volume Manager)**, también llamado **Dynamic Disks**, es la capa que permite gestionar el almacenamiento como volúmenes lógicos flexibles en vez de particiones fijas.

La cadena completa, de abajo arriba: discos físicos (posible [[RAID (Redundant Array of Independent Disks)|RAID]] por debajo, con `mdadm`) → **Partitions** → **PV (Physical Volume)**, creado con `pvcreate` (`pvdisplay`, `pvmove`); cada PV se divide en trozos llamados **PE (Physical Extents)** → **VG (Volume Group)**, creado con `vgcreate` (`vgdisplay`, `vgextend`), que agrupa varios PV formando un "pool" común de espacio → **LV (Logical Volume)**, creado con `lvcreate` (`lvdisplay`, `lvextend`) recortando espacio del VG; cada LV se divide en **LE (Logical Extents)** → sistema de ficheros, que hay que formatear y montar para poder usarlo.

Se crea una tabla de mapeo entre los PE y los LE (comando `lvdisplay -m`). Para ampliar un LV: `lvextend` + `resize2fs` + `mkfs.ext4` + `mount`.

**¿Por qué hace falta esto?**
Un LV se puede ampliar en caliente (sin desmontar, sin reiniciar) siempre que el VG tenga espacio libre — algo que con particiones tradicionales no es tan directo. El precio es una capa extra de abstracción, y por tanto de complejidad para diagnosticar problemas.

[[B4 - T1.1 ADMON SSOO]]

**Conexiones con otros conceptos TAI:**
- [[RAID (Redundant Array of Independent Disks)]] — capa independiente que suele quedar por debajo de LVM: RAID protege del fallo físico de disco, LVM aporta flexibilidad para redimensionar volúmenes.
