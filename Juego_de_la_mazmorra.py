import random
operacion_basilísco = random.randint(1, 100)
adivinanza = "Platano"
titulo = "El juego de la mazmorra" + "\n"
fin = "FIN" + "\n"
print(titulo + "-" * len(titulo) + "\n")
print("Tú y tu compañero sois dos espias galácticos encerrados en la prisión de máxima seguridad del agujero negro más próximo a la Tierra."
      "\n"
      "Habéis conseguido BAescaparos de vuestras celdas y estas reunidos en el pasillo del área de máxima seguridad."
      "Es hora de elegir que camino escoger, ir por la derecha donde hay una puerta semiabierta o ir por la izquierda bajando unas escaleras.")
opcion1 = input("[A] Izquierda / [B] Derecha")
if opcion1 == "A":
      print("Bajas las escaleras y te espera un guardia, que haces? ")
      opcion2 = input("[A] te da la opción de seguir bajando las escaleras o [B] enfrentarte a él en una batalla justa.")
      if opcion2 == "A":
            print("Mueres a manos de un extraterrestre.")
            print(fin + "-" * len(fin))
            exit()
      elif opcion2 == "B":
            palo = input("Derrotas al guardia y ves un pasillo tras de él, al entrar en el pasillo hay un palo quieres cogerlo? [A] Si o [B] No")
            print("Sigues caminando y te encuentras con un gran basilísco el cual te dice que aciertes un numero del 1 al 100")
            operacion_jugador = int(input("Elige un numero del 1 al 100"))
            if operacion_basilísco == operacion_jugador:
                  print("Mueres, al basilísco no le gusta la gente con suerte")
                  print(fin + "-" * len(fin))
                  exit()
            else:
                  print("Te haces amigo del basilísco y te deja pasar. "
                        "Caminas por un pasillo muy largo hasta que llegas a un precipicio que al otro lado tiene la salvación."
                        "Pero para saltar necesitaras el palo.")
                  if palo == "A":
                        print("Consigues saltar el precipicio y escaparte.")
                        exit()
                  elif palo == "B":
                        print("Al no coger el palo antes no logras saltar lo suficiente y mueres.")
                        print(fin + "-" * len(fin))
                        exit()
if opcion1 == "B":
      print("Abre la puerta del todo y te encuentras a un viejo sabio que te plantea una adivinanza: Oro parece, plata no es"
            "Solo tienes una oportunidad para resolver la adivinanza")
      respuesta_adivinanza = input("¿Que crees que es?")
      if respuesta_adivinanza == adivinanza:
            print("Has acertado!, continuas caminando y encuentras una piscina repleta de tiburones espaciales."
                  "\n"
                  " Al final de ella ves la salida de la carcel. ")
            piscina = input("Que quieres hacer? "
                            "\n"
                            "[A] Quieres meterte a nadar o [B] volver por donde has venido")
            if piscina == "A":
                  print("Empiezas a nadar y consigues escapar")
                  exit()
            elif piscina == "B":
                  print("Vuelves donde el viejo sabio y te mata por adivinar su genial adivinanza."
                        "\n")
                  print(fin + "-" * len(fin))

                  exit()
      else:
            print("No has resolvido la adivinanza, no eres apto."
                  "\n"
                  "Mueres a manos del viejo sabio.")
            print(fin + "-" * len(fin))

            exit()

