#Seccion 8, control de flujo segunda parte, 43: funciones.

def miFuncion():
    print("mi primera función")

miFuncion()

def imprimeDato(argumentoUno):
    print("imprime ",argumentoUno)
#Cuando escribimos código dentro del paréntesis mientras escribimos la función
#Se llama argumento

imprimeDato("parametro 1")
#y cuando escribimos dentro del paréntesis con la función ya realizada
#Se llama parametro

def imprimeDatoDos(*nombre): 
    print('El nombre completo es:', nombre[1])

imprimeDatoDos('Chancho', 'Felíz', 'Lala', 'Lele')
#Podemos usar el simbolo reservado * para transformar en lista todo 
#lo que ingresemos en los parametros de la función(imprimeDato)

#Otra forma de acceder a los argumentos de una función ...
def nombreCompleto(apellido, nombre):
    print(nombre,apellido)

nombreCompleto(nombre = 'Chanchito', apellido='Feliz')
#En caso de no recordar el orden de los argumentos podemos escribir los argumentos desordenados
#y luego reescribir el valor que queramos darle al lado


def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])
#Podemos agrupar como diccionario al argumento ingresando kwargs(argumento por llave)

nombreCompleto2(nombre='Juanjito', apellido='bkn')
#se sigue escribiendo el método

#Seccion 8, control de flujo segunda parte, 44: más funciones

#In this example we are going to add to the function a default parameter
# That is when we aren´t adding a parameter, the function will do.
def miFuncion2(argumento = 'juanjo'):
    print(argumento)

miFuncion2('batman')
miFuncion2()

#We can write functionts like a list, for example..
def mifuncionLista(lista):
    for el in lista:
        print(el)

mifuncionLista(['juanjo', 'bkn'])

#Also we can coding functions that returns a value so it using lately

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i 
#In this function we code a empty value i, then we code a for 

nombres =concatenaNombres(['Juanjo','bkn'])

#When we returns values in a function neccesarily we have to capture
#into a variable to print

print(nombres)

#Seccion 8, control de flujo segunda parte, 43: Recursividad

def recursion(i):
    if(i < 1):   
        return i
    print(i)
    recursion(i - 1)

recursion(6)
#Recursivity is usefull when we work in a data collection or when we want
# do re attemptes in case that our database failed. 

