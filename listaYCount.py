lista = [1,2,3,4,5]
#También podemos agregar elementos a la lista con la función append
# append = adjuntar
lista.append(6)
print(lista)
#Podemos crear una copia de la lista con la función copy()
lista2 = lista.copy()
#Podemos eliminar los elementos con la función clear
lista.clear()
print(lista,lista2)

#También podemos contar el valor de la lista con count()
print(lista, lista2.count(3))
#Podemos contar los valores totales de la lista con funcion len
print(len(lista), len(lista2))

#Accediento a un elemento en las filas
print(lista2[0])

#Eliminando un elemento de una lista
#lista2.pop() #pop elimina el último elemento
print(lista2)
#También podemos usar el método remove para eliminar un elemento en específico, 
#o, el primero. Dejando sólo la función
lista2.remove(3)
print(lista2)

lista2.append("hola")

#Reverse método para revertir una lista
lista2.reverse()
print(lista2)

#Sort ordena la lista de menor a mayor pero solo acepta un solo tipo de dato,
#por ende..
lista3 = [1,2,3,4,5,9,8,7,6]
lista3.sort()
print(lista3)