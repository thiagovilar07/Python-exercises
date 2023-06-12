print('-=' * 20)
print('LISTAS EM PAR OU ÍMPAR')
print('-=' * 20)
todos = []
par = []
impar = []
while True:
    todos.append(int(input('Digite um valor: ')))
    print('-=' * 20)
    continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    print('-=' * 20)
    if continuar == 'N':
        break
for numeros in todos:
    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)
print('-=' * 20)
print(f'Todos os valores digitados foram: {todos}')
print(f'Todos os valores pares foram: {par}')
print(f'Todos os valores ímpares foram: {impar}')
print('-=' * 20)