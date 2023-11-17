################################################
#   Autor: Luis Aguilar y Dylan Meza           #
#   Fecha de creación: 1/11/2023  21:28 pm     #
#   Ultimo cambio: 04/10/2023 4:55 pm          #
#   Version: 3.11.4                            #
################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from clasePersona import *
import datetime
from funciones import *
from archivos import *

global annos
global listaPersonas
global listaCedulas
global listaHombres
global listaMujeres
global provincia
global registroPersonas
listaPersonas = lee("PadresOriginales")
listaCedulasNombre = obtenerCedulaNombre(listaPersonas)
listaHombres = separarHombres(listaPersonas)
listaMujeres = separarMujeres(listaPersonas)
provincia = ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
registroPersonas = listaPersonas
annoActual = datetime.now().year
annos = [str(i) for i in range(1900, annoActual + 1)]
Variablesexo = "M"

def mostrarArbolGenealogico():
	"""
    Función: Abre una ventana para mostrar el árbol genealógico.
    
    Esta función crea una interfaz gráfica utilizando Tkinter para mostrar información del árbol genealógico.

    Ventana:
        - Título: "Árbol Genealógico"
        - Tamaño: 600x400 píxeles
        - No es redimensionable
        - Fondo: gris claro

    Componentes de la interfaz:
        - Etiqueta "Mostrar Árbol Genealógico" en fuente Arial de tamaño 17.
        - Etiqueta "Persona:" en fuente Arial de tamaño 12.
        - Cuadro combinado para seleccionar una persona.
        - Etiqueta "Resultado de la búsqueda:" en fuente Arial de tamaño 12.
        - Entradas de solo lectura para mostrar el padre, la madre y el hijo.
        - Botón "Mostrar" para realizar la búsqueda y mostrar la información.
        - Botón "Limpiar" para borrar la información mostrada.
        - Botón "Regresar" para cerrar la ventana.

    Funcionalidades:
        - El botón "Mostrar" activa una búsqueda y muestra la información correspondiente a la persona seleccionada.
        - El botón "Limpiar" borra la información mostrada en las entradas.
        - El botón "Regresar" cierra la ventana del árbol genealógico.

    Variables globales utilizadas:
        - listaPersonas: Lista de personas.
        - listaCedulas: Lista de cédulas de personas.

    """   
	ventanaArbolGenealogico = tk.Tk()
	ventanaArbolGenealogico.title("Ventana de registro")
	ventanaArbolGenealogico.geometry("600x400")
	ventanaArbolGenealogico.resizable(width=False, height=False)
	ventanaArbolGenealogico.configure(bg="light gray")
	ventanaArbolGenealogico.columnconfigure(0, weight=1)
	ventanaArbolGenealogico.columnconfigure(2, weight=1)
 
	global listaPersonas
	global listaCedulas
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelArbol = tk.Label(ventanaArbolGenealogico, text="Mostrar Árbol Genealógico", font=("Arial", 17), bg="light gray")
	labelArbol.place(x=150, y=20)

	labelPersona = tk.Label(ventanaArbolGenealogico, text="Persona:", font=("Arial", 12), bg="light gray")
	labelPersona.place(x=40, y=70)

	comboPersona = ttk.Combobox(ventanaArbolGenealogico, values=listaCedulasNombre, font=("Arial", 16))
	comboPersona.place(x=140, y=70)


	labelResultado = tk.Label(ventanaArbolGenealogico, text="Resultado de la búsqueda: ", font=("Arial", 12), bg="light gray")
	labelResultado.place(x=40, y=201)	

	entryPadreMostrar = tk.Entry(ventanaArbolGenealogico, width=14, font=("Arial", 16), state="disabled")
	entryPadreMostrar.place(x=100, y=236)

	entryMadreMostrar = tk.Entry(ventanaArbolGenealogico, width=14, font=("Arial", 16), state="disabled")
	entryMadreMostrar.place(x=310, y=236)

	entryHijo = tk.Entry(ventanaArbolGenealogico, width=14, font=("Arial", 16), state="disabled")
	entryHijo.place(x=207, y=330)
 
	def mostrarResultadoBusqueda():
		"""
	    Función: Realiza una búsqueda y muestra el árbol genealógico de una persona seleccionada.

	    Esta función recoge la selección de una persona en la interfaz gráfica y busca su información en la lista de personas.
	    Después, muestra el árbol genealógico de esa persona en las entradas correspondientes.

	    Funcionalidades:
	        - Obtiene la persona seleccionada del cuadro combinado.
	        - Busca la información de la persona en la lista de personas.
	        - Muestra el árbol genealógico de la persona en las entradas respectivas.
	        - Deshabilita el botón "Mostrar" y habilita el botón "Limpiar".

	    Variables utilizadas (globales):
	        - listaPersonas: Lista de personas.
	        - comboPersona: Cuadro combinado que contiene la lista de personas.
	        - entryHijo: Entrada para mostrar el nombre del hijo.
	        - entryMadreMostrar: Entrada para mostrar el nombre de la madre.
	        - entryPadreMostrar: Entrada para mostrar el nombre del padre.
	        - botonMostrar: Botón para iniciar la búsqueda.
	        - botonLimpiar: Botón para limpiar la información mostrada.

    	"""
		hijo = comboPersona.get()
		for persona in registroPersonas:
			if hijo[0:11] == persona.getCedula():
				entryHijo.config(state="normal", width=len(hijo[12:]))
				entryMadreMostrar.config(state="normal", width=len(persona.getMadre())+1)
				entryPadreMostrar.config(state="normal", width=len(persona.getPadre())+1)
				entryHijo.insert(0,hijo[13:-1])
				entryMadreMostrar.insert(0,str(persona.getMadre()))
				entryPadreMostrar.insert(0,str(persona.getPadre()))
				entryHijo.config(state="disabled")
				entryMadreMostrar.config(state="disabled")
				entryPadreMostrar.config(state="disabled")
				botonMostrar.config(state="disabled")
				botonLimpiar.config(state="normal")
 
	botonMostrar = tk.Button(ventanaArbolGenealogico, text="Mostrar", width=12, height=2, font=("Arial", 12), command=mostrarResultadoBusqueda)
	botonMostrar.place(x=140, y=131)

	def limpiarEntradas():
		"""
	    Función: Limpia las entradas de la interfaz gráfica del árbol genealógico.

	    Esta función restablece las entradas de la interfaz gráfica del árbol genealógico
	    para dejarlas en su estado inicial, desactivando la edición y borrando los contenidos.

	    Acciones realizadas:
	        - Habilita las entradas para edición con un ancho de 14 caracteres.
	        - Borra el contenido de las entradas.
	        - Desactiva la edición de las entradas.
	        - Deshabilita el botón "Limpiar".
	        - Habilita el botón "Mostrar".

	    Variables utilizadas (globales):
	        - entryHijo: Entrada para mostrar el nombre del hijo.
	        - entryMadreMostrar: Entrada para mostrar el nombre de la madre.
	        - entryPadreMostrar: Entrada para mostrar el nombre del padre.
	        - botonLimpiar: Botón para limpiar la información mostrada.
	        - botonMostrar: Botón para iniciar la búsqueda.

	    """
		entryHijo.config(state="normal", width=14)
		entryMadreMostrar.config(state="normal", width=14)
		entryPadreMostrar.config(state="normal", width=14)
		entryHijo.delete(0,tk.END)
		entryMadreMostrar.delete(0,tk.END)
		entryPadreMostrar.delete(0,tk.END)
		entryHijo.config(state="disabled")
		entryMadreMostrar.config(state="disabled")
		entryPadreMostrar.config(state="disabled")
		botonLimpiar.config(state="disabled")
		botonMostrar.config(state="normal")
  
	botonLimpiar = tk.Button(ventanaArbolGenealogico, text="Limpiar", width=12, height=2, font=("Arial", 12), state="disabled", command=limpiarEntradas)
	botonLimpiar.place(x=280, y=131)

	botonRegresar = tk.Button(ventanaArbolGenealogico, text="Regresar", width=12, height=2, font=("Arial", 12), command=ventanaArbolGenealogico.destroy)
	botonRegresar.place(x=420, y=131)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #	
