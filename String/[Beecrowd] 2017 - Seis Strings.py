x = input()
K = int(input())


diferenca_final = 99
item = 0
for _ in range(5):
    texto = input()
    diff = 0
    for i in range(len(texto)):
        if texto[i] != x[i]:
            diff += 1

    if(diff < diferenca_final):
        diferenca_final = diff
        item = _ + 1

print(item)
print(diferenca_final)