lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-=' * 20)
print(f'{"TABELA DE PREÇOS":^35}')
print('-=' * 20)
for material in range(0, len(lista)):
    if material % 2 == 0:
        print(f'{lista[material]:.<30}', end='')
    else:
        print(f'R${lista[material]:>7.2f}')
print('-=' * 20)
