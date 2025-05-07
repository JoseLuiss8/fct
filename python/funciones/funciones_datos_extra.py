# creando una funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante = frase("Ismael","Santos","motivador")
print(frase_resultante)

# creando la misma funcion pero con un parametro opcional y un valor por defecto

def frase_distinta(nombre,apellido,adjetivo = "torpe"):
    return f"Hola {nombre} {apellido} eres muy {adjetivo}"

frase_definitiva = frase_distinta("Ismael","Santos","astuto")
print(frase_definitiva)