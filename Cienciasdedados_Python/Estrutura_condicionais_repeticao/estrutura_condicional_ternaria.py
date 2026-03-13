saldo = 3000
saque = 800

status = "Sucesso" if saldo >= saque else "Falha"

print(f" {status} ao realizar o saque! ")