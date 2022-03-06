#The class is like a plan house
#The buildings houses are like the instances

#Sección 9: Objetos, clases y herencia. 47: Objetos y clases
#Sección 9: Objetos, clases y herencia. 48: Métodos.

#How to create a class

class Usuario: #First letter ALWAYS in capital letter
    nombre = "Juanjo" # Instances ALWAYS in lower case
    apellido = "González"

usuario = Usuario() #This way we instance and have user as object
usuario2 = Usuario()

print(usuario.nombre, usuario.apellido, usuario2.nombre)

#Other way more practice to create classes.

class UsuarioNuevo:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#1.- Set a function under the class do that the function execute each time we called to the class in one instance
#2.- self is the reference of the object(user´s instance). When we instance in different objects
#.- i mean, self = usuario.nombre, self representate user, to can create some instances of itself object.
#.-but with differents attributes
#.-__init__is the constructor of the class in which it is created a new instance of the class

    def saludo(self):
        print('hola, estoy saludando, mi nombre es: ', self.nombre, self.apellido )

usuario1 = UsuarioNuevo("Juanjo", "González")
usuario2 = UsuarioNuevo("Carlos", "Miranda")

print(usuario1.nombre, usuario1.apellido, usuario2.nombre, usuario2.apellido)


#we test our method saludo
usuario1.saludo()
usuario2.saludo()

#Sección 9: Objetos, clases y herencia. 49: self, eliminar propiedades y objetos

usuario1.nombre = "Juan José"
usuario1.saludo()

#We can directly delete the attributes of the classes or the class in the following way

del usuario1.nombre
del usuario1

#Sección 9: Objetos, clases y herencia. 50: Herencia.

class Admin(UsuarioNuevo): #for applying heredity there is to add the name of the class in or parenthesis
    def superSaludo(self):
        print('hola, me llamo: ', self.nombre, 'y soy admin')

admin = Admin('Super', 'Admin') 

admin.saludo() # admin inherited from UsuarioNuevo the functions
admin.superSaludo()

# we can not call to our father class applying son´s class.
# for example, we can´t doing this Usuario.superSaludo() !!

##Sección 9: Objetos, clases y herencia. 51: Ejercicio de Herencia.
##Sección 9: Objetos, clases y herencia. 52: Extendiendo el método init del padre

#class Animal:
#   def __init__(self, nombre, onomatopeya):
#        self.nombre = nombre
#        self.onomatopeya = onomatopeya

#class Gato(Animal):
#    def saludo(self):
#        print('Hola, soy un', self.nombre, 'y mi sonido es: ', self.onomatopeya)

#class Perro(Animal):
#    def saludo(self):
#        print('Hola, soy un' ,self.nombre, 'y mi sonido es: ', self.onomatopeya)

#gato = Gato('Conan', 'Miau')
#gato.saludo()

#perro = Perro('Hachi', 'Guau guau!')

#perro.saludo()

#THIS OTHER EXAMPLE OF HEREDITY

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("hola, soy un", self.tipo, "y mi sonido es: ",self.onomatopeya)

#The way to extend a class with the behavior of the father is the following.
class Gato(Animal):
    tipo = "gato"
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido')

#other way to extend the behavior of the method father´s class
class Perro(Animal):
    tipo = "perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("Hola, soy un perro extendido")

class Canario(Animal):
    tipo = "canario"

gato = Gato('Conan', 'Miau Miau')
gato.saludo()

perro = Perro('Hachi', 'Guau guau')
perro.saludo()

canario = Canario('Piolín', 'silvido')
canario.saludo()

