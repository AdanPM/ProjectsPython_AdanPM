# PEP8
La PEP8 es una guía que indica las convenciones estilísticas a seguir para escribir código Python. Se trata de un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible y abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener. <br>
**¿Qué es el PEP8?** <br>
PEP 8 es la guía de estilos de Python, es un documento que contiene los lineamientos necesarios para que el código en Python sea legible y consistente.

Los problemas más frecuentes al escribir código suelen ser:
1. Líneas demasiado largas.
2. Nombres de variables poco explicativos.
3. Código mal comentado.
4. Uso incorrecto de espacios y líneas en blanco.
5. Código mal identado.

 Hay dos tipos de herramientas:
1. Los linters como flake8 o pycodestyle.
2. los autoformatters como black y autopep8.

Los **autoformatters** se limitan a indicarnos donde nuestro código no cumple con las normas, y en ciertos casos realiza las correcciones automáticamente.

Así se instala autopep8, un autoformatter y se abre el archivo
```
$ pip install autopep8
$ autopep8 script.py -v -i
```

### Organización del código
1. Líneas en Blanco <br>
El uso de líneas en blanco mejora notablemente la legibilidad. Mucho código seguido puede ser difícil de leer, pero un uso excesivo de líneas en blanco puede ser molesto. Python deja su uso a nuestro criterio, siempre y cuando cumplamos lo siguiente:
- Rodear las funciones y clases con dos líneas en blanco. Cada vez que definamos una clase o una función es necesario dejar dos líneas en blanco por arriba y dos por abajo.
- Dejar una línea en blanco entre los métodos de una clase. Los métodos de una clase deberán tener una línea en blanco entre ellos.
- Usar líneas en blanco para agrupar pasos similares. Si tenemos un conjunto de código que realiza una función concreta, es conveniente delimitarlo con una línea en blanco, de la misma manera que un libro separa ideas en párrafos.

Ejemplo de como usar lineas en blanco, separando diferentes funcionalidades con espacios 
```python
def calcula_media_mediana(valores):
    # Calculamos la media
    suma_valores = 0
    for valor in valores:
        suma_valores += valor
    media = suma_valores / len(valores)
    
    # Calculamos la mediana
    valores_ordenados = sorted(valores)
    indice = len(valores) // 2
    if len(valores) % 2:
        mediana = valores_ordenados[indice]
    else:
        mediana = (valores_ordenados[indice]
                   + valores_ordenados[indice + 1]) / 2

    return media, mediana
```

### Espacios en Blanco
El uso de espacios en blanco puede resultar clave para mejorar la legibilidad de nuestro código, y es por lo que la PEP8 nos dice dónde debemos usar espacios y dónde no. <br>
Se trata de buscar un punto de equilibrio entre un código demasiado disperso y con gran cantidad de espacios, y un código demasiado junto donde no se identifican sus partes. <br>
Se nos recomienda usar espacio con operadores de asignación.
Y también con operadores relacionales. 
```python
# Correcto
x = 5

# Incorrecto
x=5

# Correcto
if x == 5:
    pass

# Incorrecto
if x==5:
    pass
```
<br>
Pero cuando tengamos funciones con argumentos por defecto, no debemos dejar espacios.
Por otro lado se recomienda no dejar espacios dentro del paréntesis y tampoco entre corchetes.

```python
# Correcto
def mi_funcion(parameto_por_defecto=5):
    print(parameto_por_defecto)

# Incorrecto
def mi_funcion(parameto_por_defecto = 5):
    print(parameto_por_defecto)

def duplica(a):
    return a * 2

# Correcto
duplica(2)

# Incorrecto
duplica( 2 )

# Correcto
lista = [1, 2, 3]

# Incorrecto
my_list = [ 1, 2, 3, ]

```
<br>



