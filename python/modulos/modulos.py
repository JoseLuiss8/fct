# importar un modulo desde otro modulo

import modulo_saludar

saludo = modulo_saludar.saludar("Ismael")
print(saludo)

print(type(modulo_saludar))


# otro ejemplo

import modulo_saludar as m_saludar # usamos la expresion as para dar un nombre de alias a libre eleccion al modulo importado

modulo_saludar = "hola"
saludo = m_saludar.saludar("Lucas")
print(modulo_saludar)