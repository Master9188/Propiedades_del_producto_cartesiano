print("Bienvenido a ... ")
print(""" ______   ______  _____ ____  
|  _ \ \ / /  _ \| ____|  _ \ 
| |_) \ V /| |_) |  _| | | | |
|  __/ | | |  _ <| |___| |_| |
|_|    |_| |_| \_\_____|____/  
""")
print("Hola usuario")
Nombre = input("Coloca tu nombre: ")
print("Hola " + Nombre + " Bienvenido a mi red")

print(" ")

print("Me gustaria conocer tu estatura en metros")
Altura = float(input("Agrega tu estatura: "))
AlturaCm = str(Altura*100)
print("Wow mides " + AlturaCm + " centimetros")

print(" ")

print("Para completar tu perfil nos gustaria conocer tu año de nacimiento")
AñoN = int(input("Ingresa tu año de nacimiento: "))
CalculoA = str(2022 - AñoN)
print("Tienes una edad estimada de: " + CalculoA + " Años")

print(" ")

print("Para finalizar cuentame")
NAmigos = input("Cuantos amigos tienes: ")
print("Increible tienes " + NAmigos + " amigos")

print("----------------------------------")
print("Muy bien " + Nombre + " con esta informacion podremos crear tu perfil con los datos")
print("----------------------------------")
print("Nombre: " + Nombre)
print("Años: " + CalculoA)
print("Altura: " + AlturaCm)
print("Amigos: " + NAmigos)
print("----------------------------------")
print("Gracias por la informacion :D, Esperemos que disfrutes mi red")
print("----------------------------------")
print(" ")

continuar = True
while continuar:
    SoN = input("Desea escribir un mensaje?   (S/N)  ")
    if SoN == "S" or SoN == "s" or SoN == " ":
        mensaje = input("Escribe aqui lo que piensas: ")
        print("----------------------------------")
        print(Nombre + " Dice: " + mensaje)
        print("----------------------------------")
    
        continuar = False

print("Gracias por usar PYRED, !Hasta pronto!")
print("--------------------------------")
