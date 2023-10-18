# reto_9
1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

*En cada uno de los programas de este punto se utilizó lambdas par definir una función en una sola línea de código*

```python
#En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones.
#Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A

if __name__ == "__main__":
    C = int(input("ingrese el número de contagiados actuales: "))
    D = int(input("ingrese el número de días: "))
    total_contagiados_funcion = lambda C,D: C*(2**D)
    total_contagiados = total_contagiados_funcion(C,D)
    print("Hasta el día " + str(D) + " hay " + str(total_contagiados) + " contagiados en total")
```
```python
#Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

if __name__ == "__main__":
    N= int(input("ingrese el número de gallinas: "))
    M= int(input("ingrese el número de gallos: "))
    K= int(input("ingrese el número de pollitos: "))
    total_carne = (lambda X,Y,Z: (6*X)+ (7*Y) + (Z))(N,M,K)
    print("El total de carne es " + str(total_carne) + " kilos")
```
```python
#Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno.
#Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

if __name__ == "__main__":
    P = int(input("ingrese el número de panes: "))
    M = int(input("ingrese el número de bolsas de leche: "))
    H = int(input("ingrese el número de huevos: "))
    B = int(input("ingrese el valor del billete en pesos: "))
    vueltas= (lambda a,b,c,d: d - ((300 * a) + (3300 * b) + (350 * c)))(P,M,H,B)

if vueltas < 0:
    print("El billete no alcanza para comprar todo eso")
else:
    print("Las vueltas son " + str(vueltas) + " pesos")
```
2.De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

*Para cada programa se usó ```args``` pensando en la posibilidad de utilizar cualquier número de variables (En este caso se solicitan 5 variables, pero la función creada se puede utilizar para el número de variables que sea necesario)*
```python
#Escriba un programa que pida 5 números reales y calcule el promedio

def calcular_promedio(*args) ->float:
  promedio = sum(args)/len(args)   #El len(args) permite dividir la suma de los elementos entre el número de elementos
  return promedio

if __name__ == "__main__":
    a = int(input("Ingrese primer número: "))
    b = int(input("Ingrese segundo número: "))
    c = int(input("Ingrese tercer número: "))
    d = int(input("Ingrese cuarto número: "))
    e = int(input("Ingrese quinto número: "))
    print("El promedio es " + str(calcular_promedio(a,b,c,d,e)))
```
*La mediana se calculó de dos formas. Utilizando la propiedad misma del arreglo que se crea con ```args``` para encontrar el elemento del medio (En su defecto se ecnontrará el elemento de la mitad porque se tratan de 5 números, en el caso de que fuera un número de elmentos par, entonces se calcurá el promedio de los 2 números que se encuentren en la mitad). La otra forma es utilizar una función importada para calcular la mediana.*
```python
#Escriba un programa que pida 5 números reales y calcule la mediana

def calcular_mediana(*args):
  orden = sorted(args)
  n = len(args)
  if n%2!=0:
    mediana = orden[n//2]
  else: mediana = (orden[n//2] + orden[(n//2)+1]/2)
  return mediana

if __name__ == "__main__":
    a = int(input("Ingrese primer número: "))
    b = int(input("Ingrese segundo número: "))
    c = int(input("Ingrese tercer número: "))
    d = int(input("Ingrese cuarto número: "))
    e = int(input("Ingrese quinto número: "))
    print("La mediana es " + str(calcular_mediana(a,b,c,d,e)))
```
```python
# Mediana utilizando función importada

import numpy as np
def calcular_mediana(*args):
  mediana = np.median(args)
  return mediana

if __name__ == "__main__":
    a = int(input("Ingrese primer número: "))
    b = int(input("Ingrese segundo número: "))
    c = int(input("Ingrese tercer número: "))
    d = int(input("Ingrese cuarto número: "))
    e = int(input("Ingrese quinto número: "))
    print("La mediana es " + str(calcular_mediana(a,b,c,d,e)))
```
*En este caso se utilizó la función ```sorted``` que sirve para ordenar la tupla generada en este caso con ```args``` de forma ascendente. La función ```sort``` no es posible usarla con tuplas, por lo que no se utiliza.*
  
```python
#Escriba un programa que pida 5 números reales y los orden ascendentemente

def calcular_orden_ascendente(*args):
  orden = sorted(args)    
  return orden

if __name__ == "__main__":
    a = int(input("Ingrese primer número: "))
    b = int(input("Ingrese segundo número: "))
    c = int(input("Ingrese tercer número: "))
    d = int(input("Ingrese cuarto número: "))
    e = int(input("Ingrese quinto número: "))
    print("El orden ascendente es " + str(calcular_orden_ascendente(a,b,c,d,e)))
```
3.Escriba una función recursiva para calcular la operación de la potencia.
```python
def potencia_recursiva(a: float, b: int):
  if b==1:
    return a
  elif b == 0:
    return 1
  else:
    return a * potencia_recursiva(a, (b-1))

if __name__ == "__main__":
  a= float(input("Ingrese un número: "))
  b= int(input("Ingrese la potencia a la que quiere elevar ese número: "))
  potencia = potencia_recursiva(a,b)
  print( str(a) + " elevado a " + str(b) + " es " + str(potencia))
```
4. Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.

*Para este punto se utilizó la plantilla dada para comparar la diferencia de tiempo de ejecución entre las dos funciones. Se estableció una diferencia de 5 segundos como significativa (Aunque este valor puede variar)*
```python
import time

start_time_1 = time.time()
def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fiboRecursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " usando función recursiva es " + str(serieFibo))


end_time_1 = time.time()

timer1 = end_time_1 - start_time_1
print("El tiempo de ejecución es de " + str(timer1))


start_time_2 = time.time()
def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
  
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

if __name__ == "__main__":
  num = int(input("Ingrese el mismo numero: "))
  serieFibo = fibo(num)
  print("La serie de Fibonacci hasta " + str(num) + " usando función convencional es " + str(serieFibo))
end_time_2 = time.time()

timer2 = end_time_2 - start_time_2
print("El tiempo de ejecución es de " + str(timer2))
diferencia = abs(timer1-timer2)
print("La diferencia en el tiempo de ejecución de ambas funciones es de " + str(diferencia))

if diferencia > 5:
  print("La diferencia en el tiempo de ejecución es significativa cuando el número dado es " + str(num))
else:
  print("La diferencia aún no es significativa cuando el número dado es: " + str(num))

if timer2>timer1:
  print("La función recursiva se ha ejecutado más rápido que la función convencional")
else:
  print("La función convencional se ha ejecutado más rápido que la función recursiva")
```
5. Crear cuenta en stackoverflow y adjuntar imagen en el repo

![image](https://github.com/isabellam242006/reto_9/assets/142249384/e42cbea9-83d6-460f-869c-516a70cd6ee7)

6. Link al perfil de Linkedin:
https://www.linkedin.com/in/isabella-moreno-14ba80228

