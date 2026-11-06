"""Ler um número inteiro e obter o resto da divisão ( % 2) se o resto for
0 (Zero) é par, se for 1 (Ímpar)."""
numero = int(input("digite um numero para saber se é impar ou par:"))
if numero%2==0: #o simbolo % mostra o resto da divsão( e não é a divisão em si)
    print("O numero", numero, "é um numero par.")
else:
    print("O numero", numero, "é um numero impar.")
    