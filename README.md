# reto_9
1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

```python
if __name__ == "__main__":
    C = int(input("ingrese el número de contagiados actuales: "))
    D = int(input("ingrese el número de días: "))
    total_contagiados_funcion = lambda C,D: C*(2**D)
    total_contagiados = total_contagiados_funcion(C,D)
    print("Hasta el día " + str(D) + " hay " + str(total_contagiados) + " contagiados en total")
```
```python
if __name__ == "__main__":
    N= int(input("ingrese el número de gallinas: "))
    M= int(input("ingrese el número de gallos: "))
    K= int(input("ingrese el número de pollitos: "))
    total_carne = (lambda X,Y,Z: (6*X)+ (7*Y) + (Z))(N,M,K)
    print("El total de carne es " + str(total_carne) + " kilos")
```
```python
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
```python
def calcular_promedio(*args) ->float:
    for i in args:
        promedio = sum(args)/5
    return promedio

if __name__ == "__main__":
    a = int(input("Ingrese primer número: "))
    b = int(input("Ingrese segundo número: "))
    c = int(input("Ingrese tercer número: "))
    d = int(input("Ingrese cuarto número: "))
    e = int(input("Ingrese quinto número: "))
    print("El promedio es " + str(calcular_promedio(a,b,c,d,e)))
```
```python
import numpy as np

def calcular_mediana(*args):
    for i in args:
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
```python
def calcular_orden_ascendente(*args):
    for i in args:
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

6. Link al perfil de Linkedin:
https://www.linkedin.com/in/isabella-moreno-14ba80228

