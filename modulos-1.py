#import modulos 
#we have to use de reserved word import by the name of the archive (import modulos)

#examples
#print(modulos.mascotas)
#modulos.saludo('pepito')

##Sección 10: Módulos 55. Renombrando módulos
##Sección 10: Módulos 56. Seleccionando lo importado
##Sección 10: Módulos 58. Usando PIP, instalando, usando, listando y éliminando módulos.

#We can re-name the name of our module in the following way

from camelcase import CamelCase
import modulos as mo


print(mo.mascotas)
mo.saludo('pepito')

#you can bring only what you use doing this

#from modulos import mascotas, saludo

c = CamelCase()
s = 'Esta oración necesita camelcase'

camelcased = c.hump(s) 
print(camelcased)




