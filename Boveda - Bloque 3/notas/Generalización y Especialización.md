Es la relación "es un" (herencia): una entidad general (superclase) se especializa en subtipos más concretos, o al revés, varios subtipos concretos se generalizan en un tipo general. Ej: `Vehículo` (general) se especializa en `Coche` y `Moto` (específicos).

Se clasifica en dos ejes **independientes entre sí** (se pueden combinar los cuatro cruces posibles):

- **Disjunta vs Solapada** — ¿puede una entidad pertenecer a más de un subtipo a la vez?
  - Disjunta: NO puede (un `Vehículo` es Coche o Moto, nunca ambos).
  - Solapada: SÍ puede (una `Persona` puede ser `Empleado` y `Cliente` a la vez).
- **Total vs Parcial** — ¿todas las entidades del tipo general deben pertenecer a algún subtipo?
  - Total: sí, obligatorio. No puede existir un `Vehículo` "suelto" que no sea ni Coche ni Moto.
  - Parcial: puede haber entidades del tipo general que no pertenezcan a ningún subtipo. Ej: `Empleado` se especializa en `Comercial` y `Directivo`, pero puede haber un administrativo que no sea ninguno de los dos.

> [!tip] Truco
> Total = "no hay huecos, todo el mundo pertenece a algún subtipo". Parcial = "puede haber entidades del tipo padre que se queden fuera de cualquier subtipo".

Cuando este esquema se transforma al modelo relacional (Tema 1.2), hay tres estrategias posibles para convertirlo en tablas: una sola tabla con discriminador, una tabla por subtipo, o una tabla por subtipo más una para el supertipo (la más normalizada). Ver `B3 - T1.2 DISENO BBDD`, sección "Del modelo E/R al modelo relacional".

[[Entidad fuerte y entidad débil]]
[[B3 - T1.1 ENTIDAD RELACION]]
[[B3 - T1.2 DISENO BBDD]]
[[B3 - T4.2 UML]] (misma relación en el diagrama de clases)
