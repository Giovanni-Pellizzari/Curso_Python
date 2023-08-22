#creando diccionarios con dict()

diccionario = dict(nombre = "giovanni", apellido= "pellizzari")

#las listas no pueden ser claves, y usamos frozenset para meter conjuntos
diccionario = {frozenset(["giovanni","pellizzari"]):"dev"}

#creando diccionaro con fromkeys() valor por defecto none
diccionario = dict.fromkeys(["nombre","apellido"])


#creando diccionaro con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "No se")







