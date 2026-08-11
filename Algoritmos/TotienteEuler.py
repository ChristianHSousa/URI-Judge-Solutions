def mdc(x,y):
    if x < y:
        x, y = y, x

    mdc = 0
    while mdc == 0:
        if(x%y == 0):
            mdc = y
        else:
            x, y = y, x % y

    return mdc

n = int(input())

totiente = 0
for i in range(1,n):
    if(mdc(n,i) == 1):
        totiente += 1

print(totiente)