"""
@author: Jon Lebrero Catalina
"""

import os

from fichero import save_file

def save_data(strFileName, dic):
    os.system('cls')
    print("Modulo Guardar datos")
    print("")
    return save_file(strFileName, dic)