#Sección 12: Ejercicios. 64: Ejercicio 1.
#Multiplicar dos números sin usar el simbolo de multiplicación.
a = 3
b = 3

resultado = 0

for x in range(a):
    resultado += b

print(resultado)

#Sección 12: Ejercicios. 65: Ejercicio 2.
#Ingresar un nombre y un apellido y imprimirlo al revés.

#primerNombre = input("Ingrese primer nombre")
#primerApellido = input("Ingrese primer apellido")

#nombreInvertido = ''.join(reversed(primerNombre))
#apellidoInvertido = ''.join(reversed(primerApellido))

#print(nombreInvertido,apellidoInvertido)

#otra forma,

nombre = 'Juan'
apellido = 'González'

concatenacion = nombre + ' ' +apellido

print(concatenacion[::-1])
#We haven´t seen this function yet. [::]

#Sección 12: Ejercicios. 66: Ejercicio 3.
#Escribir una función que encuentre el elemento menor de una lista

#my way to do the exercise
list = [6,-12,21,1,2,3,4,5,10,9]

def encontrarMenor(x):
    x.sort()
    print(x[0])

encontrarMenor(list)

#the way of the course

menor = 'init'

for x in list:
    if menor == 'init':
        menor = x
    else: 
        menor = x if x < menor else menor

print('El menor es: ',menor)

#Sección 12: Ejercicios. 67: Ejercicio 4.
#Escribir una función que devuelva el volumen de una esfera por su radio #4/3 * pi * r **(r)

#My way

def calculateRatio(r):
    var = 4/3*3.14*r**3 
    print("El volumen es de: ",var)

calculateRatio(6)
#to express the raise to te power we have to use ** before our power

#Sección 12: Ejercicios. 68: Ejercicio 5.
#Función para saber si el usuario es mayor de edad.

#My way
class User:
    name = "juanjo"
    edad = 25

user = User()


def wetherAdult(searchUser):
    try:
        if user.name == searchUser:
            if user.edad >17:
                print("el usuario es mayor de edad")
            else:
                print("El usuario no es mayor de edad")
        else:
            print("No es un usuario")
    except:
        print("Ingrese un usuario válido")
    
wetherAdult("pepito")

#course way

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)

def wetherAdult2(usuario):
    return usuario.edad>17

resultado1 = wetherAdult2(usuario)
resultado2 = wetherAdult2(usuario2)

print(resultado1, resultado2)


#Sección 12: Ejercicios. 69: Ejercicio 6.
#Escribir una función que indique si un número es par o impar.

#my way
def evenOrUneven(number):
    if  number % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

evenOrUneven(12)

#way of the course

def evenOrUneven2(number2):
    return number2 % 2 == 0

result = evenOrUneven2(11)

print(result)


#Sección 12: Ejercicios. 70: Ejercicio 7.
#Escribir una función que indique cuantas vocales tiene una palabra.

#My way
word = 'hOlanda que talca'


def countVowels():
    count = 0
    for i in word:
        
        if i == 'a' or i =='e' or i == 'i' or i =='o' or i =='u':
            count = count+1
        else:
          count += 0
    print('Hay', count, 'vocales, en tu palabra')

countVowels()

#way of the video 
#in this way the function counts the capitals
def countVowels():
    count = 0
    for i in word:
        y = i.lower()
        if y == 'a' or y =='e' or y == 'i' or y =='o' or y =='u':
            count = count+1
        else:
          count += 0
    print('Hay', count, 'vocales, en tu palabra')

countVowels()
#Sección 12: Ejercicios. 71: Ejercicio 8.
#Decir basta, luego que devuelva la suma de los números ingresados.

#way of the video

listNumbers = []
print('Ingresar números para mostrar, decir basta para parar')

while True:
    valor  = input('Ingrese valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            listNumbers.append(valor)
        except:
            print('Dato incorrecto')
            exit()
result = 0
for i in listNumbers:
    result += i
print('El resultado es de :', result)


#Sección 12: Ejercicios. 72: Ejercicio 9.
#Ejercicio de archivos...