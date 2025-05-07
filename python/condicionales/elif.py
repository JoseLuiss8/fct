# CONDICIONAL SIMPLE: Estructura y ejemplos de funcionamiento 

ingreso_mensual = 300

if ingreso_mensual > 10000:
    print("gozas de salud economica")
    
elif ingreso_mensual > 1000:
    print("te cuesta llegar a fin de mes")
    
elif ingreso_mensual > 500:
    print("te cuesta llegar a fin de mes")
    
elif ingreso_mensual > 200:
    print("te cuesta llegar a fin de mes")    
    
else:
    print("andas canino")
    

# CONDICIONALES ANIDADOS: Estructura y ejemplos de funcionamiento.

ingresos_mensuales = 72000
gastos_mensuales = 80000

if ingresos_mensuales > 10000:
    if gastos_mensuales < 7000:
        print("puedes estar tranquilo")
    else:
        print("debes revisar tus gastos")
        
        
if ingresos_mensuales > 10000:
    if ingresos_mensuales - gastos_mensuales > 3000:
        print("puedes estar tranquilo")
    else:
        print("debes revisar tus gastos")
        
        
if ingresos_mensuales > 10000:
    if ingresos_mensuales - gastos_mensuales < 0:
        print("tienes deficit")
    elif ingresos_mensuales - gastos_mensuales > 3000:
        print("no te preocupes")                
    else:
        print("debes revisar tus gastos")
        