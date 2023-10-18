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