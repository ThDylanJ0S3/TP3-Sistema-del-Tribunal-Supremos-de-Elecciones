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

def registrarPersona():

    cedula = entryCitaProvincia.get() + "-" + entryCitaTomo.get() + "-" + entryCitaAsiento.get()
    nombre = entryNombre.get()
    apellidos = entryApellidos.get()
    sexo = varSexo.get()
    localidad = entryDistrito.get() + "," + entryCanton.get() + "," + entryProvincia.get()
    nacimiento = comboDias.get() + "/" + comboMeses.get() + "/" + comboAnnos.get()
    padre = comboPadre.get()
    nacionalidadPadre = comboNacionalidadPadre.get()
    madre = comboMadre.get()
    nacionalidadMadre = comboNacionalidadMadre.get()

    nuevaPersona = Persona(
        cedula=cedula,
        nombre=nombre,
        apellidos=apellidos,
        sexo=sexo,
        localidad=localidad,
        nacimiento=nacimiento,
        padre=padre,
        nacionalidadPadre=nacionalidadPadre,
        madre=madre,
        nacionalidadMadre=nacionalidadMadre

    )

    listaPersonas.append(nuevaPersona)
