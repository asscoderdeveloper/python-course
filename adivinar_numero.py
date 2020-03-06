import random
numero_correcto = random.randint(1, 10)
numero_participante = int(input("Elige un numero del 1 al 10"))
if numero_participante > 10:
    print("Te has pasado un poco...")
if numero_participante < 1:
    print("Te has quedado corto")
if numero_participante != numero_correcto:
    print("Buen intento,hasta la próxima")
    print("El numero ganador era: {}".format(numero_correcto))
if numero_participante == numero_correcto:
    print("Has acertado, el numero correcto era: {}".format(numero_correcto))
