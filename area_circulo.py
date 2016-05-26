#	PROGRAMA PARA CALCULAR EL AREA DEL CIRCULO
import math
radio=float(input("Ingrse el valor del radio: "))

def calcular():
	area=round(math.pi*(radio*radio), 2)
	print("El area del circulo es: " + str(area))

# PROMEDIO DE NUMEROS INGRESADOS
def ingresoNumeros():
	num =1
	cont=0
	resp =0
	while num>0:
		num=int(input("Ingrese un numero: "))
		if num!=0:
			resp= resp + num
			cont=cont+1
	
	print("El promedio es: " + str(resp/cont))


calcular()
ingresoNumeros()