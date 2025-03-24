# Haz un programa que pida al usuario que ingrese una temperatura en
# grados Celsius y luego convierta esa temperatura a grados Fahrenheit,
# mostrando el resultado.

def TempEnFahrenheit(celcius):
    return (celcius * 9 / 5) + 32

celcius = int(input("ingrese temperatura en celcius: "))
print(f"la temperatura actual en celsius pasada a fahrenheit es de {TempEnFahrenheit(celcius)}")