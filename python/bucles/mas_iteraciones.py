# creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola maquina"
numeros =[2,5,8,10]

for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    
   
#iterando un bucle con la sentencia "continue", muy útil para evitar ejecutar ciertas partes del código bajo condiciones específicas, sin detener todo el bucle.   
    
for fruta in frutas:
    if fruta == "granada" :
        continue # Omite la impresión cuando fruta es granada
    print(f"Me gusta mucho una {fruta}")
    
# evitar que el bucle siga ejecutandose con la sentencia break, es util cuando quieres agilizar el programa envitando iteracciones innecesarias

for fruta in frutas:
    if fruta == "pera":
        break # finaliza el bucle llega a pera
    else:
        print(f"Hoy prefiero tomarme una {fruta}")    
        
# recorrer un string        

for letra in cadena:
    print(letra)
    
# bucle for en una sola linea de codigo (duplicando los numeros) 
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
