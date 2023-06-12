extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print('-=' * 20)
print('Descubra o número por extenso.')
print('-=' * 20)
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if n >= 0 and n <= 20:
        break
    print('Tente com um número de 0 a 20')
print('-=' * 20)
print(f'O número {n} por extenso é {extenso[n]}!')
