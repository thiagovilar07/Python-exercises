from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print('-=' * 20)
print('Sorteei alguns números de um a Dez!')
print('-=' * 20)
print(f'Os valores sorteados foram {valores}')
print('-=' * 20)
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor Sorteado foi {min(valores)}')
print('-=' * 20)
