
lista = []
i,media = 0,0


for i in range(1,4):
    while True:
        num = int(input(f"Insira o valor de num{i}: "))
        if num>=0 and num<=20:
            lista.append(num)
            break
        else:
            print("Esse valor não é valido")

for num in range(len(lista)-1):
    media+=lista[num]

media = media/len(lista)
if media>=6:
    print(f"A sua média é de {media} e está Aprovado")
else:
    print(f"A sua média é de {media} e está Reprovado")
