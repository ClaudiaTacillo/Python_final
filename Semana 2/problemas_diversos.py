#Problemas diversos

def ingresar_nota():

    try:
        nota = float(input("Introduce la nota (0 - 10): "))
        
        if nota >=0 and nota <= 10:
            return nota
        else:
            print("Nota fuera del rango")
            ingresar_nota()
    except:
        print("Ha ocurrido un error, introduzca correctamente la nota")
        ingresar_nota()

def listar_alumnos(cantidad_alumnos):
    lista_alumnos = []
    for i in range(cantidad_alumnos):
        alumno = {}
        alumno["Nombre"] = input(f"'Ingrese el nombre del alumno {i+1}: ")
    
        alumno["Nota_1"] = ingresar_nota()
        alumno["Nota_2"] = ingresar_nota()
        alumno["Nota_3"] = ingresar_nota()
    
        lista_alumnos.append(alumno)
    
    return lista_alumnos

def aprobaron(listado, n):
    c=0

    for i in range(n):
        n1 = listado[i]['Nota_1']
        n2 = listado[i]['Nota_2']
        n3 = listado[i]['Nota_3']
        Prom = (n1+n2+n3)/3
        if Prom < 4:
            c+=1
    return n-c

def Average (listado, n):
    Prom_alumno = []
    for i in range(n):
        n1 = listado[i]['Nota_1']
        n2 = listado[i]['Nota_2']
        n3 = listado[i]['Nota_3']
        Prom = (n1+n2+n3)/3
        Prom_alumno.append(Prom)
    return Prom_alumno

def promedio_notas (listado, n):
    Prom_alumno = Average(listado, n)
    Prom_tot = sum(Prom_alumno)/n
    return Prom_tot

def promedio_max_min(listado, n):
    Prom_alumno = Average(listado, n)
    maximo=max(Prom_alumno)
    minimo=min(Prom_alumno)
    a=Prom_alumno.index(maximo)
    b=Prom_alumno.index(minimo)

    print(f"El promedio más alto fue de: {listado[a]['Nombre']}")
    print(f"El promedio más bajo fue de: {listado[b]['Nombre']}")

def incluir_prom (listado, n):
    promedio = Average(listado, n)
    
    for i in range(len(listado)):
        listado[i]['Promedio'] = promedio[i]
    return listado

def buscar(texto, n):
    try:
        for i in range(n):
            if texto in listado[i]['Nombre']:
                return listado[i]
    except:
        return "No se ha encontrado ese nombre."


#Ejercicio 1
n_alumnos = int(input("Ingrese el número de alumnos: "))
listado = listar_alumnos(n_alumnos)
listado

#Ejercicio 2
aprobados = aprobaron(listado, n_alumnos)
print(f"La cantidad de aprobados es: {aprobados}")

#Ejercicio 3
promedio = promedio_notas(listado, n_alumnos)
print(f"El promedio del curso es: {promedio}")

#Ejercicio 4
promedio_max_min(listado, n_alumnos)

#Ejercicio 5
new_listado = incluir_prom(listado, n_alumnos)
name = input("Ingrese el nombre a buscar: ")
print(buscar(name, n_alumnos))