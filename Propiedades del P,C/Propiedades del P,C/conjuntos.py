
A = []
for x in range(3):
    valor=input("Ingresa elementos para el conjunto A:")
    A.append(valor)
print("----------------------------------")
print("Haz ingresado estos elementos: ")    
print(A)
print("----------------------------------")

print("  ")

B = []
for s in range(3):
    valor=input("Ingresa elementos para el conjunto B:")
    B.append(valor)
print("----------------------------------")
print("Haz ingresado estos elementos: ")    
print(B)
print("----------------------------------")

print("  ")

C = []
for t in range(3):
    valor=input("Ingresa elementos para el conjunto C:")
    C.append(valor)
print("----------------------------------")
print("Haz ingresado estos elementos: ")    
print(C)
print("----------------------------------")

print("  ")

D = []
for t in range(3):
    valor=input("Ingresa elementos para el conjunto D:")
    D.append(valor)
print("----------------------------------")
print("Haz ingresado estos elementos: ")    
print(D)
print("----------------------------------")

print("  ")
print("Estos son los elementos de tus listas")
print("Conjunto A", A)
print("Conjunto B", B)
print("Conjunto C", C)
print("Conjunto D", D)
print("  ")

Set_A = set(A)
Set_B = set(B)
Set_C = set(C)
Set_D = set(D)

print("  ")
print("---------------------------------")
print("  ")

print("Propiedad 7")
print("A x (B U C) = (A x B) U (A x C))")

print("  ")
print("Esta es la union de: (B U C)")
Union_BC = Set_B | Set_C 
print(Union_BC)
print("Este es el resultado de: A x (B U C)")
print([(mm, nn)for mm in Set_A for nn in Union_BC])

#Set_AxB = set(AxB)      #Esta es la operacion (A x B)
#Set_AxC = set(AxC)      #Esta es la operacion (A x C)

print("Este es el rescultado de: (A x B) U (A x C)")
print(Set_AxB | Set_AxC)

print("  ")
print("Esto quiere decir que son iguales o lo mismo")
print("Esta es la operacion: A x (B U C)")
print([(qq, ww)for qq in Set_A for ww in Union_BC])
print("Este es el rescultado de: (A x B) U (A x C)")
print(Set_AxB | Set_AxC)