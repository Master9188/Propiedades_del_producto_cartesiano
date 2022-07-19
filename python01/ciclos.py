"""
While   ------------------
"""
#Estructura
"""
while Condicion:
    instructiones
"""

#Convercion de C a F con while
"""
tem = 36    #Desde donde inicia

while tem < 75:     #El "75" dice en donde termina
    print(tem ," " , int((tem - 32)*5/9))
    tem=tem + 1     #Suma 1 a tem hasta llegar a "75"
"""

"""
For     -----------------
"""
#Estructura
"""
for variable in range(21):   #"tem" es donde inicia y "in" especifica donde 
    condicion           #"range" contiene hasta donde termina
"""
"""
print("f°   c°")        #la var "tem" automaticamente empieza en 0
for tem in range(50):   #range crea una secuencia de numeros desde 0, pero no cuenta el ultimo numero
    print(tem ," " , int((tem - 32)*5/9))   #No necesitas colocarle la opcion de sumar +1
"""

"""
Range   -------------------------------------
"""
#Estructura inicio y fin
"""
for variable in range(inicio, fin):    #"Inicio" indica desde que numero inicia
    condicion                   #"Fin" indica en que numero termina 
"""

#for i in range(2, 100):
#    print(i)

#Estructura inicio, fin, paso
"""
for variable in range(inicio, fin, paso):    #"paso" indica de cuanto en cuanto va la serie
    condicion
"""

#for i in range(2, 100, 5):
#    print(i)
