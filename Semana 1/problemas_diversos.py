#Problemas diversos

#Problema 1
ci = float(input("Ingrese la cantidad inicial: "))

for i in range(1,4,1):
    ci = ci*104/100
    print(f"El monto para el año {i} será: {round(ci,2)}")

#Problema 2
import math
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

d = b**2 - 4*a*c

while a != 0:
    if d <0:
        print("No existe solución real")


    elif d == 0:
        x = -b / (2*a)
        print(f"Existe una solución doble: {x}")

    else:
        x1 = (-b + math.sqrt(d))/2*a
        x2 = (-b - math.sqrt(d))/2*a
        print(f"Las soluciones son {x1} y {x2}")
    break