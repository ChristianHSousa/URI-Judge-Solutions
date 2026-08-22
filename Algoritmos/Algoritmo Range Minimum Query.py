class SparseTable:
    def __init__(self, array):
        n = len(array)
        self.n = n
        k = n.bit_length()

        self.log = [0] * (n+1)
        for i in range(2, n+1):
            self.log[i] = self.log[i // 2] + 1

        self.tabela = [array[:]]
        j = 1
        while (1 << j) <= n:
            anterior = self.tabela[j - 1]
            meio = 1 << (j - 1)
            tamanho = n - (1 << j) + 1
            atual = [min(anterior[i],anterior[i+meio]) for i in range(tamanho)]
            self.tabela.append(atual)
            j += 1

    def busca(self, l, r):
        k = self.log[r - l + 1]
        return min(self.tabela[k][l], self.tabela[k][r - (1 << k) + 1])

array = [5, 2, 4, 7, 1, 3, 6]
st = SparseTable(array)
# Qual o menor valor entre o indice 0 e indice 4
print(st.busca(0, 4))