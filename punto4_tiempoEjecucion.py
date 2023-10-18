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
  print("La serie de Fibonacci hasta " + str(num) + " usando función iterativa es " + str(serieFibo))
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
  print("La función iterativa se ha ejecutado más rápido que la función recursiva")