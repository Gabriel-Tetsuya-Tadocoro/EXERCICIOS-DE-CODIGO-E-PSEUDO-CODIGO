"""Ler nome e idade do usuário, verificar se ele tem idade para acesso
a plataforma de apostas (idade>=18)"""
nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade:"))

if idade>=18:
    print(nome, ". Acesso liberado")
else:
    print(nome, ". Acesso negado")
