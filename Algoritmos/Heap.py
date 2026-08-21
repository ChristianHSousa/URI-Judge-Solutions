class CustomHeap:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tamanho_d = 0
        self.ultimo_elemento = -1
        self.heap = []

    def right(self, i):
        return (i + 1) * 2

    def left(self, i):
        return (i * 2) + 1

    def parent(self, i):
        return (i - 1) // 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, valor):
        if self.ultimo_elemento + 1 >= self.tamanho:
            return

        self.ultimo_elemento += 1
        if self.tamanho_d > self.ultimo_elemento:
            self.heap[self.ultimo_elemento] = valor
        else:
            self.heap.append(valor)
            self.tamanho_d += 1

        i = self.ultimo_elemento
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, i):
        esquerda = self.left(i)
        direita = self.right(i)
        menor = i

        if esquerda <= self.ultimo_elemento and self.heap[esquerda] < self.heap[menor]:
            menor = esquerda
        if direita <= self.ultimo_elemento and self.heap[direita] < self.heap[menor]:
            menor = direita

        if i != menor:
            self.swap(i, menor)
            self.heapify(menor)

    def extract(self):
        if self.ultimo_elemento < 0:
            return None

        extracto = self.heap[0]
        self.heap[0] = self.heap[self.ultimo_elemento]
        self.ultimo_elemento -= 1
        self.heapify(0)
        return extracto

    def vetor(self):
        return self.heap[:self.ultimo_elemento + 1]

h = CustomHeap(30)
h.insert(10)
h.insert(100)
h.insert(4)
h.insert(10)
h.insert(8)
h.insert(-1)
h.extract()
h.insert(0)
h.insert(800)
print(h.vetor())