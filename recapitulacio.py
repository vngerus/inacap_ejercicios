"""
Validar que personas son sujetos de credito automotriz

caso 1:
    Pueden obtener un credito automotriz,
    quienes sean mayores de 22 años y menores de 70 años,
    cuyos ingresos sean mayores a $600.000
caso 2:
    Cuando la causa del no otorgamiento sea su edad,
    debe informarle al cliente el motivo y
    en cuanto tiempo más el puede aplicar para el producto
caso 3:
    Por otro lado, un motivo puede ser el nivel de ingresos,
    debemos realizar un mensaje personalizado que
    nos muestre el porcentaje de sueldo que falta
caso 4:


#edad = 25
opcion = "z"
ingreso = 700000 #sueldoLiquido, renta, monto
while opcion != "6":
    edad = int(input("Ingrese edad del cliente: "))

    if edad > 22 and edad < 70 and ingreso > 600000:
        print(" VERDADERO ")
    elif edad < 23 and ingreso > 600000:
        print("No obtiene credito automotriz por su edad,\nVuelva en {} años".format(23 - edad))
    elif 22 < edad < 70 and ingreso <= 600000:
                        #resultado = ((ingreso * 100) / 600000)
       print("Su porcentaje faltante es: {}%".format((600000 - ingreso) / 600000 * 100 ))
                        #print("Su porcentaje faltante es: {}%".format(100 - ((ingreso * 100) / 600000))
    else:
       print("FALSO")
    opcion = input("Desea salir... presione [6]")

    #print(ingreso)
"""
""" valor1 = 10
valor2= 4
resultado = valor1 + valor2
print(f"numero 1 = {valor1} numero 2 = {valor2} ... resultado: {resultado}")
print("numero 1 = {} numero 2 = {} ... resultado: {}".format(10,4,10+4))
print("- "*20) """

""" # Ingresar usuario y contraseña
userSaved = "ADMIN"
passwordSaved = "clave"

nameUser = input("Ingrese su usuario: ")
passwordUser = input("Ingrese contraseña: ")

if userSaved == nameUser or passwordSaved == passwordUser.lower() or passwordSaved == passwordUser.upper():
    print("Usuario y contraseña valido")
 """

var = "hola mundo"
for i in var:
    print(i)
print("- "*20)
for i in range(2,4):
    print(i)
print("- "*20)
for i in range(2,12,3):
    #(donde parte, hasta donde llega, de cuanto en cuanto)
    print(i)
    print("- "*20)
for i in range(10,0,-1):
    #(donde parte, hasta donde llega, de cuanto en cuanto es el decremento)
    print(i)