cadena_1 = "Buenas soy Jose Luis"
cadena_2 = "Bienvenido Caballero"
cadena_3 = "Buenas, soy, Jose, Luis"

mayusc = cadena_1.upper() # convierte a mayusculas todo el string

print(mayusc)

minusc = cadena_1.lower() # convierte a minusculas todo el string

print(minusc)

primera_letra_mayusc = cadena_1.capitalize()    # convierte a mayuscula unicamente la primera letra de una palabra

print(primera_letra_mayusc)

busqueda_find = cadena_1.find("n") # busca un string en otro string, si no hay coincidencias devuelve -1

print(busqueda_find)

# Tambien busca un string en otro string , sino hay coincidencias lanza una excepcion

busqueda_index = cadena_1.index("J")

print(busqueda_index)

# si es numerico devolvemos true, sino devolvemos false

es_numerico = cadena_1.isnumeric()

print(es_numerico)

# si es alfanumerico devolvemos true, sino devolvemos false

es_alfanumerico = cadena_1.isalpha()

print(es_alfanumerico)

# busca un string en otro string, si no hay coincidencias devuelve la cantidad de veces que coincida

contar_coincidencias = cadena_2.count("e")

print(contar_coincidencias)

# contamos cuantos caracteres tiene una cadena

contar_caracteres = len(cadena_2)

print(contar_caracteres)

# verificamos si una cadena comienza con otra cadena dada, si es asi devolvemos True

empieza_con = cadena_2.startswith("B")

print(empieza_con)

# verificamos si una cadena finaliza con otra cadena dada, si es asi devolvemos True

finaliza_con = cadena_2.endswith("l")

print(finaliza_con)

# si el valor 1, en el string original, reemplaza el valor 1 del mismo, por el valor 2

cadena_nueva = cadena_2.replace("Bienvenido Caballero", "Bienvenida Señora")

print(cadena_nueva)

# separar strings con el string que le pasemos.

cadena_separada = cadena_3.split(",")

print(cadena_separada)

print(type(cadena_separada))

print(cadena_separada[1])    