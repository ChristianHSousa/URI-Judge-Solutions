N = int(input())

lista = list(map(int, input().split()))
preFix = []
soma = 0
for i in range(N):
    soma = soma + lista[i]
    preFix.append(soma)

print(*preFix)