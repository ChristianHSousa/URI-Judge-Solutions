def Transpor(listaAdj):

    transposto = [[] for _ in range(len(listaAdj))]
    for vertice in range(len(listaAdj)):
        for destino in listaAdj[vertice]:
            transposto[destino].append(vertice)
    return transposto

listaAdj = [[1],[2,3],[0,5],[4],[2],[6],[4],[9],[7],[]]
listaAdjT = Transpor(listaAdj)

print(listaAdj)
print(listaAdjT)

