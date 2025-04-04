num = int(input("Insira um num: "))
contador = 0
for i in range(1,100):
    if num % i == 0:
        contador+=1

if contador == 2:
    print(f"O numero {num} é primo")
else:
    print(f"O numero {num} não é primo")