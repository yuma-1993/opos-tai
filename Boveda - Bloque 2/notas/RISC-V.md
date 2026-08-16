RISC-V es una **arquitectura de conjunto de instrucciones** (ISA) de hardware libre, basada en los principios de diseño **[[CISC vs RISC|RISC]]**: instrucciones simples, tamaño fijo, pensadas para ejecutarse rápido y con bajo consumo.

## Qué la hace distinta: libre y sin regalías

A diferencia de la mayoría de los conjuntos de instrucciones, el de RISC-V es **libre y abierto**, y se puede usar **sin pagar regalías** para cualquier propósito. Esto permite que cualquiera diseñe, fabrique y venda chips y software basados en RISC-V, sin depender de una licencia de un tercero.

> [!important] RISC-V vs ARM — la comparación que de verdad importa (conocimiento general)
> Ambas son arquitecturas **RISC**, y ambas se usan desde móviles hasta servidores. La diferencia real está en el **modelo de licencia**: **ARM** es una ISA propietaria — empresas como Qualcomm o Apple pagan a ARM Holdings por licencia para diseñar sus propios chips sobre ella. **RISC-V** es libre: no hay que pagar ni pedir permiso a nadie para implementarla. Es la misma distinción de fondo que "código propietario vs código abierto", aplicada al diseño de procesadores.

RISC-V no es la primera ISA de arquitectura abierta que ha existido, pero es especialmente significativa porque:

- Está diseñada para ser útil en una **amplia gama de dispositivos**, de lo más pequeño a lo más grande.
- Cuenta con un **cuerpo sustancial de software de soporte** (compiladores, herramientas), lo que evita una debilidad habitual de los conjuntos de instrucciones nuevos: quedarse sin ecosistema que los use de verdad.

> [!tip] Con qué relacionarlo si lo memorizas por analogía
> Igual que **[[Arduino]]** aplicó la filosofía de hardware/software libre (licencia GPL) para democratizar el acceso a la electrónica programable, RISC-V aplica esa misma filosofía a nivel de **arquitectura de procesador**. No son lo mismo, pero comparten el espíritu.

## 🔑 Resumen ultra-rápido

- RISC-V = ISA RISC, libre y sin regalías: cualquiera puede fabricar chips sin pagar licencia.
- ARM = también RISC, pero propietaria y con licencia de pago.
- Ventaja añadida frente a otras ISA abiertas: ecosistema de software ya maduro.

---

**Conexiones con otros conceptos TAI:**
- [[CISC vs RISC]] — la filosofía de diseño sobre la que se construye RISC-V.
- [[Pipeline]] — técnica que RISC-V aprovecha igual que cualquier diseño RISC.
- [[B2 - T1 INFORMATICA BASICA]] — arquitectura de procesadores dentro del tema.
