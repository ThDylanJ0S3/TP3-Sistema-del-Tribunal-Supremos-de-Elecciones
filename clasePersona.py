################################################
#   Autor: Luis Aguilar y Dylan Meza           #
#   Fecha de creación: 1/11/2023  21:28 pm     #
#   Ultimo cambio: 04/10/2023 4:55 pm          #
#   Version: 3.11.4                            #
################################################
import random
from archivos import *
class Persona:
    def __init__(self,cedula,nombre,apellido1, apellido2, sexo, localidad,fechaNacimiento,padre,madre,nacionalidad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.sexo = sexo
        self.localidad = localidad
        self.fechaNacimiento = fechaNacimiento
        self.padre = padre
        self.madre = madre
        self.nacionalidad = nacionalidad
    
    def getCedula(self):
        return self.cedula

    def setCedula(self, dato):
        self.cedula = dato

    def getNombre(self):
        return self.nombre

    def setNombre(self, dato):
        self.nombre = dato

    def getApellido1(self):
        return self.apellido1
    
    def setApellido1(self,dato):
        self.apellido1 = dato

    def getApellido2(self):
        return self.apellido2
    
    def setApellido2(self,dato):
        self.apellido2 = dato
    
    def getSexo(self):
        return self.sexo
    
    def setSexo(self,dato):
        self.sexo = dato
    
    def getLocalidad(self):
        return self.localidad
    
    def setLocalidad(self,dato):
        self.localidad = dato
        
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    
    def setFechaNacimiento(self,dato):
        self.fechaNacimiento = dato
    
    def getPadre(self):
        return self.padre
    
    def setPadre(self,dato):
        self.padre = dato
    
    def getMadre(self):
        return self.madre
    
    def setMadre(self,dato):
        self.madre = dato
    
    def getNacionalidad(self):
        return self.nacionalidad

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad