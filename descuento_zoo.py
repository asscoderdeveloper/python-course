
# Esta línea de abajo sirve para que el usuario introduzca su edad
edad = int(input("Dígame su edad: "))
tipo_de_carnet  = input("Dígame su tipo de carnet (E para estudiante / P para pensionista / F para familia numerosa / N nada): ")

if (edad<=35 and edad>=25 and tipo_de_carnet == "E") or\
        (edad < 10) or\
        (edad > 65 and tipo_de_carnet == "P") or\
        (tipo_de_carnet == "F"):

    print("Su descuento es del 25%")

else:
    print("Para ti no hay descuento champion")