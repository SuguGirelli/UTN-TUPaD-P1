# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla

nombre = input("Ingrese su numbre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ahora por favor ingrese su edad: ")
lugar = input("Ingrese el lugar de residencia actual: ")

print(f"Soy {nombre}, {apellido} tengo {edad} años y vivo en {lugar}. ")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = input("Ingrese (en cms) el radio de un circulo para calcular su area y su perimetro: ")

pi = 3.1416
radio = float(radio)
area = pi*(radio**2)
perimetro = (2*pi*radio)

print(f"El area de de este cirulo es de {area}cm² y su perimetro es de {perimetro}cm.")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Por favor ingrese una cantidad de segundos: "))
horas = segundos/3600, 2
print(f"Los segundos ingresados equivalen a {horas}hs.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un numero: "))

#Todavia no vi como hacer bucles en python y no quiero adelantartme.

print(f"A continuacion la tabla del numero {numero} es: ")
print(f"{numero} X 1 = {numero*1}")
print(f"{numero} X 2 = {numero*2}")
print(f"{numero} X 3 = {numero*3}")
print(f"{numero} X 4 = {numero*4}")
print(f"{numero} X 5 = {numero*5}")
print(f"{numero} X 6 = {numero*6}")
print(f"{numero} X 7 = {numero*7}")
print(f"{numero} X 8 = {numero*8}")
print(f"{numero} X 9 = {numero*9}")
print(f"{numero} X 10 = {numero*10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingrese un primer numero, diferente del cero: "))
numero2 = int(input("Ingrese un segundo numero, diferente del cero: "))

suma = numero1 + numero2
division = numero1 / numero2
multiplicacio = numero1 * numero2
resta = numero1 - numero2

print(f"Estos son los resultados de sumar, dividir, multiplicar y restar los numeros {numero1} y {numero2}:")
print(F"Suma: {numero1} + {numero2} = {suma}")
print(F"Division: {numero1} / {numero2} = {division}")
print(f"Multiplicacion: {numero1} x {numero2} = {multiplicacio}")
print(f"Resta: {numero1} - {numero2} = {resta}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso en kg/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)²

altura = float(input("Por favor ingrese su altura en metros (Ejemplo: 1.67): "))
pesokg = int(input("Por favor ingrese su peso en kg (Ejemplo: 68): "))
imc = pesokg / (altura**2)

print(f"El indice de masa corporal que posee es de {imc} ")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: fahrenheit = 9/5 x Temp Celsius + 32.

celsius = float(input("Ingrese por favor la temperatura que desee en C° (Celsius): "))

fahr = 9/5 * (celsius) + 32
print(f"El equivalente de grados Fahrenheit de {celsius}C° es de {fahr}F°")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numero1 = int(input("Ingrese un primer numero: "))
numero2 = int(input("Ingrese un segundo numero: "))
numero3 = int(input("Ingrese un tercer numero: "))
promedio = (numero1+numero2+numero3) / 3

print(f"El promedio entre estos tres numeros es de {promedio}. ")