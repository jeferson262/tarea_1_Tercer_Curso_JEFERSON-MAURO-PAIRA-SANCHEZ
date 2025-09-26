#calcular el area y perimetro de  una corona circular
import math

radio_mayor = float(input("Ingrese el radio del circulo mayor: "))
radio_menor = float(input("Ingrese el radio del circulo menor: "))

area = math.pi * (radio_mayor ** 2 - radio_menor ** 2)
perimetro = 2 * math.pi * (radio_mayor + radio_menor)

print(f"El area de la corona circular es: {area}")
print(f"El perimetro de la corona circular es: {perimetro}")