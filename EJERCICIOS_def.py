#Ejercicio 1: Calcular el área de un triángulo.

base = input("su base: ")
altura = int(input("su altura: ")) # las dos valen 

base=int(base) # las dos valen 

def calcular_area_triángulo(base, altura):
    area = (base * altura) / 2
    return area

# Ejemplo de uso:
#base = 5
#altura = 3
area_triángulo = calcular_area_triángulo(base, altura)
print("El área del triángulo es:", area_triángulo)
