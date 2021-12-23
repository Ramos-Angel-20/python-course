# string slicing, sirve para extraer uno o mas caracteres de un string.
address = "Attractive Street, Beverly Hills, CA 90210"

# Para tomar un rango de caracteres de un string podemos usar los corchetes con el 
# operador <indice inicial>:<indice final>
print(address[0:3])
# Como se ve en el ejemplo, empezamos en la posición 0 del string y terminamos
# en la posicion 3, pero lo que haya en la posición 3 no se incluye.

#Tambien funcionan los indices negativos.
print(address[-8:-6])

name = "Angel Ramos"
# Podemos hacer el slicing de strings en pasos, en el ejemplo en lugar de agarrar de 1 en 1, vamos de 2 en 2
print(name[0:11])
print(name[0:11:2])