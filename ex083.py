print('-=' * 20)
print('VALIDADOR DE EXPRESSÕES MATEMÁTICAS')
print('-=' * 20)
expressao = str(input('Digite uma expressão matematica: '))
print('-=' * 20)
pilha = []
for parenteses in expressao:
    if '(' in parenteses:
        pilha.append(parenteses)
    elif ')' in parenteses:
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) > 0:
    print('Expressão inválida!')
    print('-=' * 20)
else:
    print('Expressão válida!')
    print('-=' * 20)
