#En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones.
#Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A

if __name__ == "__main__":
    C = int(input("ingrese el número de contagiados actuales: "))
    D = int(input("ingrese el número de días: "))
    total_contagiados_funcion = lambda C,D: C*(2**D)
    total_contagiados = total_contagiados_funcion(C,D)
    print("Hasta el día " + str(D) + " hay " + str(total_contagiados) + " contagiados en total")