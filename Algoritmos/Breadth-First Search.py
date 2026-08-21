import queue
class ElementoLista:
    def __init__(self, valor=0, proximo=None):
        self.valor = valor
        self.proximo = proximo

class ListaLigada:
    def __init__(self, tamanho=0, no=None):
        self.tamanho = tamanho
        self.inicio = no
        self.final = self.inicio

    def inserir(self, valor):
        no = ElementoLista(valor, None)
        if self.final is not None:
            self.final.proximo = no
        if self.inicio is None:
            self.inicio = no

        self.final = no
        self.tamanho += 1

    def retirar(self):
        if self.inicio is None:
            return None  # lista vazia, nada a retirar

        aux = self.inicio
        self.inicio = self.inicio.proximo
        aux.proximo = None  # evita referência pendurada

        if self.inicio is None:
            self.final = None  # lista ficou vazia

        self.tamanho -= 1
        return aux

    def mostrar(self):
        atual = self.inicio
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

def BFSListaADJ(vertice, listaAdj, visitados):
    while vertice is not None:
        if vertice.valor not in visitados:
            visitados.add(vertice.valor)

            for i in listaAdj[vertice.valor]:
                lista.inserir(i)

        vertice = lista.retirar()

def BFSListaADJ(vertice, matrizAdj, visitados):
    while vertice is not None:
        if vertice.valor not in visitados:
            visitados.add(vertice.valor)

            for i in range(len(matrizAdj[vertice.valor])):
                if(matrizAdj[vertice.valor][i] == 1):
                    lista.inserir(i)

        vertice = lista.retirar()

#             0      1    2    3   4   5   6
listaAdj = [[2,3,4],[5],[6,7],[7],[6],[7],[],[1]]

matrizAdj = [[0,1,1,1,0,0,0,0], # 0
             [0,0,0,0,1,0,0,0], # 1
             [0,0,0,0,0,1,1,0], # 2
             [0,0,0,0,0,0,1,0], # 3
             [0,0,0,0,0,1,0,0], # 4
             [0,0,0,0,0,0,1,0], # 5
             [0,0,0,0,0,0,0,0], # 6
             [1,0,0,0,0,0,0,0]] # 7

# Pode se utilizar o Queue built-in python
import queue
fila = queue.Queue()
fila.put() # Adicionar elemento
fila.get() # Remover elemento
fila.empty() # retorna bool
lista = ListaLigada()
visitados = set()

for i in range(len(matrizAdj)):
    if i not in visitados:
        lista.inserir(i)
        BFSListaADJ(lista.retirar(), listaAdj, visitados)

lista = ListaLigada()
visitados = set()
for i in range(len(matrizAdj)):
    if i not in visitados:
        lista.inserir(i)
        BFSListaADJ(lista.retirar(), listaAdj, visitados)
