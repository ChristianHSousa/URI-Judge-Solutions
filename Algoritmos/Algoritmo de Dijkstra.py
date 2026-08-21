import heapq

def Dijkstra(listaAdjPonderada, inicio, distancias, anteriores, visitados):
    distancias = [999999 for i in range(len(listaAdjPonderada))]
    anteriores = [-1 for i in range(len(listaAdjPonderada))]
    distancias[inicio] = 0
    anteriores[inicio] = inicio
    fila = []
    for i in range(len(listaAdjPonderada)):
        heapq.heappush(fila, (999999, i))
    heapq.heappush(fila, (0, inicio))

    resultado = [[] for _ in range(len(listaAdjPonderada))]

    while fila:
        pesoAtual, VerticeAtual = heapq.heappop(fila)
        if(VerticeAtual not in visitados):
            if (anteriores[VerticeAtual] > -1 and anteriores[VerticeAtual] != VerticeAtual):
                resultado[anteriores[VerticeAtual]].append(VerticeAtual)

            visitados.add(VerticeAtual)
            for vizinho, pesoVizinho in listaAdjPonderada[VerticeAtual]:
                if(distancias[vizinho] > distancias[VerticeAtual] + pesoVizinho):
                    distancias[vizinho] = distancias[VerticeAtual] + pesoVizinho
                    anteriores[vizinho] = VerticeAtual
                    heapq.heappush(fila, (distancias[vizinho], vizinho))
    return (resultado)

listaAdjPonderada = [
    [[2,1],[3,3.5]],
    [[4,5],[0,6]],
    [[1,2.5],[3,2],[4,6]],
    [[5,4]],
    [[5,3]],
    [[2,4.5]]
]
inicio = 0
distancia =[]
anteriores = []
visitados = set()
print(Dijkstra(listaAdjPonderada, inicio, distancia, anteriores, visitados))