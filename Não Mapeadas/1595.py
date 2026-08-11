# O trajeto total feito por você tem S metros
# C indica quantas partes correu
# R valor somado quando a pessoa corre

# Busca gulosa
T = int(input())

for i in range(T):
    S, C, R = map(int, input().split())

    Vi = list(map(int, input().split()))

    Vi.sort(reverse=True)
    tempo = 0.0
    for v in Vi:
        velocidade = v

        if(C > 0):
            velocidade = velocidade + R
            C -= 1

        tempo += 1/velocidade

    print(f"{tempo:.2f}")