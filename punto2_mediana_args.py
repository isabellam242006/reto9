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