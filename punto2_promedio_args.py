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