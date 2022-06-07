class Lampara:
    estados = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, estado_lampara): #Constructor de la clase y darle atributos a la clase
        self.estado_lampara = estado_lampara

    def encender(self):#Cuando se llame se asignará True a la variable
        self.estado_lampara = True
        self.mostrar()

    def apagar(self):#Cuando se llame se asignará False a la variable
        self.estado_lampara = False
        self.mostrar()

    def mostrar(self):
        #Verifico el estado de la variable
        if self.estado_lampara == True:
            print(self.estados[0])

        else:
            print(self.estados[1])



def menu():
    lampara = Lampara(estado_lampara=False) #Creo el objeto lampara
    while True:
        print('''
Menú:
1 -> Encender.
2 -> Apagar.
3 -> Salir.
    ''')
        try:
            opcion = int(input())
            
            if opcion == 1:
                lampara.encender()

            elif opcion == 2:
                lampara.apagar()

            elif opcion == 3:
                break

            else:
                print('ERROR! Debe ingresar el dato como se indica...')

        except ValueError:
            print('ERROR! Debe ingresar el dato como se indica...')

menu()