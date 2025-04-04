
while(True):
    saldo_inicial = int(input("Insira o seu saldo: "))
    cheque = int(input("Insira o cheque: "))
    if cheque > saldo_inicial:
        print("Não consegue debitar esse valor do seu saldo")
    else:
        print(f"O seu saldo atual é: {saldo_inicial - cheque}")
