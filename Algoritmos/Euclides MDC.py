# Exercicio Beecrowd 1028: https://judge.beecrowd.com/pt/problems/view/1028
# Dividendo vira o divisor e o divisor vira o resto
N = int(input())
for _ in range(N):
    a,c = map(int, input().split())

    if(a > c):
        c, a = a, c

    mdc = 0
    while mdc == 0:
        if (c%a == 0):
            mdc = a
        else:
            c, a = a, c % a

    print(mdc)