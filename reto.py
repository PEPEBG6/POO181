for numero in range (1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print(numero, "Hola Mundo")
    elif numero % 3 == 0:
        print (numero, "Hola")
    elif numero % 5 == 0:
        print(numero, "Mundo")

    else:
        print(numero)
    