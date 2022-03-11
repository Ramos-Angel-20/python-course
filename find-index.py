browser = "Google Chrome"

# El metodo "find" de los string devuelve el indice
# de donde esta el substring, si no lo encuentra devuelve
# -1, si el substring aparece mas de 1 vez devuelve el indice
# del primero que encuentre.
print(browser.find("C")) 

# Exite el metodo rfind, que es una variante del metodo find, 
# trabaja igual, solo que si el caracter que le pasamos aparece
# mas de una vez, nos devuelve el indice de su ultima aparición.
print(browser.rfind("e")) # -> devuelve <int> 12

# Funciona igual a "find", con la diferencia de que si no 
# encuentra el elemento nos devuelve un ValueError y 
# creshea el programa.
print(browser.index("C"))
# De este metodo tambien tenemos la variante rindex, este
# nos devuelve el indice de la ULTIMA vez que aparece el caracter
# en caso de que no aparezca nos devuelve un ValueError



def multiply(arr, by, n):
    if (n == 10):
        arr.append(by * 10)
        return arr
    arr.append(by * n)
    return multiply(arr, by, n+1)

data = multiply([], 9, 1)
print(data)

multiply_two = lambda x, y : x * y