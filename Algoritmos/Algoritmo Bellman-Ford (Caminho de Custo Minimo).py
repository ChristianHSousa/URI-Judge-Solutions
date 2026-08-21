def listaArestas(listaAdj):
    listaArestas = []
    for i in range (len(listaAdj)):
        for lista in (listaAdj[i]):
            aux = [i]
            aux.extend(lista)
            listaArestas.append(aux)
    return listaArestas

def BellmanFord(listaAdj, inicio, distancia, anteriores):
    distancia = [999999 for i in range(len(listaAdj))]
    anteriores = [-1 for i in range(len(listaAdj))]

    distancia[inicio] = 0
    anteriores[inicio] = inicio

    arestas = listaArestas(listaAdj)

    for i in range(len(arestas)):
        origem, destino, peso = arestas[i]
        if(distancia[origem] + peso < distancia[destino]):
            distancia[destino] = distancia[origem] + peso
            anteriores[destino] = origem

    for i in range(len(arestas)):
        origem, destino, peso = arestas[i]
        if(distancia[origem] + peso < distancia[destino]):
            print("Ciclo negativo encontrado")

    print(anteriores)
listaAdj = [
    [[2,1],[3,3.5]],
    [[4,5],[0,6]],
    [[1,2.5],[3,2],[4,6]],
    [[5,4]],
    [[5,3]],
    [[2,4.5]]
]

origem = 0
distancia = []
anteriores = []
BellmanFord(listaAdj, origem, distancia, anteriores)