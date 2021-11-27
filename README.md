# Documentación
A continuación se presenta la documentación respecto al código que implementa la solución del parcial de la asignatura _Herramientas Computacionales_ 
## Problema
Las cafeterías de la **_Pontificia Javeriana Cali_** necesitan un programa que los ayude a gestionar las ventas a _estudiantes y maestros_ ya que ambos tienen un respectivo descuento (50 y 25%). Además de poder gestionar los códigos de producto, la cantidad y el precio, tomando datos acerca de el numero de identificación y de 
## Modelo Computacional
El modelo computacional que resuelve este problema es un código realizado en lenguaje Python bajo las normas de estilo del  _PEP8 _  cuya funcionalidad esta separada en una línea lógica principal y una función.
### Función "productos"
**Objetivo**
El objetivo de la función producto es gestionar los productos, es decir su precio, código y cantidad se encarga de registrar esos datos dependiendo de lo que el usuario ingrese
**Entradas**
La función producto recibe como parámetros dos variables, la variable _sumaPrecioProducto_ y _rol_ con estas dos variables la función realiza todo el proceso de calculo.
**Salida**
La función es concluyente, es decir al momento de invocarla se esta realizando la ultima acción del código que es definir si se va a añadir un producto o si se va a terminar y facturar, los datos de salida son simplemente los recuentos de las variables

| Nombre | Descripción |
|--|--|
| cedula | Es el numero de identificación del usuario |
|sumaPrecioProducto| Es la suma del precio de los productos |  
| descuento | Es el descuento correspondiente del rol |
| listaCodigosProducto | Es la lista que almacena los códigos de los productos seleccionados |
| listaCantidadProducto | Es la lista que almacena la cantidad de productos según el código del producto |

Estas variables están ordenadas para que al momento de cerrar y facturar se imprima en pantalla un mensaje como el siguiente
_”El profesor con Cedula 1454898 debe pagar $12.900 por el producto 076”_

**Como lo calcula**
La forma en que el código realiza todos los procesos es mediante operaciones aritméticas básicas, el principio hay un condicional el cual define si se trata de un estudiante o un maestro, en ambos casos el código modifica la variable de descuento al valor que debe tener, seguido de esto se hace el llamado de la función e inicia un ciclo el cual solo se detiene cuando el usuario digita 0 en el menú correspondiente, hasta entonces la única opción que poseen es de añadir productos. (Véase el archivo llamado _Parcial Final Herramientas Computacionales Copia de Modificacion_)
