def encripta():
    
    import string
    ALFABETO = string.ascii_lowercase
    plaintext = input("Ingrese el texto a encriptar: ")
    
    llave = input("Ingrese la llave: ")
    ciphertext =""
    if len(llave)!=26:
        print("La llave debe tener 26 caracteres")
        encripta()
    elif not llave.isalpha():
        print("La llave tiene caracteres no alfabeticos") 
        encripta()      
    else:
        for l in plaintext:
                    
            if l.lower() in ALFABETO:
                c = ALFABETO.find(l.lower())
        
                if l.isupper():
                    ciphertext += ciphertext.join(llave[c].upper())
                else:
                    ciphertext += ciphertext.join(llave[c].lower())
            else:
                ciphertext += ciphertext.join(l)
                
    print("Texto plano: ", plaintext)
    print("Texto encriptado: ", ciphertext)
    print("0")

encripta()