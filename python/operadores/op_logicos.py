# EXISTEN 3 TIPOS

#AND (efectivo si se cumplen ambas condiciones)
resultado = True & True # Devuelve True
resultado_2 = False & True # Devuelve False
resultado_3 = True & False # Devuelve False
resultado_4 = False & False # Devuelve False

edad = 25
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("Puedes conducir.")


#OR (efectivo si unicamente se cumpla una sola condicion)

resultado_5 = True | True # Devuelve True
resultado_6 = False | True # Devuelve True
resultado_7 = True | False # Devuelve True
resultado_8 = False | False # Devuelve False

dia_es_finde = True
es_finde_o_vacaciones = False
if dia_es_finde or es_finde_o_vacaciones:
    print("Es día de descanso.")


#NOT (invierte el valor que se nos ha dado)

resultado_9 = not True # Devuelve False
resultado_10 = not False # Devuelve True

usuario_autenticado = False
if not usuario_autenticado:
    print("Debe iniciar sesión.")
