
diccionario = {
    "nombre": "Ismael",
    "apellido": "Santos",
    "followers": 525
}

# metodo que devuelve las claves (tambien nos sirve para iterar)

claves = diccionario.keys()

print(claves)

# metodo que devuelve los valores de las claves

claves = diccionario.get("apellido")

print(claves)

# metodo que elimina todos los elementos

#claves = diccionario.clear("")

#print(claves)

# metodo que elimina un elemento o varios

claves = diccionario.pop("followers")

print(claves)

# metodo que itera en un diccionario

diccionario_iterable = diccionario.items()

print(diccionario_iterable)

