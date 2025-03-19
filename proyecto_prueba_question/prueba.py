respuesta = input("ingrese un numero del 1 al 4")

while not respuesta.isdigit() or not (1 <= int(respuesta) <= 4):
    respuesta = input("ingresa un numero valido del 1 al 4")

respuesta = int(respuesta)
print(f"elegiste la respuesta {respuesta}")