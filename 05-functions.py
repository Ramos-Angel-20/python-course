# Podemos usar la palabra reservada pass para crear una función que no haga nada
def nada():
    pass

# Podemos definir parámetros y valores por defector para esos párametros,
# si al momento de ejecutar la función nos le pasamos parámetros, automáticamente
# se toma el valor por defecto. Los parámetros opcionales deben estar AL FINAL de todo
# el listado de párametros


def output_text(text="default") -> None:
    print("Welcome to the program")
    print("Its nice to meet you")
    print("xd")
    print(text)


output_text("Camulo")

# De esta forma usamos los keyword arguments
output_text(text="Gaducito")

# Podemos definir el tipo de retorno de una función (int, float, str, bool, ...)


def get_number(number: int) -> int:
    return number



