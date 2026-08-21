def Transpor(listaAdj):
    ListaTransposta = [[] for _ in range(len(listaAdj))]
    for vertice in range(len(listaAdj)):
        for destino in listaAdj[vertice]:
            ListaTransposta[destino].append(vertice)
    return ListaTransposta

def DFSFase1(vertice, listaAdj, JaVisitados):
    if vertice not in JaVisitados:
        JaVisitados.add(vertice)
        for destino in listaAdj[vertice]:
            DFSFase1(destino, listaAdj, JaVisitados)
        stack.append(vertice)

def DFSFase2(vertice, listaAdjTransposta, JaVisitados):
    if vertice not in JaVisitados:
        JaVisitados.add(vertice)
        listaAux.append(vertice)

        for destino in listaAdjTransposta[vertice]:
            DFSFase2(destino, listaAdjTransposta, JaVisitados)

stack = []
listaAdj = [[1],[2],[0,3],[4],[5,7],[6],[4,7],[]]
listaAdjTransposta = Transpor(listaAdj)

Javisitados = set()

for vertice in range(len(listaAdj)):
    if vertice not in Javisitados:
        DFSFase1(vertice, listaAdj, Javisitados)

Javisitados = set()
listaComponentesFortementeConexos = []
while len(stack) != 0:
    vertice = stack.pop()
    if vertice not in Javisitados:
        listaAux = []
        DFSFase2(vertice, listaAdjTransposta, Javisitados)
        listaComponentesFortementeConexos.append(listaAux)
print(listaComponentesFortementeConexos)
