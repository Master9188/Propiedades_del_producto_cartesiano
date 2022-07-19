#maximo comun divisor
#dos numeros#
def mcd(n1, n2):
    temporal = 0
    while n2 != 0:
        temporal = n2
        n2 = n1 % n2
        n1 = temporal
    print(n1)
    return n1

#mcd(10,15)

#con 2 sacar a que potencia tiene que estar este para obtener ese resultado
def potencia (n):
    lista = []
    for i in range (n):
        potencia = 2**i
        if potencia <= n:
            lista.append (i)
    print (lista.pop())
    return n

#potencia(65)


 
def panprimo(n):
    def isprime(n):
        for x in range(2,n):
            if n % x == 0:
                return False;
        return True;
 
    r=str(n);
    return '0' in r and '1' in r  and '2' in r and '3' in r and '4' in r and '5' in r and '6' in r and '7' in r and '8' in r and '9' and isprime(n % 1000)
 
panprimo(643)