import random
numero_correcto = random.randint (1, 10)
numero_participante = None
while numero_participante != numero_correcto:
    numero_participante = int(input("Elige un numero del 1 al 10"))
    if numero_participante > 10:
        print("Te has pasado un poco...")
    elif numero_participante < 1:
        print("Te has quedado corto")
    if (numero_correcto -1) == numero_participante:
        print("Ui... casi")
    if   numero_participante == (numero_correcto +1):
        print("Ui casi...")
print("Has acertado, el numero correcto era: {}".format(numero_correcto))
