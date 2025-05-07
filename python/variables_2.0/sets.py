# creando un conjunto con set() usando la funcion frozenset

conjunto = set (["Dato 1"])

# metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

# teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}

#verificando si es un subconjunto. No se basa en si el resultado de la suma de ambos coincide sino en encontrar los mismos elementos del primer conjunto en el segundo conjuntoS tambien

resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

print(resultado)

#verificando si es un superconjunto.
#el método .issuperset() se utiliza con conjuntos (set) para verificar si un conjunto dado es un superset de otro conjunto. Es decir, comprueba si todos los elementos del conjunto pasado como argumento están contenidos en el conjunto sobre el que se llama el método.

resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

print(resultado)

# verificar si hay algun numero en comun
#Devuelve True si los conjuntos no comparten ningún elemento y False si tienen al menos un elemento en común.

resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)