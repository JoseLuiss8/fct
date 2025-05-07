# Una función lambda en Python es una función anónima, es decir, una función definida sin un nombre explícito, que se puede crear en una sola línea. Se utilizan principalmente para funciones cortas y de uso temporal, y son útiles cuando necesitas una función sencilla para pasar como argumento a otras funciones, como map(), filter(), o sorted().

numeros = [1,2,3,4,5,6,7,8,9]

# creando una funcion lambda para multiplicar por 2

multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5))

# creando una funcion comun que diga si es par o no
#def es_par(num):
    #if (num%2==0):
        #return True

# usando filter con una funcion comun
#numeros_pares = filter(es_par,numeros)

# creando lo mismo que antes pero con lambda
# filter es una funcion que itera sobre cada uno de los valores de una lista , en este caso numeros
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)

print(list(numeros_pares))