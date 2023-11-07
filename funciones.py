################################################
#   Autor: Luis Aguilar y Dylan Meza           #
#   Fecha de creación: 1/11/2023  21:28 pm     #
#   Ultimo cambio: 04/10/2023 4:55 pm          #
#   Version: 3.11.4                            #
################################################
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
