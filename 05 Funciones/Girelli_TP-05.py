#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

Lista100 = list(range(0,101,4))
print(Lista100)

#--------------------------------------------------------------------------------------------------------------------

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista123 = [True, "Nicolas", 7.5, 10, False]
print(lista123[-2])

#--------------------------------------------------------------------------------------------------------------------

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

lista_vacia = []
lista_vacia.append(False)
lista_vacia.append(3)
lista_vacia.append("Nicolas")

print(lista_vacia)

#--------------------------------------------------------------------------------------------------------------------

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
#Contando que el primer valor es la posicion 0 y en ultimo es la posicion 3 entonces:

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#--------------------------------------------------------------------------------------------------------------------

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)

#Lo Que realiza este programa es buscar el valor maximo en la lista "numeros" y removerlo de esta misma, luego lo muestra en pantalla.

#--------------------------------------------------------------------------------------------------------------------

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista30 = list(range(10,31,5))
pos_0_1 = lista30[0:2]

print(pos_0_1)

#--------------------------------------------------------------------------------------------------------------------

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "fox"
autos[2] = "vento"
#Lo mostramos aunque el enunciado no lo pida para demostrar que funciona.
print(autos)

#--------------------------------------------------------------------------------------------------------------------


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#--------------------------------------------------------------------------------------------------------------------

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#--------------------------------------------------------------------------------------------------------------------

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla

lista_anidada = [[], [], [], []]
lista_anidada[0].append(15)
lista_anidada[1].append(True)
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada[3].append(False)

#tambien podria sumarlas:

#listaA = [15]
#listaB = [True]
#listaC = [25.5, 57.9, 57.9, 30.6]
#listaD = [False]

#lista_anidada = listaA + listaB + listaC + listaD

print(lista_anidada)