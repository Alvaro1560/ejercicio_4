#Elabore un algoritmo que permita ingresar 10 letras cualquiera
#y luego nos indique y luego nos indique cuantas vocales y consonantes se ingresaron.

vocales = ['a', 'e', 'i', 'o', 'u']

texto = input("Ingrese una cadena de 10 letras: ")

# Verificar que el texto tenga exactamente 10 caracteres y solo letras
while len(texto) != 10 or not texto.isalpha():
    print("El texto debe tener exactamente 10 letras.")
    texto = input("Ingrese una cadena de 10 letras: ")

# Convertir el texto a minúsculas para facilitar la comparación
texto = texto.lower()

# Inicializar contadores de vocales y consonantes
contador_vocales = 0
contador_consonantes = 0

# Iterar sobre cada letra del texto
for letra in texto:
    if letra in vocales:
        contador_vocales += 1
    else:
        contador_consonantes += 1
