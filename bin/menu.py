"""
@author: Jon Lebrero Catalina
"""

import os

from lote import load_lote
from validador import validar_entero
from cargar import load_data
from guardar import save_data

def load_menu(dicLotes):
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
        load_menu(load_lote(dicLotes))
    elif menu == 2:
         print("Cargando Invernaderos")
         load_menu()
    elif menu == 3:
         print("Cargando Simular")
         load_menu()
    elif menu == 4:
         print("Cargando Información del sistema")
         load_menu()
    elif menu == 5:
         load_menu(load_data())
    elif menu == 6:
         load_menu(save_data(dicLotes))
    else:
         print("Gracias por usar Orquideas")