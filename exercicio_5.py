"""Ler nome e idade do usuário e classificar em criança (até 12 anos),
adolescente (até 17 anos), adulto (até 64 anos) e idoso (acima de 65
anos)"""
nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade:"))

if idade<=12:
    print(nome, "é uma criança")
elif idade<=17:
    print(nome, "é uma adolescente")
elif idade<=64:
    print(nome, "é uma adulto")
else:
    print(nome, "é uma idoso")
