# Exercicio Beecrowd 2590: https://judge.beecrowd.com/pt/problems/view/2590
# Precisa otimizar para numeros extremamente grandes

N = int(input())
#for _ in range(N):
X = int(input()) # Expoente
base = int(input()) # Numero a ser elevado
fora = 1
potencia = 0
while X > 1:
    if (X % 2 == 0):
        base = base * base
        X = X // 2
    else:
        fora = fora * base
        base = base * base
        X = (X - 1) // 2
print((fora*base))