def ventanaDeRegistroNacimiento():
	"""
    Función: Crea una interfaz para registrar información de un nacimiento.

    Esta función crea una interfaz gráfica utilizando Tkinter para registrar información
    relacionada con el nacimiento de una persona, incluyendo datos personales, padres y más.

    Elementos de la interfaz:
        - Campos para la cita de nacimiento.
        - Campos para el nombre y apellidos.
        - Selección de sexo mediante radio botones.
        - Campos para la ubicación (distrito, cantón, provincia).
        - Selección de fecha de nacimiento.
        - Selección del padre y la madre.
        - Selección de la nacionalidad de los padres.
        - Botones para registrar, limpiar y regresar.

    Acciones:
        - Permite ingresar datos relacionados con el nacimiento.
        - Valida la cédula y otros campos antes de registrar.
        - Muestra mensajes de error en caso de datos incorrectos o faltantes.
        - Almacena la información ingresada en una lista de registros.

    Variables utilizadas (globales):
        - annos: Lista de años para selección.
        - provincia: Lista de provincias para selección.
        - listaHombres: Lista de hombres registrados.
        - listaMujeres: Lista de mujeres registradas.
        - Variablesexo: Variable global para almacenar el sexo seleccionado.

    """
	ventanaRegistroNacimiento = tk.Tk()
	ventanaRegistroNacimiento.title("Ventana de registro")
	ventanaRegistroNacimiento.geometry("570x820")
	ventanaRegistroNacimiento.resizable(width=False, height=False)
	ventanaRegistroNacimiento.configure(bg="light gray")
	ventanaRegistroNacimiento.columnconfigure(0, weight=1)
	ventanaRegistroNacimiento.columnconfigure(2, weight=1)
	global annos
	global provincia
	global listaHombres
	global listaMujeres
	global Variablesexo
 
	nacionalidades = ["Costarricense","Mexicana","Española","Argentina","Colombiana"]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCita = tk.Label(ventanaRegistroNacimiento, text="Cita:", font=("Arial", 12), bg="light gray")
	labelCita.grid(row=0, column=0, pady=13)

	entryCitaProvincia = tk.Entry(ventanaRegistroNacimiento, width=3, font=("Arial", 16))
	entryCitaProvincia.place(x=156, y=13)

	labelGuion = tk.Label(ventanaRegistroNacimiento, text="-", font=("Arial", 16), bg="light gray")
	labelGuion.place(x=201, y=13)
         
	entryCitaTomo = tk.Entry(ventanaRegistroNacimiento, width=6, font=("Arial", 16))
	entryCitaTomo.place(x=220, y=13)

	labelGuion = tk.Label(ventanaRegistroNacimiento, text="-", font=("Arial", 16), bg="light gray")
	labelGuion.place(x=300, y=13)

	entryCitaAsiento = tk.Entry(ventanaRegistroNacimiento, width=6, font=("Arial", 16))
	entryCitaAsiento.place(x=319, y=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelNombre = tk.Label(ventanaRegistroNacimiento, text="Nombre:", font=("Arial", 12), bg="light gray")
	labelNombre.grid(row=1, column=0, pady=13)

	entryNombre = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryNombre.grid(row=1, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelApellidos = tk.Label(ventanaRegistroNacimiento, text="Apellidos:", font=("Arial", 12), bg="light gray")
	labelApellidos.grid(row=2, column=0, pady=13)

	entryApellidos = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16), state="disabled")
	entryApellidos.grid(row=2, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelSexo = tk.Label(ventanaRegistroNacimiento, text="Sexo:", font=("Arial", 12), bg="light gray")
	labelSexo.grid(row=3, column=0, pady=13)

	def asignarSexo(sexo):
		"""
	    Función: Asigna el sexo seleccionado a una variable global.

	    Esta función se utiliza para asignar el sexo seleccionado (femenino o masculino)
	    a una variable global llamada Variablesexo.

	    Argumentos:
	        - sexo (str): El sexo seleccionado ("F" para femenino, "M" para masculino).

	    Variables utilizadas (globales):
	        - Variablesexo: Variable global para almacenar el sexo seleccionado.

	    """
		global Variablesexo
		Variablesexo = sexo
  
	radioFemenino = tk.Radiobutton(ventanaRegistroNacimiento, text="Femenino",variable=Variablesexo ,value="F", font=("Arial", 15), bg="light gray", command=lambda: asignarSexo("F"))
	radioFemenino.place(x=294, y=166)

	radioMasculino = tk.Radiobutton(ventanaRegistroNacimiento, text="Masculino",variable=Variablesexo ,value="M", font=("Arial", 15), bg="light gray", command=lambda: asignarSexo("M"))
	radioMasculino.place(x=152, y=166)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelDistrito = tk.Label(ventanaRegistroNacimiento, text="Distrito:", font=("Arial", 12), bg="light gray")
	labelDistrito.grid(row=4, column=0, pady=13)

	entryDistrito = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryDistrito.grid(row=4, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCanton = tk.Label(ventanaRegistroNacimiento, text="Cantón:", font=("Arial", 12), bg="light gray")
	labelCanton.grid(row=5, column=0, pady=13)

	entryCanton = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryCanton.grid(row=5, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelProvincia = tk.Label(ventanaRegistroNacimiento, text="Provincia:", font=("Arial", 12), bg="light gray",)
	labelProvincia.grid(row=6, column=0, pady=13)

	comboProvincia = ttk.Combobox(ventanaRegistroNacimiento,values=provincia, width=21, font=("Arial", 16), state="disabled")
	comboProvincia.grid(row=6, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelDia = tk.Label(ventanaRegistroNacimiento, text="Dia:", font=("Arial", 12), bg="light gray")
	labelDia.grid(row=7, column=0, pady=13)

	dias = [str(i) for i in range(1,32)]
	comboDias = ttk.Combobox(ventanaRegistroNacimiento, values=dias, font=("Arial", 16), state="readonly")
	comboDias.grid(row=7, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelMeses = tk.Label(ventanaRegistroNacimiento, text="Mes:", font=("Arial", 12), bg="light gray")
	labelMeses.grid(row=8, column=0, pady=13)

	meses = [str(i) for i in range(1,13)]
	comboMeses = ttk.Combobox(ventanaRegistroNacimiento, values=meses, font=("Arial", 16), state="readonly")
	comboMeses.grid(row=8, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelAnnos = tk.Label(ventanaRegistroNacimiento, text="Año:", font=("Arial", 12), bg="light gray")
	labelAnnos.grid(row=9, column=0, pady=13)

	comboAnnos = ttk.Combobox(ventanaRegistroNacimiento, values=annos, font=("Arial", 16), state="readonly")
	comboAnnos.grid(row=9, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelPadre = tk.Label(ventanaRegistroNacimiento, text="Padre:", font=("Arial", 12), bg="light gray")
	labelPadre.grid(row=10, column=0, pady=13)

	lHombres = [str(str(persona.getNombre())+" "+str(persona.getApellido1())+" "+str(persona.getApellido2())) for persona in listaHombres]
	comboPadre = ttk.Combobox(ventanaRegistroNacimiento, values=lHombres, font=("Arial", 16), state="readonly")
	comboPadre.grid(row=10, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelNacionalidadPadre = tk.Label(ventanaRegistroNacimiento, text="Nacionalidad:", font=("Arial", 12), bg="light gray")
	labelNacionalidadPadre.grid(row=11, column=0, pady=13)

	comboNacionalidadPadre = ttk.Combobox(ventanaRegistroNacimiento, values=nacionalidades, font=("Arial", 16),state="disabled")
	comboNacionalidadPadre.grid(row=11, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelMadre = tk.Label(ventanaRegistroNacimiento, text="Madre:", font=("Arial", 12), bg="light gray")
	labelMadre.grid(row=12, column=0, pady=13)

	lMujeres = [str(str(persona.getNombre())+" "+str(persona.getApellido1())+" "+str(persona.getApellido2())) for persona in listaMujeres]
	comboMadre = ttk.Combobox(ventanaRegistroNacimiento, values=lMujeres, font=("Arial", 16), state="readonly")
	comboMadre.grid(row=12, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelNacionalidadMadre = tk.Label(ventanaRegistroNacimiento, text="Nacionalidad:", font=("Arial", 12), bg="light gray")
	labelNacionalidadMadre.grid(row=13, column=0, pady=13)

	comboNacionalidadMadre = ttk.Combobox(ventanaRegistroNacimiento, values=nacionalidades, font=("Arial", 16),state="disabled")
	comboNacionalidadMadre.grid(row=13, column=1, pady=13)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

	def registrarPersona():
		"""
	    Función: Registra una nueva persona con los datos proporcionados.

	    Esta función se encarga de validar y registrar una nueva persona con los datos ingresados en los campos de la ventana de registro.

	    - Verifica la validez de la cédula ingresada y los datos básicos de la persona.
	    - Asigna valores a las variables necesarias para crear una nueva instancia de la clase Persona.
	    - Crea una nueva instancia de Persona con los datos proporcionados y la añade a la lista de registroPersonas.
	    - Muestra los datos de todas las personas registradas hasta el momento.

	    Requiere que los campos de la ventana de registro estén correctamente llenados.

	    Argumentos:
	        No tiene argumentos, pero hace uso de los datos ingresados en la interfaz gráfica.

	    Variables utilizadas (globales):
	        - Variablesexo: Variable global para almacenar el sexo seleccionado.
	        - registroPersonas: Lista que almacena las instancias de la clase Persona.

	    """
		if entryCitaProvincia.get().isdigit() and entryCitaTomo.get().isdigit() and entryCitaAsiento.get().isdigit():
			if (1 <= int(entryCitaProvincia.get()) <= 9) and (len(entryCitaTomo.get()) == len(entryCitaAsiento.get()) == 4):
				try:
					global Variablesexo
					cedula = entryCitaProvincia.get() + "-" + entryCitaTomo.get() + "-" + entryCitaAsiento.get()

					valorProvincia = ""
     
					if entryCitaProvincia.get() == "1":
						valorProvincia = "San José"
					elif entryCitaProvincia.get() == "2":
						valorProvincia = "Alajuela"
					elif entryCitaProvincia.get() == "3":
						valorProvincia = "Cartago"
					elif entryCitaProvincia.get() == "4":
						valorProvincia = "Heredia"
					elif entryCitaProvincia.get() == "5":
						valorProvincia = "Guanacaste"
					elif entryCitaProvincia.get() == "6":
						valorProvincia = "Puntarenas"
					elif entryCitaProvincia.get() == "7":
						valorProvincia = "Limón"
					if entryCitaProvincia.get() == "8" or entryCitaProvincia.get() == "9":
						comboProvincia.config(state="readonly")
      
					if valorProvincia in provincia:
						comboProvincia.current(provincia.index(valorProvincia))
						
					nombre = entryNombre.get()
					sexo = Variablesexo
					fechaNacimiento = comboDias.get() + "/" + comboMeses.get() + "/" + comboAnnos.get()
					padre = comboPadre.get()
					madre = comboMadre.get()
					apellido = padre.split(" ")[1] +" "+ madre.split(" ")[1]

					for nombrePadres in registroPersonas:
						if padre == str(nombrePadres.getNombre())+" "+str(nombrePadres.getApellido1())+" "+str(nombrePadres.getApellido2()):
							comboNacionalidadPadre.current(nacionalidades.index(nombrePadres.getNacionalidadPadre()))
						if madre == str(nombrePadres.getNombre())+" "+str(nombrePadres.getApellido1())+" "+str(nombrePadres.getApellido2()):
							comboNacionalidadMadre.current(nacionalidades.index(nombrePadres.getNacionalidadMadre()))
       
					nacionalidadPadre = comboNacionalidadPadre.get()
					nacionalidadMadre = comboNacionalidadMadre.get()
					if comboProvincia.get() != "":
						localidad = entryDistrito.get() + "," + entryCanton.get() + "," + comboProvincia.get()
					else:
						comboProvincia.current.index(0)
						localidad = entryDistrito.get() + "," + entryCanton.get() + "," + comboProvincia.get()
					entryApellidos.config(state="normal")
					entryApellidos.insert(0,apellido)
					entryApellidos.config(state="disabled")
					nuevaPersona = Persona(
						cedula=cedula,
						nombre=nombre,
						apellido1=padre.split(" ")[1],
						apellido2=madre.split(" ")[1],
						sexo=sexo,
						localidad=localidad,
						fechaNacimiento=fechaNacimiento,
						padre=padre,
						nacionalidadPadre=nacionalidadPadre,
						madre=madre,
						nacionalidadMadre=nacionalidadMadre

					)
					
					if nuevaPersona.getSexo() == "M":
						listaHombres.append(nuevaPersona)
					else:
						listaMujeres.append(nuevaPersona)
					registroPersonas.append(nuevaPersona)
					
					for i in registroPersonas:
						i.mostrarTodo()
				except:
					messagebox.showerror("Error",f"Rellene los espacios solicitados")
			else:
				messagebox.showerror("Error","El primer digito de la cedula no puede ser menor a 1 o mayo a 9")
		else:
			messagebox.showerror("Error","La cedula debe ser en digitos")

	botonRegistrar = tk.Button(ventanaRegistroNacimiento, text="Registrar", width=12, height=1, font=("Arial", 12), command=registrarPersona)
	botonRegistrar.grid(row=14, column=0, pady=10)

	def limpiarDatos():
		"""
		Función: Limpia los datos de la interfaz de registro.

		Esta función borra los datos ingresados en varios campos de la interfaz de registro.

		- Acciones:
		    - Borra el contenido de los campos de entrada relacionados con la cita (provincia, tomo, asiento).
		    - Elimina los datos ingresados en los campos de nombre, apellidos, distrito y cantón.
		    - Restablece a un estado vacío los campos de selección (provincia, días, meses, años, padres y nacionalidades).
		"""
		entryCitaProvincia.delete(0, 'end')
		entryCitaTomo.delete(0, 'end')
		entryCitaAsiento.delete(0, 'end')
		entryNombre.delete(0, 'end')
		entryApellidos.config(state="normal")
		entryApellidos.delete(0, 'end')
		entryApellidos.config(state="disabled"	)
		entryDistrito.delete(0, 'end')
		entryCanton.delete(0, 'end')
		comboProvincia.set('')
		comboDias.set('')
		comboMeses.set('')
		comboAnnos.set('')
		comboPadre.set('')
		comboNacionalidadPadre.set('')
		comboMadre.set('')
		comboNacionalidadMadre.set('')

	botonLimpiar = tk.Button(ventanaRegistroNacimiento, text="Limpiar", command=limpiarDatos, width=12, height=1, font=("Arial", 12))
	botonLimpiar.grid(row=14, column=1, pady=10)

	botonRegresar = tk.Button(ventanaRegistroNacimiento, text="Regresar", width=12, height=1, font=("Arial", 12), command=ventanaRegistroNacimiento.destroy)
	botonRegresar.grid(row=14, column=2, pady=10)
 # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaReportesProvincia():
	"""
    Función: Crea una ventana para generar reportes por provincia.

    Esta función despliega una ventana que permite al usuario seleccionar una provincia y generar un reporte en HTML
    que contiene información relacionada con personas registradas en la provincia seleccionada.

    - Interfaz gráfica: Se presenta una ventana con un Combobox para elegir la provincia y botones para generar y salir.

    Argumentos:
        No recibe argumentos.

    Variables utilizadas (globales):
        - provincia: Lista de nombres de provincias.
        - registroPersonas: Lista de objetos de personas registradas.

    Acciones:
        - Crea una nueva ventana de reportes.
        - Muestra un Combobox para seleccionar la provincia.
        - El botón 'Crear' genera un reporte en HTML basado en la provincia seleccionada y los datos registrados.
        - El botón 'Salir' cierra la ventana de reportes.

    """
	ventanaReporte = tk.Tk()
	ventanaReporte.title("Ventana principal")
	ventanaReporte.geometry("400x300")
	ventanaReporte.resizable(width=False, height=False)
	ventanaReporte.configure(bg="light gray")
	ventanaReporte.columnconfigure(0, weight=1)
	ventanaReporte.rowconfigure(1, weight=1)
	global provincia
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
	labelReport = tk.Label(ventanaReporte, text="Provincias", font=("Arial", 12), bg="light gray")
	labelReport.grid(row=0, column=0, pady=10)

	entryProvinciaVar = tk.StringVar() 
	entryProvincia = ttk.Combobox(ventanaReporte,values=provincia, width=21, font=("Arial", 16), state="readonly", textvariable=entryProvinciaVar)
	entryProvincia.grid(row=1, column=0, pady=10)

	valorPredeterminado = "San José"
	if valorPredeterminado in provincia:
		entryProvincia.current(provincia.index(valorPredeterminado))

	def crearRep():
		"""
		Función: Genera un archivo HTML basado en la provincia seleccionada.

		Esta función toma la provincia seleccionada en la interfaz gráfica, la convierte en un código correspondiente
		y utiliza esta información para generar un archivo HTML que contiene datos de personas registradas en la provincia.

		- Argumentos: No recibe argumentos.

		Acciones:
		    - Mapea el nombre de la provincia seleccionada a su código correspondiente.
		    - Llama a la función 'generarHTMLProvincia()' con el código de la provincia, el nombre de la provincia y
		      la lista de personas registradas.
		    - Muestra un mensaje de éxito informando que se ha creado el archivo HTML.

		"""
		prov = "1"
		if entryProvincia.get() == "San José":
		    prov = "1" 
		elif entryProvincia.get() == "Alajuela":
		    prov = "2"
		elif entryProvincia.get() =="Cartago":
		    prov = "3"
		elif entryProvincia.get() =="Heredia":
		    prov = "4"
		elif entryProvincia.get() =="Guanacaste":
		    prov = "5"
		elif entryProvincia.get() =="Puntarenas":
		    prov = "6"
		elif entryProvincia.get() =="Limón":
		    prov = "7"
		generarHTMLProvincia(prov, entryProvincia.get(), registroPersonas)
		messagebox.showinfo("Exito","El archivo ha sido creado")

	botonCrear = tk.Button(ventanaReporte, text="Crear", width=20,height=2, command=crearRep)
	botonCrear.grid(row=2,column=0,pady=10)

	botonSalir = tk.Button(ventanaReporte, text="Salir", width=20, height=2, command=ventanaReporte.destroy)
	botonSalir.grid(row=3, column=0, pady=10)
 # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaReportesAnnos():
	"""
    Función: Abre una ventana para generar un reporte según el año ingresado.

    Esta función abre una interfaz gráfica que permite al usuario ingresar un año.
    Luego, al presionar el botón 'Personas por año', recopila los años de nacimiento
    de las personas registradas y genera un reporte en HTML para el año ingresado.

    - Argumentos: No recibe argumentos.

    Acciones:
        - Abre una ventana gráfica con la opción de ingresar un año.
        - Al presionar el botón 'Personas por año':
            - Verifica si el año ingresado es válido.
            - Recopila los años de nacimiento de las personas registradas.
            - Genera un archivo HTML que contiene datos de personas nacidas en el año ingresado.
            - Muestra un mensaje de éxito si se genera el reporte correctamente, o un error si el año ingresado no es válido.

    """
	ventanaReporte = tk.Tk()
	ventanaReporte.title("Ventana principal")
	ventanaReporte.geometry("400x300")
	ventanaReporte.resizable(width=False, height=False)
	ventanaReporte.configure(bg="light gray")
	ventanaReporte.columnconfigure(0, weight=1)
	ventanaReporte.rowconfigure(1, weight=1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	def crearRep():
		"""
	    Función: Crea un reporte según el año ingresado.

	    Esta función recopila los años de nacimiento de las personas registradas y genera un reporte en HTML
	    para el año ingresado por el usuario.

	    - Acciones:
	        - Recopila los años de nacimiento de las personas registradas.
	        - Verifica si el año ingresado es válido.
	        - Si el año es válido:
	            - Genera un archivo HTML que contiene datos de personas nacidas en el año ingresado.
	            - Muestra un mensaje de éxito indicando que se generó el reporte para el año ingresado.
	        - Si el año no es válido:
	            - Muestra un mensaje de error pidiendo al usuario que ingrese un año válido.
	    """
		listaAnnios = []
		for persona in registroPersonas:
			annio = persona.getFechaNacimiento().split("/")[2]
			if not int(annio) in listaAnnios:
				listaAnnios.append(int(annio))
		listaAnnios = sorted(listaAnnios)
		annoSeleccionado = entryAnno.get()
		if annoSeleccionado.isdigit():
			print(listaAnnios)
			generarHTMLAnno(int(annoSeleccionado), registroPersonas, listaAnnios)
			messagebox.showinfo("Éxito", f"Se generó el reporte para el año {annoSeleccionado}")
		else:
			messagebox.showerror("Error", "Por favor, ingrese un año válido")

	labelReport = tk.Label(ventanaReporte, text="Ingrese un año:", font=("Arial", 12), bg="light gray")
	labelReport.grid(row=0, column=0, pady=10)

	entryAnno = tk.Entry(ventanaReporte, font=("Arial", 16))
	entryAnno.grid(row=1, column=0, pady=10)

	botonanno = tk.Button(ventanaReporte, text="Crear", width=20, height=2, command=crearRep)
	botonanno.grid(row=2, column=0, pady=10)

	botonSalir = tk.Button(ventanaReporte, text="Salir", width=20, height=2, command=ventanaReporte.destroy)
	botonSalir.grid(row=3, column=0, pady=10)
	
 # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaReportesHospital():
	"""
	Función: Crea reportes de personas por hospital.

	Esta función genera un reporte en HTML según el tomo de registro de las personas en el hospital.

	- Acciones:
	    - Crea una ventana para generar reportes por tomo de registro en el hospital.
	    - Muestra una lista desplegable con los tomos disponibles de las personas registradas en el hospital.
	    - Permite al usuario seleccionar un tomo y generar un reporte en HTML para las personas registradas en ese tomo.
	    - Proporciona botones para crear el reporte o cerrar la ventana.
	"""
	ventanaReporte = tk.Tk()
	ventanaReporte.title("Ventana principal")
	ventanaReporte.geometry("400x300")
	ventanaReporte.resizable(width=False, height=False)
	ventanaReporte.configure(bg="light gray")
	ventanaReporte.columnconfigure(0, weight=1)
	ventanaReporte.rowconfigure(1, weight=1)
	
	listaTomos = []
	for persona in registroPersonas:
		if not persona.getCedula().split("-")[1] in listaTomos:
			listaTomos.append(persona.getCedula().split("-")[1])
   
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelReport = tk.Label(ventanaReporte, text="Reportes", font=("Arial", 12), bg="light gray")
	labelReport.grid(row=0, column=0, pady=10)
	
	entryTomoHospVar = tk.StringVar()
	entryTomoHosp = ttk.Combobox(ventanaReporte,values=listaTomos, width=21, font=("Arial", 16), state="readonly", textvariable=entryTomoHospVar)
	entryTomoHosp.grid(row=1, column=0, pady=10)
	if listaTomos and listaTomos[0] in listaTomos:
    		entryTomoHosp.current(listaTomos.index(listaTomos[0]))

	def crearPorTomo():
		tomo = entryTomoHosp.get()
		generarHTMLTomo(tomo, registroPersonas)
  
	botonProvincia = tk.Button(ventanaReporte, text="Crear", width=20, height=2, command=crearPorTomo)
	botonProvincia.grid(row=2, column=0, pady=10)

	botonSalir = tk.Button(ventanaReporte, text="Salir", width=20, height=2, command=ventanaReporte.destroy)
	botonSalir.grid(row=4, column=0, pady=10)

 # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaDeReportes():
	"""
	Función: Abre una ventana principal para generar diferentes reportes.
	    
	Esta función crea una interfaz gráfica con botones que permiten al usuario generar varios tipos de reportes
	relacionados con personas registradas.

	- Acciones:
	    - Crea una ventana con botones para generar reportes por provincia, año de nacimiento y hospital.
	    - Los botones están vinculados a funciones específicas que generan diferentes tipos de informes.
	    - Proporciona un botón para cerrar la ventana principal.
	"""
	ventanaReporte = tk.Tk()
	ventanaReporte.title("Ventana principal")
	ventanaReporte.geometry("400x300")
	ventanaReporte.resizable(width=False, height=False)
	ventanaReporte.configure(bg="light gray")
	ventanaReporte.columnconfigure(0, weight=1)
	ventanaReporte.rowconfigure(1, weight=1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelReport = tk.Label(ventanaReporte, text="Reportes", font=("Arial", 12), bg="light gray")
	labelReport.grid(row=0, column=0, pady=10)

	botonProvincia = tk.Button(ventanaReporte, text="Personas por provincia", width=20, height=2, command=ventanaReportesProvincia)
	botonProvincia.grid(row=1, column=0, pady=10)

	botonNacidos = tk.Button(ventanaReporte, text="Personas por año", width=20, height=2, command=ventanaReportesAnnos)
	botonNacidos.grid(row=2, column=0, pady=10)

	botonHospital = tk.Button(ventanaReporte, text="Personas por hospital", width=20, height=2,command=ventanaReportesHospital)
	botonHospital.grid(row=3, column=0, pady=10)

	botonSalir = tk.Button(ventanaReporte, text="Salir", width=20, height=2, command=ventanaReporte.destroy)
	botonSalir.grid(row=4, column=0, pady=10)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaCertificado():
	"""
	Función: Abre una ventana para generar certificados.

	Esta función crea una ventana que permite al usuario ingresar una cédula y generar certificados en formatos HTML y XML
	basados en la información asociada con la cédula proporcionada.

	- Acciones:
	    - Abre una ventana para ingresar la cédula en tres campos separados.
	    - Permite al usuario generar certificados en HTML y XML haciendo uso de la cédula ingresada.
	    - Verifica la validez de la cédula ingresada antes de generar los certificados.
	    - Muestra un mensaje de error si la cédula no cumple con los criterios de validación.
	    - Proporciona botones para buscar la información y para cerrar la ventana de certificados.
	"""
	ventanaCert = tk.Tk()
	ventanaCert.title("Ventana Certificado")
	ventanaCert.geometry("400x300")
	ventanaCert.resizable(width=False, height=False)
	ventanaCert.configure(bg="light gray")
	ventanaCert.columnconfigure(0, weight=1)
	ventanaCert.rowconfigure(1, weight=1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCedula = tk.Label(ventanaCert, text="Ingrese la cedula:", font=("Arial", 12), bg="light gray")
	labelCedula.grid(row=0, column=0, pady=10)

	entryCitaProvincia = tk.Entry(ventanaCert, width=3, font=("Arial", 16))
	entryCitaProvincia.place(x=85, y=60)

	labelGuion = tk.Label(ventanaCert, text="-", font=("Arial", 16), bg="light gray")
	labelGuion.place(x=126, y=60)

	entryCitaTomo = tk.Entry(ventanaCert, width=6, font=("Arial", 16))
	entryCitaTomo.place(x=140, y=60)

	labelGuion = tk.Label(ventanaCert, text="-", font=("Arial", 16), bg="light gray")
	labelGuion.place(x=217, y=60)

	entryCitaAsiento = tk.Entry(ventanaCert, width=6, font=("Arial", 16))
	entryCitaAsiento.place(x=234, y=60)
 
	def validarCedula():
		"""
		Función: Valida la cédula ingresada.

		Esta función verifica la validez de una cédula ingresada en tres campos distintos: provincia, tomo y asiento.

		- Acciones:
		    - Verifica si los campos de provincia, tomo y asiento contienen únicamente dígitos.
		    - Confirma que el primer dígito de la provincia esté entre 1 y 9.
		    - Confirma que la longitud de los campos tomo y asiento sea 4.
		    - Si la cédula es válida:
		        - Genera un certificado HTML y XML utilizando los datos de la cédula y la lista de personas registradas.
		    - Si la cédula no es válida:
		        - Muestra un mensaje de error indicando que los datos ingresados no cumplen con los criterios necesarios.
		"""
		if entryCitaProvincia.get().isdigit() and entryCitaTomo.get().isdigit() and entryCitaAsiento.get().isdigit():
			if (1 <= int(entryCitaProvincia.get()) <= 9) and (len(entryCitaTomo.get()) == len(entryCitaAsiento.get()) == 4):
				cedula = entryCitaProvincia.get() + "-" + entryCitaTomo.get() + "-" + entryCitaAsiento.get()
				generarCertificadoHtml(cedula, registroPersonas)
				generarCertificadoXml(cedula, listaPersonas)
			else:
				messagebox.showerror("Error","El primer digito de la cedula no puede ser menor a 1 o mayo a 9")
		else:
			messagebox.showerror("Error","La cedula debe ser en digitos")

	botonCertificado = tk.Button(ventanaCert, text="Buscar", width=20, height=2, command=validarCedula)
	botonCertificado.grid(row=2, column=0, pady=10)

	botonSalir = tk.Button(ventanaCert, text="Salir", width=20, height=2, command=ventanaCert.destroy)
	botonSalir.grid(row=3, column=0, pady=10)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaDeInicio():
	"""
	Función: Crea la ventana principal del sistema.

	Esta función genera la ventana principal con distintas opciones para interactuar con el sistema de registro de nacimientos.

	- Acciones:
	    - Crea una ventana principal para el sistema.
	    - Incluye botones para registrar nacimientos, mostrar árbol genealógico, generar certificados de nacimiento, 
	      acceder a informes y reportes, y salir del sistema.
	"""
	ventanaInicio = tk.Tk()
	ventanaInicio.title("Ventana principal")
	ventanaInicio.geometry("400x300")
	ventanaInicio.resizable(width=False, height=False)
	ventanaInicio.configure(bg="light gray")
	ventanaInicio.columnconfigure(0, weight=1)
	ventanaInicio.rowconfigure(1, weight=1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	botonNacimiento = tk.Button(ventanaInicio, text="Registrar Nacimiento", width=20, height=2, command=ventanaDeRegistroNacimiento)
	botonNacimiento.grid(row=0, column=0, pady=10)

	botonMostrarArbolGenealogico = tk.Button(ventanaInicio, text="Mostrar Árbol Genealógico", width=20, height=2, command=mostrarArbolGenealogico)
	botonMostrarArbolGenealogico.grid(row=1, column=0, pady=10)

	botonCertificadoNacimiento= tk.Button(ventanaInicio, text="Certificado de Nacimiento", width=20, height=2, command=ventanaCertificado)
	botonCertificadoNacimiento.grid(row=2, column=0, pady=10)

	botonReportes = tk.Button(ventanaInicio, text="Reportes", width=20, height=2,command=ventanaDeReportes)
	botonReportes.grid(row=3, column=0, pady=10)

	botonSalir = tk.Button(ventanaInicio, text="Salir", width=20, height=2, command=ventanaInicio.destroy)
	botonSalir.grid(row=4, column=0, pady=10)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaDeRegistro():
	"""
	Función: Crea la ventana de registro de usuarios.

	Esta función genera una ventana donde se pueden ingresar credenciales de usuario para acceder al sistema de registro de nacimientos.

	- Acciones:
	    - Crea una ventana de registro con campos para ingresar nombre de usuario y contraseña.
	    - Verifica las credenciales ingresadas.
	    - Permite al usuario iniciar sesión si las credenciales coinciden con los datos almacenados.
	    - Proporciona opciones para limpiar los campos y acceder al sistema.
	"""
	ventanaRegistro = tk.Tk()
	ventanaRegistro.title("Ventana de registro")
	ventanaRegistro.geometry("400x200")
	ventanaRegistro.resizable(width=False, height=False)
	ventanaRegistro.configure(bg="light gray")

	labelUsuario = tk.Label(ventanaRegistro, text="Usuario:", font=("Arial", 12), bg="light gray")
	labelUsuario.place(x=20, y=15)

	entryUsuario = tk.Entry(ventanaRegistro, width=25, font=("Arial", 12))
	entryUsuario.place(x=120, y=17)

	labelContra = tk.Label(ventanaRegistro, text="Contraseña:", font=("Arial", 12), bg="light gray")
	labelContra.place(x=20, y=60)

	entryContra = tk.Entry(ventanaRegistro, width=25, font=("Arial", 12))
	entryContra.place(x=120, y=60)
	
	def registrarse():
		"""
		Función: Verifica las credenciales de usuario para el acceso.

		Esta función valida las credenciales ingresadas por el usuario al intentar iniciar sesión en el sistema de registro de nacimientos.

		- Acciones:
		    - Lee los datos de usuarios registrados desde el archivo "Administradores.txt".
		    - Obtiene el nombre de usuario y la contraseña ingresados por el usuario.
		    - Comprueba si las credenciales coinciden con los datos almacenados.
		    - Si las credenciales son correctas:
		        - Cierra la ventana actual de registro.
		        - Abre la ventana principal del sistema de registro de nacimientos.
		    - Si las credenciales son incorrectas:
		        - Muestra un mensaje de advertencia indicando que las credenciales no coinciden.
		"""
		inicio = False
		usuarios = leerRegistro("Administradores.txt")
		nombreUsuario = entryUsuario.get()
		contrasennia = entryContra.get()
		botonLimpiar.config(state="normal")
		botonIngresar.config(state="disabled")
		for credenciales in usuarios:
			if credenciales[0] == nombreUsuario and credenciales[1] == contrasennia:
				inicio = True
				cerrarVentana(ventanaRegistro)
				ventanaDeInicio()
             
		if not inicio:	
			messagebox.showwarning("Error","El usuario o contraseña no coinciden")
  
	def limpiar():
		"""
		Función: Limpia los campos de entrada del formulario de registro.

		Esta función borra los datos ingresados en los campos de usuario y contraseña del formulario de registro y restablece
		los botones para su uso normal.

		- Acciones:
		    - Borra el contenido de los campos de entrada para el usuario y la contraseña.
		    - Deshabilita el botón "Limpiar" después de la limpieza.
		    - Habilita el botón "Ingresar" para permitir nuevos intentos de inicio de sesión.
		"""
		entryUsuario.delete(0,tk.END)
		entryContra.delete(0,tk.END)
		botonLimpiar.config(state="disabled")
		botonIngresar.config(state="normal")
  
	botonIngresar = tk.Button(ventanaRegistro, text="Ingresar", width=20, height=2, command=registrarse)
	botonIngresar.place(x=40, y=120)

	botonLimpiar = tk.Button(ventanaRegistro, text="Limpiar", width=20, height=2, state="disabled", command=limpiar)
	botonLimpiar.place(x=200, y=120)

	ventanaRegistro.mainloop()
 

ventanaDeRegistro()