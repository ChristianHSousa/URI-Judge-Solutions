#def conta_divisores(exponentes):
#    exp = 1
#    for i in range(len(exponentes)):
#        if (exponentes[i] != -1):
#            exp = exp * (exponentes[i] + 2)
#    return exp

def verifica_primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limite = num ** (1/2)

    if(limite.is_integer()):
        return False

    limite = int(limite) + 1

    for i in range(3, limite, 2):
        if(num%i == 0):
            return False
    return True


num = int(input())
exponentes = []

implementacao = 1

limite = int((num ** 0.5)) + 1

if(implementacao == 1):
    primos = [True] * (limite+1)
    primos[0] = primos[1] = False

    # Crivo de Erastotenes
    for i in range(2,limite):
        if(primos[i]):
            for j in range(i*i, limite+1, i):
                primos[j] = False
    primos = [numero for numero, eh_primo in enumerate(primos) if eh_primo]

    for i in range(len(primos)):
        while num % primos[i] == 0:
            num = num // primos[i]
            exponentes.append(primos[i])
else:
    for i in range(2, limite):
        if(verifica_primo(i)):
            while num % i == 0:
                num = num // i
                exponentes.append(i)

if(num > 1 ):
    exponentes.append(num)

print(exponentes)