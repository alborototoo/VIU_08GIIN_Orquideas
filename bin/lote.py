"""
@author: Jon Lebrero Catalina
"""

import os

from validador import validar_entero
from validador import validar_texto

def load_lote(dicLotes):
    os.system('cls')
    print("Modulo Lotes de Orquídeas")
    print("")
    
    strLote = validar_texto("Lote:")
    while strLote in dicLotes:
        print("El Lote ya existe. Introduzca un nuevo lote")
        strLote = validar_texto("Lote:")
        
    intCantidadPlanta = validar_entero("Cantidad Planta:")
    
    strClima = validar_texto("Clima(Andes o Costa):")
    while(strClima.capitalize() != 'Andes' and strClima.capitalize() != 'Costa'):
        print("El valor introducido no pertenece al pedido")
        intContinuar = validar_texto("Clima(Andes o Costa):")
        
    intDiasAndes = validar_entero("Dias Andes:")
    
    intDiasCosta = validar_entero("Dias Costa:")
    
    dicLotes[strLote] = {
          'Cantidad Plantas':intCantidadPlanta,
          'Clima':strClima,
          'Dias Andes':intDiasAndes,
          'Dias Costa':intDiasCosta
    }     
    print(dicLotes)
    
    intContinuar = validar_entero("¿Introducir Lote adicional(1) o Salir(0)?:")
    while(intContinuar != 1 and intContinuar != 0): 
        print("El valor introducido no pertenece al pedido")
        intContinuar = validar_entero("¿Introducir Lote adicional(1) o Salir(0)?:")
    
    if intContinuar == 1 :
        load_lote(dicLotes)
        
    return dicLotes