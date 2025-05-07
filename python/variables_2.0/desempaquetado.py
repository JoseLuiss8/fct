# ejemplo de encapsulamiento y posterior desempaquetado donde primero asignamos valores dentro de variables compuestas y segundo variables compuestas en el mismo orden que han sido escritas para que sean efectivas.
#IMPORTANTE : De no coincidir el mismo numero de variables y valores nunca funcionara debidamente el encapsulamiento y desempaquetado.

#encapsulamiento mediante una tupla

datos_en_tupla = ("Ismael","Santos",168000)
datos_en_lista = ["Ismael","Santos",168000]

#desempaquetado

nombre,apellido,suscriptores = datos_en_lista

# mostrando resultados

print(suscriptores)

print(nombre)

print(apellido)
