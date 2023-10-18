#Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

if __name__ == "__main__":
    N= int(input("ingrese el número de gallinas: "))
    M= int(input("ingrese el número de gallos: "))
    K= int(input("ingrese el número de pollitos: "))
    total_carne = (lambda X,Y,Z: (6*X)+ (7*Y) + (Z))(N,M,K)
    print("El total de carne es " + str(total_carne) + " kilos")