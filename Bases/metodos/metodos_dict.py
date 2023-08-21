diccionario = {
    "nombre" : 'Giovanni',
    "apellido" : 'Pellizzari',    
    "años": 22
}

#devuelve un objeto tipo dict_item
claves = diccionario.keys()

#llama a un elemento del diccionario 
diccionario.get("nombre")

#elimina todo del diccionario
#diccionario.clear()

#eliminando elementos del diccionario
diccionario.pop("años")

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()


