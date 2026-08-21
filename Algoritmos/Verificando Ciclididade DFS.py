def DFS(vertice, listaAdj, cores):
    if cores[vertice] == "B":
        cores[vertice] = "C"
        for i in listaAdj[vertice]:
            if cores[i] == "B": #Branco
                DFS(i, listaAdj, cores)
            if cores[i] == "C":
                print(f"Ciclididade em {vertice} para {i}")
        cores[vertice] = "P"


listaAdj = [[1,2,3],[4],[5,6],[6],[5],[6],[0]]
cores = {}
for i in range(len(listaAdj)):
    cores[i] = "B"

for i in range(len(listaAdj)):
    if cores[i] == "B":
        DFS(i, listaAdj, cores)