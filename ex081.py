print('-=' * 20)
print('ANALISE DE NUMEROS')
valores = []
print('-=' * 20)
while True:
    valores.append(int(input('Digite um valor: ')))
    print('-=' * 20)
    continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    print('-=' * 20)
    if continuar == 'N':
        break
print(f'A quantidade de valores digitados: {len(valores)}')
print('-=' * 20)
valores.sort(reverse=True)
print(f'Os valores ordenados de forma decrescente: {valores}')
print('-=' * 20)
if 5 in valores:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')
print('-=' * 20)
