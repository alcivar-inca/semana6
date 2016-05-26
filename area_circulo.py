import math
radio=float(input("Ingrse el valor del radio: "))

def calcular():
	area=round(math.pi*(radio*radio), 2)
	print("El area del circulo es: " + str(area))

calcular()