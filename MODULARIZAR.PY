import operaciones

productos = {
    "cereales":58,
    "carne": 150,
    "gaseosas":84,
    "arroz":259,
    "papel":78,
    "maletas":598
}

iva = operaciones.calcular(productos, operaciones.porcentaje2)
desc = operaciones.calcular(productos, operaciones.descuento)

print(f"iva: {iva}")
print(f"descuento: {desc}")


# pagina para sacar codigos ya hechos https://pypi.org/project/pip/
