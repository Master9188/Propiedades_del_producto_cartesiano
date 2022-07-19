print("Dame tres conjuntos A, B y C")
print("  ")

A=[]
for x in range(3):
    valor=input("Ingresa elementos para el conjunto A:")
    A.append(valor)
print("----------------------------------")
print("Haz ingresado estos elementos: ")    
print(A)
print("----------------------------------")

print("  ")

B=[]
for s in range(3):
    valor=input("Ingresa elementos para el conjunto B:")
    B.append(valor)
print("----------------------------------")
print("Haz ingresado estos elementos: ")    
print(B)
print("----------------------------------")

print("  ")

C=[]
for t in range(3):
    valor=input("Ingresa elementos para el conjunto C:")
    C.append(valor)
print("----------------------------------")
print("Haz ingresado estos elementos: ")    
print(C)
print("----------------------------------")

print("  ")
print("Estos son los elementos de tus listas")
print("Conjunto A", A)
print("Conjunto B", B)
print("Conjunto C", C)
print("  ")

print("----------------------------------")
print("Propiedad 1")
print("A * B NO= B * A")
print("----------------------------------")
print("Conjunto A", A)
print("  ")
print("Conjunto B", B)
print("  ")

print("Esto es A * B")
print([(x, s)for x in A for s in B])

print("Esto es B * A")
print([(s, x)for s in B for x in A])
print("Esto demuestra que A * B no es igual a B * A")

print("----------------------------------")
print("  ")

print("Propiedad 2")
print("A x 0 = 0")

print("  ")
print("----------------------------------")
print("  ")
O = []
print("conjunto A =", A)
print("Conjunto vacio u 0 =", O)
print("A x 0 = 0")
A.clear()
print("Obtendriamos el conjunto A: ", A)
