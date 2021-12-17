# En Python todo es un objeto, una variable es un nombre que hace referencia a un objeto.
name = "Angel"
age = 22

# En la mayoria de los lenguajes la convención para nombrar variables es camelCase, en Python es snake_case
favorite_language = "Python"

print(age + 5)
print("My name is", name, "and i am", age, "years old")

fact_or_fiction = 6 < 10
print(fact_or_fiction)

# Podemos hacer asignaciones de variables y valores multiples en una sola línea.
a, b = 5, 10
print(a)
print(b)

# La función input nos ayuda a almacenar los datos a traves de la consola.
name = input("Dame tu nombre: ")
# Tambien podemos usar conversion de tipos en conjunto con esta función.
age = int(input("Dame tu edad: "))

# Tarea: convertir farenheit a celcius
farenheit = float(input("Introduzca una temperatura en farenheit: "))
celcius = (farenheit - 32) * (5/9)
print("Temperatura en °c", celcius)
