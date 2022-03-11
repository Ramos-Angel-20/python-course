salutation = "Mr. Kermit the Frog"

# El metodo "startswith" devuelve True si
# el string comienza con el substring que 
# le pasamos
print(salutation.startswith("M")) # -> True
print(salutation.startswith("Mr")) # -> True
print(salutation.startswith("Mr.")) # -> True
print(salutation.startswith("m")) # -> False

# El metodo "endswith" funciona igual que "startswith",
# solo que busca el substring al final en lugar de al principio
print(salutation.endswith("g")) # -> True
print(salutation.endswith("og")) # -> True
print(salutation.endswith("Frog")) # -> True
print(salutation.endswith("frog")) # -> false