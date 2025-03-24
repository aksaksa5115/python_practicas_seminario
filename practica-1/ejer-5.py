# implementa un programa que solicite al usuario que ingrese una lista de
# números. Luego, imprime la lista pero detén la impresión si encuentras un
# número negativo. Nota: utilice la sentencia break cuando haga falta.
def crearLista(numeros):
    cant = int(input("ingrese cantidad de elementos a agregar: "))
    for i in range(cant):
        x = int(input("ingrese numero a guardar: "))
        numeros.append(x)


numeros = []
crearLista(numeros)
for i in numeros:
    if (i < 0):
        break
    print(i)

