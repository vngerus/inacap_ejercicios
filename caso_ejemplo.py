""" 
Validar que personas son sujetos de credito automitrz

    caso 1: Pueden obtener un credito automotriz, 
        quienes sean mayores de 22 años y menores de 70 años,
        cuyos ingresos sean mayores a $600.000
    caso 2: Cuando la causa del no otorgamiento sea su edad,
        debe informarle al cliente el motivo y en cunto tiempo mas puede
        aplicar para el credito automotriz.
    caso 3: Por otro lado, un motivo puede ser el nivel de ingreso,
        debemos realizar un mensaje personalizado que nos muestre el porcentaje que falta.

"""

#caso 1 
#se ingresa el nombre
nombre = input("Ingrese su nombre: ")
#se ingresa la edad
edad = int(input("Ingrese su edad: "))
#se ingresa el ingreso
ingreso = int(input("Ingrese su ingreso: "))
#se ingresa el nombre2
# calcular el resultado de ambos para definir quien es mayor de 22  
# y menor de 70 con un ingreso mayor a 600.000
if edad > 22 and edad < 70 and ingreso > 600000:
    print("El usuario", nombre, "es sujeto de credito automotriz")
#si el usuario no cumple con los requisitos, debe informarle el motivo y en cuanto podrá obtenerlo
#si no cumple con la edad calcular cuanto tiempo le falta para cumplir 22 y si sobre pasa la edad decir que no cumple por ello
# si su ingeso no llega a 600.000, informarle que no cumple por ello y hacer una funcion de explicar cuanto le falta para llegar a ese monto
#si sobre pasa el monto, y cumple con la edad si es apto
#   caso 1: Pueden obtener un credito automotriz, 
#        quienes sean mayores de 22 años y menores de 70 años,
#        cuyos ingresos sean mayores a $600.000
#    caso 2: Cuando la causa del no otorgamiento sea su edad,
#        debe informarle al cliente el motivo y en cunto tiempo mas puede
#        aplicar para el credito automotriz.
#    caso 3: Por otro lado, un motivo puede ser el nivel de ingreso,
#        debemos realizar un mensaje personalizado que nos muestre el porcentaje que falta
""" else : 
    #si es mayor a 22 y menor a 70 y su ingreso es mayor a 600.000, es apto
    if edad < 22 and ingreso > 600000:
        print("El usuario", nombre,
            "no es sujeto de credito automotriz por su edad, le falta",
            22 - edad, "años para poder aplicar")
        #si es mayor a 22 y menor a 70 y su ingreso es menor a 600.000, no es apto
    elif edad > 70 and ingreso > 600000:
        print("El usuario", nombre,
            "no es sujeto de credito automotriz por su edad, ya no puede aplicar")
        #si es mayor a 22 y menor a 70 y su ingreso es menor a 600.000, no es apto
    elif ingreso < 600000 and edad > 22 and edad < 70:
        print("El usuario", nombre,
            "no es sujeto de credito automotriz por su ingreso, le faltan $",
            600000 - ingreso, "para poder aplicar") 
 """


#ejemplo del profesor

opcion = "z"
ingreso = 700000  # sueldo líquido

while opcion != "s":
    edad = int(input("Ingrese su edad: "))
    
    if 22 <= edad <= 70:
        if ingreso > 600000:
            print("Puede solicitar el crédito automotriz.")
        else:
            porcentaje_faltante = (600000 - ingreso) / 600000 * 100
            print(f"No obtiene crédito automotriz por su ingreso. Le falta un {porcentaje_faltante:.2f}% para alcanzar el mínimo requerido.")
    elif edad < 22:
        print(f"No obtiene crédito automotriz por su edad. Vuelva en {22 - edad} años.")
    else:  # edad > 70
        print("No obtiene crédito automotriz por su edad. Ya no puede aplicar.")
    
    opcion = input("¿Desea continuar? (s/n): ").lower()