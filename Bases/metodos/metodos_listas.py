#creando una lista con list 
lista = list(["Giovanni", "Pellizzari", 20])
lista2 = list([32 ,3 ,6 ,100 ,2023])
cadena = "hola mi hermano"

#devuelve la cantidad de elementos de una lista
resultado = len(lista)
print(resultado)

#agrega elementos a una lista
lista.append("Crack")

#agrega un elemento a la lista en un indice especifico 
lista.insert(1 , "The machine")

#agrega varios elementos a la lista
lista.extend(["by","Argentina"])

#elimina un indice de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 el anteultimo y asi sucesivamente

#remueve un elemento de la lista por su valor 
lista.remove("Crack")

#elimina todos los elementosde la lista
#lista.clear()

#ordena los elementos numericos en una lista de menor a mayor(reverse=true para invertir)[no acepta cadenas de texto]
lista2.sort()

#invierte los elementos de una lista
lista2.reverse()


print(lista2)


