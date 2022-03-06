#Seccion 8 control de flujo 40 loop.
i=0

while i < 5:
    print(i)
    if i == 3:
        #continue, continua haciendo una acción omitiendo la accion en curso
        break #break detiene la iteración en caso de ser i = 3
    i += 1 # i+=1 le suma 1 a la variable. 

p=0

while p < 5:
    p += 1
    if p == 3:
        continue
    print(p)

#42. for loop. for se utiliza cuando queremos iterar sobre listas o tuplas

usuarios = ['juanjo', 'carlos', 'camila','pedro']

for usuario in usuarios:
    if usuario == 'juanjo':
        print('pulento')
        break
    print(usuario)

# imprimiendo cada uno de los carácteres de un string

string = 'juanjo'

for c in string:
    print(c)

#utilizando range en for

for x in range(1,6,3): #Además podemos poner un rango de inicio y final (1,6) 
    #también podemos agregar (, , 3) para indicar que vaya aumentando por partes
    print(x)
else: #en for también podemos agregegar else, y se ejecuta solo cuando termina for
    print("hemos terminado")


#Ejemplo de for en un for (no muy recomendable)

edades = ['24','25','26','27']

for usuarios in usuario:
    for edad in edades:
        print(usuario, edad)
#siempre los for que estén más a la derecha serán los primeros en ejecutarse

