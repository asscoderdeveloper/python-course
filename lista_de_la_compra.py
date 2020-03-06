#1º Posibilidad

"""lista = list()
input_usuario = None

print("Este es el programa lista de la compra..."
      "\n")
while input_usuario != "Q":
    input_usuario = input("¿Que desea comprar? ([Q] para salir)")
    if input_usuario == "Q":
        pass
    elif input_usuario in lista:
        print("{} ya esta en la lista de la compra".format(input_usuario))
    else:
        if input("¿Seguro que desea añadir {} a la lista de la compra? [S]i [N]o".format(input_usuario)) == "S":
            lista.append(input_usuario)

print("La lista de la compra es: {}".format(lista))"""

#2º Posibilidad

lista = list()
input_usuario = None

print("Este es el programa lista de la compra..."
      "\n")
while True:
    input_usuario = input("¿Que desea comprar? ([Q] para salir)")
    if input_usuario == "Q":
        break
    elif input_usuario in lista:
        print("{} ya esta en la lista de la compra".format(input_usuario))
    else:
        if input("¿Seguro que desea añadir {} a la lista de la compra? [S]i [N]o".format(input_usuario)) == "S":
            lista.append(input_usuario)

print("La lista es: {}".format(lista))
