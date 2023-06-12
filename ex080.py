lista = []
for valores in range(0, 5):
    numero = int(input('Digite um numero: '))
    if valores == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        posicao = 0
        while posicao <= len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
            posicao += 1
print('-=' * 15)
print(f'Esses foram os valores que voce digitou {lista}')
print('-=' * 15)
