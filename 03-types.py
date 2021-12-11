# La función type() nos devuelve el tipo de datos de una variable o valor

print(type(5))
print(type(5))

print(type(3.8))
print(type(5.0))

print(type("Computer"))
print(type("Laptop"))

print(type(5) == type(10))
print(type("Computer") == type("Laptop"))
print(type(5) == type(5.0))

print(type([1, 2, 3]))
print(type({"NJ": "Trenton"}))

# Conversión de tipos

# Podemos convertir un número flotante a un entero con la función int(),
# es importante mencionar que esta funcion NO redondea, solo quita los
# valores despues del punto decimal.
print(int(3.14))
print(int(3.99))

# Con int() tambien podemos convertir strings a enteros.
print(int("3"))
# NO podemos convertir strings con apariencia de flotante a entero, ejemplo: int("3.2") -> da error


# La función float() hace lo mismo que int(), con la diferencia de que
# convierte valores a flotante.
print(float("3"))
print(float(3))


# La función str convierte valores a string
print(str(32))
print(str(3.2))
alumnos = {"1": "Angel", "2": "Ruben"}
print(str(alumnos))
print(str(5) + "hello")



