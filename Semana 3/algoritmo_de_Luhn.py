def luhn(n_tarjeta):

    suma = 0

    alt = False

    i = len(n_tarjeta) - 1

    valor = 0
    
    while i >= 0:
        valor = int(n_tarjeta[ i ])
        if alt:
            valor = valor * 2
            if valor > 9:
                valor = (valor % 10) + 1  

        suma = suma + valor
        alt = not alt 
        i -= 1

    if suma % 10 == 0:
        return True
    else:
        return False

def tipo_tarjeta(n_tarjeta):        
    lu = luhn(n_tarjeta)
    le = len(n_tarjeta)
    if lu and n_tarjeta[0] == "4" and (le >= 13 or le <= 16):
        return "VISA"
    elif lu and n_tarjeta[0] == "3" and le == 15:
        return "AMEX"
    elif lu and n_tarjeta[0] == "5" and le == 16:
        return "MASTERCARD"
    else :
        return "Inválido"
        
n = input("Ingrese número de tarjeta: ")
luhn(n)
t = tipo_tarjeta(n)

print("Number: {} \n{}".format(n, t))

    