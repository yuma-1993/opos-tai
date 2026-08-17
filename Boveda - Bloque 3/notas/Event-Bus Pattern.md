Patrón de **arquitectura** en el que productores y consumidores se comunican de forma **asíncrona** a través de un bus intermedio: los productores (*source*) publican en un canal (*channel*), el canal entrega al bus, y los consumidores (*listener*) se suscriben a él.

Dos conceptos derivados de este patrón: el [[ESB (Enterprise Service Bus)]], que mezcla la idea de cola de mensajes (bus) con el filtrado; y [[SOA (arquitectura orientada a servicios)]], el estilo arquitectónico que se apoya en este tipo de comunicación desacoplada.

[[B3 - T4.1 PATRONES DE DISENO Y SOLID]]
