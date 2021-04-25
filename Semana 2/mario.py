def mario(height):
    for i in range(height):
        print(" "*(height - i - 1) + "#"*(i + 1))

height = int(input("Ingrese la altura: "))

while not (height > 0 and height <= 8):
    height = int(input("Valor inválido. Ingrese la altura: "))

mario(height)