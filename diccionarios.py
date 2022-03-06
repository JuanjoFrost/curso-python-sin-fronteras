#Los diccionarios son similares a las listas, con la sutil diferencia que 
#para acceder a un dato vamos a utilizar Strings en vez de números
diccionario= {
    'nombre': "gatito",
    'raza' : "pop",
    'edad' : 5
}
print(diccionario)
#vamos a acceder a un atributo individual de diccionario.
print(diccionario['nombre'])
print(diccionario['raza'])
#no es necesario usar sieeempre los parentesis cuadrados.
#Se puede usar el metodo get
print(diccionario.get('nombre'))
#para modificar un diccionario se hace de la siguiente manera.
diccionario['nombre'] = 'conan'
print(diccionario)
print(len(diccionario))
#Para agregar datos al diccionario, se hace de la siguiente manera
diccionario['Ronronea'] = 'Si'
print(diccionario)
#Para eliminar un dato de un diccionario se puede usar pop y se puede asignar cual queremos eliminar,
diccionario.pop('Ronronea')
print(diccionario)
#Otro método par eliminar una propiedad se puede utilizar popitem()(elimina el último valor que se agregó al diccionario)
diccionario.popitem()
#Otro método es la palabra reservada del
#del diccionario['ronronea']
#También se puede copiar un diccionario
copiaDiccionario = diccionario.copy()
#Otra función de copia de diccionarios es dict()
#copiaDiccionario = dict(diccionario)
#Eliminar TODOS los elementos de un diccionario, se usa la función clear
diccionario.clear()
#verificación
print(diccionario, copiaDiccionario)

#Sección 27. Profundización en diccionarios

#Podemos usar diccionarios anidados, es decir, diccionarios dentro de diccionarios
gatitos = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba": {
        "nombre": "Black Mamba",
        "edad": 12
    }
}
#Otra forma de crearlos

Fluffy = {
     "nombre": "Fluffy",
     "edad": 4
}
Mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}
gatitos2 = {
    "Fluffy" : Fluffy,
    "Mamba" : Mamba
}
#prueba
print(gatitos, gatitos2)
#OTRA FORMA, de agregar propiedades a un diccionario    
perritos = dict(nombre = "rambo", edad = 15)
#Todas estas formas son validas para escribir diccionarios, generalmente
#depende de la empresa como utilicen la sintaxis

#Leccion 29, Booleans
#Las variables booleanas son siempre true or false
verdadero = True
falso = False
print(verdadero, falso)