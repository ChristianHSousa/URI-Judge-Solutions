n, p = map(int, input().split())

dividendo = 1
divisor = 1
if n == p:
    print("1")
else:
    comum = n - p
    while max(comum,p) < n:
        dividendo *= n
        n -= 1
    menor = min(comum,p)
    while menor > 1:
        divisor *= menor
        menor -= 1

print(dividendo)
print(divisor)
print(dividendo/divisor)