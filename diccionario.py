palabras = {
    "CRINGE": "accion/palabra rara embarazosa",
    "XD": "cara sonriente",
    "LOL": "sentimiento de sorpresa"
}


for i in range(5):
    consulta= int(input("Que quieres hacer en el diccionario? añadir palabra = 1, conocer significado = 2"))
    if consulta == 1:
        print("proximamente")
    elif consulta == 2:
        word= input("Introduce tu palabra en mayusculas porfavor")
        if word in palabras.keys():
            print(palabras[word])
        else:
            print("no se encontro la palabra")
    else: 
        print("esa no es la pregunta!!")
