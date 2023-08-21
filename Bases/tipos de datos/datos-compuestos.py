#conjunto de datos que se puede modificar
lista = ["Giovanni ", " Pellizzari ", 21]

print(lista[0] + lista[1])

#conjunto de datos que no se pueden modificar
tupla = ("Giovanni ", " Pellizzari ", 21)

print(tupla[0])

#esto es valido
lista[2] = 22 

#esto no 
#tupla[2] = 22 

print(lista)
print(tupla)

#creando un conjunto (set) similar a las tuplas pero no puedo accerde por un indice son desordenados y no almacena datos duplicados
conjunto = {"Giovanni", "pellizzari", 21}
#print(conjunto[1]) error
#correcto
print(conjunto)

#creando un diccionario (dict) 
diccionario = {
#0
 'nombre' : "Giovanni",
#1
 'apellido' : "Pellizzari",
#2
 'edad': 21
}

print(diccionario['edad'])

