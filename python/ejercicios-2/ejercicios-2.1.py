# haz un programa en el que ingrese la edad y el nombre de sus integrantes para averiguar por el parametro de edad quien es el profesor y quienes son los alumnos

# pedir el nombre y la edad de los compañeros.


# funcion para obtener el asistente y el profesor segun la edad.
def obtener_compañeros(cantidad_de_compañeros):
    
    # creando la lista de los compañeros
    compañeros = []
    
    # ejecutando bucle for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)

        # agregando la informacion a la lista
        compañeros.append(compañero)
        
    # ordenandolos de menor a mayor segun su edad
    compañeros.sort(key=lambda x:x[1]) # esto viene a decir que la lista sera ordenada por el metodo sort usando una funcion lambda cuyo criterio es ordenar los elementos en base al segundo parametro que es edad [1]
    
    # compañeros[x] devuelve una tupla con [nombre,edad] y despues accedemos al nombre para definir al asistente y al profesor
    asistente = compañeros[0][0] # esto viene a decir que la variable accede dentro de la lista compañeros a su primer elemento[0] y despues al primer valor de dicho elemento[0]
    profesor = compañeros[-1][0] # esto viene a decir que la variable accede dentro de la lista compañeros a su ultimo elemento[-1] y despues al primer valor de dicho elemento[0]
    
    # retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

# mostramos el resultado

print(f"El profesor es: {profesor} y su asistente es: {asistente}")    