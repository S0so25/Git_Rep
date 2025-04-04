
lista = []
i,media,numacima = 0,0,0


for i in range(0,10):
    while True:
        num = int(input(f"Insira a nota do aluno{i+1}: "))
        if num>=0 and num<=20:
            lista.append(num)
            break
        else:
            print("Esse valor não é valido")

for aluno in range(len(lista)):
    media+=lista[aluno]

media = media/len(lista)

print(f"A média é: {media}")
