texto_ingresado = input("Ingrese el texto que desea analizar: ")
texto_ingresado = texto_ingresado.lower()
print("Ingrese las 3 letras que desea analizar: ")
letra1 = (input("Ingrese la primera letra: "))
letra2 = (input("Ingrese la segunda letra: "))
letra3 = (input("Ingrese la tercera letra: "))
cantidad_letra1 = texto_ingresado.count(letra1)
cantidad_letra2 = texto_ingresado.count(letra2)
cantidad_letra3 = texto_ingresado.count(letra3)
print(f"La cantidad de {letra1} es: {cantidad_letra1}")
print(f"la cantidad de {letra2} es: {cantidad_letra2}")
print(f"la cantidad de {letra3} es: {cantidad_letra3}")

#Contador de palabras

palabras = texto_ingresado.split()
print(f"El texto tiene {len(palabras)} palabras")

#Primera y ultima letra del texto
print(f"La primera letra del texto es {texto_ingresado[0]} y la ultima {texto_ingresado[-1]}")

#Invertir el orden de las palabras

texto_invertido = palabras[::-1]
print(" ".join(texto_invertido))

#Revisar si existe una palabra en el texto
booleano = "python"in palabras
if booleano == True:
    print("El texto tiene la palabra python")
else:
    print("El texto no tiene la palabra python")