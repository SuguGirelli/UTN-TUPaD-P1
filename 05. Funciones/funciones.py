#Hola Mundo:
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Saludar Usuario:
def saludar_usuaruio(nombre):
    print(f"Hola {nombre}!")

#Informacion personal:
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}.")

#area y perimetro:
def calcular_area_circulo(radio):
    import math
    return math.pi * radio ** 2

def calcular_perimetro_ciruclo(radio):
    import math
    return 2 * math.pi * radio

#Segundos en horas
def segundos_a_horas(segundos):
    return segundos/3600

#Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del numero: {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#Op basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b!= 0 else print("Indefinido (division por cero)")
    
    return (suma, resta, multiplicacion, division)

#IMC
def calcular_IMC(peso, altura):
    return peso / (altura ** 2)

#De C° a F°
def celsius_a_fahrenheir(celsius):
    return celsius * (9/5) + 32

#Promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

