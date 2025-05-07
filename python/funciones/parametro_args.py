# forma no optima de sumar valores
#def suma(lista):
    #numeros_sumados = 0
    #for numero in lista:
        #numeros_sumados = numeros_sumados + numero
    #return numeros_sumados    

#resultado = suma([5,3,9,10,20])

# forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])

print(resultado2)


# lo mismo que arriba pero utilizando el operador * como argumento (*args), siempre hay que usarlo al final porque sino bloquea todo lo que se escribiera despues.

def suma(nombre,*numeros): # cuando ponemos un * siempre delante del nombre del parametro nos esta indicando en este caso que con todos los argumentos que le asignemos los va convertir en un solo numero precedido de una suma previa
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Lucas",5,3,9,10,20,3)
print(resultado)

