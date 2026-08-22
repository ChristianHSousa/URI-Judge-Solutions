quantidade_de_conjuntos = 10
pais = [i for i in range(quantidade_de_conjuntos)]
ranks = [0] * quantidade_de_conjuntos

def achar(conj_1):
    if pais[conj_1] != conj_1:
        pais[conj_1] = achar(pais[conj_1])
    return pais[conj_1]

def unir(conj_1, conj_2, quantidade_de_conjuntos):
    raiz_1 = achar(conj_1)
    raiz_2 = achar(conj_2)
    if raiz_1 != raiz_2:
        if(ranks[raiz_1] < ranks[raiz_2]):
            pais[conj_1] = conj_2
        elif(ranks[raiz_1] > ranks[raiz_2]):
            pais[conj_2] = conj_1
        else:
            pais[conj_2] = conj_1
            ranks[raiz_1] += 1
        quantidade_de_conjuntos = quantidade_de_conjuntos - 1
        return True, quantidade_de_conjuntos
    return False, quantidade_de_conjuntos

resultado, quantidade_de_conjuntos = unir(0,1,quantidade_de_conjuntos)