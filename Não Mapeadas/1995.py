class No:
    def __init__(self, raiz):
        self.raiz = raiz
        self.esq = None
        self.dir = None

casos = int(input())


raiz = No(None)
for c in range(casos):
    entrada = map(int, input().split())
    arv = raiz
    for num in entrada:
        if num > arv.raiz and arv.esq != None:
            arv = arv.esq