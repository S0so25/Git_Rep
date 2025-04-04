lista = []
media,i = 0, 0


while (i<=30):
    num = int(input("Insira um numero: "))
    if num>=1 and num <=50 and num % 2 == 0:
        lista.append(num)
        i+=1
    else:
        print("O numero não está entre 1 e 50 ou não é par")
    
for nmr in lista:
    media+=nmr

media= media / 30

print(f"A média é: {media}")