#creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "holaGiova"
numeros = [2,3,5,6,7]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una {fruta}")

#evitar que el bucle siga ejecutandose (el else tmp se ejecuta) 
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:
    print("Terminado")

#recorrer una cadena de texto 
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
    
    
    