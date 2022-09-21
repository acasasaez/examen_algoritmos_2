# examen_algoritmos_2
La solución al examen se encuentra en el siguiente enlace: https://github.com/acasasaez/examen_algoritmos_2.git

En esta prueba se nos propone un ejercicio de POO donde debemos crear dos clases 


Clase 1: Punto


Esta nos permite definir puntos (objetos) del plano cartesiano.


Sus atributos determinarán las coordenadas de los mismos (x,y)


Por otro lado, cuenta con los siguientes métodos:


  1. getters y setters, que nos permiten definir el valor de las coordenadas (en caso contrario se tomará el punto de origen)


  3. show que nos devolverá las coordenadas como una tupla de valores


  5. cuadrante, que nos indicará el cuadrante del eje en el que se encuentra el punto


  7. vector, que nos permite calcular a partir de nuestro punto y  las coordenadas de otro punto el vector que se genera.


  9. distancia, que nos permite calcular la distancia de un punto al nuestro.
  
  Clase 2: Rectangulo
  
  
    1.Creamos una clase rectangulo
    
    
    2. Creamos su constructor, esta clase viene determinada por 2 puntos y la recta que los une será la diagonal de dicho rectángulo
    
    
    3. creamos sus métodos:
      a.Base
      b.Altura
      c.Area
      
Código
1. Class_Punto
```from cmath import sqrt
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

def main():
    if __name__ == "__main__":
        main()
      
2. Class_Rectangulo
from Class_Punto import*
class rectangulo():
    def init (self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2
    
    def set_punto1(self, punto1):
        self.punto1 = punto1
    def set_punto2(self, punto2):
        self.punto2 = punto2

    def get_punto1(self):
        return self.punto1
    def get_punto2(self):
        return self.punto2 

    #def base()
    
    #def altura()
   
    #def area()
   
    
def main():
    if __name__ == "__main__":
        main()
3. Main
from Class_Punto import*
from Class_Rectangulo import*

A= Punto()
B = Punto()
C= Punto()
D = Punto()
A.set_x(2)
A.set_y(3)
B.set_x(5)
B.set_y(5)
C.set_x(-3)
C.set_y(-1)
D.set_x()
D.set_y()
xa = A.get_x()
ya = A.get_y()
xb = B.get_x()
yb = B.get_y()
xc = C.get_x()
yc = C.get_y()
xd = D.get_x()
yd = D.get_y()
puntoA = A.show()
puntoB=B.show()
puntoC=C.show()
puntoD = D.show()
print ("El punto A tiene coordenadas:", puntoA)
print("El punto B tiene coordenadas:", puntoB)
print("El punto C tiene coordenadas:", puntoC)
print("El punto D tiene coordenadas:", puntoD)
A.cuadrante()
C.cuadrante()
D.cuadrante()
AB =A.vector(xb,yb)
BA = B.vector(xa,ya)
distancia_AB =A.distancia(xb,yb)
distancia_BA = B.distancia(xa,ya)
print ("El vector AB=", AB)
print("El vector BA=", BA)

print("La distancia de A a B es",distancia_AB)
print("La distancia de B a A es", distancia_BA)

rectangulo = rectangulo()
rectangulo.set_punto1 (A)
rectangulo.set_punto2(B)


  
  
