import string

def caesar (k, plain_text):
    Alfabeto = string.ascii_lowercase
    cipher_text = ''
    for l in plain_text:
        
        if l.lower() in Alfabeto:
            p = Alfabeto.find(l.lower())
            c = (p + k) % 26
            
            if l.isupper():
                cipher_text += cipher_text.join(Alfabeto[c].upper())
            else:
                cipher_text += cipher_text.join(Alfabeto[c])
        else:
            cipher_text += cipher_text.join(l)
    return cipher_text

k = int(input("Ingrese el valor de k: "))
plain_text = input("Ingrese el texto a cifrar: ")

cipher_text  = caesar (k, plain_text)

print(f"texto encriptado: {cipher_text}")