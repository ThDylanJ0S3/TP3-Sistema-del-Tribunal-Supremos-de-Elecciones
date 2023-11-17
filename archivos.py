################################################
#   Autor: Luis Aguilar y Dylan Meza           #
#   Fecha de creación: 1/11/2023  21:28 pm     #
#   Ultimo cambio: 04/10/2023 4:55 pm          #
#   Version: 3.11.4                            #
################################################
import pickle
from datetime import datetime
import xml.etree.ElementTree as ET
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
    """
    Función: Genera un archivo HTML con detalles de personas por provincia.

    Esta función crea un archivo HTML que muestra una tabla con información detallada de las personas pertenecientes a una provincia específica.

    - Entrada:
        - nProvincia: Número de la provincia.
        - provincia: Nombre de la provincia.
        - listaPersonas: Lista de objetos que contienen información de las personas registradas.

    - Acciones:
        - Crea un archivo HTML con un encabezado y una tabla.
        - Filtra las personas de la lista por la provincia especificada.
        - Ordena la lista de personas según el sexo y el nombre.
        - Crea una tabla con detalles como cédula, nombre completo, fecha de nacimiento y sexo de cada persona.
        - Guarda el archivo HTML en el directorio actual.

    Nota: La información mostrada en la tabla está organizada por columnas que incluyen cédula, nombre completo, fecha de nacimiento y sexo.
    """
    with open(f"./personasPorProvincia.html","w", encoding="utf-8") as archivo:
            archivo.write("<meta charset='UTF-8'>")
            archivo.write("<html><head><title>Personas por Provincia</title></head><body>")
            archivo.write(f"<h1>Personas de {provincia}</h1>")
            archivo.write("<table>")
            archivo.write("<tr style='background-color: #a2c8cc;'><th>Cedula</th><th>Nombre Completo</th><th>Fecha de Nacimiento</th><th>Sexo</th></tr>")
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
                archivo.write(f"<tr style='background-color: {fondo}'>")
                archivo.write(f"<td>{personas[0]}</td>")
                archivo.write(f"<td>{personas[1]}</td>")
                archivo.write(f"<td>{personas[2]}</td>")
                archivo.write(f"<td>{personas[3]}</td>")
                i += 1
                archivo.write("</tr>")

            archivo.write("</table></body></html>")
            archivo.close() 


def generarHTMLAnno(anno, listaPersonas, listaAnnios):
    """
    Función: Genera un archivo HTML con detalles de personas nacidas a partir de un año específico.

    Esta función crea un archivo HTML que muestra información detallada de personas nacidas a partir del año especificado.

    - Entrada:
        - anno: Año a partir del cual se desea filtrar la información.
        - listaPersonas: Lista de objetos que contienen información de las personas registradas.
        - listaAnnios: Lista de años registrados en el conjunto de personas.

    - Acciones:
        - Crea un archivo HTML con un encabezado y secciones para cada año desde el especificado hasta el año más reciente.
        - Filtra las personas por año de nacimiento.
        - Organiza la información por columnas que incluyen cédula, nombre completo, fecha de nacimiento, sexo, nombre del padre y nombre de la madre.
        - Guarda el archivo HTML en el directorio actual.

    Nota: La información en la tabla está organizada por años, mostrando detalles como cédula, nombre completo, fecha de nacimiento, sexo, nombre del padre y nombre de la madre para cada persona nacida a partir del año especificado.
    """
    with open(f"./personasPorAño{anno}.html","w", encoding="utf-8") as archivoAnno:
        archivoAnno.write("<meta charset='UTF-8'>")
        archivoAnno.write("<html><head><title>Personas por Año</title></head><body>")
        archivoAnno.write(f"<h1>Personas nacidas a partir del año {anno}</h1>")
        
        i = 0
        
        for annoRegistrado in listaAnnios:
            print(annoRegistrado)
            print(listaAnnios)
            if annoRegistrado >= anno:
                archivoAnno.write(f"<h2>Personas nacidas en el año {annoRegistrado}</h2>")
                archivoAnno.write("<table>")
                archivoAnno.write("<tr style='background-color: #a2c8cc;'><th>Cedula</th><th>Nombre Completo</th><th>Fecha de Nacimiento</th><th>Sexo</th><th>Nombre del Padre</th><th>Nombre de la Madre</th></tr>")
                listaImprimir = []
                for persona in listaPersonas:
                    fechaNacimiento = persona.getFechaNacimiento().split("/")
                    if int(fechaNacimiento[-1]) == annoRegistrado:
                        cedula = persona.getCedula()
                        nombre = f"{persona.getNombre()} {persona.getApellido1()} {persona.getApellido2()}"
                        fechaNacimiento = persona.getFechaNacimiento()
                        sexo = persona.getSexo()
                        padre = persona.getPadre()
                        madre = persona.getMadre()

                        listaImprimir.append([cedula, nombre, fechaNacimiento, sexo, padre, madre])

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
            
