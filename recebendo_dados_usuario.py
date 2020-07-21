"""
    recebendo dados do usuario
"""
# input de dados
print("Qual seu Nome?")
nome = input()

# Exemplo da versão 2 do python
# print("Bem vindo: %s" % (nome))
print("Bem vindo: {0}".format(nome))
print(f'bem vindo ao python 3.7 {nome}')

idade = input("Qual a sua idade?")

# Saida dos dados
# Exemplo da versão 2 do python
# print("A pessoa: %s tem %s anos." % (nome, idade))
print("A pessoa: {0} tem {1} anos.".format(nome, idade))

# int fazendo o type cast do tipo string
print(f'A pessoa: {nome} tem {idade} anos, nasceu em  {2020 - int(idade)}')
