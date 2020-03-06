dolar_euro = 0.91
libra_euro = 1.18

opcion = input("¿Qué cambio deseas realizar:" + "\n"
               "A --> Dolar a Euro"+"\n"
               "B --> Libra a Euro")
if opcion == "A":
    cantidad_de_dinero = float(input("¿Cuántos dolares quieres pasar a euros?"))
    euros_totales = cantidad_de_dinero * dolar_euro
    print("{} dolares son: {} euros".format(cantidad_de_dinero, euros_totales))
elif opcion == "B":
    cantidad_de_dinero = float(input("¿Cuántas libras quieres pasar a euros?"))
    euros_totales2 = cantidad_de_dinero * libra_euro
    print("{} libras son: {} euros".format(cantidad_de_dinero, euros_totales2))
else:
    print("Opcion no valida")
    exit()