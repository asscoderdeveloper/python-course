titulo = "Bienvenido al Test sobre los quesos"
print(titulo + "\n" + "-" * len(titulo) + "\n")
puntuacion = 0
print("Pregunta 1: ")
pregunta1 = input("¿Qué haces cuando ves una tabla de quesos? "
                  "(A salgo corriendo / "
                  "B pruebo un queso o puede que varios / "
                  "C devoro la tabla)")
if pregunta1 == "A":
    puntuacion += 0
elif pregunta1 == "B":
    puntuacion += 5
elif pregunta1 == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son: A, B y C")
    exit()
print("Pregunta 2: ")
pregunta2 = input("¿Cómo te comes la hamburguesa? (A sin queso / "
                  "B con queso / "
                  "C con extra de queso)")
if pregunta2 == "A":
    puntuacion += 0
elif pregunta2 == "B":
    puntuacion += 5
elif pregunta2 == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son: A, B y C")
    exit()
print("Pregunta 3: ")
pregunta3 = input("¿Eres intolerante a la lactosa? (A si / "
                  "B a veces / "
                  "C no)")
if pregunta3 == "A":
    puntuacion += 0
elif pregunta3 == "B":
    puntuacion += 5
elif pregunta3 == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son: A, B y C")
    exit()
print("Pregunta 4: ")
pregunta4 = input("¿Qué es eso? (A ??? / "
                  "B no lo entiendo / "
                  "C eso es queso)")
if pregunta4 == "A":
    puntuacion += 0
elif pregunta4 == "B":
    puntuacion += 5
elif pregunta4 == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son: A, B y C")
    exit()
if puntuacion >= 20:
    print("\n" + "Eres un amante del queso")
elif 20<puntuacion<40:
    print("\n" + "Te gusta el queso")
elif puntuacion < 20:
    print("\n" + "Odias el queso")