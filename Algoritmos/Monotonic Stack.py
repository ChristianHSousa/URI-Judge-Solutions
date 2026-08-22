# O que é. pliha que mantem os elementos em uma ordem crescente ou decrescente
# Encontrar o maior, ou maior anterior | menor, ou menor anterior

def proximo_maior(numeros):
    tamanho = len(numeros)
    resultado = [-1] * tamanho
    pilha = []

    for i in range(tamanho):
        # > - pega o proximo maior
        # < - pega o proximo menor
        while pilha and numeros[i] < numeros[pilha[-1]]:
            index = pilha.pop()
            resultado[index] = i
        pilha.append(i)
    return resultado

numeros = [2,1,5,6,2,3]
# Retorna os indices do proximo maior/menor
print(proximo_maior(numeros))