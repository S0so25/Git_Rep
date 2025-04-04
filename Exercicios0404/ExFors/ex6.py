lista = []

for i in range(1,11):
    contador = 0
    for h in range(1,11):
        if i % h == 0:
            contador+=1

    if contador == 2:
        lista.append(i)


for num in lista:
    print(num)