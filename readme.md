<h1 align="center" > <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" style="width: 50px; height: auto;">TRABAJO FINAL INTEGRADOR <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" style="width: 50px; height: auto;"></h1>

<h4 align="center" > CONCEPTOS Y PARADIGMAS DE LENGUAJES DE PROGRAMACIÓN </h4>

----

### Requisitos: 
- *Este trabajo final es obligatorio para aquellos que quieren promocionar. Puede realizarse en grupos de hasta 2 personas.*

- *Para promocionar tuvieron que haber explicado oralmente los ejercicios prácticos solicitados durante la cursada, aprobar el examen parcial y aprobar este TP Integrador junto con su exposición oral que son obligatorios.*

### Presentación:
- *El trabajo debe subirse a la plataforma, en el módulo Trabajo Final Integrador y debe exponerse oralmente.*

- *La fecha de entrega del trabajo final es: 30 de noviembre*

- *La fecha de la exposición y defensa: viernes 1ero de diciembre 8 hs.virtual.*

### Objetivo del trabajo: 
- Se va a solicitar profundizar sobre las características de un lenguaje de programación a elección, desde tres perspectivas:
    - *Desde su concepción original*
    - *Desde cómo se presenta en la actualidad en sus últimas versiones* 
    - *Cómo lo infiere y describe la inteligencia artificial IA*
- Indicar como mínimo los siguientes puntos organizados a su criterio:

---- 

## LENGUAJE DE PROGRAMACIÓN ELEGIDO: 

<img src="https://www.python.org/static/img/python-logo.png">

---- 

## Fuentes y bibliografías: 

