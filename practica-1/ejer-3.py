# Crea un programa que calcule la suma de los primeros 100 números
# naturales utilizando un bucle for.

def suma_total():
    x = 0
    for i in range(101):
        x += i
    return x


print(f"la suma de los primeros 100 numeros naturales es de {suma_total()}")