"""
    Falando sobre escopo de variaveis

    variaveis Globais
        Seu escopo compreende o codigo completo

    variaveis Locai
        Seu escopo é somento o bloco declarado

"""

valor = 10


def funcao():
    valor = 5
    print(f'Meu valor e: {valor}')


funcao()
print(f'Meu valor e: {valor}')
