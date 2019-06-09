"""
@author: Jon Lebrero Catalina
"""

import os

from lote import load_lote
from validador import validar_entero
from cargar import load_data
from guardar import save_data
from invernadero import load_invernadero
from informacion import load_informacion

strFileNameLote = "file_lote"
strFileNameInvernadero = "file_invernadero"

def load_menu(dicLotes, dicInvernaderos):
    os.system('cls')
    print("--- Orquideas ---")
    print("")
    print("  1 - Lotes de Orquídeas")
    print("  2 - Invernaderos")
    print("  3 - Simular")
    print("  4 - Información del sistema")
    print("  5 - Cargar datos")
    print("  6 - Guardar datos")
    print("")
    print("  0 - Salir")
    print("-----------------")
    menu = validar_entero("Opcion:")

    while(menu > 6): 
        print("El valor introducido no pertenece al pedido")
        menu = validar_entero("Opcion:")
         
    if menu == 1:
        dicLotes = load_lote(dicLotes)
        load_menu(dicLotes, dicInvernaderos)
    elif menu == 2:
         dicInvernaderos = load_invernadero(dicInvernaderos)
         load_menu(dicLotes, dicInvernaderos)
    elif menu == 3:
         print("Cargando Simular")
         load_menu(dicLotes, dicInvernaderos)
    elif menu == 4:
         load_informacion(dicLotes, dicInvernaderos)
         load_menu(dicLotes, dicInvernaderos)
    elif menu == 5:
        dicLotes = load_data(strFileNameLote)
        dicInvernaderos = load_data(strFileNameInvernadero)
        load_menu(dicLotes, dicInvernaderos)
    elif menu == 6:
        dicLotes = save_data(strFileNameLote, dicLotes)
        dicInvernaderos = save_data(strFileNameInvernadero, dicInvernaderos)
        load_menu(dicLotes, dicInvernaderos)
    else:
         print("Gracias por usar Orquideas")