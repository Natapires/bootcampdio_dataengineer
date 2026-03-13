def sacar(valor):
    saldo = 1000

    if saldo >= valor:
        print("Saque com sucesso!")
        print("Retire as células na boca do caixa abaixo.")
    
    print("Obrigado por utilizar o banco 24horas!")

def depositar(valor):
    saldo = 300
    saldo += valor

sacar(1700)