### Identación del código
Como ya hemos visto en otros artículos, Python no usa {} para designar bloques de código como otros lenguajes de programación, sino que usa bloques identados para indicar que un determinado bloque de código pertenece a por ejemplo un if.
```python
if x > 5:
    pass
```
Un bloque identado se representa usando cuatro espacios y aunque el uso del tabulador pueda parecer lo mismo, Python 3 no recomienda su uso. Como regla de oro:
- Usa siempre cuatro espacios.
-	Usa tabuladores si trabajas sobre código ajeno que ya use tabuladores.
- Bajo ningún concepto mezcles uso de espacios y tabuladores.

```python
# Correcto
def mi_funcion(primer_parametro, segundo_parametro,
               tercer_parametro, cuarto_parametro,
               quinto_parametro):
    print("Python")

# Incorrecto
def mi_funcion(primer_parametro, segundo_parametro, tercer_parametro, cuarto_parametro, quinto_parametro):
    print("Python")
```

### Tamaño de linea
Se recomienda limitar el tamaño de cada línea a 79 caracteres, para evitar tener que hacer scroll a la derecha. Este límite también permite tener abiertos múltiples ficheros en la misma pantalla, uno al lado de otro. Por otro lado se limita el uso de docstrings y comentarios a 72 caracteres. <br>
1. Operaciones largas <br>
Si queremos realizar una operación muy larga que no entra en una línea, tendremos que dividirla en múltiples. Lo recomendado es usar el operador al principio de cada línea, ya que resulta mas fácil de leer.
```python
# Recomendado
income = (variable_a
          + variable_b
          + (variable_c - variable_d)
          - variable_e
          - variable_f)

# No recomendado
income = (variable_a +
          variable_b +
          (variable_c - variable_d) -
          variable_e -
          variable_f)
```

2. Codificación de ficheros <br>
Los ficheros se codifican por defecto en ASCII para Python 2 y UTF-8 para Python 3, por lo que será necesario definir la codificación que usemos cuando queramos usar otro tipo.

### Convenciones al Nombrar Elementos: CamelCase y snake_case
A la hora de escribir código, todo tiene nombres: variables, clases, funciones, paquetes, módulos, etc. Es por lo tanto muy importante seguir unas directrices determinadas para que nuestro código sea lo más legible posible. No se nombra igual a una clase que a una función, y tampoco suele ser recomendable usar nombres como a o x ya que aporta poca información. 

### Eligiendo Nombres
Antes de nada debemos debemos pensar el nombre que le vamos dar a nuestra variable clase o función. Es importante tener en cuenta lo siguiente:
-	Evitar usar palabras reservadas. Si es necesario usar una palabra reservada como class, usar class_ como alternativa.
-	Evitar usar l O y I, ya que pueden ser confundidas.
-	Usar _variable para especificar uso interno. Por ejemplo from m import * no importaría lo que empieza con _.
-	Se puede usar __variable para invocar el name mangling y hacer privadas determinadas variables o métodos.
-	Para métodos mágicos usar siempre __init__, pero no son nombres que debemos crear sino reutilizar los que Python nos ofrece.

#### Estilos: Camel Case y snake_case
Supongamos que ya sabemos como vamos a nombrar a nuestra clase, función o variable. Pongamos que queremos llamar a nuestra función “mi función de prueba”. Dado que no podemos utilizar espacios para nombrar variables, hay diferentes alternativas:
- mi_funcion_de_prueba
-	MiFuncionDePrueba
-	MIFUNCIONDEPRUEBA
-	MI_FUNCION_DE_PRUEBA
-	mifunciondeprueba

Algunas de estas alternativas son conocidas como Camel Case o snake_case en el mundo de la programación. Pues bien, Python define cómo nombrar a cada tipo de la siguiente manera:
-	Funciones: Letras en minúscula separadas por barra baja: funcion, mi_funcion_de_prueba.
-	Variables: Al igual que las funciones: variable, mi_variable.
-	Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba.
-	Métodos: Al igual que las funciones, usar snake case: metodo, mi_metodo.
-	Constantes: Nombrarlas usando mayúsculas y separadas por barra bajas: UNA_CONSTANTE, OTRA_CONSTANTE.
-	Módulos: Igual que las funciones: modulo.py, mi_modulo.py.
-	Paquetes: En minúsculas pero sin separar por barra bajas: packete, mipaquete

