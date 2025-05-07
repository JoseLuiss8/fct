# creando una funcion que nos devuelva los numeros primos entre el 0 y el argumento que pasamos


# creando una funcion que verifique si un numero es primo

def es_primo(num):
    # verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        # si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    # si termina el bucle, significa que no fue divisible y entonces es primo
    return True

resultado = es_primo(29)
print(resultado)


# creando funcion que retorne una lista con todos los primos
def primos_hasta(num):
    # creamos la lista
    primos = []
    for i in range(3,num+1):
        # verificamos si el valor es primo
        results = es_primo(i)
        # en caso de que sea lo agregamos a la lista
        if results == True: primos.append(i)
    # devolvemos la lista
    return primos

# creamos el resultado llamando a la funcion y lo mostramos
results = primos_hasta(98)
print(results)