texto = input("ingrese un texto : ")
texto_transformado = texto.split(" ")

cantidad_de_palabras = len(texto_transformado)

tiempo_en_decirlo = cantidad_de_palabras / 2

dalto = cantidad_de_palabras * 100 // 2.6 / 100

if tiempo_en_decirlo > 60:
    print("Para flaco tampoco te pedi un testamento")


print(f"-Una persona promedio tardaria {tiempo_en_decirlo} segundos en decirlo")
print(f"-El texto tiene {cantidad_de_palabras} palabras")
print (f"-Dalto tardaría {dalto} segundos")


