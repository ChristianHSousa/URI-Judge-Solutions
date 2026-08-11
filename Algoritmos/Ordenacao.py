n, k, m = map(int, input().split())

lista = [n,k,m]

if(lista[0] > lista[1]):
    lista[0], lista[1] = lista[1], lista[0]

if(lista[1] > lista[2]):
    lista[1], lista[2] = lista[2], lista[1]

if(lista[0] > lista[1]):
    lista[0], lista[1] = lista[1], lista[0]
print(lista)

