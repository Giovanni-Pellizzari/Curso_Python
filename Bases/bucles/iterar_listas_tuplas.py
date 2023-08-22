#para cualquiera de estos casos es valido tambien utilizar tuplas y conjuntos

animales = ["gato", "perro","loro","cocodrilo"]
numeros = [2,4,5,6]

#recorriendo la lista animales
for animal in animales:
    print(animal)

#recorriendo la lista numeros y multiplicando por 2
for numero in numeros:
    resultado = numero * 2
    print(resultado)

#para iterar dos listas al mismo tiempo tienen que tener la misma cantidad de elementos
for numero,animal in zip(animales,numeros):
    print(numero)
    print(animal)

#puede variar en listas y tuplas pero en conjuntos si es de otra manera no funcionaia
for num in range(0,11):
    print(num)   


#forma corecta de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")


#usando el else 
for numero in numeros:
    print(numero)
else:
    print("TERMINO")




