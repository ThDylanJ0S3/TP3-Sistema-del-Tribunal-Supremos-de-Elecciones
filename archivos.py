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
    except Exception as e:
        print("Error al leer el archivo: ", nomArchLeer, f"error {e}")
    return lista

def leerRegistro(nombreArch):
    """
    Función: leer el registro de usuarios
    Entrada: nombreArch(str): nombre del archivo a leer
    Salida:
        -usuarios(list):
    """
    usuarios = []
    
    try:
        with open(nombreArch, 'r') as archivo:
            for linea in archivo:
                usuario, contraseña = linea.strip().split(',')
                usuarios.append((usuario, contraseña))
    except FileNotFoundError:
        print(f"Error: El archivo {nombreArch} no fue encontrado.")
    except Exception as e:
        print(f"Error: {e}")

    return usuarios


def generarHTMLProvincia(nProvincia, provincia, listaPersonas):
    with open(f"./personasPorProvincia.html","w", encoding="utf-8") as archivoContinente:
            archivoContinente.write("<meta charset='UTF-8'>")
            archivoContinente.write("<html><head><title>Personas por Provincia</title></head><body>")
            archivoContinente.write(f"<h1>Personas de {provincia}</h1>")
            archivoContinente.write("<table>")
            archivoContinente.write("<tr style='background-color: #a2c8cc;'><th>Cedula</th><th>Nombre Completo</th><th>Fecha de Nacimiento</th><th>Sexo</th></tr>")
            i = 0
            listaImprimir = []
            #Ciclo para crear cada fila
            for personas in listaPersonas:
                if personas.getCedula()[0] == nProvincia:
                    cedula = personas.getCedula()
                    nombre = str(personas.getNombre())+" "+str(personas.getApellido1())+" "+str(personas.getApellido2())
                    nacimiento = personas.getFechaNacimiento()
                    sexo = personas.getSexo()

                    listaImprimir.append([cedula, nombre, nacimiento, sexo])

            listaImprimir = sorted(listaImprimir, key=lambda x:(x[3]=="M", x[1]))

            for personas in listaImprimir:
                if i % 2 == 0:
                    fondo = "#c5e0dc"
                else:
                    fondo = "#f8edeb"
                archivoContinente.write(f"<tr style='background-color: {fondo}'>")
                archivoContinente.write(f"<td>{personas[0]}</td>")
                archivoContinente.write(f"<td>{personas[1]}</td>")
                archivoContinente.write(f"<td>{personas[2]}</td>")
                archivoContinente.write(f"<td>{personas[3]}</td>")
                i += 1
                archivoContinente.write("</tr>")

            archivoContinente.write("</table></body></html>")
            archivoContinente.close() 


def generarHTMLAnno(annos, listaPersonas):
    with open(f"./personasPorAnno{anno}.html","w", encoding="utf-8") as archivoAnno:
        archivoAnno.write("<meta charset='UTF-8'>")
        archivoAnno.write("<html><head><title>Personas por Año</title></head><body>")
        archivoAnno.write(f"<h1>Personas nacidas en el año {anno}</h1>")
        archivoAnno.write("<table>")
        archivoAnno.write("<tr style='background-color: #a2c8cc;'><th>Cedula</th><th>Nombre Completo</th><th>Fecha de Nacimiento</th><th>Sexo</th><th>Nombre del Padre</th><th>Nombre de la Madre</th></tr>")
        
        i = 0
        listaImprimir = []

        for persona in listaPersonas:
            fechaNacimiento = persona.getFechaNacimiento().split("/")
            if fechaNacimiento[-1] == anno:
                cedula = persona.getCedula()
                nombre = f"{persona.getNombre()} {persona.getApellido1()} {persona.getApellido2()}"
                fechaNacimiento = persona.getFechaNacimiento()
                sexo = persona.getSexo()
                padre = persona.getPadre()
                madre = persona.getMadre()

                listaImprimir.append([cedula, nombre, nacimiento, sexo, padre, madre])

        listaImprimir = sorted(listaImprimir, key=lambda x: (x[3]=="M", x[1]))

        for persona in listaImprimir:
            if i % 2 == 0:
                fondo = "#c5e0dc"
            else:
                fondo = "#f8edeb"
            archivoAnno.write(f"<tr style='background-color: {fondo}'>")
            archivoAnno.write(f"<td>{persona[0]}</td>")
            archivoAnno.write(f"<td>{persona[1]}</td>")
            archivoAnno.write(f"<td>{persona[2]}</td>")
            archivoAnno.write(f"<td>{persona[3]}</td>")
            archivoAnno.write(f"<td>{persona[4]}</td>")
            archivoAnno.write(f"<td>{persona[5]}</td>")
            i += 1
            archivoAnno.write("</tr>")

        archivoAnno.write("</table></body></html>")

def generarCertificadoHtml(persona):
    contenido_html = f'''
    <html>
    <head>
        <title>Certificado de Nacimiento</title>
    </head>
    <body>
        <h1>Certificado de Nacimiento</h1>
        <p>Dice que: {persona.nombre}</p>
        <p>Sexo: {persona.sexo}</p>
        <p>Nació en: {persona.lugar_nacimiento}</p>
        <p>El día: {persona.fecha_nacimiento}</p>
        <p>Padre: {persona.padre}</p>
        <p>Nacionalidad: {persona.nacionalidad_padre}</p>
        <p>Madre: {persona.madre}</p>
        <p>Nacionalidad: {persona.nacionalidad_madre}</p>
    </body>
    </html>
    '''

    # Guardar el contenido en un archivo HTML
    with open('certificado_nacimiento.html', 'w') as file:
        file.write(contenido_html)

    print("Se ha generado el archivo HTML 'certificado_nacimiento.html'")