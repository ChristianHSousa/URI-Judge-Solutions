def BFS(fila, listaAdj):
    while fila:
        atual = fila.pop(0)

        for destino in listaAdj[atual]:
            if destino not in visitados:
                visitados.add(destino)
                fila.append(destino)
                distancia[destino] = distancia[atual] + 1


visitados = set()
fila = []
listaAdj = [[1,2],[6,7],[3,4],[5],[],[],[],[]]
distancia = [0] * (len(listaAdj))
# Distancia do vertice 0 até todos os outros nós (menor caminho contando arestas)
for vertice in range(len(listaAdj)):
    if vertice not in visitados:
        visitados.add(vertice)
        fila.append(vertice)
        BFS(fila, listaAdj)
print(distancia)