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
        """ help for my function """
        return valor_um + 1

    def incrementadois(valor_um):
        """
            help da minha funcao
            asdgaas
            asdasdasd
            ads
        """
        return valor_um + 2


calc = CalculadoraTeste
print(help(calc.incrementadois))