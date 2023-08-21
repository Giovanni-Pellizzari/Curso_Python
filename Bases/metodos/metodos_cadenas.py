#Estructura de los metodos "Dato.metodo()"

#Estructura de funciones "Funcion(dato)"

cadena1 = "hola mostro"
cadena2 = "QUEASE"


print (dir(cadena1)) #dir nos permite saber todo lo que podemos hacer con ese tipo de dato

#-----------------------------------------------------------------------------------------

print (cadena1.upper()) #upper es una funcion por lo tanto se declara de esta manera y lo que hace es colocar mayusculas

print (cadena2.lower()) #lower combierte a minusculas al contrario que upper 

print (cadena1.capitalize()) #combierte solo la primera letra en mayuscula

#------------------------------------------------------------------------------------------

print(cadena1.find("a")) #busca una cadena en otra cadena y nos retorna la posicion en la que la encuentra (si no encuentra retorna -1)

print(cadena1.index("a")) #busca una cadena en otra cadena y nos retorna la posicion en la que la encuentra (si no encuentra da una excepcion)

#------------------------------------------------------------------------------------------

print (cadena1.isnumeric()) #devuelve true si es un dato numerico

print (cadena1.isalpha()) #devuelve true si es alfanumerico (sin espacios)

#------------------------------------------------------------------------------------------

print (cadena1.count("o")) #cuenta la cantidad de veces que hay un caracter 

print (len(cadena1)) # funcion que cuenta cuantos caracteres tiene una cadena 

#------------------------------------------------------------------------------------------

print (cadena1.startswith("hola")) #verifica si una cadena empieza con otra cadena dada, si es asi devuelve true

print (cadena1.endswith("mostro")) #verifica si una cadena termina von otra cadena dada, si es asi devuelve true

#------------------------------------------------------------------------------------------

print (cadena1.replace("hola", "chau")) #remplaza una cadena con otra cadena dada

print (cadena1.split(" ")) #separa las cadenas devolviendo una lista





