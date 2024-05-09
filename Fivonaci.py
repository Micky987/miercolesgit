def fibonacci1 (limite): 
    a,b = 0,1                  # es un mentodo no devuelve un valor, imprime directamente 
                            # funcion es cando hacemos que devuelva una funcion

#limite = 59
    while a < limite:
        print (a, end=", ")
        a, b = b, a+b


def fibonacci2 (limite):  # regresa el valor devolviendo, (metodo)
    serie = []
    a,b = 0,1
    while a < limite:
        serie.append(a)
        a, b = b, a+b
    return serie

fibonacci1(80) # metodo

print("")
print(serie_fibonacci)
