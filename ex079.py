print('-=' * 10)
print('LISTA DE VALORES')
print('-=' * 10)
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('este valor já está na lista.')
    else:
        lista.append(n)
    continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print('-=' * 10)
print(f'A lista que você digitou contém os seguintes valores {lista}')
