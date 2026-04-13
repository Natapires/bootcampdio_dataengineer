contatos = {
    "natapires@gmail.com": {"nome": "Natã Pires", "telefone": "5555-1235"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "98956-4585"},
    "andreymattos@gmail.com": {"nome": "Andrey Mattos", "telefone": "4321-1235"},
    "mariana@gmail.com": {"nome": "Mariana", "telefone": "1516-1218"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)