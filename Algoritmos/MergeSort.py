def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

def MergeSort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr)//2
    esq = arr[:meio]
    dir = arr[meio:]

    esq = MergeSort(esq)
    dir = MergeSort(dir)
    return merge(esq, dir)