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
#Creamos el método cuadrante que nos permite identificar el cuadrante al que pertenece nuestro
#punto
    def cuadrante(self): 
        if self.x == 0 and self.y== 0:
            print("El punto es el origen de coordenadas")
        elif self.x == 0 and self.y != 0:
            print("El punto se encuentra en el eje de ordenada")
        elif self.x != 0 and self.y== 0:
            print("El punto se encuentra en el eje de abcisas")
        elif self.x > 0 and self.y>0:
            print("El punto esta en el primer cuadrante")
        elif self.x < 0 and self.y >0:
            print("El punto esta en el segundo cuadrante")
        elif self.x< 0 and self.y< 0:
            print("El punto esta en el tercer cuadrante")
        elif self.x > 0 and  self.y< 0:
            print("El punto esta en el cuarto cuadrante")
#Creamos el método vector 
#Le pasamos por parámetro unas nuevas coordenadas x, y de un punto   
#La función devuelve el vector que va desde nuestro punto hasta el punto cuyas coordenadas hemos pasado por parámetro
    def vector(self, x=0,y=0):
        a = x - self.x  
        b =y - self.y
        vector2 = (a,b)
        return vector2

#Creamos el método distancia 
#Calcula la distancia entre un punto (x,y) cuyas coordenadas pasamos por parámetro y nuestro punto.
    def distancia (self, x=0,y=0):
        d = math.sqrt((x-self.x)**2 + (y-self.y)**2)
        return d