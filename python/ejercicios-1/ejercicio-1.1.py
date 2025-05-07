#promedio duraciones de los cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_dalto = 1.5

# duración de videos en bruto

bruto_promedio = 5 
bruto_dalto = 3.5

# diferencias de duracion

diferencia_con_min = 100 - curso_dalto / otros_cursos_min * 100
diferencia_con_max = 100 - curso_dalto * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - curso_dalto / otros_cursos_promedio * 100

# calculando el porcentaje del tiempo vacio eliminado.

tiempo_vacio_eliminado = 100 - otros_cursos_promedio * 1000 // bruto_promedio / 10
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // bruto_dalto / 10

# mostrando las diferencias de duracion
print("---------------")
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el mas promedio")
print("---------------")

# mostrando la cantidad de espacios que se eliminan

print(f"El curso de Dalto dura un {tiempo_vacio_eliminado}")
print(f"Este curso elimino el {tiempo_vacio_eliminado}% de tiempo vacio")
print("---------------")

# mostrando diferencias si los cursos duraran 10 horas

print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio *1000 // curso_dalto / 100} horas de otros cursos")
print(f"Ver 10 horas de este curso equivale a ver {curso_dalto *1000 // otros_cursos_promedio / 100} horas de otros cursos")
print("---------------")