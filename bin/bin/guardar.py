"""
@author: Jon Lebrero Catalina
"""

from fichero import save_file

def save_data(strFileName, dic):
    if len(dic) == 0:
        return dic
    return save_file(strFileName, dic)