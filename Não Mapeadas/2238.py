a,b,c,d = map(int, input().split())
if(a > c):
    c, a = a, c

X = a
Y = c

mdc = 0
while mdc == 0:
    if (c%a == 0):
        mdc = a
    else:
        c, a = a, c % a

mmc = (X*Y) // mdc
for i in range(X,mmc//X):
    x = X*i
    if(x%b != 0) and (d%x != 0):
        print(x)
        break