"""
@author: Jon Lebrero Catalina
"""

def load_muestra_lote(dicLotes):
    print("")
    print_muestra(dicLotes)
    print("")   
    
def load_muestra_invernadero(dicInvernaderos):
    print("")
    print_muestra(dicInvernaderos)
    print("")  
    
def load_muestra_asignada():
    print("")
    
def print_muestra(dic):
    for key, line in dic.items():
        print("\t", "-", key)
        for attribute, value in line.items():
            print("\t", "\t", "--", '{} : {}'.format(attribute, value))