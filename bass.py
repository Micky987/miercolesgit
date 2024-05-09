
def porcentaje2 (numero, porcentaje):
    resultado = numero * (porcentaje / 100)
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
#copiado de funciones 4


