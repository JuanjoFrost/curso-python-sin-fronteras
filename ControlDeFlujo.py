#if y condiciones
if 2 <5:
    print("2 es menor que 5")

#Doble igualdad a == b
#Menor que a < b
#Mayor que a > b
#Diferente de a != b
#Menor que a <= b
#Mayor que a < = b

if 2 ==2:
    print("2 es igual a 2")

if 2==3:
    print("2 es igual a 3"
    )
if 2 > 5:
    print("2 es mayor a 5")

if 5 > 2:
    print("5 es distinto a 2")

if 2 != 2: 
    print("2 es distinto de 2")

if 3 != 2:
    print("3 es distinto de 2")

if 3 >= 2:
    print("3 es mayor o igual a 2")

if 3 >= 3:
    print('3 es menor o igal a 3')

#Sección 6, 32. IF, ELIF, ELSE
if 2 < 5:
    print("dos es menor a 5 en if")
elif 2 < 5:
    print('2 menor a 5 en elif')
else:
    print('Yo me imprimo solo si todo lo anterior se evalúa en falso')


if 2 > 5:
    print("dos es menor a 5 en if")
elif 2 > 5: #elif lo podemos encadenar todas las veces que queramos
    print("yo me imprimo en caso de que lo primero sea falso")
elif 2< 5:
    print("2 menor que 5, este se imprime")
else:
    print('Yo me imprimo solo si todo lo anterior se evalua en falso')

#Sección 6, 33. IF cortos y itinerarios

if 2 < 5: print('if de 1 linea')
#otra forma de escribir el if, se conocen como operadores ternarios "cuando evalúa en true y también en false"
print('cuando devuelve true') if 5>2 else print('cuando devuelve false')

#and
if 2 < 5 and 3 > 2:
    print('ambas devuelven true')

#or
if 2 > 3 or 3 > 2:
    print('como una de las condiciones es true, esto se mostrara')