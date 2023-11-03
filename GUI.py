import tkinter as tk
from tkinter import ttk
import datetime

def ventanaDeRegistroNacimiento():
	ventanaRegistroNacimiento = tk.Tk()
	ventanaRegistroNacimiento.title("Ventana de registro")
	ventanaRegistroNacimiento.geometry("540x800")
	ventanaRegistroNacimiento.resizable(width=False, height=False)
	ventanaRegistroNacimiento.configure(bg="light gray")
	ventanaRegistroNacimiento.columnconfigure(0, weight=1)
	ventanaRegistroNacimiento.columnconfigure(1, weight=1)
	ventanaRegistroNacimiento.columnconfigure(2, weight=1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCita = tk.Label(ventanaRegistroNacimiento, text="Cita:", font=("Arial", 12), bg="light gray")
	labelCita.grid(row=0, column=0, pady=16)

	entryCitaProvincia = tk.Entry(ventanaRegistroNacimiento, width=3, font=("Arial", 16))
	entryCitaProvincia.place(x=220, y=13)

	labelGuion = tk.Label(ventanaRegistroNacimiento, text="-", font=("Arial", 16), bg="light gray")
	labelGuion.place(x=264, y=13)

	entryCitaTomo = tk.Entry(ventanaRegistroNacimiento, width=6, font=("Arial", 16))
	entryCitaTomo.place(x=280, y=13)

	labelGuion = tk.Label(ventanaRegistroNacimiento, text="-", font=("Arial", 16), bg="light gray")
	labelGuion.place(x=360, y=13)

	entryCitaAsiento = tk.Entry(ventanaRegistroNacimiento, width=6, font=("Arial", 16))
	entryCitaAsiento.place(x=378, y=13)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelNombre = tk.Label(ventanaRegistroNacimiento, text="Nombre:", font=("Arial", 12), bg="light gray")
	labelNombre.grid(row=1, column=0, pady=16)

	entryNombre = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryNombre.grid(row=1, column=1, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelApellidos = tk.Label(ventanaRegistroNacimiento, text="Apellidos:", font=("Arial", 12), bg="light gray")
	labelApellidos.grid(row=2, column=0, pady=16)

	entryApellidos = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryApellidos.grid(row=2, column=1, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelSexo = tk.Label(ventanaRegistroNacimiento, text="Sexo:", font=("Arial", 12), bg="light gray")
	labelSexo.grid(row=3, column=0, pady=16)

	varSexo = tk.StringVar()
	radioMasculino = tk.Radiobutton(ventanaRegistroNacimiento, text="Masculino", variable=varSexo, value="Masculino", font=("Arial", 13), bg="light gray")
	radioMasculino.place(x=213, y=189)

	radioFemenino = tk.Radiobutton(ventanaRegistroNacimiento, text="Femenino", variable=varSexo, value="Femenino", font=("Arial", 13), bg="light gray")
	radioFemenino.place(x=330, y=189)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelDistrito = tk.Label(ventanaRegistroNacimiento, text="Distrito:", font=("Arial", 12), bg="light gray")
	labelDistrito.grid(row=4, column=0, pady=16)

	entryDistrito = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryDistrito.grid(row=4, column=1, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCanton = tk.Label(ventanaRegistroNacimiento, text="Cantón:", font=("Arial", 12), bg="light gray")
	labelCanton.grid(row=5, column=0, pady=16)

	entryCanton = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryCanton.grid(row=5, column=1, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelProvincia = tk.Label(ventanaRegistroNacimiento, text="Provincia:", font=("Arial", 12), bg="light gray")
	labelProvincia.grid(row=6, column=0, pady=16)

	entryProvincia = tk.Entry(ventanaRegistroNacimiento, width=21, font=("Arial", 16))
	entryProvincia.grid(row=6, column=1, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelDia = tk.Label(ventanaRegistroNacimiento, text="Dia:", font=("Arial", 12), bg="light gray")
	labelDia.grid(row=7, column=0, pady=16)

	dias = [str(i) for i in range(1,32)]
	comboDias = ttk.Combobox(ventanaRegistroNacimiento, values=dias, font=("Arial", 12))
	comboDias.grid(row=7, column=1, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelMeses = tk.Label(ventanaRegistroNacimiento, text="Mes:", font=("Arial", 12), bg="light gray")
	labelMeses.grid(row=8, column=0, pady=16)

	meses = [str(i) for i in range(1,12)]
	comboMeses = ttk.Combobox(ventanaRegistroNacimiento, values=meses, font=("Arial", 12))
	comboMeses.grid(row=8, column=1, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelAños = tk.Label(ventanaRegistroNacimiento, text="Año:", font=("Arial", 12), bg="light gray")
	labelAños.grid(row=9, column=0, pady=16)

	annoActual = datetime.datetime.now().year
	annos = [str(i) for i in range(1900, annoActual + 1)]
	comboAños = ttk.Combobox(ventanaRegistroNacimiento, values=annos, font=("Arial", 12))
	comboAños.grid(row=9, column=1, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCita = tk.Label(ventanaRegistroNacimiento, text="Padre:", font=("Arial", 12), bg="light gray")
	labelCita.grid(row=10, column=0, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCita = tk.Label(ventanaRegistroNacimiento, text="Nacionalidad Padre:", font=("Arial", 12), bg="light gray")
	labelCita.grid(row=11, column=0, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCita = tk.Label(ventanaRegistroNacimiento, text="Madre:", font=("Arial", 12), bg="light gray")
	labelCita.grid(row=12, column=0, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
	labelCita = tk.Label(ventanaRegistroNacimiento, text="Nacionalidad Madre:", font=("Arial", 12), bg="light gray")
	labelCita.grid(row=13, column=0, pady=16)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


	ventanaRegistroNacimiento.mainloop()

def ventanaDeInicio():
	ventanaInicio = tk.Tk()
	ventanaInicio.title("Ventana principal")
	ventanaInicio.geometry("400x300")
	ventanaInicio.resizable(width=False, height=False)
	ventanaInicio.configure(bg="light gray")
	ventanaInicio.columnconfigure(0, weight=1)
	ventanaInicio.rowconfigure(1, weight=1)

	frame = tk.Frame(ventanaInicio)
	frame.grid(row=0, column=0, pady=10)

	botonNacimiento = tk.Button(ventanaInicio, text="Registrar Nacimiento", width=20, height=2)
	botonNacimiento.grid(row=0, column=0, pady=10)

	botonIngresar = tk.Button(ventanaInicio, text="Mostrar Árbol Genealógico", width=20, height=2)
	botonIngresar.grid(row=1, column=0, pady=10)

	botonIngresar = tk.Button(ventanaInicio, text="Certificado de Nacimiento", width=20, height=2)
	botonIngresar.grid(row=2, column=0, pady=10)

	botonIngresar = tk.Button(ventanaInicio, text="Reportes", width=20, height=2)
	botonIngresar.grid(row=3, column=0, pady=10)

	botonIngresar = tk.Button(ventanaInicio, text="Salir", width=20, height=2)
	botonIngresar.grid(row=4, column=0, pady=10)

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

	botonIngresar = tk.Button(ventanaRegistro, text="Ingresar", width=20, height=2, command=ventanaDeInicio)
	botonIngresar.place(x=40, y=120)

	botonLimpiar = tk.Button(ventanaRegistro, text="Limpiar", width=20, height=2)
	botonLimpiar.place(x=200, y=120)

	ventanaRegistro.mainloop()

ventanaDeRegistroNacimiento()