"""Exercico: Ler nome e idade e verificar se ele tem idade mínima para votar (16
anos), se sim, informar que ele precisa procurar um cartório eleitoral,
se não, informar que ele não tem idade mínima de acordo com a
legislação eleitora."""

nome = input("digite o seu nome:")
idade = int(input("digite a sua idade:"))

if idade >=16:
    print(nome, ", voce possui a maioridade para votar, procure o cartorio eleitoral mais proximo.")
else:
    print(nome, ", voce não possui idade minima de acordo com a legislação eleitoral para votar.")
