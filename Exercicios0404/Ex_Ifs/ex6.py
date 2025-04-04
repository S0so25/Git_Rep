

nome = input("Insira o seu nome: ")
valorcompra = int(input("Insira o valor da sua compra: "))

if valorcompra <= 200:
    percentual = 10
elif valorcompra <= 500:
    percentual = 15
else:
    percentual = 20

desconto_valor = valorcompra * (percentual/100)
valor_final = valorcompra - desconto_valor
    
print(f"Nome: {nome}, valor da compra: {valorcompra}, percentual: {percentual}, valor do desconto: {desconto_valor}, valor total a pagar: {valor_final}")