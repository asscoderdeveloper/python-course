from random import randint
import os
print("Bienvenidos a mi combate Pokemon"
      "\n")

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 80

TAMAÑO_BARRA_DE_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

def barra_vida_pikachu():
    barra_de_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu,
                                              " " * (TAMAÑO_BARRA_DE_VIDA - barra_de_vida_pikachu), vida_pikachu,
                                              VIDA_INICIAL_PIKACHU))
def barra_vida_squirtle():
    barra_de_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle,
                                              " " * (TAMAÑO_BARRA_DE_VIDA - barra_de_vida_squirtle), vida_squirtle,
                                              VIDA_INICIAL_SQUIRTLE))
while vida_pikachu > 0 and vida_squirtle > 0:

    #Turno de Pikachu

    print("Turno de Pikachu"
          "\n")
    ataque_cpu = randint (1, 3)
    if ataque_cpu == 1:
        print("Pikachu ha usado impactrueno"
              "\n")
        vida_squirtle -= 30
    elif ataque_cpu == 2:
        print("Pikachu ha usado rayo"
              "\n")
        vida_squirtle -= 15
    elif ataque_cpu == 3:
        print("Pikachu ha usado trueno"
              "\n")
        vida_squirtle -= 4

    if vida_squirtle < 0:
        vida_squirtle = 0

    elif vida_pikachu < 0:
        vida_pikachu = 0

    barra_vida_pikachu()

    barra_vida_squirtle()

    input("Enter para continuar ...\n\n")
    os.system("cls")

    if vida_pikachu == 0:
        print("Ha ganado Squirtle")
        exit()
    if vida_squirtle == 0:
        print("Ha ganado Pikachu")
        exit()


#Turno Squirtle
    print("Turno de squirtle"
          "\n")
    ataque_squirtle = None
    while ataque_squirtle != "H" and ataque_squirtle != "BL" and ataque_squirtle != "PA" and ataque_squirtle != "N":
        ataque_squirtle = input("¿Qué ataque deseas realizar?""Hidrobomba [H], Bomba Lodo [BL], Pistola agua [PA], para no atacar [N]")

    if ataque_squirtle == "H":
        print("Has elegido Hidrobomba, es eficaz"
              "\n")
        vida_pikachu -= 20
    elif ataque_squirtle == "DF":
        print("¡Bomba lodo!"
              "\n")
    elif ataque_squirtle == "PA":
        print("Pistola agua, no es muy eficaz"
              "\n")
        vida_pikachu -= 10
    if ataque_squirtle == "N":
        print("Squirtle no hace nada"
              "\n")

    if vida_squirtle < 0:
        vida_squirtle = 0

    elif vida_pikachu < 0:
        vida_pikachu = 0

    barra_vida_pikachu()

    barra_vida_squirtle()

    input("Enter para continuar...")
    os.system("cls")

if vida_pikachu > vida_squirtle:
    print("\n"
          "Ha gando Pikachu")
else:
    print("\n"
          "Ha ganado squirtle")
        



