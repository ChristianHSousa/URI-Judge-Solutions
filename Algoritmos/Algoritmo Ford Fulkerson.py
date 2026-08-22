def FordFulkerson(grafo, fonte, pia):
    flow_maximo = 0
    while BFS(grafo, fonte, pia):
        caminho_flow = float("Inf")  # REPRESENTAÇÃO DOS INFINITOS POSITIVOS
        p = pia

        while p != fonte:
            caminho_flow = min(caminho_flow, grafo[anteriores[p]][p])
            p = anteriores[p]
        flow_maximo += caminho_flow

        p = pia
        while p != fonte:
            pai = anteriores[p]
            grafo[pai][p] -= caminho_flow
            grafo[p][pai] += caminho_flow
            p = anteriores[p]

    return flow_maximo

def BFS(grafo, fonte, pia):
    visitados = set()
    fila = []
    fila.append(fonte)
    visitados.add(fonte)

    while fila:
        atual = fila.pop(0)
        for vertice, fluxo in enumerate(grafo[atual]):
            if vertice not in visitados and fluxo > 0:
                fila.append(vertice)
                visitados.add(vertice)
                anteriores[vertice] = atual

                if vertice == pia:
                    return True

    # Busca em profundidade não achou a pia
    return False


grafo = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

fonte = 0
pia = 5
anteriores = [-1 for _ in range(len(grafo))]
print(FordFulkerson(grafo, fonte, pia))

