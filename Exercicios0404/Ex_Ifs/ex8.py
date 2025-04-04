
lista = []
i,media,numacima = 0,0,0


for i in range(1,11):
    while True:
        num = int(input(f"Insira a nota do aluno{i}: "))
        if num>=0 and num<=20:
            lista.append(num)
            break
        else:
            print("Esse valor não é valido")

for aluno in range(len(lista)-1):
    media+=lista[aluno]

media = media/len(lista)

for aluno in lista:
    if aluno >= media:
        numacima+=1

if media>=6:
    print(f"A média é de {media:.2f} e {numacima} estão acima da media")
else:
    print(f"A sua média é de {media:.2f} e {len(lista)-numacima} estão abaixo da média")
