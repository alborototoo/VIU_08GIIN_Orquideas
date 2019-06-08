"""
@author: Jon Lebrero Catalina
"""

import os

from fichero import save_file

def save_data(dicLotes):
    os.system('cls')
    print("Modulo Guardar datos")
    print("")
    return save_file(dicLotes)