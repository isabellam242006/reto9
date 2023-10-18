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