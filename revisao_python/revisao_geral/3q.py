nome = input("digite seu nome: ")
idade = int(input("digite seu idade: "))
if (idade < 16):
    print(f"{nome} não está apto(a) para votar")
else:
    print(f"{nome} está apto(a) para votar")
