N, x, y = map(int, input().split())

dx = [2, 2, 1, 1,-2,-2,-1,-1]
dy = [1,-1, 2,-2, 1,-1,-2, 2]

matriz = [[0] * N for _ in range(N)]

def aceitavel(u,v):
    if(u >= 0 and u < N and v >= 0 and v < N and matriz[u][v] == 0):
        return True
    return False

def testa(i, x, y):

    feito = (i > N*N)
    u = 0
    v = 0
    k = 0
    while (not feito and k < 8):
        u = x + dx[k]
        v = y + dy[k]
        if(aceitavel(u,v)):
            matriz[u][v] = i
            feito = testa(i+1, u, v)
            if(not feito):
                matriz[u][v] = 0
        k += 1
    return feito


matriz[x][y] = 1
f = testa(2,x,y)

if(f):
    for linha in matriz:
        for elemento in linha:
            print("".join(f"{elemento:3d}"),end="")
        print()
else:
    print("Impossivel")