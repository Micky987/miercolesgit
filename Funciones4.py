productos = {
    "arroz":58,
    "gaseosas":50,
    "trigo":25,
    "arina":100
}

def porcentaje2 (numero, porcentaje=13):
    resultado = numero * (porcentaje / 13)
    return resultado

# funcion que calcule un descuento
# si el precio es mayor a 100 entonces el descuento es del 15%
# si es menor a 100 entonces 5%
def descuento(precio):
    descuento = 0
    if precio > 100:
        descuento=porcentaje2(precio, 15)
    else:
        descuento=porcentaje2(precio, 5)
    return descuento
    
#print(descuento(85))

def calcular (lista, funcion):
    total = 0
    for producto,precio in lista.items():
        total += funcion(precio)
    return total


iva = calcular (productos, porcentaje2)
print(f"iva total: {iva}")
total = calcular (productos, descuento)
print(f"total: {total}")