op = None

def menu():
    print("CALCULADORA PYTHON")
    print("Escolha uma operação:\n")
    print("0. Encerrar programa")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Exponenciação")
    print("")

def numeros():
    n1 = float(input("Digite n1: "))
    n2 = float(input("Digite n2: "))
    return n1, n2

def soma(n1, n2):
    print(f"{n1} + {n2} = {n1+n2}")

def sub(n1, n2):
    print(f"{n1} - {n2} = {n1-n2}")

def mult(n1, n2):
    print(f"{n1} x {n2} = {n1*n2}")

def div(n1, n2):
    if n2 == 0:
        print("Não existe divisão por 0")
    else:
        print(f"{n1} ÷ {n2} = {n1/n2}")

def exp(n1, n2):
    print(f"{n1} elevado a {n2} = {n1**n2}")

ops = ["1","2","3","4","5"]

while op != "0":
    print("")
    menu()
    op = input("Operação: ")
    if op in ops:
        n1, n2 = numeros()
        if (op == "1"):
            soma(n1, n2)
        elif (op == "2"):
            sub(n1, n2)
        elif (op == "3"):
            mult(n1, n2)
        elif (op == "4"):
            div(n1, n2)
        elif (op == "5"):
            exp(n1, n2)
    elif op != "0":
        print("Essa opção não existe. Escolha uma das opções a partir dos seus respectivos números.")
print("Encerrando programa...")