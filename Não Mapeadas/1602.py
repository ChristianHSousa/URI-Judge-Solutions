def conta_divisores(expoentes):
    exp = 1
    for i in range(len(expoentes)):
        if (expoentes[i] != -1):
            exp = exp * (expoentes[i] + 2)

    return exp


num = int(input())
limite = int((num ** 0.5)) + 1
primos = [True] * (num + 1)
primos[0] = primos[1] = False
for i in range(2, limite):
    x = 2
    while x * i <= num:
        primos[x * i] = False
        x = x + 1

primos_int = [numero for numero, eh_primo in enumerate(primos) if eh_primo]


hiperprimos = 1
for i in range(2,num):
    expoentes = []
    aux = i
    novoLim = int(i ** (1/2)) + 1
    for j in range(novoLim):
        exp = -1
        while aux % primos_int[j] == 0:
            aux = aux / primos_int[j]
            exp = exp + 1
        expoentes.append(exp)

    if(primos[conta_divisores(expoentes)]):
        hiperprimos = hiperprimos + 1

print(hiperprimos)