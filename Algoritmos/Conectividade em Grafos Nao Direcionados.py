def DFS(vertice, visitados, listaAdj):
    if vertice not in visitados:
        visitados.add(vertice)
        listaAux.append(vertice)
        for destino in listaAdj[vertice]:
            if destino not in visitados:
                DFS(destino, visitados, listaAdj)

listaAdj = [[1,2],[0,3,4,5],[0,5,6],[1,4],[1,3],[1,2],[2],[8],[7]]

visitados = set()
componentesConexos = []
for vertice in range(len(listaAdj)):
    listaAux = []
    if vertice not in visitados:
        DFS(vertice, visitados, listaAdj)
        componentesConexos.append(listaAux)

print(componentesConexos)