#las librerias o modulos 
#son partes de codigo ya escritas por otros programadores
#los cuales ya realizan una funcion 

#ejemplos
#random o math 
"""
primer metodo
"""
#import <libreria o modulo>

#import math
"""
segundo metodo
"""
#from <libreria> import 
#<elemento1>, <Elemento2>

#from math import pow, sqrt

"""
tercer metodo
"""
#from <modulo> import <elemento1> as <alias>

#from math import e as euler

"""
Ejemplo----------------------------------------------------------------
"""
"""
import math
math.sin(0)

from random import uniform
uniform(0, 1)
"""
#modulos

#math
#permite hacer calculos complejos y acceder a constantes conocidas

#random
#permite generar numeros pseudoaletorios

#sirve para no programar de mas

"""
modulos
"""
#Todos los archivos de python son .py
#Los modulos tienen conjunto de funciones y constantes importables desde otro programa o lado

#from funciones import calculo
#Asi se pasa una funcion de una hoja o archivo a otra
def funcion(x):
  n = 3
  return x!=n
print(funcion(9))
print(funcion(10))