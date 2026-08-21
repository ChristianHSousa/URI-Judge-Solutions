def DFS(vertice, listaAdj, cores):
    if cores[vertice] == "B":
        cores[vertice] = "C"
        for i in listaAdj[vertice]:
            if cores[i] == "B":
                DFS(i, listaAdj, cores)

    ordenacaoTopologica.append(vertice)
    cores[vertice] = "P"

cores = {}
listaAdj = [[1,2,3],[4],[5,6],[],[5],[6],[]]
ordenacaoTopologica = []
for i in range(len(listaAdj)):
    cores[i] = "B"

for i in range(len(listaAdj)):
    if cores[i] == "B":
        DFS(i,listaAdj,cores)

ordenacaoTopologica.reverse()
print(ordenacaoTopologica)