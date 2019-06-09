"""
@author: Jon Lebrero Catalina
"""

import os

from validador import validar_entero
from validador import validar_texto

def load_invernadero(dicInvernaderos):
    os.system('cls')
    print("Modulo Invernaderos")
    print("")
    
    strInvernadero = validar_texto("Invernadero:")
    while strInvernadero in dicInvernaderos:
        print("El Lote ya existe. Introduzca un nuevo invernadero")
        strInvernadero = validar_texto("dicInvernaderos:")
    
    strClima = validar_texto("Clima(Andes o Costa):")
    while(strClima.capitalize() != 'Andes' and strClima.capitalize() != 'Costa'):
        print("El valor introducido no pertenece al pedido")
        intContinuar = validar_texto("Clima(Andes o Costa):")
        
    intCapacidad = validar_entero("Capacidad:")
    
    dicInvernaderos[strInvernadero] = {
          'Clima':strClima.lower().capitalize(),
          'Capacidad':intCapacidad,
          'Lote:':""
    }     
    
    intContinuar = validar_entero("¿Introducir Invernadero adicional(1) o Salir(0)?:")
    while(intContinuar != 1 and intContinuar != 0): 
        print("El valor introducido no pertenece al pedido")
        intContinuar = validar_entero("¿Introducir Invernadero adicional(1) o Salir(0)?:")
    
    if intContinuar == 1 :
        load_invernadero(dicInvernaderos)
        
    return dicInvernaderos