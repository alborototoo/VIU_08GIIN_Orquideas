"""
@author: Jon Lebrero Catalina
"""

import json

strFileNameLote = "file_lote"
strFileNameInvernadero = "file_invernadero"

def create_file():
    try:
        file = open(strFileNameLote,"a")
        file.close()
    except ValueError:
        print("")

def load_file():
    try:
        create_file()
        file = open(strFileNameLote,"r")
        dicLotes = json.load(file)
        print(dicLotes)
        file.close()
        return dicLotes
    except ValueError:
        print("")
        
def save_file(dicLotes):
    try:
        create_file()
        file = open(strFileNameLote,"a")
        file.write(json.dumps(dicLotes))
        file.close()
        return dicLotes
    except ValueError:
        print("")