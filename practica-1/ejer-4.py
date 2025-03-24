# Cree un programa que dada una lista de números imprima sólo los que son
# pares. Nota: utilice la sentencia continue donde haga falta.

numeros = [1, 5, 3, 2, 6, 8, 10, 11, 12, 13, 100]

for i in numeros:
    if (i % 2 != 0):
        continue
    print(i)

