for x in range (0, 5):
    numero = int(input("Ingrese un numero: "))
    if numero %2 == 0 and numero %3:
        print(numero, "es múltiplo de 2 y de 3")
    elif numero %3 == 0:
        print(numero," El numero es múltiplo de 3")
    elif numero %2 == 0:
        print(numero,"es múltiplo de 2")