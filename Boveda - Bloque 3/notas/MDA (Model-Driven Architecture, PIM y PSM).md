**MDA** (Model-Driven Architecture) es el acercamiento al diseño de software propuesto por OMG (el mismo organismo detrás de UML): dirigir el desarrollo por modelos en vez de por código. Dentro de MDA se distinguen dos tipos de modelo: el **PIM** (Platform Independent Model), independiente de la tecnología concreta, y el **PSM** (Platform Specific Model), ya particularizado para una plataforma de destino.

*(Ampliación, no viene literal de la fuente):* el flujo típico de MDA consiste en generar, a partir de un único PIM, varios PSM (uno por plataforma destino — Java, .NET, etc.) mediante transformaciones automáticas o semiautomáticas, y de cada PSM derivar el código final. La idea es poder cambiar de plataforma sin tener que rehacer el análisis y el diseño.

[[B3 - T4.2 UML]]
