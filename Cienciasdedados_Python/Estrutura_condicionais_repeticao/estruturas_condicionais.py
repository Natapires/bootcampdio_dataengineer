maior_idade = 18
idade_especial = 17


idade = int(input("Informe a sua idade: "))

if idade >= maior_idade:
    print("Maior de Idade, apropriado para tirar CNH. ")

if idade < maior_idade:
    print("Você é menor de idade, não pode tirar CNH. ")



if idade >= maior_idade:
    print("Maior de Idade, apropriado para tirar CNH. ")
else:
    print("Você é menor de idade, não pode tirar CNH. ")


if idade >= maior_idade:
    print("Maior de Idade, pode tirar CNH.")
elif idade == idade_especial:
    print("Pode fazer as aulas teóricas.")
else:
    print("Ainda não pode ter CNH")