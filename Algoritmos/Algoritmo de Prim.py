import heapq # Buil-in Python para HEAP (Fila de Prioridade)

def Prim(fila, listaAdj, JaVisitados, anterior, custo):
    while (len(fila) > 0):
        pesoAtual, atual = heapq.heappop(fila)
        if atual not in JaVisitados:
            JaVisitados.add(atual)
            custo[atual] = pesoAtual

            if(anterior[atual] > -1):
                resultado[anterior[atual]].append(atual)

            for destino, peso in listaAdj[atual]:
                if destino not in JaVisitados and custo[destino] > peso:
                    heapq.heappush(fila, (peso, destino))
                    anterior[destino] = atual
                    custo[destino] = peso

listaAdjPonderada = [
    [[1,4],[4,3]],                  #0
    [[0,4],[2,3],[4,5],[5,6]],      #1
    [[1,3],[3,2],[5,4]],            #2
    [[2,2],[7,5]],                  #3
    [[0,3],[1,5],[5,7],[6,4]],      #4
    [[1,6],[2,4],[4,7],[6,5],[7,3]],#5
    [[4,4],[5,5],[7,7]],            #6
    [[3,5],[5,3],[6,7]]]            #7

VerticesAnterior = [-1 for _ in range(len(listaAdjPonderada))]
JaVisitados = set()
custo = [999999 for _ in range(len(listaAdjPonderada))]
fila = []
resultado = [[] for _ in range(len(listaAdjPonderada))]

for vertice in range(len(listaAdjPonderada)):
    if vertice not in JaVisitados:
        VerticesAnterior[vertice] = -1
        JaVisitados.add(vertice)
        for destino, peso in listaAdjPonderada[vertice]:
            if destino not in JaVisitados and custo[destino] > peso:
                heapq.heappush(fila, (peso, destino))
                VerticesAnterior[destino] = vertice
                custo[destino] = peso

        Prim(fila, listaAdjPonderada, JaVisitados, VerticesAnterior, custo)

print(resultado)
identificador = 0

import heapq # Buil-in Python para HEAP (Fila de Prioridade)
fila = []
heapq.heappush(fila, (peso, identificador)) #Adiciona elemento com priori
elemento = heapq.heappop(fila) #Retira elemento