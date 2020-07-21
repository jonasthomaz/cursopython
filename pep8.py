"""
PEP8 - Apenas treinamento de Padr

[1] - Camel case em nomes de Classes
[2] - Utilize nomes em minusculo, separados por underline para funcoes ou variaveis
"""


class Calculadora:
    pass


class CalculadoraTeste(Calculadora):
    pass

    @staticmethod
    def incrementa(valor_um):
        return valor_um + 1