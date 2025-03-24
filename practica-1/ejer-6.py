# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
# listas, una con los número pares y otras con los que son impares. Imprima
# las listas al terminar de procesarlas.
def listas(numeros, pares, impares):
    for i in numeros:
        if (i % 2 == 0):
            pares.append(i)
        else:
            impares.append(i) 


pares = []
impares = []
numeros = [1, 5, 3, 2, 6, 8, 10, 11, 12, 13, 100]

listas(numeros, pares, impares)
for i in numeros:
    if (i % 2 != 0):
        continue
    print(i)


print("----------LISTAS NUEVAS------------")
print(f"numeros pares: {pares}")
print(f"numeros impares: {impares}")