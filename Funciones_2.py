#numero = input("introduce tu numero: ")
#porcentaje = input("introduce tu %: ")

def porcentaje1 (numero, porcentaje): # los dos valores son requeridos
    resultado = numero * (porcentaje / 100)
    return resultado
resultado = porcentaje1(numero=80, porcentaje=10)
print (resultado)
##################################################################################################
def porcentaje2 (numero, porcentaje=10): # un valor ya esta definido y el otro no son requeridos 
    resultado = numero * (porcentaje / 100)
    return resultado


resultado = porcentaje2(numero=80)
print(resultado)
resultado = porcentaje2(numero=80, porcentaje=25)
print(resultado)


print(type(porcentaje2))  
#funcio esto 

# funcion regresa algo  
# metodo no regresa nada= solo imprime

