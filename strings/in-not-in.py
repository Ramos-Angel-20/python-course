announcement = "The winners of the prize are Boris, Andy and Adam"

# Con el operador "in" podemos buscar un substring dentro
# de un string, esto devuelve True o False, tenemos que 
# tomar en cuenta que es "case-sensitive"
print("Boris" in announcement) # -> True
print("Angel" in announcement) # -> False

# El operador "not in" hace lo opuesto al "in",
# devuelve True si el substring NO esta en el string
print("Angel" not in announcement) # -> True
print("Boris" not in announcement) # -> False