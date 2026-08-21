from collections import deque # Atual como uma fila normal

def BFS(fila, cores, listaAdj, bipartido ):
    while fila:
        vertice = fila.popleft()
        for destino in listaAdj[vertice]:
            if cores[destino] == -1:
                cores[destino] = 1 - cores[vertice]
                fila.append(destino)
            else:
                if cores[destino] == cores[vertice]:
                    bipartido = False
    return bipartido


listaAdj = [[1,5],[0,2,8],[1,3,7],[2,4],[3,5],[4,6],[5,7],[6,8],[7]]
fila = deque()
cores = {}
for i in range(len(listaAdj)):
    cores[i] = -1

bipartido = True
for vertice in range(len(listaAdj)):
    if cores[vertice] == -1:
        cores[vertice] = 0
        fila.append(vertice)
        bipartido = BFS(fila, cores, listaAdj,bipartido)
if(bipartido):
    print("Grafo é bipartido")
else:
    print("Grafo não é bipartido")