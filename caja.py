'''
Escribir una clase Caja para representar cuánto dinero hay en una caja de un negocio, desglosado por tipo de billete 
(por ejemplo, en el quiosco de la esquina hay 5 billetes de 10 pesos, 7 monedas de 25 centavos y 4 monedas de 10 centavos).
Se tiene que poder comparar cajas por la cantidad de dinero que hay en cada una, y además ordenar una lista de cajas de
menor a mayor según la cantidad de dinero disponible.
'''
class Cajas:
    def __init__(self,billete10, moneda25, moneda10):
        self.billete10 = billete10
        self.moneda25 = moneda25
        self.moneda10 = moneda10


class Caja1(Cajas):
    def __init__(self, billete10, moneda25, moneda10):
        super().__init__(billete10, moneda25, moneda10)

    def __add__(self, otra_entrada):
        total = (((self.billete10 + otra_entrada.billete10)* 10)+ ((self.moneda10 + otra_entrada.moneda10) * 0.10)+ ((self.moneda25 + otra_entrada.moneda25) * 0.25))
        return total 
    
    def __str__(self):
        return f"CAJA 1 hubo: {str(self.billete10)} Billetes de 10 Pesos, {str(self.moneda10)} Monedas de 10 Centavos y {str(self.moneda25)} Monedas de 25 Centavos."


class Caja2(Cajas):
    def __init__(self, billete10, moneda25, moneda10):
        super().__init__(billete10, moneda25, moneda10)

    def __add__(self, otra_entrada):
        return (((self.billete10 + otra_entrada.billete10)* 10)+ ((self.moneda10 + otra_entrada.moneda10) * 0.10)+ ((self.moneda25 + otra_entrada.moneda25) * 0.25))
        
    def __str__(self):
        return f"CAJA 2 hubo: {str(self.billete10)} Billetes de 10 Pesos, {str(self.moneda10)} Monedas de 10 Centavos y {str(self.moneda25)} Monedas de 25 Centavos."



#Creación de Objetos
print(f"""
Resumen de Cajas:
{'-' * 100} """)

#Para CAJA 1:
entrada1_caja1 = Caja1(15, 3, 25)
entrada2_caja1 = Caja1(0,20,15)

print(f"En la Entrada 1 de la {entrada1_caja1}")
print(f"En la Entrada 2 de la {entrada2_caja1}")

#Para CAJA 2:
entrada1_caja2 = Caja2(5, 0, 25)
entrada2_caja2 = Caja2(2,5,1)

print(f"En la Entrada 1 de la {entrada1_caja2}")
print(f"En la Entrada 2 de la {entrada2_caja2}")

#Operaciones entre objetos:
total_caja1 = entrada1_caja1 + entrada2_caja1
print(f"En la CAJA 1 hay un total de: {total_caja1}$\n")

total_caja2 = entrada1_caja2 + entrada2_caja2
print(f"En la CAJA 1 hay un total de: {total_caja2}$\n")

#Comparación entre CAJA 1 y CAJA 2:
if total_caja1 == total_caja2:
    print("Ambas cajas recolectaron la misma cantidad de dinero.")
elif total_caja1 > total_caja2:
    print(f"CAJA 1 recolectó {total_caja1 - total_caja2}$ más que CAJA 2.")
elif total_caja1 < total_caja2:
    print(f"CAJA 2 recolectó {total_caja2 - total_caja1}$ más que CAJA 1.")
