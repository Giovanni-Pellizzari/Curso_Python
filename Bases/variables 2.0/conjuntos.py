#creando un conjunto con set()
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto 

conjunto1 = frozenset({"dato1", "dato2"})
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)


#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#las dos fomas son validas para verificar si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

print(resultado)

#las dos formas son validas para verificar si es un superconjunto 
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1


#verificar si hay un resultado en común
resultado = conjunto2.isdisjoint(conjunto1)




