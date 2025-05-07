# Estilos de escritura de variables

# Variable con estilo camelCase (uso en JAVA)
nombreCompletoDeTuEmpresa = "Land Rover"

# Variable con estilo snake_case (uso en PYTHON)
nombre_completo_de_tu_empresa = "Land Rover"

# Ejemplo sencillo de como operar con numeros usando diversas variables
a = 2
b = 3
c = a+b

print(c)

# Las variables pueden sufrir modificaciones en sus valores,abajo un ejemplo de como modificar una de ellas con mismo nombre y distinto contenido (priorizará el ultimo valor declarado)

nombre = "Ismael"
nombre = "Alberto"

print(nombre)

# Las variables que contienen numeros cuando usan y combinan simultaneamente operadores de asignación (+, -, =) como el siguiente ejemplo viene a decir también que la variable puede alterar su valor numérico anteponiendo un simbolo matemático (sea de sumar o restar) delante del igual para poder incrementarlo o disminuirlo y al igual que en texto también la última declaración es la que prevalecerá

numero = 10
numero +=5
numero -=7

print(numero)

# Concatenación o suma de strings

huesped = "Sasha"
saludo = "Hola " + huesped + " ¿Como estás?"
# Antes de imprimir nunca olvidar que dentro de las comillas de un string un espacio vacio suma como un caracter más,los cuales son usados para separar la suma o concatenación de strings para que la totalidad del texto aparezca bien redactado respetando la separación entre palabras.
print(saludo)

# Concatenación de strings + numeros mediante el uso de llaves {} (usando letra f delante para indicar que se le da formato a la variable contenida en las llaves)

turno = 5
dependiente = f"Hola {turno} ¿Que desea?"

print(dependiente)

# Concatenación de strings + booleanos mediante el uso de llaves {} (usando letra f delante para indicar que se le da formato a la variable contenida en las llaves)

declaro = True
conclusion = f"Its {declaro} this question"

print(conclusion)

# En los siguientes 2 ejemplos se usa con booleanos los operadores de verificacion o pertenencia (it, not in) llamado in para comprobar si una porcion de texto o string esta o no dentro de la variable indicada a continuacion.

ubicacion = True
localiza = f"su traduccion es {True}"

print("meli" in localiza)

dictar = False
veredicto = f"That statement is {dictar}"

print("ola" not in veredicto)

# Ejemplo de uso de booleano donde aprendemos la influencia del case sensitive dentro del codigo ASCII al distinguir minusculas de mayusculas

encuentro = True
conversacion = f"Hola {encuentro} ¿Como estas?"

print("hola" in conversacion) # En este caso al empezar "Hola" con mayuscula y printar con minuscula, lo reconoce como falso al ser un caracter distinto en el ASCII

