Patrón **creacional** que resuelve el problema de construir un objeto muy complejo, compuesto por muchas partes (por ejemplo, un objeto de negocio con 15 partes, o un DOM construido nodo a nodo). Un **Director** construye el objeto final apoyándose en varios "builders" concretos (por ejemplo, `CabeceraBuilder`, `CuerpoBuilder`, `ColaBuilder`), cada uno responsable de construir su parte, y el director se encarga de ensamblar las partes.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
