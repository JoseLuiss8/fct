# LISTA (su contenido SI puede modificarse)
lista = ["Jose Luis", "Land Rover", "True", "1.85"]

print(lista[1]) 
# Aunque llamemos al elemento 1 y printe el segundo elemento de la lista,python siempre empieza a contar desde cero.

# Ejemplo de modificación llevada a cabo
lista [3] = "figuron"

print(lista [3])

# TUPLA (su contenido total puede modificarse pero el de sus elementos)
tupla = ("Jose Luis", "Land Rover", "True", "1.85")

print(tupla [0])

# Ejemplo de modificacion NO llevada a cabo

#tupla[3] = "figuron"

print(tupla [3])

# Set ( al igual que en las tuplas ,se puede modificar el contenido total del conjunto yel orden de los elementos pero nunca el contenido de estos ultimos)
conjunto = {"Jose Luis", "Land Rover", "True", "1.85"}

conjunto = {"el cambio es efectivo"}

print(conjunto) # Solo se puede printar el cojunto y nunca sueltos los elementos individuales

# DICCIONARIO
diccionario = {
    'nombre' : "Jose Luis" ,
    'empresa' : "Land Rover" ,
    'esta aprendiendo' : True ,
    'estatura' : 1.79 ,
    'dato_duplicado' : "Land Rover"
}

print(diccionario ['estatura'])

print(lista[2])