# 1435

def impl1():
    while True:
        entrada = int(input())

        if(entrada == 0):
            break

        max_num = (entrada+1) //2 + 1

        M = [[1] * entrada for _ in range(entrada)]

        for val in range(2,max_num):
            for i in range(val-1,entrada-(val-1)):
                for j in range(val-1,entrada-(val-1)):
                    M[i][j] = val


        for l in M:
            #for i in l:
            #    print(f"{i:>3}",end='')
            #print()
            print("".join(f"{x:3d}" for x in l))
        print()

while True:
    entrada = int(input())

    if (entrada == 0):
        break

    for i in range(entrada):
        for j in range(entrada):
            print("".join(f"{min(min(entrada - i - 1, entrada - j - 1),min(i,j)) + 1:3d}"),end="")
        print()
    print()
    #for l in matriz:


