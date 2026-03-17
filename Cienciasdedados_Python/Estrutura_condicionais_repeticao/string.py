nome = "NaTã"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "    Bootcamp Engenharia de Dados!  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Programação"

print("####" + menu + "####")
print(menu.center(12))
print(menu.center(12, "#"))
print("P-y-t-h-o-n")

for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu))