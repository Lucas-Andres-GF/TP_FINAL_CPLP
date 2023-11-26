<h1 align="center" > <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" style="width: 50px; height: auto;">TRABAJO FINAL INTEGRADOR <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" style="width: 50px; height: auto;"></h1>

<h4 align="center" > CONCEPTOS Y PARADIGMAS DE LENGUAJES DE PROGRAMACIÓN </h4>

----

### Requisitos: 
- *Este trabajo final es obligatorio para aquellos que quieren promocionar. Puede realizarse en grupos de hasta 2 personas.*

- *Para promocionar tuvieron que haber explicado oralmente los ejercicios prácticos solicitados durante la cursada, aprobar el examen parcial y aprobar este TP Integrador junto con su exposición oral que son obligatorios.*

### Presentación:
- *El trabajo debe subirse a la plataforma, en el módulo Trabajo Final Integrador y debe exponerse oralmente.*

- *La fecha de entrega del trabajo final es: 27 de noviembre*

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
        - Python soporta programación funcional, la idea es descoponer un problema en funciones. idealmente las funciones reciben datos de entrada y devuelven un unico valor de salida, sin producir efectos secundarios sobre otros componentes del programa.
        ```python
        # Programación funcional
        
        

    
- *Su sintaxis*

    - Estructura de un programa
         - https://docs.python.org/es/3/reference/executionmodel.html#:~:text=4.1.-,Estructura%20de%20un%20programa,y%20una%20definici%C3%B3n%20de%20clase.
    
    - Identificadores
        
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

- *Tipos de datos*

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
- *Incluya conclusiones respecto de las tres perspectivas de análisis solicitadas. Puede agregar aportes de su parte, comentarios, opiniones, críticas, o si se quiere agregar algo más.* asd