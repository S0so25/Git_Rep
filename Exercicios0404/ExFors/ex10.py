
num = int(input("insira um num: "))
divisor = 0
for i in range(1,1000):
    if num % i == 0:
        divisor+=1

    
print(f"O numero {num} tem {divisor}")