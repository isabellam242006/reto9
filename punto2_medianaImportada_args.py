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