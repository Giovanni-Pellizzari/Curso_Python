diccionario = {
    "nombre": "Giovanni",
    "apellido": "Pellizzari",
    "edad" : 22
}

#ecorriendo diccionaio para obtener las claves
for key in diccionario:
    print(key)

#recorriendo diccionario con indices utilizando items() para obtener la clave y el valor 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")








