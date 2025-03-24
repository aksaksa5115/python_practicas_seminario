# Desarrolla un programa que solicite al usuario que ingrese su edad y luego
# calcule y muestre cuántos años le faltan para alcanzar los 100 años.

def calcularEdad(edad):
    return 100 - edad

edad = int(input("ingrese edad actual: "))
print(f"la cantidad de años que le faltan para llegar a los 100 es de {calcularEdad(edad)}")