# creando diccionarios con dict()
diccionario = dict(nombre="Ismael",apellido="Santos")

print(diccionario)

# las listas nunca pueden ser claves porque son mutables y debemos usar frozenset para incorporar conjuntos

diccionario = {frozenset(["dalto","rancio"]):"jaja"}

print(diccionario)

# los sets no pueden ser claves al ser mutables

#diccionario = {["dalto","rancio","jaja"]}

#print(diccionario)

# creando diccionarios con el metodo fromkeys
# sino se especifican valores concretos para las claves nos devolvera none(vacio) por defecto

diccionario = dict.fromkeys(["nombre","apellidos","suscriptores"])

print(diccionario)

diccionario = dict.fromkeys("ABCDE")

print(diccionario)

diccionario = dict.fromkeys("ABCDE","VALOR2")

print(diccionario)

# las tuplas si pueden ser claves al ser inmutables.

diccionario = {("dalto","rancio","jaja")}

print(diccionario)