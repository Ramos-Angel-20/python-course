""" Metodo format introducido en python 3.8 """

#name, adjetive, anoun
mad_libs = "{} laughed at the {} {}."
"""
Teniendo estos strings podemos meter valores a los corchetes con el metodo format(), como si fuera 
un Template String de Javascript `${nombre} como estas`.

Si no le pasamos el mismo numero de parametros a format() como los que hay en el string, nos devuelve un 
error, en este caso si de tres parametros solo le pasamos 2 nos dara error.
"""

print(mad_libs.format("Boby", "green", "alien"))
print(mad_libs.format("Jennifer", "silly", "tomato")) 


"""
Pasandole un numero a las llaves {} podemos alterar el resultado en base a la posición
"""
sentence1 = "Hola {0} bienvenido, tienes el rol de {1}"
print(sentence1.format("Angel", "Administrador")) # Hola Angel bienvenido, tienes el rol de Administrador

sentence2 = "Hola {1} bienvenido, tienes el rol de {0}"
print(sentence2.format("Angel", "Administrador")) # Hola Administrador bienvenido, tienes el rol de Angel

sentence3 = "Adios {type} con el nombre {user_name}"
print(sentence3.format(type="Administrador", user_name="Angel"))


def fizzbuzz(limit):
    for i in range(limit + 1):
        if (i == 0):
            continue
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)