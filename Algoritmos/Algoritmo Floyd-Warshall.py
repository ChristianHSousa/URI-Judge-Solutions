def criaMatrizes(listaAdjPonderada):
    distancia = [[999999 for j in range(len(listaAdjPonderada))] for _ in range(len(listaAdjPonderada))]
    anteriores = [[-1 for j in range(len(listaAdjPonderada))] for _ in range(len(listaAdjPonderada))]
    for i in range(len(listaAdjPonderada)):
        for j in range(len(listaAdjPonderada[i])):
            distancia[i][listaAdjPonderada[i][j][0]] = listaAdjPonderada[i][j][1]
            anteriores[i][listaAdjPonderada[i][j][0]] = i
        distancia[i][i] = 0
        anteriores[i][i] = i
    return distancia, anteriores

def FloydWarshall(listaAdjPonderada):
    distancias, anteriores = criaMatrizes(listaAdjPonderada) # Inicialização

    for k in range(len(listaAdjPonderada)):
        for i in range(len(listaAdjPonderada)):
            for j in range(len(listaAdjPonderada)):
                if(distancias[i][j] > distancias[i][k] + distancias[k][j]):
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
                    anteriores[i][j] = anteriores[k][j]

    return distancias, anteriores

listaAdjPonderada = [
    [[2,1],[3,3.5]],
    [[4,5],[0,6]],
    [[1,2.5],[3,2],[4,6]],
    [[5,4]],
    [[5,3]],
    [[2,4.5]]
]

distancias, anteriores = FloydWarshall(listaAdjPonderada)
for linha in anteriores:
    print(*linha)