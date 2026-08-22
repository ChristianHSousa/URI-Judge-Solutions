def DFS(vertice):
    visitados.add(vertice)
    euler.append(vertice)
    for destino in listaAdj[vertice]:
        if( destino not in visitados ):
            DFS(destino)
    euler.append(vertice)

listaAdj = [[1,2],[6,7],[3,4],[5],[],[],[],[]]
euler = []
visitados = set()
DFS(0)
print(euler)