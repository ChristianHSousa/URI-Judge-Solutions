import math

def DFS(vertice_1, vertice_2, ancestrais, niveis_nos, log, listaAdj):
    ancestrais[vertice_1][0] = vertice_2
    for i in range(1, log + 1):
        ancestrais[vertice_1][i] = ancestrais[ancestrais[vertice_1][i - 1]][i - 1]

    for destino in listaAdj[vertice_1]:
        if destino != vertice_2:
            niveis_nos[destino] = niveis_nos[vertice_1] + 1
            DFS(destino, vertice_1, ancestrais, niveis_nos, log, listaAdj)

# Verifica o ancestral comum entre o vertice1 e vertice2
def lca(vertice1, vertice2,log, niveis_nos, ancestrais):
    if(niveis_nos[vertice1] < niveis_nos[vertice2]):
        vertice1, vertice2 = vertice2, vertice1

    for i in range(log, -1, -1):
        if(niveis_nos[vertice1] - pow(2,i)) >= niveis_nos[vertice2]:
            vertice1 = ancestrais[vertice1][i]

    if vertice1 == vertice2:
        return vertice2

    for i in range(log, -1, -1):
        if ancestrais[vertice1][i] != ancestrais[vertice2][i]:
            vertice1 = ancestrais[vertice1][i]
            vertice2 = ancestrais[vertice2][i]

    return ancestrais[vertice1][0]

listaAdj = [[1,2],[],[3,4],[5],[],[]]

nos = len(listaAdj)
log = math.ceil(math.log(nos,2))
ancestrais = [[-1 for i in range(log + 1)] for j in range(nos)]
niveis_nos = [0 for i in range(nos)]

DFS(0,0,ancestrais,niveis_nos,log,listaAdj)
print(lca(5,4,log,niveis_nos,ancestrais))