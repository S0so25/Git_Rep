nomes = []
i=0
while True:

    num = int(input("1- Adicionar Pessoas\n2- ListarPessoas\n3- Apagar pessoas\nOpçao: "))

    match(num):
        case 1:
            nome = input("Insira o seu nome: ")
            palavra = ""
            checar = []
            for caractere in nome:
                if caractere != ' ':
                    palavra+=caractere
                else:
                    if palavra != "":
                        checar.append(palavra)
                        palavra = ""

            if palavra != "":
                checar.append(palavra)

            if len(checar) < 2:
                print("Insira o primeiro e o ultimo nome")

            if (65 <= ord(checar[0][0]) <= 90) and (65 <= ord(checar[1][0]) <= 90):
                idade = int(input("Insira a idade: "))
                if idade <= 0 or idade >= 115:
                    print("Idade invalida")
                else:
                    nomes.append([nome,idade])
            else:
                print("O nome não está correto. O primeiro e o último nome devem começar com letra maiúscula.")
        
            if nome.upper() ==  "SAIR":
                break
        case 2:
            for item in nomes:
                    print(f"Nome: {item[0]}\nIdade: {item[1]}")

        case 3:
            nome_input = input("Insira o primeiro ou último nome que deseja apagar: ")

            i = 0
            while i < len(nomes):
                nome_completo = nomes[i][0]

                primeiro_nome = ""
                for char in nome_completo:
                    if char != ' ':
                        primeiro_nome += char
                    else:
                        break  

                ultimo_nome = ""
                for char in reversed(nome_completo):
                    if char != ' ':
                        ultimo_nome = char + ultimo_nome
                    else:
                        break  

               
                if nome_input == primeiro_nome or nome_input == ultimo_nome:
                    nomes.remove(nomes[i])  
                    break  
                else:
                    i += 1  


    if nome.upper() ==  "SAIR":
        break
    

