#Ejercicios prácticos de Python
# 1. Verificar si un número es positivo o negativo python
print("--- verifica si un número es positivo o negativo ---")
num = int(input("Ingrese un número: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else: 
    print("El número es 0.")

# 2. Determinar si una persona es mayor de edad
print("--- determina si una persona es mayor de edad ---")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")

# 3. Imprimir los números del 1 al 10
print("--- imprime los números del 1 al 10 ---")
for i in range(1, 11):
    print(i)


# 4. Sumar los números del 1 al 100
print("--- suma los números del 1 al 100 ---")
suma = 0
for i in range(1, 101):
    suma += i
print("La suma es:", suma)

# 5. Contar hacia atrás desde 10
print("--- cuenta hacia atrás desde 10 ---")
for i in range(10, 0, -1):
    print(i)

# 6. Verificar si un número es par o impar
print("--- verifica si un número es par o impar ---")
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# 7. Bucle hasta escribir 'salir'
print("--- bucle hasta escribir 'salir' ---")
while True:
    palabra = input("Escribe 'salir' para terminar: ")
    if palabra.lower() == 'salir':
        break
    else:
        print("Has escrito:", palabra)

# 8. Juego de adivinar el número aleatorio
print("--- juego de adivinar el número aleatorio ---")
import random
random = random.randint(1, 100)
intentos = 0
while True:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
    if intento < random:
        print("Demasiado bajo.")
    elif intento > random:
        print("Demasiado alto.")
    else:
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
        break

# 9. Tabla de multiplicar de un número
print("--- tabla de multiplicar de un número ---")
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

# 10. Contar repeticiones de una letra en una frase
print("--- cuenta repeticiones de una letra en una frase ---")
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra a contar: ")
contador = 0
for char in frase:
    if char == letra:
        contador += 1
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

# 11. Mostrar números pares del 1 al 20
print("--- muestra números pares del 1 al 20 ---")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 12. Sumar los dígitos de un número
print("--- suma los dígitos de un número ---")
num = input("Ingrese un número: ")
suma = 0
for digit in num:
    suma += int(digit)
print(f"La suma de los dígitos es: {suma}")


# 13. Calcular el promedio de 5 notas
print("--- calcula el promedio de 5 notas ---")
notas = []
for i in range(7):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
promedio = sum(notas) / len(notas)

# 14. Conversión de Celsius a Fahrenheit hasta escribir 'fin'
print("--- conversión de Celsius a Fahrenheit ---")
while True:
    celsius = input("Ingrese grados Celsius (o 'fin' para terminar): ")
    if celsius.lower() == 'fin':
        break
    else:
        try:
            celsius = float(celsius)
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C es igual a {fahrenheit}°F")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# 15. Validar contraseña con 3 intentos
print("--- valida contraseña con 3 intentos ---")
contraseña_correcta = "1234"
intentos = 0
while intentos < 3:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == contraseña_correcta:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta.")
        intentos += 1
if intentos == 3:
    print("Has agotado los intentos.")

# 16. Mostrar solo las vocales de una frase
print("--- muestra solo las vocales de una frase ---")
frase = input("Ingrese una frase: ")
vocales = "aeiouAEIOU"
resultado = ""
for char in frase:
    if char in vocales:
        resultado += char
print("Las vocales en la frase son:", resultado)

# 17. Simular cuenta regresiva con pausa
print("--- simula cuenta regresiva con pausa ---")
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

# 18. Determinar si un año es bisiesto
print("--- determina si un año es bisiesto ---")
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")

# 19. Encontrar el número mayor entre tres
print("--- encuentra el número mayor entre tres ---")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} es el mayor.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} es el mayor.")
elif num3 >= num1 and num3 >= num2:
    print(f"{num3} es el mayor.")
    
# 20. Crear una pirámide de asteriscos
print("--- crea una pirámide de asteriscos ---")
filas = int(input("Ingrese el número de filas: "))
for i in range(filas):
    print(" " * (filas - i - 1) + "*" * (2 * i + 1))