lista = []
for num in range(0,3):
    num = int(input("Insira um nmr1: "))
    lista.append(num)

maior = lista[0]
menor = lista[0]


for num in lista:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num


print(f"Maior: {maior}, menor: {menor}")