#Las funciones sirven para reutilzar codigo
#se puede usar en otro lado u hoja

#funciones
#fragmentos de codigo que recibe parametros, ejecuta acciones y retorna un resultado

def calculo(N1, N2):
    resultado = N1 - N2
    print(resultado)
    return resultado

#calculo(100,50)     #Llama a la funcion y da los parametros 

#Primero creas el proceso
#Si no se llama a la funcion no hara nada

"""
Scope
"""
#Corresponde al manejo de las variables dentro de la misma

#Es ver si la variable esta definida dentro de la funcion o fuera
#-> tambien se les llama "variables locales"
def mcd(n1, n2):
    temporal = 0
    while n2 != 0:
        temporal = n2
        n2 = n1 % n2
        n1 = temporal
    print(n1)
    return n1

mcd(10,15)