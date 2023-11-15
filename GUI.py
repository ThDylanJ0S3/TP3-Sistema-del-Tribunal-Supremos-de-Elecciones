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

global listaPersonas
global listaCedulas
global listaHombres
global listaMujeres
global provincia
listaPersonas = lee("PadresOriginales")
listaCedulasNombre = obtenerCedulaNombre(listaPersonas)
listaHombres = separarHombres(listaPersonas)
listaMujeres = separarMujeres(listaPersonas)
provincia = ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]

def mostrarArbolGenealogico():    
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
		hijo = comboPersona.get()
		for persona in listaPersonas:
			if hijo[0:9] == persona.getCedula():
				entryHijo.config(state="normal", width=len(hijo[11:]))
				entryMadreMostrar.config(state="normal", width=len(persona.getMadre())+1)
				entryPadreMostrar.config(state="normal", width=len(persona.getPadre())+1)
				entryHijo.insert(0,hijo[11:-1])
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
	ventanaRegistroNacimiento = tk.Tk()
	ventanaRegistroNacimiento.title("Ventana de registro")
	ventanaRegistroNacimiento.geometry("570x820")
	ventanaRegistroNacimiento.resizable(width=False, height=False)
	ventanaRegistroNacimiento.configure(bg="light gray")
	ventanaRegistroNacimiento.columnconfigure(0, weight=1)
	ventanaRegistroNacimiento.columnconfigure(2, weight=1)
	global provincia
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

	entryApellidos = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryApellidos.grid(row=2, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelSexo = tk.Label(ventanaRegistroNacimiento, text="Sexo:", font=("Arial", 12), bg="light gray")
	labelSexo.grid(row=3, column=0, pady=13)

	varSexo = tk.StringVar()
	radioMasculino = tk.Radiobutton(ventanaRegistroNacimiento, text="Masculino", variable=varSexo, value="M", font=("Arial", 15), bg="light gray")
	radioMasculino.place(x=152, y=166)

	radioFemenino = tk.Radiobutton(ventanaRegistroNacimiento, text="Femenino", variable=varSexo, value="F", font=("Arial", 15), bg="light gray")
	radioFemenino.place(x=294, y=166)
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
	labelProvincia = tk.Label(ventanaRegistroNacimiento, text="Provincia:", font=("Arial", 12), bg="light gray")
	labelProvincia.grid(row=6, column=0, pady=13)

	entryProvincia = ttk.Combobox(ventanaRegistroNacimiento,values=provincia, width=21, font=("Arial", 16), state="readonly")
	entryProvincia.grid(row=6, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelDia = tk.Label(ventanaRegistroNacimiento, text="Dia:", font=("Arial", 12), bg="light gray")
	labelDia.grid(row=7, column=0, pady=13)

	dias = [str(i) for i in range(1,32)]
	comboDias = ttk.Combobox(ventanaRegistroNacimiento, values=dias, font=("Arial", 16))
	comboDias.grid(row=7, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelMeses = tk.Label(ventanaRegistroNacimiento, text="Mes:", font=("Arial", 12), bg="light gray")
	labelMeses.grid(row=8, column=0, pady=13)

	meses = [str(i) for i in range(1,12)]
	comboMeses = ttk.Combobox(ventanaRegistroNacimiento, values=meses, font=("Arial", 16))
	comboMeses.grid(row=8, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelAnnos = tk.Label(ventanaRegistroNacimiento, text="Año:", font=("Arial", 12), bg="light gray")
	labelAnnos.grid(row=9, column=0, pady=13)

	annoActual = datetime.now().year
	annos = [str(i) for i in range(1900, annoActual + 1)]
	comboAnnos = ttk.Combobox(ventanaRegistroNacimiento, values=annos, font=("Arial", 16))
	comboAnnos.grid(row=9, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelPadre = tk.Label(ventanaRegistroNacimiento, text="Padre:", font=("Arial", 12), bg="light gray")
	labelPadre.grid(row=10, column=0, pady=13)

	comboPadre = ttk.Combobox(ventanaRegistroNacimiento, values="", font=("Arial", 16))
	comboPadre.grid(row=10, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelNacionalidadPadre = tk.Label(ventanaRegistroNacimiento, text="Nacionalidad:", font=("Arial", 12), bg="light gray")
	labelNacionalidadPadre.grid(row=11, column=0, pady=13)

	comboNacionalidadPadre = ttk.Combobox(ventanaRegistroNacimiento, values=nacionalidades, font=("Arial", 16))
	comboNacionalidadPadre.grid(row=11, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelMadre = tk.Label(ventanaRegistroNacimiento, text="Madre:", font=("Arial", 12), bg="light gray")
	labelMadre.grid(row=12, column=0, pady=13)

	comboMadre = ttk.Combobox(ventanaRegistroNacimiento, values="", font=("Arial", 16))
	comboMadre.grid(row=12, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelNacionalidadMadre = tk.Label(ventanaRegistroNacimiento, text="Nacionalidad:", font=("Arial", 12), bg="light gray")
	labelNacionalidadMadre.grid(row=13, column=0, pady=13)

	comboNacionalidadMadre = ttk.Combobox(ventanaRegistroNacimiento, values=nacionalidades, font=("Arial", 16))
	comboNacionalidadMadre.grid(row=13, column=1, pady=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

	#def 

	botonRegistrar = tk.Button(ventanaRegistroNacimiento, text="Registrar", width=12, height=1, font=("Arial", 12), command=registrarPersona)
	botonRegistrar.grid(row=14, column=0, pady=10)

	botonLimpiar = tk.Button(ventanaRegistroNacimiento, text="Limpiar", width=12, height=1, font=("Arial", 12))
	botonLimpiar.grid(row=14, column=1, pady=10)

	botonRegresar = tk.Button(ventanaRegistroNacimiento, text="Regresar", width=12, height=1, font=("Arial", 12), command=ventanaRegistroNacimiento.destroy)
	botonRegresar.grid(row=14, column=2, pady=10)

 # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaReportesProvincia():
	ventanaReporte = tk.Tk()
	ventanaReporte.title("Ventana principal")
	ventanaReporte.geometry("400x300")
	ventanaReporte.resizable(width=False, height=False)
	ventanaReporte.configure(bg="light gray")
	ventanaReporte.columnconfigure(0, weight=1)
	ventanaReporte.rowconfigure(1, weight=1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelReport = tk.Label(ventanaReporte, text="Provincias", font=("Arial", 12), bg="light gray")
	labelReport.grid(row=0, column=0, pady=10)

	botonProvincia = tk.Button(ventanaReporte, text="Personas por provincia", width=20, height=2, command=mostrarArbolGenealogico)
	botonProvincia.grid(row=1, column=0, pady=10)

	botonNacidos = tk.Button(ventanaReporte, text="Personas nacidas a partir de", width=20, height=2)
	botonNacidos.grid(row=2, column=0, pady=10)

 # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaReportesAnnos():
	ventanaReporte = tk.Tk()
	ventanaReporte.title("Ventana principal")
	ventanaReporte.geometry("400x300")
	ventanaReporte.resizable(width=False, height=False)
	ventanaReporte.configure(bg="light gray")
	ventanaReporte.columnconfigure(0, weight=1)
	ventanaReporte.rowconfigure(1, weight=1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelReport = tk.Label(ventanaReporte, text="Ingrese un año", font=("Arial", 12), bg="light gray")
	labelReport.grid(row=0, column=0, pady=10)

	botonProvincia = tk.Button(ventanaReporte, text="Personas por provincia", width=20, height=2, command=mostrarArbolGenealogico)
	botonProvincia.grid(row=1, column=0, pady=10)

	botonNacidos = tk.Button(ventanaReporte, text="Personas nacidas a partir de", width=20, height=2)
	botonNacidos.grid(row=2, column=0, pady=10)

 # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaReportesHospital():
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

	botonProvincia = tk.Button(ventanaReporte, text="Personas por provincia", width=20, height=2, command=mostrarArbolGenealogico)
	botonProvincia.grid(row=1, column=0, pady=10)

	botonNacidos = tk.Button(ventanaReporte, text="Personas nacidas a partir de", width=20, height=2)
	botonNacidos.grid(row=2, column=0, pady=10)

 # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaDeReportes():
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

	botonNacidos = tk.Button(ventanaReporte, text="Personas nacidas a partir de", width=20, height=2, command=ventanaReportesAnnos)
	botonNacidos.grid(row=2, column=0, pady=10)

	botonHospital = tk.Button(ventanaReporte, text="Personas por hospital", width=20, height=2,command=ventanaReportesHospital)
	botonHospital.grid(row=3, column=0, pady=10)

	botonSalir = tk.Button(ventanaReporte, text="Salir", width=20, height=2, command=ventanaReporte.destroy)
	botonSalir.grid(row=4, column=0, pady=10)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaDeInicio():
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

	botonCertificadoNacimiento= tk.Button(ventanaInicio, text="Certificado de Nacimiento", width=20, height=2)
	botonCertificadoNacimiento.grid(row=2, column=0, pady=10)

	botonReportes = tk.Button(ventanaInicio, text="Reportes", width=20, height=2,command=ventanaDeReportes)
	botonReportes.grid(row=3, column=0, pady=10)

	botonSalir = tk.Button(ventanaInicio, text="Salir", width=20, height=2, command=ventanaInicio.destroy)
	botonSalir.grid(row=4, column=0, pady=10)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
def ventanaDeRegistro():
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