- [Documentation oficial de Python](https://docs.python.org/3/)

- [Seminario de Python 2022](https://python-unlp.github.io/2022/)

- [Libro "A Byte of Python"](https://python.swaroopch.com/)

- ["Exceptions"](https://book.pythontips.com/en/latest/exceptions.html)

- ["Definiendo Excepciones"](https://ellibrodepython.com/estructuras-control-python)

- ["El Libro de Python"](https://ellibrodepython.com/)

- ["Hektor Profe"](https://docs.hektorprofe.net/)

----

## Parte A: Respecto al análisis del lenguaje de programación elegido tanto original como actualmente. 

### Enunciado:
- *Se debe describir dicho lenguaje según los conocimientos adquiridos en la asignatura. Especifique el manual o las fuentes que ha utilizado.*
---- 

- *Debe indicar las alternativas que existen y la decisión tomada por dicho lenguaje seleccionado tanto cuando fue creado como en su versión actual.*

----

- *Realizar el análisis haciendo un recorrido por lo abordado en la asignatura, como:*
    - *Introducción del lenguaje de programación seleccionado.*
    - *Características - simplicidad y legibilidad, claridad en los bindings, confiabilidad, soporte, abstracción, ortogonalidad, eficiencia.*
    - *Paradigma o paradigmas que respeta.*
    - *Su sintaxis – estructura de un programa, identificadores, operadores, palabras clave y reservadas, comentarios.*
    - *Su semántica - tipo de traducción Interpretación, Compilación o combinación.*
    - *Su semántica operacional*
    - *Variables*
    - *Pilas*
    - *Parámetros*
    - *Tipos de datos*
    - *Excepciones*

----
Para hacer el análisis del lenguaje de programación elegido el cual es Python, iniciaremos con una descripción del mismo, empezando por su historia, características, paradigmas, sintaxis, semántica, tipos de datos, variables, (TERMINAR)

### Historia 
Python fue creado a principios de la década de 1990 por Guido van Rossum en Stichting Mathematisch Centrum en los Países Bajos como sucesor de un idioma llamado ABC. Guido sigue siendo el autor principal de Python, aunque incluye muchas contribuciones de otros.

Su nombre se debe al programa de la BBC "Monty Python's Flying Circus"

Python es un ejemplo de FLOSS (software gratuito y de código abierto). En términos simples, puede distribuir libremente copias de este software, leer su código fuente, realizar cambios y utilizar partes del mismo en nuevos programas gratuitos. FLOSS se basa en el concepto de una comunidad que comparte conocimientos. Esta es una de las razones por las que Python es tan bueno: ha sido creado y mejorado constantemente por una comunidad que solo quiere ver un Python mejor.

### Implementación y sus alternativas

- *CPython:* Es la implementación original, y la más mantenida, de Python y está escrita en C. Las nuevas características del lenguaje normalmente aparecen primero aquí.

- *Jython:* Python implementado en Java. Esta implementación puede utilizarse como lenguaje de scripting para aplicaciones Java, o para crear aplicaciones utilizando las bibliotecas de clases Java. También se utiliza a menudo para crear pruebas para bibliotecas Java.

- *Python for .NET:* Esta implementación, de hecho, usa la implementación CPython, pero es una aplicación .NET gestionada y usa librerías .NET. Ha sido creada por Brian Lloyd.

- *IronPython:* Es una implementación alternativa de Python diseñada específicamente para el entorno .NET. A diferencia de Python.NET, IronPython es una implementación completa de Python que genera código de lenguaje intermedio (IL) y compila directamente el código Python en ensamblados .NET. Este proyecto fue creado por Jim Hugunin, quien también es el creador original de Jython. 

- *PyPy:* Es una implementación de Python escrita completamente en Python. Soporta varias características avanzadas que no se encuentran en otras implementaciones como soporte stackless y un compilador Just in Time. Uno de los objetivos del proyecto es fomentar la experimentación con el propio lenguaje facilitando la modificación del intérprete (ya que está escrito en Python).


### Características
- *Introducción del lenguaje de programación seleccionado.*
    - Python es un lenguaje de programación potente y fácil de aprender. Tiene estructuras de datos de alto nivel eficientes y un simple pero efectivo sistema de programación orientado a objetos. La elegante sintaxis de Python y su tipado dinámico, junto a su naturaleza interpretada lo convierten en un lenguaje ideal para scripting y desarrollo rápido de aplicaciones en muchas áreas, para la mayoría de plataformas. 
    - El intérprete de Python y la extensa librería estándar se encuentran disponibles y se pueden distribuir libremente, al igual que modulos de terceros, programas, herramientas y documentación. 

- *Características*
    - *Comentario de docentes de Cátedra lenguaje Python:*
        - Python es un lenguaje simple y fácil de enseñar.  Es un lenguaje de tipado dinámico pero es fuertemente tipado,  Es un lenguaje ortogonal porque se pueden combinar sus componentes. Su código es legible, confiable por ser fuertemente tipado y proveer manejo de excepcioenes,

    - Simplicidad y legibilidad
        - Es un lenguaje de alto nivel, muy expresivo y legible, con una sintaxis muy clara y fácil de aprender.

    - Bindings
        - Los identificadores se ligan a sus atributos o propiedades en tiempo de ejecución (infiriendo el tipo), por lo tanto posee una ligadura dinámica (binding dinámico), el contenido de una variable puede cambiar durante la ejecución del programa exepto que sea declarada como constante.
        
    - Confiabilidad y seguridad
        - *Cheque de tipos*
            - Python es de tipado dinámico, por lo tanto el chequeo de tipos se realiza en tiempo de ejecución. en caso de la existencia de un error, se encuentra en tiempo de ejecución, lo que hace que sea más tardío encontrarlo.
        
        - *Manejo de excepciones*
            - Python cuenta con un sistema de manejo de excepciones que permite interceptar errores en tiempo de ejecución, tomar medidas correctivas y continuar con la ejecución del programa. (Mas adelante se explicara con mas detalle). 

    - Soporte
        - *"Debería ser accesible para cualquiera que quiera usarlo o instalarlo"*
            
            - Python es FLOSS (software libre y de código abierto) por lo tanto se puede distribuir libremente copias, leer su código fuente, realizar cambios y utilizar partes del mismo en nuevos programas gratuitos. El termino FLOSS se basa en el concepto de una comunidad que comparte conocimientos. Esta es una de las razones por las que Python es tan bueno: ha sido creado y mejorado constantemente por una comunidad que solo quiere ver un Python mejor.
            
        - *"Lo ideal sería que su compilador o intérprete sea de dominio público"*

            - Al ser un lenguaje de código abierto, su intérprete es de dominio público, por lo que cualquiera puede acceder a el.
        
        - *"Deberían existir diferentes medios para poder familiarizarse con el lenguaje"*

            - A lo largo de todo internet se pueden encontrar diferentes medios para poder familiarizarse con el lenguaje, desde la documentacion oficial, cursos gratuitos, cursos pagos, tutoriales, libros, foros, entre otros.            

    - Abstracción
        - Python es un lenguaje de alto nivel (Similar al lenguaje humano), cuenta con multiples funciones y librerias que permiten abstraerse de los detalles de bajo nivel.

    - Ortogonalidad
         - La Ortogonalidad nos permite combinar diferentes elementos de manera independiente y coherente, sin existir restricciones.
         - Por ejemplo en el caso de Python, mediante el operador "+" podemos concatenar enteros con reales o incluso con Strings sin necesidad de convertir las variables. 

        ```python
        print(1 + 2) # 3
        print(1 + 2.0) # 3.0
        print(1 + "2") # 12
        ```
        

    - Eficiencia
        - Tiempo y espacio
            - Python 

- *Paradigma o paradigmas que respeta.*
    Python es un lenguaje de programación multiparadigma, ya que soporta múltiples paradigmas de programación. 
    
    - Programación imperativa
        - Python soporta programación imperativa (listas de instrucciones que le dicen a la computadora qué hacer con la entrada del programa). 
        ```python
        # Programación imperativa
        a = 1 # declaro la variable a = 1
        b = 2 # declaro la variable b = 2
        print(a + b) # devuelve 3
        ```

    - Programación orientada a objetos
        - Python soporta programación orientada a objetos, ya que permite definir clases, crear objetos, herencia, polimorfismo, etc.
        ```python
        class Persona:
            def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad

            def __str__(self):
                return "Nombre: " + self.nombre + ", Edad: " + str(self.edad)

        class Empleado(Persona):
            def __init__(self, nombre, edad, sueldo):
                super().__init__(nombre, edad)
                self.sueldo = sueldo

            def __str__(self):
                return super().__str__() + ", Sueldo: " + str(self.sueldo)

        persona = Persona("Juan", 28)
        empleado = Empleado("Pedro", 30, 50000)

        print(persona) # Nombre: Juan, Edad: 28
        print(empleado) # Nombre: Pedro, Edad: 30, Sueldo: 50000
        ```

        El código anterior muestra un ejemplo de herencia, donde la clase Empleado hereda de la clase Persona, y la clase Empleado sobreescribe el método __str__(Metodo que se ejecuta al hacer un print de un objeto) de la clase Persona.
    
    - Programación funcional
        - Python soporta programación funcional, la idea es descoponer un problema en funciones. La programación funcional prefiere también las funciones puras, es decir, funciones sin side effects (Efectos secundarios o laterales), Las funciones puras no dependen de variables externas o globales. Esto significa que para las mismas entradas, siempre se producen las mismas salidas. sin producir efectos secundarios sobre otros componentes del programa. Python nos ofrece algunas funciones primitivas propias de lenguajes funcionales, como map, filter y reduce.
        
        - *Función map* toma dos entradas:
            - Una lista o iterable que será modificado en una nueva.
            - Una función, que será aplicada a cada uno de los elementos de la lista o iterable anterior.
            Nos devuelve una nueva lista donde todos y cada uno de los elementos de la lista original han sido pasados por la función.

            map(funcion_a_aplicar, entrada_iterable)
            Imaginemos que queremos multiplicar por dos todos los elementos de una lista. La primera forma que se nos podría ocurrir sería la siguiente. 

            ```python
            lista = [1, 2, 3, 4, 5]
            lista_pordos = []
            for l in lista:
                lista_pordos.append(l*2)

            print(lista_pordos)
            # [2, 4, 6, 8, 10]
            ```

            Pero veamos como darle un enfoque funcional. Podemos definir una función por_dos, que pasaremos a map junto con nuestra lista inicial.

            ```python
            lista = [1, 2, 3, 4, 5]

            def por_dos(x):
                return x * 2

            lista_pordos = map(por_dos, lista)

            print(list(lista_pordos))
            # [2, 4, 6, 8, 10]
            ```

            es posible usar funciones lambda para compactar un poco el código, quedando lo siguiente:
                
            ```python
            lista = [1, 2, 3, 4, 5]
            lista_pordos = map(lambda x: 2*x, lista)
            print(list(lista_pordos))
            # [2, 4, 6, 8, 10]
            ```	

        - *La función filter* recibe: 
            - Una función. 
            - Una lista pero el resultado es la lista inicial filtrada. Es decir, se pasa cada elemento de la lista por la función, y sólo si su resultado es True, se incluye en la nueva lista.

            filter(funcion_filtrar, entrada_iterable)
            Al igual que hacíamos antes, usamos las funciones lambda que nos permiten declarar y asignar una función en la misma línea de código.

            ```python
            lista = [7, 4, 16, 3, 8]
            pares = filter(lambda x: x % 2 == 0, lista)
            print(list(pares))
            # [4, 16, 8] 
            ```	

            Nótese que el siguiente código sería equivalente:
            
            ```python
            lista = [7, 4, 16, 3, 8]
            def es_par(x):
                return x % 2 == 0
            pares = filter(es_par, lista)
            print(list(pares))
            # [4, 16, 8]
            ```            

            Una vez más, resaltar que no estamos usando bucles. Simplemente damos la entrada y la función a aplicar a cada elemento, y filter se encarga del resto. Esta es una de las características clave de la programación funcional. Se centra más en el qué hacer que en el cómo hacerlo. Para ello se usan funciones predefinidas como las que estamos viendo, a las que sólo tenemos que pasar las entradas y hacer el trabajo por nosotros.
    
        - *La función reduce*:
            - Podemos usar reduce para reducir todos los elementos de la entrada a un único valor aplicando un determinado criterio. Por ejemplo, podemos sumar todos los elementos de una lista de la siguiente manera.

            ```python
            from functools import reduce
            lista = [1, 2, 3, 4, 5]
            suma = reduce(lambda acc, val: acc + val, lista) # acc es el acumulador, val es el valor
            print(suma) # 15
            ```

            Lo que podría reescribirse usando la función add:

            ```python
            from operator import add
            from functools import reduce
            lista = [1, 2, 3, 4, 5]
            suma = reduce(add, lista)
            print(suma) # 15
            ```

            O también los podemos multiplicar, modificando la función lambda.

            ```python
            from functools import reduce
            lista = [1, 2, 3, 4, 5]
            multiplicacion = reduce(lambda acc, val: acc * val, lista)
            print(multiplicacion) # 120
            ```

            - Es importante notar que la función recibe dos argumentos: el acumulador y cada uno de los valores de la lista.

                - El acumulador es el valor devuelto en la iteración anterior, que va acumulando un resultado hasta que llegamos al final.
                - El valor es cada uno de los elementos de nuestra lista, que en nuestro caso vamos añadiendo al acumulador.
            
            El uso de reduce es especialmente útil cuando tenemos por ejemplo una lista de diccionarios y queremos sumar todos los valores de un campo en concreto. Veamos un ejemplo donde calculamos la edad media de varias personas.
                
            ```python
            from functools import reduce
            personas = [
                {'Nombre': 'Alicia', 'Edad': 22},
                {'Nombre': 'Bob', 'Edad': 29},
                {'Nombre': 'Charlie', 'Edad': 33}
            ]
            suma_edad = reduce(lambda total, p: total + p['Edad'], personas, 0)
            print(suma_edad/len(personas)) # 28.0
            ```

            Nótese que llamamos a reduce con un valor adicional 0, que es el valor inicial del acumulador. Una vez más, hemos resuelto un problema en el que tradicionalmente usaríamos bucles con las primitivas de la programación funcional.
            
- *Su sintaxis*

    - Estructura de un programa

        - Para definir la estructura de un programa en Python, debemos conocer los bloques de codigo más comunes, siendo las funciones, clases y modulos. 

        - Como sabemos Python es un lenguaje interpretado, el intérprete de Python lee y ejecuta el código python directamente, de ser necesario las cleses, modulos y funciones se declaran antes de ser utilizadas. 

        ```python
        # Definicion de una clase
        class Persona:
            def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad

            def __str__(self):
                return "Nombre: " + self.nombre + ", Edad: " + str(self.edad)
        
        # Definicion de una funcion
        def funcion1():
            print("funcion1")
        
        # Programa principal
        persona = Persona("Juan", 28)
        print(persona) # Nombre: Juan, Edad: 28
        funcion1() # funcion1
        ```

        - Si se declaran 2 funciones con el mismo nombre, la ultima declarada sera la que se ejecute.
        ```python	
        def funcion1():
            print("funcion1")
        
        def funcion1():
            print("funcion1 modificada")
        
        funcion1() # funcion1 modificada
        ```
        
        - Los import se realizan al principio del archivo, y se pueden importar modulos, clases o funciones. 

        ```python
        import math # importo el modulo math
        print(math.pi) # 3.141592653589793
        ```
        
    - Identificadores

        - Un identificador de Python es un nombre utilizado para identificar una variable, función, clase, módulo u otro objeto. 
        
        - Un identificador comienza con una letra de la A a la Z o de la a a la z o un guión bajo (_) seguido de cero o más letras, guiones bajos y dígitos (0 a 9).

        - Python no permite caracteres de puntuación como @, $ y % dentro de los identificadores.

        - Python es un lenguaje de programación que distingue entre mayúsculas y minúsculas (case-sensitive), Por lo tanto, Manpower y manpower son dos identificadores diferentes en Python.

        - Convenciones de nomenclatura para identificadores de Python:

            - Los nombres de las clases de Python comienzan con una letra mayúscula. Todos los demás identificadores comienzan con una letra minúscula.

            - Comenzar un identificador con un único guión bajo indica que el identificador es privado.

            - Comenzar un identificador con dos guiones bajos indica un identificador fuertemente privado.

            - Si el identificador también termina con dos guiones bajos al final, el identificador es un nombre especial definido por el idioma.(dunders)

    - Operadores 
        - Los siguientes tokens son operadores:

            | + | - | * | ** | / | // | % |
            | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
            | @ | << | >> | & | \| | ^ | ~ |
            | < | > | <= | >= | == | != | := |
        
    - Palabras claves
        - Palabras claves reservadas: Los siguientes identificadores se utilizan como palabras reservadas, o palabras clave del idioma, y no pueden utilizarse como identificadores ordinarios. Deben escribirse exactamente como están escritas aquí:

            | False | await | else | import | pass |
            | :---: | :---: | :---: | :---: | :---: |
            | None | break | except | in | raise |
            | True | class | finally | is | return |
            | and | continue | for | lambda | try |
            | as | def | from | nonlocal | while |
            | assert | del | global | not | with |
            | async | elif | if | or | yield |

        - Palabras claves blandas: Algunos identificadores sólo se reservan en contextos específicos. Estos se conocen como palabras clave blandas.

            | match | case | type | _ |
            | :---: | :---: | :---: | :---: |

    - Comentarios
        - Los comentarios comienzan con el carácter # y se extienden hasta el final de la línea física. Un comentario puede aparecer al principio de una línea o después de un espacio en blanco o código, pero no dentro de una cadena literal. Los comentarios son ignorados por el compilador de Python.
        ```python
        # Esto es un comentario
        print("Hello, World!") # Esto es un comentario en línea
        ```

        - Los comentarios multilínea se usan para documentar cadenas de documentación de módulos, funciones, clases y métodos. El intérprete de Python ignora los comentarios multilínea.
        ```python	
        """Este es un comentario multilínea.
        Son usados para documentar cadenas de documentación de módulos, funciones, clases y métodos.
        """
        print("Hello, World!")
        ```
 
- *Su semántica*
    - Tipo de traducción Interpretación, Compilación o combinación.
        - Python es un lenguaje interpretado, lo que significa que no necesita ser compilado antes de que se ejecute. El intérprete de Python lee y ejecuta el código python directamente. Esto hace que el desarrollo sea muy rápido y cómodo. El intérprete de Python está disponible para la mayoría de las plataformas, incluidas Linux, Mac OS X y Windows.

        - El proceso que realiza cuando se ejecuta sobre cada una de las sentencias del programa es el siguiente:

            ![Alt text](/screenshots/image.png)

        - Sólo pasa por ciertas instrucciones no por todas, según sea la ejecución. 

        - Por cada posible acción hay un subprograma en lenguaje de máquina que ejecuta esa acción.
        
        - La interpretación se realiza llamando a estos subprogramas en la secuencia adecuada hasta generar el resultado de la ejecucon.

            ![Alt text](/screenshots/image2.png)


- *Su semántica operacional*

- *Variables*
    - Nombre: El nombre de una variable (identificador) debe cumplir ciertas condiciones:
         - Puede contener solamente letras (mayúsculas y minúsculas), números, y guión bajo; todas las letras deben pertenecer al código de caracteres ASCII básico, y no contener caracteres extendidos.
         - El primer carácter no puede ser un número.
         - Las palabras reservadas del lenguaje no pueden usarse como identificadores.
    - Alcance: En Python, el alcance de una variable se refiere a la región del código en la que la variable es válida y puede ser utilizada. Hay varios tipos de alcance en Python:
         - Global: Son aquellas definidas en el cuerpo principal del programa fuera de cualquier función. Son accesibles desde cualquier punto del programa, incluso desde dentro de funciones. También se puede acceder a las variables globales de otros programas o módulos importados.
         - Local: Son aquellas definidas dentro de una función. Solamente son accesibles desde la propia función y dejan de existir cuando esta termina su ejecución.
         - NonLocal: Son un mecanismo que nos permite hacer acceso de escritura de una variable local desde dentro de otra  función definida en el mismo ámbito, es decir, desde una función anidada.
         - Module: Es un fichero .py que alberga un conjunto de funciones, variables o clases y que puede ser usado por otros módulos. Nos permiten reutilizar código y organizarlo mejor en namespaces.
    - Tiempo de Vida: Las variables en python duran el tiempo que siga ejecutandose el modulo que lo contiene.
    - L-valor: 
        En python tiene dos tipos de l-valor: 
            - Automatica: 
            - Dinamica:
    - R-valor: La declaración e inicialización se hace en la misma linea, por lo tanto el r-valor es el valor que se le asigna a la variable.

- *Pilas*

- *Parámetros*
    
    - Python Envía objetos que pueden ser “inmutables” o “mutables” (objeto que pueden ser o no modificados). Si es inmutable actuará  como por valor y, si es mutable, ejemplo: listas, no se hace una copia, sino que se trabaja sobre él.

    Dependiendo del tipo de dato que enviemos a la función, podemos diferenciar dos comportamientos:

    - Paso por valor: Se crea una copia local de la variable dentro de la función.

    - Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro de la función le afectarán también fuera.
    
    Tradicionalmente:

    Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
    Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...
    Ejemplo de paso por valor
    Como ya sabemos los números se pasan por valor y crean una copia dentro de la función, por eso no les afecta externamente lo que hagamos con ellos:

    ```python
    def doblar_valor(numero):
        numero *= 2

    n = 10
    doblar_valor(n)
    print(n) #10
    ```

    Ejemplo de paso por referencia
    Sin embargo las listas u otras colecciones, al ser tipos compuestos se pasan por referencia, y si las modificamos dentro de la función estaremos modificándolas también fuera:

    ```python
    def doblar_valores(numeros):
        for i,n in enumerate(numeros):
            numeros[i] *= 2

    ns = [10,50,100]
    doblar_valores(ns)
    print(ns)# [20, 100, 200]
    ```

    Para modificar los tipos simples podemos devolverlos modificados y reasignarlos:

    ```python
    def doblar_valor(numero):
        return numero * 2

    n = 10
    n = doblar_valor(n)
    print(n)#20
    ```

    Y en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia:

    ```python
    def doblar_valores(numeros):
        for i,n in enumerate(numeros):
            numeros[i] *= 2

    ns = [10,50,100]
    doblar_valores(ns[:])  #Una copia superficial de la lista ns con [:]
    print(ns)#[10, 50, 100]
    ```

- *Tipos de datos*
    - Podemos definir a un tipo de dato como un conjunto de valores  y  un conjunto de operaciones que se pueden utilizar para manipularlos. 

    - Tipo de datos predefinidos (built-in/primitivos)
        - Normalmente reflejan  el  comportamiento  del  hardware  subyacente. 

        - Las ventajas de los tipos predefinidos son:
            - Invisibilidad de la representación
            - Verificación estática
            - Desambiaguar operadores
            - Control de precisión

        - Python cuenta con los siguientes tipos primitivos: 
            - Numeric(numerico) - int, float, complex
            - String(cadena) - str
            - Boolean - bool            
            - Binary(binario) - bytes, bytearray, memoryview            
            - None - NoneType 

    - Tipo de datos definidos por el programador (user-defined)
        - Permiten al  programador especificar agrupaciones de objetos de datos elementales ( tipos  predefinidos ).  

        - Separan la especificación de la implementación. Se definen  los tipos que el problema necesita. 
            - Definir nuevos tipos e instanciarlos
            - Chequeo de consistencia

        - Las ventajas de los tipos definidos por el programador son:
            - Legibilidad : elección apropiada de nuevos Nombres. 
            - Estructura jerárquica de las definiciones de tipos: proceso de refinamiento (creacion de clases). 
            - Modificabilidad : Solo se cambia en la definición. 
            - Factorización: Se usa la cantidad de veces necesarias. 
            - La instanciación de los objetos en un tipo dado implica una descripción abstracta de sus valores. Los detalles de la implementación solo quedan en la definición del tipo. 

        - Python cuenta con los siguientes tipos de datos definidos por el programador:
            - Sequence(secuencia) - list, tuple, range
            - Mapping(Mapeo) - dict
            - Set(conjuntos) - set, frozenset
            - Objets(objetos) - class

- *Excepciones*
    - En terminología básica conocemos la estructura try/except. El código que puede causar una excepción se coloca en el bloque try y el manejo de la excepción se implementa en el bloque except. El código del bloque except solo se ejecutará si el bloque try se encuentra con una excepción.
        ```python
        try:
            file = open('test.txt', 'r')
            print(file.read())
        except IOError as exception:
            print('Ocurrio un IOError. {}'.format(exception.args[-1]))
        ```

    - Manejo de múltiples excepciones:
        - El primero implica poner todas las excepciones que probablemente ocurran en una tupla.
        ```python
        try:
            file = open('test.txt', 'r')
        except (IOError, EOFError) as exception:
            print("Ocurrio un error. {}".format(exception.args[-1]))
        ```
        
        - El segundo método consiste en manejar excepciones individuales en bloques except separados. Podemos tener tantos bloques except como queramos. De esta manera, si la excepción no es manejada por el primer bloque except, entonces puede ser manejada por un bloque siguiente, o ninguno en absoluto.
        ```python
        try:
            file = open('test.txt', 'r')
        except EOFError as exception:
            print("Ocurrio un error EOFError.")
        except IOError as exception:
            print("Ocurrio un error.")
        ```
        
        - Ahora el último método implica atrapar todas las excepciones. Esto puede resultar útil cuando no tiene idea de las excepciones que puede generar su programa. Si solo busca capturar todas las excepciones, pero en realidad no le importa cuáles son.
        ```python
        try:
            file = open('test.txt', 'r')
        except Exception as exception:
            print("Se atrapo un excepción.")
        ``` 
    
    -  Cláusula Finally
        - En este ejemplo también usaremos una tercera cláusula, que es la cláusula finally. El código incluido en la cláusula finally se ejecutará independientemente de que se produzca o no una excepción. Podría usarse para realizar una limpieza después de un script.    
        ```python
        try:
            file = open('test.txt', 'r')
        except IOError as exception:
            print('Ocurrio un error IOError. {}'.format(exception.args[-1]))
        finally:
            print("¡Esto se imprimiría independientemente de que ocurriera o no una excepción!")
        ```
        
    - Cláusula Try/Else 
        - Muchas veces es posible que deseemos que se ejecute algún código si no se produce ninguna excepción. Esto se puede lograr fácilmente mediante el uso de una cláusula else.
        ```python
        try:
            print('¡Estoy seguro de que no ocurrirá ninguna excepción!')
        except Exception:
            print('Hubo una excepción.')
        else:
            print('Esto sólo se ejecutará si no se produce ninguna excepción. Y un error aquí NO se detectaría.')
        finally:
            print('¡Esto se imprimiría independientemente de que ocurriera o no una excepción!')
        ```
        - La cláusula else sólo se ejecutará si no se produce ninguna excepción y se ejecutará antes de la cláusula finally.

    - Algunos tipos de Excepciones del lenguaje
        - Definidas por el lenguaje:    
        <img src="https://www.maestrosdelweb.com/images/2011/11/chule_exceptions.png">
        
        - Definidas por el usuario:
            - A pesar de que Python define un conjunto de excepciones por defecto, podrían no ser suficientes para nuestro programa. En ese caso, deberíamos definir nuestra propias excepciones.

            - Si queremos crear una excepción, solamente tenemos que crear una clase que herede de la clase Exception. Es tan sencillo como el siguiente ejemplo.
            ```python
            # Creamos una excepción personalizada
            class MiExcepcionPersonalizada(Exception):
                pass
            ```
            - Y ya podríamos lanzarla con raise cuando quisiéramos.
             ```python
            raise MiExcepcionPersonalizada()
            ```
            - También se pueden pasar parámetros de entrada al lanzarla. Esto es muy útil para dar información adicional a la excepción. En el siguiente ejemplo se pasan dos parámetros. Para ello tenemos que modificar la función __init__() de la siguiente manera.
            ```python
            # Creamos nuestra propia excepción heredando
            # de la clase Exception
            class MiExcepcionPersonalizada(Exception):
                def __init__(self, parametro1, parametro2):
                    self.parametro1 = parametro1
                    self.parametro2 = parametro2
            ```
            - Y una vez hemos creado nuestra excepción, podemos lanzarla con raise como ya hemos visto. También es posible acceder a los parámetros pasados como argumentos al lanzar la excepción.
            ```python
            # Lanzamos con raise la excepción que hemos creado
            try:
                raise MiExcepcionPersonalizada("ValorPar1", "ValorPar2")
            except MiExcepcionPersonalizada as ex:
                p1, p2 = ex.args
                print(type(ex))
                print("parametro1 =", p1)
                print("parametro2 =", p2)
            
            #<class '__main__.MiExcepcionPersonalizada'>
            #parametro1 = ValorPar1
            #parametro2 = ValorPar2
            ```

---- 


## Parte B: Respecto al análisis a realizar con IA. 
- *Utilizar dos sistemas de Inteligencia artificial como ChatGPT, GoogleBard, Perplexity, etc y compare los resultados que dan estos motores respecto a lo indicado por Ud. sobre el lenguaje de programación que eligió. Es importante realizar este análisis comparativo entre lo inferido por la IA respecto a lo descripto en la bibliografía tanto de Conceptos de lenguajes como del manual mismo del lenguaje.*

### Historia
|Tema |ChatGPT|GoogleBard| Perplexity|
|:---:|:---:|:---:|:---:|
|Historia| Python fue creado por Guido van Rossum y lanzado por primera vez en 1991. Van Rossum buscaba un lenguaje de programación de fácil lectura y con una sintaxis clara. Python ha evolucionado a lo largo de los años, siendo Python 2 y Python 3 las principales versiones. Es conocido por su versatilidad, legibilidad y amplio uso en áreas como desarrollo web, inteligencia artificial y análisis de datos.| Python fue creado por Guido van Rossum en 1989 como un lenguaje de programación de alto nivel, interpretado y de propósito general. El objetivo de van Rossum era crear un lenguaje que fuera fácil de aprender y usar, y que fuera lo suficientemente potente para una amplia gama de aplicaciones.La primera versión de Python, 0.9.0, se lanzó en 1991. La versión 1.0 se lanzó en 1994, y la versión 2.0 se lanzó en 2000. La versión 3.0, que introdujo una serie de cambios importantes en la sintaxis y la semántica de Python, se lanzó en 2008.| Python ha ganado una gran popularidad en los últimos años, convirtiéndose en uno de los lenguajes de programación más utilizados en el mundo. Se utiliza para una amplia gama de aplicaciones, incluyendo desarrollo web, ciencia de datos, machine learning, inteligencia artificial, automatización y videojuegos.La historia del lenguaje de programación Python se remonta a finales de los 80 y principios de los 90. Fue desarrollado por Guido van Rossum, quien comenzó su implementación en diciembre de 1989 en CWI en los Países Bajos. Python fue concebido como un sucesor de ABC capaz de manejo de excepciones e interacción con el sistema operativo Amoeba.Desde entonces, ha experimentado varias actualizaciones y se ha convertido en uno de los lenguajes de programación más populares del mundo.|
|Introdución|Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Destaca por su sintaxis clara y legible, fomentando la facilidad de uso y la productividad. Es multiplataforma, soporta programación orientada a objetos, funcional y estructurada. Ampliamente utilizado en desarrollo web, automatización, ciencia de datos, inteligencia artificial y más. Su lema es "Leeability counts" (La legibilidad cuenta), resaltando su enfoque en la legibilidad del código.|Python es un lenguaje de programación de alto nivel, interpretado y de propósito general, fácil de aprender y usar. Se puede utilizar para una amplia gama de aplicaciones, incluyendo desarrollo web, ciencia de datos, machine learning e inteligencia artificial.|Python es un lenguaje de programación de propósito general, ampliamente utilizado para desarrollar aplicaciones de diversos tipos. Es un lenguaje interpretado, lo que significa que el código no se compila a lenguaje máquina y que el tipo de las variables se resuelve en tiempo de ejecución. Python es compatible con diferentes sistemas operativos, como Linux, Windows y Mac OS, y su sintaxis es sencilla y legible, lo que lo hace accesible tanto para principiantes como para desarrolladores experimentados|
|Caracteristicas| | | | 
|simplicidad y legibilidad|La simplicidad y legibilidad son pilares fundamentales en Python. El diseño del lenguaje se centra en facilitar la escritura y comprensión del código. La sintaxis clara y la estructura intuitiva permiten a los programadores expresar ideas de manera concisa. El principio clave es que un código legible es preferible a uno ingenioso, fomentando un enfoque práctico y accesible que beneficia tanto a principiantes como a desarrolladores experimentados.|Python es un lenguaje de programación de alto nivel, interpretado y de propósito general que se caracteriza por su simplicidad y legibilidad. La sintaxis de Python es limpia y concisa, con reglas claras y consistentes. Esto hace que el código sea fácil de entender y leer, incluso para aquellos que no están familiarizados con el lenguaje.|La simplicidad y legibilidad son principios fundamentales en el diseño de Python. Según "The Zen of Python", un conjunto de principios que guían el diseño del lenguaje, se enfatiza que "la legibilidad cuenta" y que "lo simple es mejor que lo complejo" Estos principios se reflejan en la sintaxis clara y en la facilidad para escribir y comprender el código en Python, lo que lo hace accesible tanto para principiantes como para desarrolladores experimentados.|
|bindigs|En Python, la ligadura de un identificador con sus atributos se refiere a la asociación de un nombre (identificador) con las propiedades o características específicas de un objeto. Los atributos son accesibles mediante la notación de punto, permitiendo a los programadores acceder y manipular los datos asociados con ese identificador. Esta ligadura dinámica facilita la creación y manipulación de objetos al vincular nombres con sus respectivas propiedades, brindando flexibilidad y claridad en la estructura del código.|En Python, la ligadura de identificador con sus atributos se realiza mediante el operador .. Por ejemplo, si x es una instancia de la clase Persona, podemos acceder al atributo nombre de x mediante x.nombre.Esta característica permite acceder a los datos y métodos de un objeto de manera sencilla.|La ligadura de un identificador con sus atributos se refiere a la asociación entre una entidad, como una variable, y alguno de sus atributos, como su tipo o valor. En el contexto de Python, la ligadura ocurre cuando se asigna un valor a una variable, creando una asociación entre el nombre de la variable y el valor que representa|
|Confiabilidad y seguridad|La confiabilidad y seguridad en Python se derivan de su diseño centrado en la legibilidad y simplicidad. La gestión automática de la memoria, el manejo de excepciones y el tipado dinámico contribuyen a la confiabilidad, facilitando la detección temprana de errores. Además, el énfasis en la seguridad se refleja en la ejecución segura del código y en prácticas como el sandboxing. La amplia adopción y la comunidad activa respaldan la identificación y corrección de posibles vulnerabilidades, consolidando a Python como una opción confiable y segura para una variedad de aplicaciones.|Python es un lenguaje de programación fiable y seguro, pero es importante tener en cuenta la confiabilidad y la seguridad al desarrollar aplicaciones en Python. Esto se puede hacer siguiendo buenas prácticas de codificación, utilizando bibliotecas y herramientas seguras, y manteniendo el código actualizado con las últimas correcciones de seguridad.|La confiabilidad y seguridad de Python se derivan en parte de su sintaxis clara y legible, lo que facilita la detección de errores y la comprensión del código. Además, Python cuenta con un sistema de gestión de memoria automático, lo que significa que los desarrolladores no tienen que preocuparse por la asignación y liberación de memoria, reduciendo la probabilidad de errores de memoria. Asimismo, la amplia adopción de Python y su gran comunidad de usuarios contribuyen a la identificación y corrección proactiva de vulnerabilidades, lo que aumenta su confiabilidad y seguridad|
|Soporte|El soporte en Python es sólido y diverso, respaldado por una comunidad global comprometida. La documentación extensa, tutoriales y foros facilitan la resolución de problemas. Python Software Foundation gestiona actualizaciones y desarrollo, asegurando la estabilidad del lenguaje. Además, la presencia activa en redes sociales y plataformas de desarrollo colaborativo como GitHub permite una interacción rápida y efectiva entre usuarios, promoviendo un robusto ecosistema de apoyo.|Soporte de Python es la asistencia técnica y los recursos que se proporcionan a los usuarios de Python para que puedan utilizarlo de manera eficaz. El soporte de Python está disponible a través de una variedad de canales, incluidos la documentación oficial, los foros de la comunidad, los chats en línea y el soporte comercial.|El soporte de Python se destaca por su gran comunidad de usuarios, que contribuye al desarrollo de bibliotecas, frameworks y herramientas, y a la disponibilidad de recursos de aprendizaje, foros de discusión y documentación. Esta comunidad activa brinda soporte técnico, comparte buenas prácticas y colabora en la identificación y solución de problemas, lo que hace que Python sea una opción confiable para el desarrollo de software en diversos ámbitos|
|Abstracción|La abstracción en Python se refiere a la capacidad de simplificar y ocultar detalles complejos, permitiendo a los programadores centrarse en conceptos de alto nivel. La orientación a objetos en Python facilita la creación de abstracciones mediante clases y objetos, encapsulando datos y comportamientos. Esta característica, junto con la sintaxis clara del lenguaje, fomenta la construcción de código legible y modular, donde los detalles de implementación se pueden abstractar, promoviendo así una programación más efectiva y fácil de mantener.|La abstracción en Python se implementa utilizando clases abstractas. Las clases abstractas no pueden ser instanciadas directamente, sino que se usan como base para otras clases.Las clases abstractas se definen utilizando el módulo abc (Abstract Base Class). Las clases que heredan de una clase abstracta deben implementar los métodos abstractos definidos en la clase base.La abstracción en Python permite a los programadores crear sistemas más modulares y reusables.|La abstracción en Python se refiere a la capacidad de ocultar la complejidad intrínseca de una aplicación y centrarse en cómo puede ser utilizada, lo que se conoce como interfaz. En Python, la abstracción se logra a través de la creación de clases y la definición de métodos que ocultan los detalles de implementación subyacentes, permitiendo a los usuarios interactuar con la aplicación sin necesidad de conocer su complejidad interna | 
|Ortogonalidad|En Python, la ortogonalidad se refiere a la consistencia y coherencia de las características del lenguaje, donde conceptos diferentes no interactúan inesperadamente. La ortogonalidad en Python se destaca por la consistencia en la aplicación de reglas y principios, como el uso uniforme de la sintaxis y la capacidad de combinar construcciones de manera predecible. Esto simplifica el aprendizaje y la comprensión del lenguaje, ya que las reglas se aplican de manera uniforme, lo que permite a los programadores combinar y utilizar conceptos de manera predecible y eficiente.|En Python, la ortogonalidad se refiere a dos vectores que tienen un producto interno nulo. En otras palabras, dos vectores son ortogonales si no tienen ninguna componente en común.La ortogonalidad se puede verificar utilizando la función numpy.dot(). Si el resultado de la función es 0, entonces los vectores son ortogonales.La ortogonalidad se utiliza en una variedad de aplicaciones en Python, incluidas la descomposición de matrices, la resolución de sistemas de ecuaciones lineales y la compresión de datos.|La ortogonalidad en Python se refiere a la independencia entre distintas características o funcionalidades del lenguaje, de modo que un cambio en una parte del sistema no afecte a otras partes. En el contexto de la programación, la ortogonalidad implica que las diferentes características del lenguaje pueden combinarse de manera predecible y coherente, lo que facilita la escritura de código claro y conciso. Python se esfuerza por mantener la ortogonalidad, lo que contribuye a su legibilidad y facilidad de uso |
|Eficiencia|La eficiencia en Python se logra mediante la ejecución rápida de tareas y la gestión eficaz de recursos. Aunque Python puede ser menos eficiente en ciertos casos comparado con lenguajes de bajo nivel, su enfoque en la legibilidad y productividad compensa en muchos escenarios. La integración de extensiones en C, el uso de bibliotecas optimizadas y la atención a la optimización en implementaciones específicas, como PyPy, contribuyen a mejorar la eficiencia. Python ofrece un equilibrio pragmático entre rendimiento y facilidad de desarrollo, siendo una elección eficaz para una amplia gama de aplicaciones.| La eficiencia en Python se refiere a la rapidez y el uso mínimo de recursos con la que un programa se ejecuta. Se puede mejorar utilizando estructuras de datos adecuadas, optimizando el código y utilizando bibliotecas eficientes.|La eficiencia en Python se deriva de su sintaxis clara y legible, que facilita el desarrollo de código conciso y la detección temprana de errores. Además, Python cuenta con una amplia gama de bibliotecas y frameworks que permiten a los desarrolladores realizar tareas de manera eficiente, como el procesamiento de datos, la creación de interfaces gráficas y el desarrollo web| 
| | | | |
|Paradigma o paradigmas que respeta |Python es políglota en términos de paradigmas de programación, ya que soporta programación imperativa, orientada a objetos y funcional. Permite a los desarrolladores adoptar diferentes estilos de programación según las necesidades del proyecto. La orientación a objetos es prominente con el uso de clases y objetos, mientras que características como funciones de orden superior y lambdas respaldan la programación funcional. La flexibilidad de Python para adaptarse a múltiples paradigmas facilita el desarrollo de código modular y expresivo, ofreciendo a los programadores diversas herramientas para abordar problemas de manera efectiva.|Python es un lenguaje de programación multiparadigma, lo que significa que soporta múltiples paradigmas de programación. Los principales paradigmas que respeta Python son el paradigma imperativo, el paradigma funcional y el paradigma orientado a objetos.|Python es un lenguaje de programación de alto nivel que respeta varios paradigmas, como el imperativo, orientado a objetos (POO) y funcional Esto significa que Python admite diferentes enfoques para el desarrollo de software, lo que permite a los desarrolladores elegir el paradigma más adecuado según las necesidades de cada proyecto.|
| | | | |
|Su sintaxis | | | |
|Estructura de un programa |La estructura de un programa en Python sigue un formato claro y legible. Comienza con importaciones para incluir módulos necesarios, seguido por definiciones de funciones o clases. El código principal se ubica en un bloque principal o en la ejecución condicional bajo la cláusula if __name__ == "__main__":, permitiendo la reutilización de código en módulos. La indentación determina la estructura, reemplazando las llaves o palabras clave utilizadas en otros lenguajes. Esta estructura facilita la comprensión y mantenimiento del código, enfocándose en la legibilidad y facilitando la colaboración entre desarrolladores. |De manera corta y precisa, en un único párrafo, responde: Estructura de un programa |La estructura básica de un programa en Python incluye elementos como comentarios, importaciones, variables y funciones. El código de un programa en Python está dividido en líneas, y cada línea es una secuencia de caracteres. Python hace distinción entre mayúsculas y minúsculas, y los identificadores se utilizan para nombrar diferentes objetos de Python, como variables, funciones y clases. Además, se pueden incluir comentarios en el código para documentar el programa, y existen diferentes tipos de comentarios, como los que abarcan hasta el fin de línea o los que se extienden por varias líneas |
|Identificadores|En Python, los identificadores son nombres utilizados para referenciar variables, funciones, clases u otros objetos. Siguen reglas específicas: deben comenzar con una letra o guion bajo, seguido de letras, números o más guiones bajos. Python distingue entre mayúsculas y minúsculas en los identificadores. Es importante elegir nombres descriptivos y seguir convenciones de estilo, como PEP 8, para mejorar la legibilidad del código. Los identificadores no pueden ser palabras clave reservadas y se recomienda evitar sombrear funciones o variables integradas para evitar confusiones.|Los identificadores en Python son nombres que se utilizan para referirse a variables, funciones, clases, módulos u otros objetos. Los identificadores deben comenzar con una letra o un guión bajo, seguido de cero o más letras, números o guiones bajos.Los identificadores en Python distinguen entre mayúsculas y minúsculas, por lo que "nota" es diferente de "Nota".Es importante elegir buenos identificadores que sean descriptivos y fáciles de recordar. |En Python, un identificador es el nombre utilizado para identificar una variable, función, clase, módulo u otro objeto. Los identificadores en Python deben comenzar con una letra o un guión bajo, seguido de cero o más letras, guiones bajos y números. Python distingue entre mayúsculas y minúsculas, lo que significa que los identificadores con diferentes mayúsculas y minúsculas se consideran diferentes. Además, Python no permite signos de puntuación como @, $ y %, excepto el guión bajo (_)|
|Operadores|Python ofrece una variedad de operadores para realizar acciones en variables y valores. Incluyen operadores aritméticos como +, -, *, / para operaciones matemáticas, operadores de comparación como ==, !=, <, > para comparar valores, operadores lógicos como and, or, not para evaluar expresiones booleanas, y operadores de asignación como = para asignar valores a variables. Además, hay operadores de pertenencia (in, not in) y de identidad (is, is not) para verificar la relación entre objetos y variables. La comprensión de estos operadores es esencial para manipular datos y controlar el flujo de ejecución en programas Python.|Los operadores en Python son símbolos que se utilizan para realizar operaciones matemáticas, lógicas, de comparación, de asignación, de identidad y de pertenencia. Los operadores tienen una precedencia específica, que determina el orden en que se evalúan las operaciones.Es importante conocer los operadores en Python para poder escribir código eficaz y eficiente. |Los operadores en Python son símbolos reservados que se utilizan para realizar operaciones sobre uno o más elementos, llamados operandos. Los tipos de operadores en Python incluyen operadores aritméticos (como suma, resta, multiplicación, división), operadores de comparación (para comparar valores), operadores lógicos (and, or, not), operadores de asignación, operadores de pertenencia (in, not in) y operadores de identidad (is, is not) |
|Palabras claves|Las palabras clave en Python son términos reservados que tienen significados específicos en el lenguaje y no pueden ser utilizados como identificadores para variables, funciones u otros elementos del código. Algunas de las palabras clave incluyen if, else, while, for, def, class, return, True, False y None. Estas palabras clave definen la estructura y la lógica del código, y su uso sigue reglas sintácticas que contribuyen a la coherencia y legibilidad del código Python.|Las palabras clave en Python son palabras que tienen un significado especial en el lenguaje. Se utilizan para controlar el flujo del programa, declarar variables, crear funciones y clases, y realizar otras tareas.Las palabras clave en Python distinguen entre mayúsculas y minúsculas, por lo que "while" es diferente de "While".Es importante conocer las palabras clave en Python para poder escribir código válido y eficaz.|Las palabras clave o reservadas en Python son aquellas que el lenguaje ha reservado para realizar ciertas tareas y no pueden ser utilizadas como nombres de variables, funciones u otros identificadores. Algunas de estas palabras clave incluyen "False", "None", "True", "and", "as", "assert", "break", "class", "def", "del", "elif", "else", "except", "finally", "for", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while" y "with" |
|Comentarios|En Python, los comentarios son líneas precedidas por el símbolo '#', y se utilizan para añadir explicaciones o notas al código sin afectar su ejecución. Los comentarios son útiles para documentar el propósito de ciertas líneas de código, facilitar la comprensión del mismo y colaborar con otros programadores. Pueden estar al inicio de una línea o después de código existente. El intérprete ignora los comentarios durante la ejecución, por lo que no afectan el funcionamiento del programa. El uso adecuado de comentarios mejora la legibilidad y mantenibilidad del código en Python.|Los comentarios en Python son líneas de texto que no se ejecutan. Se utilizan para documentar el código, explicar su funcionamiento y facilitar su comprensión.Los comentarios en Python comienzan con el carácter numeral (#) y se extienden hasta el final de la línea.Es importante documentar el código con comentarios claros y concisos para facilitar su comprensión y mantenimiento.|Los comentarios en Python se utilizan para explicar el código y son ignorados durante la ejecución. Se pueden crear comentarios precediéndolos con el símbolo de numeral (#) en una línea, o utilizando triple comilla doble (""") al principio y al final del comentario para comentarios multilínea |
| | | | |
|Su semántica| | | |
|Tipo de traducción Interpretación, Compilación o combinación.|Python utiliza un enfoque de interpretación para la traducción y ejecución del código fuente. Durante la ejecución, el intérprete traduce el código fuente a bytecode, que es un código de bajo nivel específico de Python. Este bytecode se ejecuta en la máquina virtual de Python (PVM), que es parte del intérprete, permitiendo la portabilidad del código entre diferentes plataformas. Aunque este enfoque puede ser ligeramente más lento que la compilación estática en algunos casos, proporciona flexibilidad y portabilidad, ya que el mismo código fuente puede ejecutarse en diferentes entornos sin necesidad de recompilación. |Python es un lenguaje interpretado, lo que significa que el código fuente se traduce a código máquina línea por línea a medida que se ejecuta. Esto hace que Python sea más lento que los lenguajes compilados, pero también más flexible y fácil de depurar.|La traducción e interpretación en Python se refiere a la capacidad del lenguaje para procesar y ejecutar código de manera dinámica, sin necesidad de compilarlo previamente. El intérprete de Python lee el código línea por línea y lo ejecuta en tiempo real, lo que permite una mayor flexibilidad y rapidez en el desarrollo de aplicaciones. Además, Python cuenta con bibliotecas y herramientas que permiten la traducción automática de texto, lo que facilita la creación de aplicaciones multilingües|
| | | | |
|Su semántica operacional| | | |
|Variables|En la semántica operacional de Python, las variables son símbolos que se asocian con valores y se utilizan para almacenar información. Durante la ejecución del programa, el intérprete asigna y gestiona estas variables de acuerdo con las operaciones y expresiones presentes en el código. Las variables en Python son dinámicamente tipadas, lo que significa que su tipo puede cambiar durante la ejecución del programa. La semántica operacional de Python define cómo se evalúan y actualizan las variables en respuesta a las operaciones y expresiones, contribuyendo a la ejecución efectiva y coherente del código.|En la semántica operacional de Python, las variables son referencias a valores. Se definen mediante la asignación de un valor a una variable. El valor de una variable se puede acceder mediante su nombre.El alcance de una variable determina dónde se puede acceder a ella. Las variables globales tienen un alcance global, lo que significa que se pueden acceder a ellas desde cualquier parte del programa. Las variables locales tienen un alcance local, lo que significa que solo se pueden acceder a ellas dentro del bloque de código en el que se declaran.La semántica operacional de las variables en Python es simple y eficiente. Esto hace que Python sea un lenguaje fácil de aprender y usar. |La semántica operacional de las variables en Python se refiere a cómo se manejan y evalúan las variables en el contexto de la ejecución del programa. Esto incluye aspectos como la asignación de valores a las variables, la manipulación de su contenido y el alcance de las mismas. La semántica operacional define las reglas y comportamientos que rigen el uso de las variables en el lenguaje, lo que es fundamental para comprender su funcionamiento interno y su interacción con otras partes del programa |
|Pilas|La pila de ejecución en Python es un componente crucial de su modelo de ejecución. Cuando se llama a una función, se crea un marco de ejecución que contiene información sobre la función en curso, como sus variables locales y la posición de retorno. Estos marcos se apilan unos sobre otros, formando la pila de ejecución. A medida que se completan las funciones, se desapilan, y la ejecución regresa al marco anterior. Esto permite un seguimiento eficiente del flujo del programa y garantiza la correcta gestión de variables locales. La pila de ejecución juega un papel fundamental en la recursión y en la gestión de llamadas a funciones en Python.|La pila de ejecución en Python es una estructura de datos que almacena las funciones que están siendo ejecutadas actualmente. La pila de ejecución se utiliza para mantener el estado de las funciones, incluidas las variables locales, los parámetros y el estado de ejecución.La pila de ejecución se implementa como una estructura de datos LIFO (último en entrar, primero en salir). Esto significa que la última función que se llama se almacena en la parte superior de la pila, y la primera función que se llamó se almacena en la parte inferior.La pila de ejecución se utiliza para implementar funciones recursivas, así como para gestionar el alcance de las variables. |La pila de ejecución en Python se refiere a la estructura de datos utilizada por el intérprete de Python para llevar un registro de las funciones que se han llamado y las variables asociadas a ellas. Cada vez que se llama a una función, se crea un nuevo marco de ejecución que se agrega a la pila, y cuando la función termina, el marco se elimina de la pila. La pila de ejecución es importante para el seguimiento de la ejecución del programa y para la gestión de la memoria, ya que los marcos de ejecución contienen información sobre las variables y los argumentos de la función|
|Parámetros|En Python, los parámetros son valores que una función acepta durante su definición, mientras que los argumentos son los valores reales pasados a la función durante su llamada. Python admite parámetros posicionales, palabras clave, valores predeterminados y la posibilidad de aceptar un número variable de argumentos (*args) o argumentos de palabras clave (**kwargs). La semántica de paso de argumentos en Python facilita la flexibilidad y expresividad en la definición y llamada de funciones, permitiendo a los programadores adaptarse a diversas necesidades de programación.|Los parámetros en Python son los valores que se pasan a una función. Se utilizan para proporcionar datos a la función y controlar su comportamiento.Los parámetros se definen en la declaración de la función. Pueden ser de cualquier tipo de datos, incluyendo números, cadenas, listas, diccionarios, etc.Los parámetros se pueden pasar a una función por valor o por referencia. Cuando se pasan por valor, la función recibe una copia del valor del parámetro. Cuando se pasan por referencia, la función recibe una referencia al valor del parámetro.Los parámetros son una herramienta importante para la programación modular. Permiten que las funciones sean más flexibles y reutilizables. |Los parámetros en Python son valores que se pasan a una función cuando es llamada. Estos valores son utilizados por la función para realizar ciertas operaciones y pueden ser de diferentes tipos, como enteros, cadenas, listas, entre otros. Los parámetros se definen entre paréntesis en la declaración de la función y se utilizan para transferir la información a la función.|
|Tipos de datos|Python incluye diversos tipos de datos, como enteros, flotantes, cadenas, listas, tuplas, conjuntos y diccionarios. La asignación de tipo es dinámica, permitiendo a las variables cambiar de tipo durante la ejecución. Además, Python admite tipos de datos personalizados mediante clases y módulos, facilitando la manipulación de información de manera versátil. La diversidad de tipos y la flexibilidad en su uso contribuyen a la eficacia y expresividad del lenguaje, adaptándose a una amplia gama de aplicaciones y escenarios de programación. |En Python, los tipos de datos definen el tipo de valor que puede almacenar una variable. Los tipos de datos básicos en Python son los números, las cadenas, los booleanos, las listas, los diccionarios y los conjuntos.Los números pueden almacenar valores enteros, de coma flotante o complejos. Las cadenas pueden almacenar secuencias de caracteres. Los booleanos pueden almacenar valores verdaderos o falsos. Las listas pueden almacenar secuencias de valores de cualquier tipo. Los diccionarios pueden almacenar pares clave-valor. Los conjuntos pueden almacenar colecciones de valores únicos.Los tipos de datos son importantes para la programación en Python. Permiten que el compilador de Python verifique el tipo de los valores y asegure que se utilicen correctamente. |Python admite varios tipos de datos, como números, cadenas, booleanos, listas, tuplas, conjuntos y diccionarios. Los números pueden ser enteros, flotantes o complejos, y las cadenas son secuencias de caracteres. Los booleanos son valores verdadero o falso, y las listas, tuplas y conjuntos son colecciones de elementos. Los diccionarios se utilizan para almacenar pares clave-valor. Python también admite otros tipos de datos, como secuencias y mapeos, y proporciona una variedad de bibliotecas y herramientas para trabajar con diferentes tipos de datos|
|Excepciones|En Python, las excepciones son eventos que interrumpen el flujo normal de ejecución del programa cuando ocurre un error. Utilizando bloques try-except, los programadores pueden manejar estas excepciones de manera controlada, permitiendo la ejecución de código específico en caso de fallo. Python proporciona una variedad de excepciones incorporadas, como ValueError o FileNotFoundError, y permite la creación de excepciones personalizadas. El manejo de excepciones mejora la robustez del código, facilitando la identificación y gestión de errores de manera estructurada y evitando la terminación abrupta del programa.|En Python, las excepciones son objetos que representan un error que ocurre durante la ejecución de un programa. Las excepciones se pueden utilizar para controlar el flujo de ejecución del programa y para proporcionar información sobre el error que ocurrió.Las excepciones se pueden tratar mediante la instrucción try-except. La instrucción try ejecuta un bloque de código que puede generar una excepción. La instrucción except se ejecuta si se produce una excepción.Las excepciones son una herramienta importante para la programación en Python. Permiten que los programas sean más robustos y fáciles de depurar. |Las excepciones en Python son eventos que ocurren durante la ejecución de un programa y que interrumpen su flujo normal. Estas excepciones pueden ser causadas por errores de sintaxis, errores de tiempo de ejecución o errores de lógica, entre otros. Python proporciona un mecanismo para manejar estas excepciones, lo que permite al programador controlar el comportamiento del programa en caso de que se produzca una excepción. El manejo de excepciones en Python se realiza mediante la utilización de bloques try-except, que permiten capturar y manejar las excepciones que se produzcan durante la ejecución del programa
 |

### Implementación y sus alternativas

### Características

## Parte C: Conclusiones finales
- *Incluya conclusiones respecto de las tres perspectivas de análisis solicitadas. Puede agregar aportes de su parte, comentarios, opiniones, críticas, o si se quiere agregar algo más.* 