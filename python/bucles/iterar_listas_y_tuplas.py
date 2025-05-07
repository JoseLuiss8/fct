# iterando listas

animales = ["gato","perro","loro","cocodrilo"]
numeros = [10,62,12,72]

# recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a : {animal}")


# recorriendo la lista numeros y multiplicando cada valor por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)


# iterando sobre 2 listas en el mismo bucle con la funcion zip de manera paralela y simultanea.
for numero,animal in zip(animales,numeros):
    print(f"recorriendo primera lista: {numero}")
    print(f"recorriendo segunda lista: {animal}")
    

#maneras no adecuadas de recorrer una lista, ya sea con indice o sin indice. 
    
for num in range(5,10): #sino le ponemos un numero al inicio del rango(donde esta 5), por defecto interpretra que tiene que comenzar desde cero.
    print(num)
    
    
for num in range(len(numeros)):
    print(numeros[num])
    
    
# manera adecuada de recorre una lista con su indice.

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es : {indice} y el valor es: {valor}")
    
    
# usando el for/else
for numero in numeros:
    print(f"ejecuntando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    

# IMPORTANTE: TODO LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS
    