def operar(oper):
    numeros = []
    for x in range(2):
        numeros.append(input(f'digite n{x+1}: ')) 
    n1, n2 = numeros
    if n2 == '0' and oper == '/':
        print('Não existe divisão por 0')
    else:
        cal = n1 + str(oper) + n2
        print(f'{n1} {oper} {n2} = {eval(cal)}')

def menu():
    print('''
    CALCULADORA PYTHON
    Escolha uma das operações.
    
    0. Encerrar Programa.
    1. Soma.
    2. Subtração.
    3. Multiplicação.
    4. Divisão.
    5. Exponencial.
       ''' )
    
ops = {
    '1': '+',
    '2': '-',
    '3': '*',
    '4': '/',
    '5': '**',
}

op = None
while op != '0':
    menu()
    op = input('Operação: ')
    if op in ops:
        operar(ops[op])
    elif op != '0':
        print('Escolha uma opção válida.')

print('Encerrando programa...')
