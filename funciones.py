################################################
#   Autor: Luis Aguilar y Dylan Meza           #
#   Fecha de creación: 1/11/2023  21:28 pm     #
#   Ultimo cambio: 04/10/2023 4:55 pm          #
#   Version: 3.11.4                            #
################################################
from clasePersona import *

def cerrarVentana(ventana):
    ventana.destroy()

def obtenerCedulaNombre(lista):
    listaCedulaNombre = []
    for persona in lista:
        listaCedulaNombre.append([persona.getCedula(),str(persona.getNombre())+" "+str(persona.getApellido1())+" "+str(persona.getApellido2())])
    return listaCedulaNombre   
        
def separarMujeres(lista):
    listaMujeres = []
    for persona in lista:
        if persona.getSexo() == "F":
            listaMujeres.append(persona)
    return listaMujeres

def separarHombres(lista):
    listaHombres = []
    for persona in lista:
        if persona.getSexo() == "M":
            listaHombres.append(persona)
    return listaHombres

