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