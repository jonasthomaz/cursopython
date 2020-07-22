"""
    Curso de Python
    Lidando com o tipo numérico em python
"""

# lidando com numeros inteiros
num = 10;
print(f'O numero informado e: {num}')
print(f'5+2: {5 + 2}')
print(f' 5 // 2 e: {5 // 2}')
print(f' 5 / 2 e: {5 / 2}')
print(f' 5%2 e: {5 % 2}')
print(f' 5**2 e: {5 ** 2}')

# o limite do python é a memoria
print(f' 5**1000 e: {5 ** 1000}')

# facilitando leitura
print(f' 1_000_000 e: {1_000_000}')

# lidando com pontos Flutuantes
print("\n\nlidando com float")
print(f'1.44 :{1, 44}')  # lida como se fosse uma tupla
print(f'1.44 :{1.44}')
print(f'1.44 * 3 :{1.44 * 3}')

valor1, valor2 = 1.33, 3.75
print(f'valor1: {valor1} - valor2: {valor2}')

print(f'valor1 com typecast: {int(valor1)}')
print(f'valor2 com typecast: {int(valor2)}')

print(f'Numeros Complexos : {2j}')
print(f'Numeros Complexos : {type(2j)}')
print(f'Numeros Complexos 2j**2 : {2j**2}')





# lidando com números Boleanos
print("\n\n\n\nBoleanos")
print(f'True: {True}')
print(f'False: {False}')
print(f'Negando True: {not True}')
print(f'Negando False: {not False}')
print("\n")
print(f'OR: (True or False): {True or False}')
print(f'OR: (True or True): {True or True}')
print(f'OR: (False or False): {False or False}')
print("\n")
print(f'AND: (True and False): {True and False}')
print(f'AND: (True and True): {True and True}')
print(f'AND: (False and False): {False and False}')


# LIdando com tipo string
print("\n\n\n\nLidando com strings")
# Aspas simples e triplas tambem é tratada como string
print(f'Meu nome:  {"jonas"}')
print(f'Meu nome:  {"""jonas"""}')

nome = 'Jonas Thomaz de Faria'
print(f'Meu nome:  {nome}')
print(nome.split())
print(nome.split()[0])
print(f'Pedaços do meu nome:  {nome[0]}')
print(f'Pedaços do meu nome:  {nome[0:5]}')
print(f'Pedaços do meu nome:  {nome[-5]}')

# <string>[<inicio>:<fim>:<extra>]
print(f'Pedaços do meu nome:  {nome[-5:]}')
print(f'Nome Invertido:  {nome[::-1]}')
print(f'Nome em minusculo invertido:  {nome.lower()[::-1]}')
print(f'Nome em maiusculo invertido:  {nome.upper()[::-1]}')
