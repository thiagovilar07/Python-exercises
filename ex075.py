from time import sleep
n = (int(input('Digite o primeiro valor: ')),
     int(input('Digite o segundo valor: ')),
     int(input('Digite o terceiro valor: ')),
     int(input('Digite o quarto valor: ')))
print('-=' * 20)
print('Vou analisar os valores digitados...')
sleep(1)
if 9 in n:
    print('-=' * 20)
    print(f'O número nove apareceu {n.count(9)} vezes.')
else:
    print('-=' * 20)
    print('O número nove não apareceu.')
sleep(1)
if 3 in n:
    print('-=' * 20)
    print(f'O número três apareceu pela primeira vez na {n.index(3) + 1}ª posição.')
else:
    print('-=' * 20)
    print('O número três não apareceu.')
sleep(1)
print('-=' * 20)
print('Os valores pares são:', end=' ')
for par in n:
    if par % 2 == 0:
        print(par, end=' ')
print('-=' * 20)