### Importando Paquetes: Orden y Organización
Los import deben separarse en diferentes líneas.
```python
# Correcto
import os
import sys

# Incorrecto
import os, sys
```
Sin embargo cuando se importen varios elementos de una misma librería, si sería correcto importarlos en la misma línea.
```python
# Correcto
from subprocess import Popen, PIPE
```
Con respecto a su ubicación, deberán seguir la siguiente:
-	Deben ir al principio del fichero.
-	Después de comentarios del módulo y docstrings.
-	Antes de los global y las constantes.



Con respecto a su organización, debiendo haber una línea de separación entre cada grupo:
-	Primero las librerías estándar.
-	Segundo las librerías externas.
-	Tercero las librerías locales.
Con respecto a su tipo:
-	Se recomienda usar imports absolutos.
-	Aunque también se permiten los relativos.

Por último, deben evitarse el from <módulo> import *. El uso de * importa todo lo presente en el <módulo>, por lo que no queda claro que se está usando y que no.

#### Comas al Final de Línea
El uso de comas al final de la línea suele ser opcional, salvo cuando se quiera crear tuplas de un sólo elemento como se muestra a continuación.
- Comentarios
Los comentarios son muy importantes para realizar anotaciones a futuros lectores de nuestro código, y aunque resulta difícil definir cómo se se debe comentar el código, hay ciertas directrices que debemos seguir:
-	Cualquier comentario que contradiga el código es peor que ningún comentario. Por ello es muy importante que si actualizamos el código, no olvidarnos de actualizar los comentarios para evitar crear inconsistencias.
-	Los comentarios deben ser frases completas, con la primera letra en mayúsculas.
-	Si el comentario es corto, no hace falta usar el punto y final.
-	Si el código es comentado en Inglés, usar Strunk/White.
-	Aunque cada uno es libre de escribir sus comentarios en el idioma que considere oportuno, se recomienda hacerlo en Inglés.
-	Evitar comentarios poco descriptivos que no aporten nada más allá de lo que ya se ve a simple vista.
-	En lo relativo a los comentarios docstrings, usar la PEP257 como referencia. 
<br><br>

# Módulos y paquetes en Python
Un **módulo** es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. 
Se trata simplemente de una forma de organizar grandes códigos.

Como ejemplo consideremos el archivo `aritmetica.py`
```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b
```

Podemos acceder a ellas desde otro archivo de Python ubicado en la misma ruta importando el módulo.
```python
import aritmetica

print(aritmetica.sumar(7, 5))
```
Una sintaxis alternativa para importar objetos desde un módulo es la siguiente.
```python
from aritmetica import sumar

print(sumar(7, 5))
```
Tambien se pueden importar varios objetos usando comas (,) o llamar a todos usando *
```python
from aritmetica import sumar, restar, mult, div

print(sumar(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))

#LLAMANDO A TODOS
from aritmetica import *
```
Un **paquete** es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.
```
matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py
```

Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.
```python
import matematica.aritmetica

print(matematica.aritmetica.sumar(7, 5))
```
O bien de la siguiente.
```python
from matematica import aritmetica

print(aritmetica.sumar(7, 5))
```
También, esta otra:
```python
from matematica.aritmetica import sumar

print(sumar(7, 5))
```
Python incluye una inmensa cantidad de módulos y paquetes en su instalación (aún más grande es aquella desarrollada por la comunidad, de la que hablaremos más adelante), a los que se conoce como librería estándar. 

