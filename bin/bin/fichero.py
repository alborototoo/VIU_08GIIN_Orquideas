"""
@author: Jon Lebrero Catalina
"""

import json

def create_file(strFileName):
    try:
        file = open(strFileName,"a")
        file.close()
    except ValueError:
        print(ValueError)

def load_file(strFileName):
    try:
        create_file(strFileName)
        file = open(strFileName,"r")
        dicLotes = json.load(file)
        file.close()
        return dicLotes
    except ValueError:
        print(ValueError)
        
def save_file(strFileName, dic):
    try:
        create_file(strFileName)
        file = open(strFileName,"a")
        file.write(json.dumps(dic))
        file.close()
        return dic
    except ValueError:
        print(ValueError)