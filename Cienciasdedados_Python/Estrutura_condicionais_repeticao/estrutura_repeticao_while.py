opcao = 1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato Bancário \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Retire o seu Extrato Bancário")    
else:
    print("Obrigado por usar nosso sistema Bancário, até mais!")