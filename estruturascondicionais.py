"""
    Estruturas condicionais
    if

    else

    elif

"""

valor = True

if valor:
    print("true")
else:
    print("false")

valor = False
valor2 = False
if valor:
    print("true")
elif not valor and not valor2:
    print("Segunda condicao")
else:
    print("false")
