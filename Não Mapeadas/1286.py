while True:
    N = int(input())
    P = int(input())
    if N == 0:
        break
    pedidos = []
    for i in range(N):
        pedidos.append(list(map(int, input().split())))

    pedidos.sort(key=lambda x: (x[0], -x[1]))
    print(pedidos)
    pizzas = 0
    tempo = 0
    for i in range(N):
        if(P >= pizzas + pedidos[i][1]):
            pizzas += pedidos[i][1]
            tempo += pedidos[i][0]

    print(tempo)
    print(pizzas)