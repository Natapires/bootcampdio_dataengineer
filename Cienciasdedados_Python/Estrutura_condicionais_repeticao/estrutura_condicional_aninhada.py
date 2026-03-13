conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 2500
cheque_especial = 800

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
elif conta_especial:
    print("Conta especial selecionada.")
else:
    print("Sistema não reconheceu seu tipo de conta, contate seu gerente bancário.")