m, n = map(int, input().split())

R_Q = []

if(m > n):
    m, n = n, m

mdc = 0
while mdc == 0:
    lista = [n % m, n // m]
    R_Q.append(lista)
    if(n%m == 0):
        mdc = m
    else:
        n, m = m, n%m

A_B = [[1,0], [0,1]]
index = 0
for R, Q in R_Q:
    lista = [A_B[index][0] - (A_B[index+1][0] * Q), A_B[index][1] - (A_B[index+1][1] * Q)]
    A_B.append(lista)
    index += 1
print(R_Q)
print(A_B)