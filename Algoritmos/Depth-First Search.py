def DFSListaADJ(vertice, visitados, listaAdj):
    if(vertice not in visitados):
        print(f"Visitou {vertice}")
        visitados.add(vertice)
        for i in ((listaAdj[vertice][:])):
           DFSListaADJ(i, visitados, listaAdj)
        print(f"Finalizou {vertice}")

def DFSMatrizADJ(vertice, visitados, MatrizAdj):
    if(vertice not in visitados):
        print(f"Visitou {vertice}")
        visitados.add(vertice)
        for i in range(len(MatrizAdj[vertice])):
            if MatrizAdj[vertice][i] == 1:
                DFSMatrizADJ(i, visitados, MatrizAdj)
        print(f"Finalizou {vertice}")

#             0      1    2    3   4   5   6
listaAdj = [[1,2,3],[4],[5,6],[6],[5],[6],[]]

matrizAdj = [[0,1,1,1,0,0,0], # 0
             [0,0,0,0,1,0,0], # 1
             [0,0,0,0,0,1,1], # 2
             [0,0,0,0,0,0,1], # 3
             [0,0,0,0,0,1,0], # 4
             [0,0,0,0,0,0,1], # 5
             [0,0,0,0,0,0,0]] # 6

visitados = set()
print("Lista de ADJ")
for i in range(len(listaAdj)):
    if i not in visitados:
        DFSListaADJ(i, visitados, listaAdj)

print("Matriz de ADJ")
visitados = set()
for i in range(len(matrizAdj)):
    if i not in visitados:
        DFSMatrizADJ(i, visitados, matrizAdj)
