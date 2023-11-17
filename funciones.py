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
    """
    Función: Obtiene una lista de pares de cédula y nombre completo de personas.

    Esta función recibe una lista de objetos que contienen información de personas registradas y devuelve una lista de listas, donde cada sublista contiene la cédula y el nombre completo de cada persona.

    - Entrada:
        - lista: Lista de objetos que contienen información de las personas registradas.

    - Salida:
        - listaCedulaNombre: Lista de listas, donde cada sublista contiene la cédula y el nombre completo de cada persona.

    - Acciones:
        - Itera sobre la lista de personas.
        - Para cada persona en la lista, crea una sublista que contiene la cédula y el nombre completo (nombre, apellido1 y apellido2 concatenados) de la persona.
        - Agrega cada sublista a una lista general.
        - Devuelve la lista de listas que contiene la cédula y el nombre completo de cada persona.
    """
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