def generarHTMLTomo(tomo, listaPersonas):
    """
    Función: Genera un archivo HTML con detalles de personas por tomo de cédula.

    Esta función crea un archivo HTML que muestra información detallada de personas asociadas a un tomo específico de la cédula de identidad.

    - Entrada:
        - tomo: Número correspondiente al tomo de la cédula de identidad.
        - listaPersonas: Lista de objetos que contienen información de las personas registradas.

    - Acciones:
        - Crea un archivo HTML con un encabezado que muestra el tomo específico.
        - Filtra y muestra la información de personas asociadas al tomo de la cédula, organizando los datos en una tabla que incluye cédula, nombre completo, fecha de nacimiento, sexo, nombre de la madre y nombre del padre.
        - Guarda el archivo HTML en el directorio actual.

    Nota: La tabla muestra información organizada por cédula, nombre completo, fecha de nacimiento, sexo, nombre de la madre y nombre del padre para cada persona asociada al tomo de la cédula especificado.
    """
    with open(f"./personasPorTomo.html","w", encoding="utf-8") as archivo:
            archivo.write("<meta charset='UTF-8'>")
            archivo.write("<html><head><title>Personas por Provincia</title></head><body>")
            archivo.write(f"<h1>Personas del tomo {tomo}</h1>")
            archivo.write("<table>")
            archivo.write("<tr style='background-color: #a2c8cc;'><th>Cédula</th><th>Nombre Completo</th><th>Fecha de Nacimiento</th><th>Sexo</th><th>Nombre de la madre</th><th>Nombre del padre</th></tr>")
            i = 0
            listaImprimir = []
            #Ciclo para crear cada fila
            for personas in listaPersonas:
                if personas.getCedula().split("-")[1] == tomo:
                    cedula = personas.getCedula()
                    nombre = str(personas.getNombre())+" "+str(personas.getApellido1())+" "+str(personas.getApellido2())
                    nacimiento = personas.getFechaNacimiento()
                    sexo = personas.getSexo()
                    padre = personas.getPadre()
                    madre = personas.getMadre()

                    listaImprimir.append([cedula, nombre, nacimiento, sexo, madre, padre])

            listaImprimir = sorted(listaImprimir, key=lambda x:(x[3]=="F", x[1]))

            for personas in listaImprimir:
                if i % 2 == 0:
                    fondo = "#c5e0dc"
                else:
                    fondo = "#f8edeb"
                archivo.write(f"<tr style='background-color: {fondo}'>")
                archivo.write(f"<td>{personas[0]}</td>")
                archivo.write(f"<td>{personas[1]}</td>")
                archivo.write(f"<td>{personas[2]}</td>")
                archivo.write(f"<td>{personas[3]}</td>")
                archivo.write(f"<td>{personas[4]}</td>")
                archivo.write(f"<td>{personas[5]}</td>")
                i += 1
                archivo.write("</tr>")

            archivo.write("</table></body></html>")
            archivo.close()
            
