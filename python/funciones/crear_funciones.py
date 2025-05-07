# creando una funcion simple
#def saludar():
#    print("Que pasa figura, como va eso?")
    
#ejecutando la funcion simple
#saludar()    

# crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo= sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
        
    else:
        adjetivo = "amor"
        
    
    print(f"Ei {nombre}, compañero {adjetivo} ¿Como va eso?")
    
saludar("Camila","Mujer")    

#  crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return (contraseña) #----> Este uso es adecudado cuando queremos que se oculte la contraseña por el terminal.
    
password = crear_contraseña_random(1) # Este uso es adecuado cuando queremos que se muestre la contraseña por el terminal
frase = f"Tu contraseña nueva es: {password}"
print(frase)

# desempaquetando la funcion

password,primer_numero = crear_contraseña_random(398) # Aqui es donde entran en juego las variables de asignación multiple que sirven para agilizar el funciomamiento del programa en un solo codigo,indicandole en este caso que queremos invocar la funcion usando el primer numero de la contraseña asignada en los argumentos.

# mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue:   {primer_numero}")

