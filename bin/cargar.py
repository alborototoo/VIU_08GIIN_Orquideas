"""
@author: Jon Lebrero Catalina
"""

import os

from fichero import load_file

def load_data(strFileName):
    os.system('cls')
    print("Modulo Cargar datos")
    print("")
    return load_file(strFileName)