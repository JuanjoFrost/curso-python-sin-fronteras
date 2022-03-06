#Las tuplas son muy similares a las listas PERO estas no se pueden modificar
#después de crearlas
tupla = ('hola', 'la', 'mama', 'de', 'la', 'mama') #para tupla se usa parentesis redondo
#Las tuplas tienen BASTANTES menos métodos
#Ejemplos:
#Index devuelve la posición de donde encontró un elemento
print (tupla.index('hola'))
#ESTO CON UNA TUPLA NO SE PUEDE HACER
#tupla.append('chao')
#Para transformar una tupla a lista...
listaDeTupla = list(tupla)
listaDeTupla.append('chao')
print(listaDeTupla)

#Rangos. Los rangos son para trabajar con una cantidad determinada de datos

rango = range(6)
print(rango) # el rango va de 0 a 6

