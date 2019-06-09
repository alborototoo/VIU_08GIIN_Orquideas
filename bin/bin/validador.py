"""
@author: Jon Lebrero Catalina
"""

def validar_entero(texto):
    correcto = False
    variable = 0
    while(not correcto):
        try:
            variable = int(input(texto))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return variable

def validar_texto(texto):
    correcto = False
    variable = 0
    while(not correcto):
        try:
            variable = str(input(texto))
            correcto=True
        except ValueError:
            print('Error, introduce valor no nulo')
    return variable