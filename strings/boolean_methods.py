""" Metodo islower() devuelve True si todas las letras de un string son minusculas """
print("winter".islower()) 
print("winter#5432@".islower())

""" Metodo isupper() devuelve True si todas las letras de un string son mayusculas  """
print("SUMMER".isupper())

""" Metodo istitle() devuelve True si todas las letras de cada palabra en un string son mayusculas """
print("The Cruel Intentions".istitle()) #Devuelve True
print("The cruel intentions".istitle()) #Devuelve False

""" Metodo isalpha() devuelve True si todos los elementos de un string son parte del alfabeto """
print("fwfwegRTW".isalpha()) #Devuelve True
print("fwfwegRTW4".isalpha()) #Devuelve False, 4 no es parte del alfabeto

""" Metodo isnumeric() devuelve True si todos los elementos de un string son numeros """
print("51".isnumeric()) #Devuelve True
print("Area 51".isnumeric()) #Devuelve False

""" Metodo  isalnum() devuelve True si todos los caracteres de un string son alfanumericos (numeros y letras) NO SIMBOLOS """
print("Area51".isalnum()) #Devuelve True
print("Area 51".isalnum()) #Devuelve False (por el espacio)
print("Area".isalnum()) #Devuelve True
print("51".isalnum()) #Devuelve True


""" Metodo isspace() devuelte True si el string consta unicamente de espacios """
print(" ".isspace()) #Devuelve True
print("              ".isspace()) #Devuelve True
print("  4 ".isspace()) #Devuelve False