#Seccion 7, 36: Calculadora
#Seccion 7, 37: moviendo la validación
#La función input interperta como strings por lo tanto hay que cambiar los datos a int
##Seccion 7, 38: agregando más operaciones
primero = input("Ingrese primer numero")
#Transformación
#Acá en el try except ponemos un valor como 'hola' en caso de que el valor
#que agreguemos a la calculadora no pueda ser transformado a entero y pongamos cualquier cosa
try:
    primero = int(primero)
except:
    primero = 'hola'
if primero =='hola':
    print("el valor ingresado no es entero")
    exit()

segundo = input("ingrese segundo número")
try:
    segundo = int(segundo)
except:
    segundo = 'hola'
#Otra forma de validar
if segundo =='hola':
    print('el valor ingresado, no es un entero')
    exit()

print(primero+segundo)

#Acá en el if agarramos la excepción del hola, en caso que el usuario
#halla escrito cualquier string y mostrará "ingresaste mal un dato"
if primero == 'hola' or segundo == 'hola':
    print('ingresaste mal un dato')
else:
    print(primero+segundo)
#Acá harémos una calculadora que haga todas las opreaciones básicas
simbolo = input('ingrese operacion')

if simbolo == '+':
    print('Suma:', primero+segundo)
elif simbolo == '-':
    print('Resta',primero-segundo)
elif simbolo == '*':
    print("Multiplicación:",primero*segundo)
elif simbolo == '/':
    print("División:", primero/segundo)
else:
    print("Este simbolo no es válido")



  

