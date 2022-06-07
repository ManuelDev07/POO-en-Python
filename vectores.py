'''Vectores
a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán sus coordenadas. En el método __str__ se imprime su contenido 
con el formato [x,y,z].
b) Crear un método escalar que reciba un número y devuelva un nuevo vector, con los elementos multiplicados por ese número.
c) Crear un método sumar que recibe otro vector, verifica si tienen la misma cantidad de elementos y devuelve un nuevo vector con la suma de ambos. Si no 
tienen la misma cantidad de elementos debe levantar una excepción.
'''

class Vector:
    def __init__(self, lista):
        self.lista = lista
    
    def escalar(self, num):
        nuevo_vector = [numero*num for numero in self.lista]
        return nuevo_vector

    def __add__(self, otro_vector):
        if len(self.lista) == len(otro_vector.lista):
            suma_vector = [self.lista[numero] + otro_vector.lista[numero] for numero in range(len(self.lista))]
            return print(f"La Suma de los Ambos Vectores es:  {suma_vector}")

        else:
            print("ERROR! No se puede hacer una Suma de Vectores ya que no tienen la misma cantidad de elementos")
            

    def __str__(self):
        return f"[{str(self.lista[0])},{str(self.lista[1])},{str(self.lista[2])}]"

#Creación de objeto:
vector1 = Vector([5,2,7])
print(vector1)

vector2 = Vector([4,1])
vector3 = Vector([9,56,12])

#Método Escalar:
try:
    x = int(input('Ingrese un número entero: '))
    vector_escalar = Vector.escalar(vector1,x)
    print(f"El Vector Escalar es: {vector_escalar}")
except ValueError:
    print('ERROR! Debe ingresar un número entero. Intente de nuevo....')


#Método Sumar:
suma1 = vector1 + vector2
suma2 = vector1 + vector3
#y = Vector.__add__(vector1,vector2)