# Entorno virtual en Python
Los entornos virtuales se pueden describir como directorios de instalación aislados. Este aislamiento te permite localizar la instalación de las dependencias de tu proyecto, sin obligarte a instalarlas en todo el sistema. <br>
Beneficios:
-	Puedes tener varios entornos, con varios conjuntos de paquetes, sin conflictos entre ellos. De esta manera, los requisitos de diferentes proyectos se pueden satisfacer al mismo tiempo.
-	Puedes lanzar fácilmente tu proyecto con sus propios módulos dependientes.

### Virtualenv
*virtualenv* es una herramienta que se utiliza para crear entornos Python aislados. 

Crea una carpeta que contiene todos los ejecutables necesarios para usar los paquetes que necesitaría un proyecto de Python.

Puedes instalarlo con pip:
```
pip install virtualenv
```
Verifica la instalación con el siguiente comando:
```
virtualenv --version
```

### Crear un entorno
Para crear un entorno virtual utiliza:
```
virtualenv --no-site-packages my-env
```
Esto crea una carpeta en el directorio actual con el nombre del entorno (my-env/). 
Esta carpeta contiene los directorios para instalar módulos y ejecutables de Python.
También puedes especificar la versión de Python con la que quieres trabajar. Simplemente usa el argumento 
--python=/ruta/a/la/version/de/python. Por ejemplo, python2.7:
virtualenv --python=/usr/bin/python2.7 my-env
```
virtualenv --python=/usr/bin/python2.7 my-env
```

### Lista de entornos
Puedes enumerar los entornos disponibles con:
```
lsvirtualenv
```
Activar un entorno: Antes de utilizar el entorno, debes activarlo:
```
source my-env/bin/activate
```
Esto asegura que solo se usen los paquetes bajo my-env/.
Notarás que el nombre del entorno se muestra a la izquierda de la línea de comandos. De esta forma puedes ver cuál es el entorno activo.

### Instalar paquetes
Puede instalar paquetes uno por uno o configurando un archivo `requirements.txt` para tu proyecto.
```
pip install algun-paquete

pip install -r requirements.txt
```
Si quieres crear un archivo requirements.txt  a partir de los paquetes ya instalados, ejecuta el siguiente comando:
```
pip freeze > requirements.txt
```
El archivo contendrá la lista de todos los paquetes instalados en el entorno actual y sus respectivas versiones. Esto te ayudará a lanzar tu proyecto con sus propios módulos dependientes.

### Desactivar un entorno
Si has terminado de trabajar con el entorno virtual, puedes desactivarlo con:
```
deactivate
```
Esto te devuelve al intérprete de Python predeterminado del sistema con todas sus bibliotecas instaladas.

### Eliminar un entorno
Simplemente elimina la carpeta del entorno.

### Conda
Conda es una gestión de paquetes, dependencias y entornos para muchos lenguajes, incluido Python.

Para instalar Conda, sigue estas instrucciones.

### Crear un entorno

Para crear un entorno virtual, 
use:
```
conda create --name my-env
```
Conda creará la carpeta correspondiente dentro del directorio de instalación de Conda.

También puedes especificar con qué versión de Python quieres trabajar:
```
conda create --name my-env python=3.6
```
### Lista de entornos
Puedes enumerar los entornos disponibles con:
```
conda info --envs
```
Activar un entorno
Antes de utilizar el entorno, debes activarlo:

source activate my-env

### Instalar paquetes
Igual que con virtualenv.

Desactivar un entorno

Si has terminado de trabajar con el entorno virtual, puedes desactivarlo con:
```
source deactivate
```
### Eliminar un entorno
Si quieres eliminar un entorno de Conda, utiliza:
conda remove --name my-env

# PYPI
py.pi o the **Python Package Index** es una herramientas de Python que funciona como un repositorio de software para el lenguaje de programación. En esta plataforma se encuentran paquetes de dependencias y otras herramientas, cada vez más avanzadas, para el mismo lenguaje.

En esta plataforma, al igual que cualquier otro repositorio de código, como Github o Gitlabs, te permite crear una cuenta de usuario para poder agregar nuevos paquetes, buscarlos o guardarlos para utilizarlos después en la escritura de tus códigos.