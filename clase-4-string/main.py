

name = "Wilfredo"

last_name = "Barquero Herrera"

# string templates
print(f"Hello {name} {last_name}")

# Concatenation de strings
print(name + " " + last_name)

# Repetition, repite una cadena n veces
print(name * 3)

# Indexing, retorna un caracter
print(name[0])

# Slicing, retorna una subcadena
print(name[0:3])

# Length, retorna la longitud de la cadena
print(len(name))

# Split, separa una cadena en una lista
print(last_name.split(" "))

# Replace, reemplaza una cadena por otra
print(last_name.replace("Barquero", "Perez"))

# Find, retorna la posicion de la primera ocurrencia
print(last_name.find("Barquero"))

# Count, cuenta cuantas veces aparece un caracter
print(last_name.count("r"))

# Upper, todo en mayuscula
print(last_name.upper())

# Lower, todo en minuscula
print(last_name.lower())

# Capitalize, primera letra en mayuscula
print(last_name.capitalize())

# Title, primera letra de cada palabra en mayuscula
print(last_name.title())

# Strip, elimina espacios en blanco
print("    Hello World    ".strip())

# Isalnum, retorna True si todos los caracteres son alfanumericos
print("HelloWorld".isalnum())

# Isalpha, retorna True si todos los caracteres son alfabeticos
print("HelloWorld".isalpha())

# Isdigit, retorna True si todos los caracteres son digitos
print("123".isdigit())

# Islower, retorna True si todos los caracteres estan en minuscula
print("helloworld".islower())

# Isupper, retorna True si todos los caracteres estan en mayuscula
print("HELLOWORLD".isupper())

# Startswith, retorna True si la cadena comienza con el caracter especificado
print("HelloWorld".startswith("H"))

# Endswith, retorna True si la cadena termina con el caracter especificado
print("HelloWorld".endswith("d"))

# Isnumeric, retorna True si todos los caracteres son numericos
print("123".isnumeric())

# Isdecimal, retorna True si todos los caracteres son decimales
print("123.45".isdecimal())

# Isidentifier, retorna True si la cadena es un identificador valido
print("HelloWorld".isidentifier())

# Isprintable, retorna True si todos los caracteres son imprimibles
print("HelloWorld".isprintable())

# Isspace, retorna True si todos los caracteres son espacios en blanco
print(" ".isspace())
