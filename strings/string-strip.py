empty_space = "        content         "
print(empty_space)

""" Metodo lstrip() quita el espacio vacio del lado izquierdo de un string """
print(empty_space.lstrip())

""" Metodo rstrip() quita el espacio vacio del lado derecho de un string """
print(empty_space.rstrip())

""" Metodo strip() quita el espacio vacio de ambos extremos de un string """
print(empty_space.strip())

""" Tambien se pueden remover substrings de un string """
url = "www.python.org"
print(url.lstrip("w")) #Quita todas las w del lado izquierdo del string
print(url.rstrip("org")) #Quita las palabras org del lado derecho del string