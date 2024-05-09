lista = [1,1,2,3,3,1,4,8,3]
lista_unica = []

for numero in lista:
    if numero not in lista_unica:
        lista_unica.append(numero) # .append agregar
print (lista_unica)

lista_unica_2 = set(lista) # set devuelve el mismo resultado solo que en {} que es tipo de dato
print(lista_unica_2)
print(type(lista_unica_2))


# operaciones con cadenas 
grupo1 = set("abracadabra") # set saca los los caracteres repetidos
grupo2 = set("alacazam")
print (grupo1)
print (grupo1 - grupo2) # resta de conjuntos
print(grupo1 | grupo2) # union de conjuntos 
print(grupo1 & grupo2) # elementos que aparecen en el grupo 1 y 2
print(grupo1 ^ grupo2) # los elementos repetidos no aparecen en el resultado
#print((grupo1 & grupo2) | (grupo2 - grupo 1))

