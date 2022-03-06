dato = input("ingrese dato")

lista = ['hola', 'mundo', 'la','mama','de','la','mama']

if lista.count(dato) > 0:
    print('el dato existe: ', dato, 'y son: ', lista.count(dato))
else: 
    print('el dato no existe :(: ', dato)

