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

for num in lista:
    if num != maior and num != menor:
        meio = num

        
decrescente = [maior, meio, menor]
crescente = [menor, meio, maior]
print(f"Crescente: {crescente}, Decrescente: {decrescente}")