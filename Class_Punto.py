from cmath import sqrt
import math
#Creamos la clase Punto y definimos el método constructor para crear puntos facilmente
import math
class Punto():
    def init (self, X=0 ,Y=0):
        self.x = X
        self.y = Y
#Creación de setters and getters: Métodos de acceso a los atributos de una clase

#Creamos los "set" que nos permiten modificar el valor de su respectivo atributo
    def set_x(self,X=0):
        self.x=X
    def set_y(self,Y=0):
        self.y=Y
#Creamos los "get" que nos permiten mostrar el valor de su respectivo atributo
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
#Creamos el método show que nos devuelve  la tupla de coordenadas
    def show (self):
        return (self.x, self.y)