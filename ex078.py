print('VERIFICADOR DE VALORES')
print('-=' * 20)
valores = []
maior = menor = 0
for valor in range(1, 6):
    valores.append(int(input(f'Digite o {valor}º valor: ')))
    print('-=' * 20)
    if valor == 1:
        maior = menor = valores[0]
for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print(f'O maior valor é {maior} nas posições', end=' ')
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f'{posicao + 1}', end=' ')
print(f'\nO menor valor é {menor} nas posições', end=' ')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao + 1}', end=' ')
