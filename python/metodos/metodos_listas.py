# creando una lista con el metodo list
lista = list(["Ei", "Pepito", 65])
lista_2=list([False,22,89,131,True])

print(lista)

# devuelve la cantidad de elementos

cantidad_elementos = len(lista)

print(cantidad_elementos)

# agrega un elemento al final de la lista

lista.append("ajajajajaj")

print(lista)

# agregando un elemento a la lista en un indice especifico.

lista.insert(2, "toma moreno")

print(lista)

# agregando varios elementos a la lista

lista.extend([False,2030])

print(lista)

# eliminando un elemento de la lista (por su indice)

print(len(lista))

lista.pop(0)

print(lista)

print(len(lista))

# removiendo un elemento de la lista por su valor

lista.remove("toma moreno")

print(lista)

# ordenando los elementos de una lista (solamente efectivo cuando se trata de numeros o booleanos,otro tipo de caracteres genera excepcion)

lista_2.sort() # de menor a mayor primero los booleanos y despues numeros

print(lista_2)

lista_2.sort(reverse=True) # invierte de mayor a menor el orden para mostrar primero los numeros y luego los booleanos

print(lista_2)

# invirtiendo los elementos de una lista

lista_2.reverse()

print(lista_2)


# eliminando todos los elementos de la lista

lista.clear

print(lista)