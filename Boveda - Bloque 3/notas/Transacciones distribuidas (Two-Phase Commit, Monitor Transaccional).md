Una [[ACID (transacciones)|transacción]] puede ser **local** (afecta a un solo SGBD) o **distribuida** (afecta a varios sistemas a la vez). Las transacciones distribuidas se coordinan con el protocolo **two-phase commit** (commit en dos fases): en la fase de *preparación* el coordinador pregunta a todos los participantes si pueden confirmar su parte; solo si todos responden que sí, el coordinador ordena el *commit* definitivo a todos (si alguno falla, ordena rollback a todos). Así se garantiza atomicidad aunque la transacción abarque varios sistemas.

El componente que coordina esto se llama **Monitor Transaccional** — ejemplos: **CICS** y **Tuxedo**. En **JEE**, el monitor transaccional vive dentro del servidor de aplicaciones (JBoss, WebLogic, WebSphere), y la API de Java para hablar con él es **JTA** (Java Transaction API).

[[B3 - T3 SQL]]
