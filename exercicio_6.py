"""Solicitar nome, e curso do aluno, emitir uma mensagem de boas
vindas, informar a grade de horário, solicitando o dia da semana, e
informar de acordo com a opção escolhida (nome da disciplina,
nome do professor e sala de aula). Usar sua grade horária como
referência."""
nome = input("digite o seu nome:")
curso = input("digite o seu curso:")

print("Seja Bem-Vindo", nome, "ao curso de", curso )

grade_horaria_ads = input("digite o dia da semana( de segunda a sexta):")

match grade_horaria_ads:
    case "segunda":
        print ("Aula de Desenvovimento Web, ministrada pelo professor Afonso, sala 9.2.LAB1")
    case "terça":
        print("Aula de Comunicação, ministrada pela professora Silvia, sala 5.2.16")
    case "quarta":
        print ("Aula de Gestão de Pessoas, ministrada pelo professor Gustavo, sala B4")
    case "quinta":
        print ("Aula de Programação, ministrada pelo professor Marco Sales, sala 9.2.LAB1 1")
    case "sexta":
        print ("Aula de Banco de Dados, ministrada pelo professor Israel, sala 9.2.LAB1")
        