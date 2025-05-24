
diccionario = {
    "nombre": "jilber",
    "edad": 16,
    "ciudad": "san vicente",
    1:"uno",
    True: "hola"
}

print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["ciudad"])

print(diccionario[1])
print(diccionario[True])

diccionario["profecion"]=["sistemas","arquitecto","arqueologo","futbolista"]

print(diccionario)
 
print(diccionario["profecion"])

diccionario.pop("ciudad")
del diccionario [True]
print(diccionario)

print(len (diccionario))

#diccionario.clear()
#print(diccionario)

