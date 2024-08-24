nome = input("Nome: ")
disciplina = input("Disciplina: ")
nota = float(input("Nota: "))

if 0 <= nota <= 10:
    if 5.5<= nota <=5.9:
        nota = 6.0
    if nota >= 6.0:
        status = 'aprovado'
    else:
        status = 'reprovado'
    print(f"{nome} está {status} na matéria de {disciplina} com a nota: {nota}.")
else:
    print("Dados inválidos. Tente novamente.")