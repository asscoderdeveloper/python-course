print("¿Qué movil deberías comprar?" + "\n")
opcion1 = input("¿Qué sistema operativo deseas?"
                "A --> IOS" + "\n"
                "B --> Android")
if opcion1 == "B":
    opcion2 = input("¿Tienes dinero?" + "\n"
                    "A --> No" + "\n"
                    "B --> Si")
    if opcion2 == "A":
        print("Comprate un Android chino")
    else:
        opcion3 =  input("¿Te importa la cámara?" + "\n"
                                                    "A --> Si" + "\n"
                                                    "B --> No")
        if opcion3 == "A":
            print("Google Pixel")
        else:
            print("Android calidad-precio")
else:
    opcion4 = input("¿Tienes dinero?" + "\n"
                                        "A --> Si" + "\n"
                                        "B --> No")
    if opcion4 == "A":
        print("Iphone 11 Pro Max")
    else:
        print("Iphone reacondicionado")