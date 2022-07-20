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

D=[]
for h in range(3):
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
Lista_A = A.copy()
A.clear()
print("Obtendriamos el conjunto A: ", A)

print("  ")
print("----------------------------------")
print("  ")

print("Propiedad 3")
print("(A x B) C no= A (B x C)")

print("Conjunto A =", Lista_A)
print("  ")
print("Conjunto B =", B)
print("  ")
print("Conjunto C =", C)
print(" ")

print("Esto es (A * B)")
List_AB = [(x, s)for x in Lista_A for s in B]
print(List_AB)
print("Esto es (A * B) x C")
print([(ph, ps)for ph in List_AB for ps in C])

print("  ")
print("Esto es (B * C)")
List_BC = [(xh, xs)for xh in B for xs in C]
print(List_BC)
print("Esto es A x (B * C)")
print([(tr, ts)for tr in Lista_A for ts in List_BC])

print(" ")
print("Esto quiere decir que no son iguales")
print("Esto es (A * B) x C")
print([(ph, ps)for ph in List_AB for ps in C])
print("Esto es A x (B * C)")
print([(tr, ts)for tr in Lista_A for ts in List_BC])

print("  ")
print("---------------------------------")
print("  ")

print("Propiedad 4")
#La interseccion solo toma los numeros que se repiten en los dos conjuntos
print("(A n B) x (C n D) no= (A n C) x (B n D)")

Set_A = set(Lista_A)
Set_B = set(B)
Set_C = set(C)          #Esto cambia de una lista a un conjunto
Set_D = set(D)

print("Esta es la interseccion de A n B")
Inter1 = Set_A & Set_B
List_AB = list(Inter1)      #Inter 1 es la interseccion de A n B
print(List_AB)

print("  ")
print("Esta es la interseccion de C n D")
Inter2 = Set_C & Set_D
List_CD = list(Inter2)       #Inter 2 s la interseccion de C n D
print(List_CD)

print("  ")
print("Esta es la operacion: (A n B) x (C n D)")
print([(p, l)for p in List_AB for l in List_CD])

print("  ")
print("Esta es la interseccion de A n C")
Inter3 = Set_A & Set_C
List_AC = list(Inter3)      #Inter 3 es la interseccion de A n C
print(List_AC)

print("  ")
print("Esta es la interseccion de B n D")
Inter4 = Set_B & Set_D
List_BD = list(Inter4)      #Inter 4 es la interseccion de B n D
print(List_BD)

print("  ")
print("Esta es la operacion: (A n C) x (B n D)")
print([(Z, F)for Z in List_AC for F in List_BD])

print("  ")
print("Esto da como resultado: ")
print("Esta es la operacion: (A n B) x (C n D)")
print([(p, l)for p in List_AB for l in List_CD])
print("Esta es la operacion: (A n C) x (B n D)")
print([(Z, F)for Z in List_AC for F in List_BD])
print("  ")

print("Esto comprueba que no son lo mismo")

print("  ")
print("---------------------------------")
print("  ")

print("Propiedad 5")
#La union une los conjuntos en uno mismo, sin repetir los elementos repetidos
print("(A u B) x (C u D) no= (A u C) x (B u D)")

print("  ")
print("Esta es la union de (A U B)")
Union_AB = Set_A | Set_B    #Esta hace la unio de el conjunto A y B
print(Union_AB)

print("  ")
print("Esta es la union de (C U D)")
Union_CD = Set_C | Set_D 
print(Union_CD)

print("  ")
print("Esta es la operacion: (A u B) x (C u D)")
print([(ss, aa)for ss in Union_AB for aa in Union_CD])

print("  ")
print("Esta es la union de (A U C)")
Union_AC = Set_A | Set_C 
print(Union_AC)

print("  ")
print("Esta es la union de (B U D)")
Union_BD = Set_B | Set_D 
print(Union_BD)

print("  ")
print("Esta es la operacion: (A u C) x (B u D)")
print([(tt, hh)for tt in Union_AC for hh in Union_BD])

print("  ")
print("Esto da como resultado")
print("Esta es la operacion: (A u B) x (C u D)")
print([(ss, aa)for ss in Union_AB for aa in Union_CD])
print("Esta es la operacion: (A u C) x (B u D)")
print([(tt, hh)for tt in Union_AC for hh in Union_BD])

print("Esto demuestra que la operacion es cierta")

print("  ")
print("---------------------------------")
print("  ")

print("Propiedad 6")
print("A x (B n C) = (A x B) n (A x C)")

print("  ")
print("Esta es la interseccion (B n C)")
inter_BC = Set_B & Set_C
print(inter_BC)
print("Esta es la operacion: A x (B n C)")
print([(qq, ww)for qq in Set_A for ww in inter_BC])

print("  ")
print("Esta es la operacion (A x B)")
print([(cc, vv)for cc in Set_A for vv in Set_B])
AxB = [(cc, vv)for cc in Set_A for vv in Set_B]
Set_AxB = set(AxB)
print("  ")
print("Esta es la operacion (A x C)")
print([(jj, uu)for jj in Set_A for uu in Set_C])
AxC = [(jj, uu)for jj in Set_A for uu in Set_C]
Set_AxC = set(AxC)
print("Este es el rescultado de: (A x B) n (A x C)")
print(Set_AxB & Set_AxC)

print("  ")
print("Esto quiere decir que son iguales o lo mismo")
print("Esta es la operacion: A x (B n C)")
print([(qq, ww)for qq in Set_A for ww in inter_BC])
print("Este es el rescultado de: (A x B) n (A x C)")
print(Set_AxB & Set_AxC)

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
print("Este es el rescultado de: (A x B) U (A x C)")        #Estan acomodados de diferente forma pero son los mismos
print(Set_AxB | Set_AxC)
