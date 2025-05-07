numeros = [4,7,1,42,15]

# encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# redondeando a 6 decimales
numero = round(12.345678,6) # el segundo parametro se usa para indicar el numero de decimales a printar

print(numero)

# retorna False -> 0, vacio,False, None \ True, cadena, datos no vacios.(
resultado_bool = bool("soyverdadero")

print(resultado_bool)

#retorna True si todos los valores son verdaderos
resultado_all = all([234,"true",[344,23]])

print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)
