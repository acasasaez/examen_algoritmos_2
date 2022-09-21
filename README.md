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
      ```
      

  
  
