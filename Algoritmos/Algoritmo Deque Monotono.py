def janela_deslizante(numeros, tamanho_janela):
    fila = []
    resultado = []

    for index, numero in enumerate(numeros):
        if fila and fila[0] < index - tamanho_janela + 1:
            fila.pop(0)
        while fila and numeros[fila[-1]] < numero:
            fila.pop()

        fila.append(index)
        if index >= tamanho_janela - 1:
            resultado.append(numeros[fila[0]])

    return resultado

vetor = [1, 3, -1, -3, 5, 3, 6, 7]
tamanho_janela = 3
print(janela_deslizante(vetor, tamanho_janela))