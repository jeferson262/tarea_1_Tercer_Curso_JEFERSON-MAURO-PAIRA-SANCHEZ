#resolver el area y perimetro de un trapesoide

base_mayor = float(input("Ingrese la base mayor del trapesoide: "))
base_menor = float(input("Ingrese la base menor del trapesoide: "))
altura = float(input("Ingrese la altura del trapesoide: "))

area = (base_mayor + base_menor) * altura / 2
perimetro = base_mayor + base_menor +( 2 * altura)

print(f"El area del trapesoide es: {area}")
print(f"El perimetro del trapesoide es: {perimetro}")