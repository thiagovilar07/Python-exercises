palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'ESTUDAR', 'MERCADO', 'FUTURO', 'PROGRAMADOR')
for p in palavras:
    print(f'\nAs vogais na palavra {p} são: ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
