
# for es iterar, los metodos sirven para reutilizarlos, como si crearamos un codigo o formula que podemos 
# reutilizar, en este ejemplo se agarra el porsentaje de 10 del anterior ejercicio, (porcentaje2)
def porcentaje2 (numero, porcentaje=10): # un valor ya esta definido y el otro no son requeridos 
    resultado = numero * (porcentaje / 100)
    return resultado
# for = para , Se utiliza para recorrer una secuencia de elementos, como una lista, una cadena de texto
def aplicar_porcentaje (lista):
    resultado_pocentaje = []
    for numero in lista:  
        resultado = porcentaje2(numero)
# .append = es un método que se utiliza en Python para agregar un elemento al final de una lista existente.
        resultado_pocentaje.append(resultado)
    return resultado_pocentaje

lista_numeros = [50,80,66,45,69]
resultado_pocentaje = aplicar_porcentaje(lista_numeros)
print(resultado_pocentaje)


