El ***magic number*** (o *signature*) de un fichero binario son los **primeros N bytes** del fichero, que identifican de forma fiable qué tipo de fichero es en realidad — independientemente de la extensión que tenga el nombre del archivo.

**Apache Tika** es una librería de Java que detecta y extrae los metadatos de los ficheros precisamente inspeccionando su *magic number*.

**Ejemplos concretos (ampliación, no viene literalmente del tema)**: un PNG siempre empieza por los bytes `89 50 4E 47` (que en ASCII incluye la cadena "PNG"), y un PDF siempre empieza por la cadena literal `%PDF-`. Por eso renombrar un fichero cambiándole la extensión **no cambia su tipo real**: el sistema o la aplicación que lo abre puede inspeccionar esos primeros bytes en vez de fiarse de la extensión.

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