def generarCertificadoHtml(cedula, listaPersonas):
    """
    Función: Genera un certificado de nacimiento en formato HTML.

    Esta función crea un archivo HTML que contiene información detallada sobre el nacimiento de una persona, identificada por su número de cédula.

    - Entrada:
        - cedula: Número de cédula de la persona para la que se genera el certificado.
        - listaPersonas: Lista de objetos que contienen información de las personas registradas.

    - Acciones:
        - Busca la persona asociada a la cédula proporcionada en la lista de personas.
        - Si encuentra la persona:
            - Crea un archivo HTML que muestra información detallada sobre el nacimiento de la persona, incluyendo su tomo, asiento, nombre completo, sexo, localidad de nacimiento, fecha de nacimiento, nombres de los padres y nacionalidades.
            - Guarda el archivo HTML con el nombre 'certificadoNacimiento.html' en el directorio actual.
        - Si no encuentra la persona:
            - Imprime un mensaje indicando que la persona con la cédula proporcionada no está en la lista.

    Nota: El archivo HTML generado contiene información detallada sobre el nacimiento de la persona, organizada en una tabla con las siguientes secciones: tomo, asiento, cédula, nombre completo, sexo, localidad de nacimiento, fecha de nacimiento, nombre del padre con su nacionalidad, nombre de la madre con su nacionalidad.
    """

    persona = None

    # Buscar la persona con la cédula proporcionada en la lista
    for p in listaPersonas:
        if p.getCedula() == cedula:
            persona = p
            break

    if persona:
        contenidoHtml = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Certificado de Nacimiento</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                h1 {{
                    text-align: center;
                }}
                table {{
                    width: 70%;
                    margin: auto;
                    border-collapse: collapse;
                }}
                th, td {{
                    padding: 8px;
                    border-bottom: 1px solid #ddd;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h1>Certificado de Nacimiento</h1>
            <table>
                <tr>
                    <th>Al tomo:</th>
                    <td>{persona.getCedula().split("-")[1]}</td>
                </tr>
                <tr>
                    <th>Asiento:</th>
                    <td>{persona.getCedula().split("-")[2]}</td>
                </tr>
                <tr>
                    <th>Cita:</th>
                    <td>{persona.getCedula()}</td>
                </tr>
                <tr>
                    <th>Dice que:</th>
                    <td>{persona.getNombre()} {persona.getApellido1()} {persona.getApellido2()}</td>
                </tr>
                <tr>
                    <th>Sexo:</th>
                    <td>{persona.getSexo()}</td>
                </tr>
                <tr>
                    <th>Nació en:</th>
                    <td>{persona.getLocalidad()}</td>
                </tr>
                <tr>
                    <th>El día:</th>
                    <td>{persona.getFechaNacimiento()}</td>
                </tr>
                <tr>
                    <th>Padre:</th>
                    <td>{persona.getPadre()}</td>
                </tr>
                <tr>
                    <th>Nacionalidad:</th>
                    <td>{persona.getNacionalidadPadre()}</td>
                </tr>
                <tr>
                    <th>Madre:</th>
                    <td>{persona.getMadre()}</td>
                </tr>
                <tr>
                    <th>Nacionalidad:</th>
                    <td>{persona.getNacionalidadMadre()}</td>
                </tr>
            </table>
        </body>
        </html>
        '''

        # Guardar el contenido en un archivo HTML
        with open('certificadoNacimiento.html', 'w') as file:
            file.write(contenidoHtml)

        print("Se ha generado el archivo HTML 'certificadoNacimiento.html'")
    else:
        print("La persona con la cédula proporcionada no está en la lista")
        
def generarCertificadoXml(cedula, listaPersonas):
    """
    Función: Genera un certificado de nacimiento en formato XML.

    Esta función crea un archivo XML que contiene información detallada sobre el nacimiento de una persona, identificada por su número de cédula.

    - Entrada:
        - cedula: Número de cédula de la persona para la que se genera el certificado.
        - listaPersonas: Lista de objetos que contienen información de las personas registradas.

    - Acciones:
        - Busca la persona asociada a la cédula proporcionada en la lista de personas.
        - Si encuentra la persona:
            - Crea una estructura XML que contiene información detallada sobre el nacimiento de la persona, incluyendo su tomo, asiento, cédula, nombre completo, sexo, localidad de nacimiento, fecha de nacimiento, nombres de los padres y nacionalidades.
            - Guarda el archivo XML con el nombre 'certificadoNacimiento.xml' en el directorio actual.
        - Si no encuentra la persona:
            - Imprime un mensaje indicando que la persona con la cédula proporcionada no está en la lista.

    Nota: El archivo XML generado contiene información detallada sobre el nacimiento de la persona, estructurada con etiquetas que incluyen el tomo, asiento, cédula, nombre completo, sexo, localidad de nacimiento, fecha de nacimiento, nombre del padre con su nacionalidad, nombre de la madre con su nacionalidad.
    """
    persona = None

    for p in listaPersonas:
        if p.getCedula() == cedula:
            persona = p
            break

    if persona:
        certificado = ET.Element("CertificadoNacimiento")

        alTomo = ET.SubElement(certificado, "AlTomo")
        alTomo.text = persona.getCedula().split("-")[1]

        asiento = ET.SubElement(certificado, "Asiento")
        asiento.text = persona.getCedula().split("-")[2]

        cita = ET.SubElement(certificado, "Cita")
        cita.text = persona.getCedula()

        diceQue = ET.SubElement(certificado, "DiceQue")
        diceQue.text = f"{persona.getNombre()} {persona.getApellido1()} {persona.getApellido2()}"

        sexo = ET.SubElement(certificado, "Sexo")
        sexo.text = persona.getSexo()

        nacioEn = ET.SubElement(certificado, "NacioEn")
        nacioEn.text = persona.getLocalidad()

        elDia = ET.SubElement(certificado, "ElDia")
        elDia.text = persona.getFechaNacimiento()

        padre = ET.SubElement(certificado, "Padre")
        padre.text = persona.getPadre()

        nacionalidadPadre = ET.SubElement(certificado, "NacionalidadPadre")
        nacionalidadPadre.text = persona.getNacionalidadPadre()

        madre = ET.SubElement(certificado, "Madre")
        madre.text = persona.getMadre()

        nacionalidadMadre = ET.SubElement(certificado, "NacionalidadMadre")
        nacionalidadMadre.text = persona.getNacionalidadMadre()

        arbolXml = ET.ElementTree(certificado)

        arbolXml.write("certificadoNacimiento.xml")

        print("Se ha generado el archivo XML 'certificadoNacimiento.xml'")
    else:
        print("La persona con la cédula proporcionada no está en la lista")