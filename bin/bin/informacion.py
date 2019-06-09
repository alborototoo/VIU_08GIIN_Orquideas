"""
@author: Jon Lebrero Catalina
"""

import os

from validador import validar_entero
from muestra_informacion import load_muestra_lote
from muestra_informacion import load_muestra_invernadero
from muestra_informacion import load_muestra_asignada

def load_informacion(dicLotes, dicInvernaderos):
    os.system('cls')
    print("Modulo Información del sistema")
    print("")
    print("  1 - Mostrar Lotes")
    print("  2 - Mostrar Invernaderos")
    print("  3 - Mostrar Invernaderos con Lotes")
    print("")
    print("  0 - Salir")
    print("-----------------")
    menu = validar_entero("Opcion:")
    
    while(menu > 3): 
        print("El valor introducido no pertenece al pedido")
        menu = validar_entero("Opcion:")
         
    if menu == 1:
        load_muestra_lote(dicLotes)
        load_informacion(dicLotes, dicInvernaderos)
    elif menu == 2:
         load_muestra_invernadero(dicInvernaderos)
         load_informacion(dicLotes, dicInvernaderos)
    elif menu == 3:
         load_muestra_asignada()
         load_informacion(dicLotes, dicInvernaderos)
    else:
         print("")