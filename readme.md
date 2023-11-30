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

## Parte C: Conclusiones finales
- *Incluya conclusiones respecto de las tres perspectivas de análisis solicitadas. Puede agregar aportes de su parte, comentarios, opiniones, críticas, o si se quiere agregar algo más.* 