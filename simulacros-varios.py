# Datos ejemplo para calculos en porcentajes
curso_dalto = 50  # duración del curso Dalto en horas
otros_cursos_min = 40
otros_cursos_max = 60
otros_cursos_promedio = 50

# Cálculos
diferencia_con_min = ((otros_cursos_min - curso_dalto) / otros_cursos_min) * 100
diferencia_con_max = ((otros_cursos_max - curso_dalto) / otros_cursos_max) * 100
diferencia_con_promedio = ((otros_cursos_promedio - curso_dalto) / otros_cursos_promedio) * 100

print(f"Diferencia con mínimo: {diferencia_con_min:}%")
print(f"Diferencia con máximo: {diferencia_con_max:}%")
print(f"Diferencia con promedio: {diferencia_con_promedio:}%")

#Funcion con valor predeterminado para un parametro.

def despedirse(nombre="Amigo"):
    print(f"Adiós, {nombre}!")

# Ejecutar sin pasar argumento
despedirse()

# Ejecutar pasando un argumento
despedirse("Carlos")


#Funcion que realiza varias acciones

def operaciones(a, b):
    suma = a + b
    resta = a - b
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")

# Ejecutar la función
operaciones(10, 4)

# ejemplo sencillo para generar la secuencia de Fibonacci en Python:

# Número de términos que deseas generar
n = 10

# Inicialización de los primeros dos términos
a, b = 0, 1

# Lista para almacenar la secuencia de Fibonacci
fibonacci_sequence = []

for _ in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b

print(f"La secuencia de Fibonacci con {n} términos es:")
print(fibonacci_sequence)
