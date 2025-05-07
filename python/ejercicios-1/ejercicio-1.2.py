# le pedimos al usuario que nos escriba una frase (o varias)
frase = input("Hazme un comentario para poder calcular lo que tardas en decirlo:  ")

# creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

# usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_palabras = len(palabras_separadas)

# en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_palabras > 10:
    print("No hace falta tanto")

# calculamos cuanto tardaría en decir las palabras y se lo decimos

print(f"Dijiste {cantidad_palabras} palabras y tardaste {cantidad_palabras/2} segundos en decirlo")

print(f"Dalto es capaz de decirlo en {cantidad_palabras * 100 // 2 *1.3 / 100} segundos")

