print("Bienvenido a la calculadora")

Nm1 = int(input("Dame un numero: "))
Nm2 = int(input("Dame un numero: "))

print("Que operacion te gustaria hacer")

print("1 = suma")
print("2 = resta")
print("3 = division")
print("4 = multiplicacion")
print("5 = modulo")

operacion = int(input("Dame el numero de la operacion que quieras hacer:"))

if operacion == 1:
    suma = Nm1+Nm2
    print(suma)
elif operacion == 2:
    suma = Nm1-Nm2
    print(suma)
elif operacion == 3:
    suma = Nm1/Nm2
    print(suma)
elif operacion == 4:
    suma = Nm1*Nm2
    print(suma)
elif operacion == 5:
    suma = Nm1%Nm2
    print(suma)
else:
    print("Esto no es lo pedido")

