#

diccionario = {
    "nombre" : "Ismael",
    "apellido" : "Santos",
    "suscriptores" : 18000
}

print(diccionario)

#mostrara solo las claves

for key in diccionario:
    print(key)

# mostrara claves y valores al completo con el metodo items()
    
for key in diccionario.items():
    print(key)    
    
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es {key} y el valor es: {value}")
        