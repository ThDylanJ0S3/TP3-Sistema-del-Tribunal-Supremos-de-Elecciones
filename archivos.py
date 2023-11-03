################################################
#   Autor: Luis Aguilar y Dylan Meza           #
#   Fecha de creación: 1/11/2023  21:28 pm     #
#   Ultimo cambio: 04/10/2023 4:55 pm          #
#   Version: 3.11.4                            #
################################################
import pickle
from datetime import datetime
#from funciones import *

def graba(nomArchGrabar,lista):
    """
    Función: graba en un archivo binario
    Entrada:
        - nomArchGrabar (str): El nombre del archivo en el que se guardarán los datos.
        - lista (list): La lista de datos que se desea guardar en el archivo.
    Salida: None
    """
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        print("Archivo grabado: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
    return

def lee(nomArchLeer):
    """
    Función: lee un archivo binario
    Entrada:
        - nomArchLeer (str): El nombre del archivo que se desea leer.
    Salida:
        - lista (list): La lista de datos leída desde el archivo.
    """
    lista = []
    try:
        f=open(nomArchLeer,"rb")
        lista = pickle.load(f)
        print("Archivo leído: ", nomArchLeer)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return lista