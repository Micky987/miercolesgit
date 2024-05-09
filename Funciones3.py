productos = {
    "arroz":58,
    "gaseosas":50,
    "trigo":25,
    "arina":100
}

def porcentaje2 (numero, porcentaje):
    resultado = numero * (porcentaje / 100)
    return resultado

# iterar (for) mi lista y calcular el iva acumulado
#   for, clave, valor in diccionario.items():
# iterar diccionario
# calcula iva

def calcular(lista):#####################################################
    total=0
    for producto,precio in lista.items():
        #arroz,58
        total += porcentaje2(precio, 13) 
    return total 
    # return tiene que esta fuera del for
    # si lo pongo al nivel del total solo calcula un elemento arroz alli termina
    # procentaje2 lo usamos arriba 
total_iva = calcular(productos)
print(total_iva)
        














'''
lista = [1,1,2,3,3,1,4,8,3]
lista_unica = []

for numero in lista:
    if numero not in lista_unica:
        lista_unica.append(numero) # .append agregar
print (lista_unica)

lista_unica_2 = set(lista) # set devuelve el mismo resultado solo que en {} que es tipo de dato
print(lista_unica_2)
print(type(lista_unica_2))
'''