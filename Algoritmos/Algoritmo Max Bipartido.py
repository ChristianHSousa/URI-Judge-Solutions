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
            grafo[p][pai] = grafo[p].get(pai, 0) + caminho_flow
            p = anteriores[p]

    return flow_maximo

def BFS(grafo, fonte, pia):
    visitados = set()
    fila = []
    fila.append(fonte)
    visitados.add(fonte)

    while fila:
        atual = fila.pop(0)

        if(not grafo[atual]):
            continue

        for vertice, fluxo in (grafo[atual].items()):
            if vertice not in visitados and fluxo > 0:
                fila.append(vertice)
                visitados.add(vertice)
                anteriores[vertice] = atual

                if vertice == pia:
                    return True

    # Busca em profundidade não achou a pia
    return False


def BFSBipartido(fila, cores, listaAdj, bipartido ):
    while fila:
        vertice = fila.pop(0)
        for destino in listaAdj[vertice]:
            if cores[destino] == -1:
                cores[destino] = 1 - cores[vertice]
                fila.append(destino)
            else:
                if cores[destino] == cores[vertice]:
                    bipartido = False
    return bipartido


listaAdj = [[1,5],[0,2,8],[1,3,7],[2,4],[3,5],[4,6],[5,7],[6,8],[7]]
fila = []
cores = {}
for i in range(len(listaAdj)):
    cores[i] = -1

bipartido = True
for vertice in range(len(listaAdj)):
    if cores[vertice] == -1:
        cores[vertice] = 0
        fila.append(vertice)
        bipartido = BFSBipartido(fila, cores, listaAdj,bipartido)

if(bipartido):
    A = set(chave for chave, valor in cores.items() if valor == 0)
    B = set(chave for chave, valor in cores.items() if valor == 1)
    fonte = {valor + 1: 1 for valor in A}
    listaAdjPonderada = [fonte]
    pia = 1 + len(listaAdj)
    for vertice in range(len(listaAdj)):
        aux = {}
        if(vertice in A):
            for destino in listaAdj[vertice]:
                aux[destino + 1] = 1
        if(vertice in B):
            aux[pia] = 1
        listaAdjPonderada.append(aux)
    listaAdjPonderada.append({})
    anteriores = [-1 for _ in range(len(listaAdjPonderada))]
    print(FordFulkerson(listaAdjPonderada,0,pia))