#a una lista puede estar formada tanto por numero, textos o booleans

mi_lista2=["Francis", 2, True, 4,56]
print(mi_lista2)

mi_lista=["pepe", "Ramon", "rodri", "adios"]
print(mi_lista[1])#accede a la posicion marcada 

print(mi_lista[1:3])#accede a las posiciones que estan entre ese rango, contado al primero pero no al ultimo

print(mi_lista[1:])#accede a las posiciones empezando a contar de la posicion que tu ordenes

mi_lista.append("rauul") #Se añade un dato mas al final de la lista
print(mi_lista) #no abrir corchetes sino se le va a indicar una posicion

mi_lista.insert(1,"Vanesa") #añade un dato mas a la posicion que tu indiques
print(mi_lista)

mi_lista.extend(["andres", "carlos"]) #añade mas de un elemento a la lista todas las funciones anteriores solo añadian un elemento a la lista
print(mi_lista)

print(mi_lista.index("rodri")) #para saber en que posicion se encuentra el elemento que marcamos si hay 2 elementos con el mismo nombre nos devolvera el elemento con menor posicion

print("adios" in mi_lista) #le preguntamos si ese elemento esta en mi_lista nos devolvera un valor booleano

mi_lista.remove("rodri",) # para eliminar un solo elemento de la lista, siempre se debe de ordenar esta funcion antes de imprimir la lista
print(mi_lista)

mi_lista.pop() #elimina el ultimo elemento de una lista
print(mi_lista)

mi_lista3=mi_lista+mi_lista2 #para sumar listas
print(mi_lista3)

mi_lista4=["pep", "jeromin", 3, 67,34] *3 #para multiplica una lista las veces que tu desees
print(mi_lista4)
mi_lista.count("pepe") #cuenta cuantas veces se encuentre ese elemento en la lista

mi_tupla = ("awesome", 17, True)
mi_lista5 = list(mi_tupla) #conviert las tuplas a listas
mi_tupla2 = tuple(mi_lista) #convierte las listas a tuplas