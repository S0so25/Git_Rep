def numero_perfeito(n):
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    return soma_divisores == n

# Ler entrada do utilizador
limite = int(input("Insere um número: "))

contador = 0
print("Números perfeitos encontrados:")

for num in range(1, limite + 1):
    if numero_perfeito(num):
        print(num)
        contador += 1

print(f"\nTotal de números perfeitos até {limite}: {contador}")