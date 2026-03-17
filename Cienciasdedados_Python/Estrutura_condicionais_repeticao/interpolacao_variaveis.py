nome = "Natã"
idade = 27
profissao = "Engenheiro de Software"
linguagem = "Python"
saldo = 45.435

people = {"nome": "Natã", "idade": 27, "profissao": "Engenheiro de Software"}

print("Olá, me chamo %s, tenho %d anos, atualmente atuo como %s com a linguagem de programação %s." % (nome, idade, profissao, linguagem))

print("Olá, me chamo {nome}, tenho {idade} anos, atualmente atuo como {profissao} com a linguagem de programação {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Nome: {1} Idade: {0} Profissão: {1} Linguagem: {1}".format(nome, idade, profissao, linguagem))

print("Nome: {nome} Idade: {idade} Profissão: {profissao}".format(**people))

print(f"Nome: {nome} Idade: {idade} Profissão: {profissao}")
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Saldo: {saldo:0.2f}")
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Saldo: {saldo:10.2f}")
