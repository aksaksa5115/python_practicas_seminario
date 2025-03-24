# Escribe un programa que tome una lista de números enteros como entrada
# del usuario. Luego, convierte cada número en la lista a string y únelos en
# una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier
# número que sea múltiplo de 3 de la cadena final.

def String(numeros):
    cadena = ''
    for i in numeros:
        if (i % 3 != 0):
            cadena += f"{i} - "
    cadena = cadena[:-2]
    return cadena


numeros = [1, 5, 3, 2, 6, 8, 10, 11, 12, 13, 100] # que paja hacer el imput
print(String(numeros))


