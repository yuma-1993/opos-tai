**Model-View-Controller**: patrón que separa una aplicación en tres partes — el **Modelo** (los datos y la lógica de negocio), la **Vista** (lo que ve el usuario) y el **Controlador** (que recibe los eventos de entrada y decide cómo actualizar el modelo). Flujo típico: los eventos de entrada llegan a la Vista, esta se los pasa al Controlador, el Controlador actualiza el Modelo, y el Modelo notifica el cambio a la Vista, que vuelve a consultarlo para refrescarse.

MVC es un caso particular: es el único patrón que se clasifica a la vez como patrón de **arquitectura** y como patrón de **diseño**.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
