num = int(input("Insira um numero: "))
soma, multiplicacao = 0,1
divisao, subtracao = num, num

for i in range(1,num+1):
    soma+=i
    multiplicacao*=i

for h in range(num,0,-1):
    divisao /= h
    subtracao-=h


print(f"Soma: {soma:.2f}")
print(f"Divisao: {divisao:.2f}")
print(f"Multiplicacao: {multiplicacao:.2f}")
print(f"Subtracao: {subtracao:.2f}")