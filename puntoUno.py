flag = 5
participantes =[]
print("Menu")
print("1. ingresar un participante")
print("2. Listar los participante")
print("3. cambiar el tiempo del participante")
print("4. Eliminar un participante")
id = 1
while flag != 0:
    flag = int(input("Ingrese un numero del menú: "))
    if flag == 1:
        participante = {}
        participante["id"] = id 
        id += 1
        participante["nombre"] = input("Ingrese el nombre del participante: ")
        participante["edad"] = int(input("Ingrese por favor la edad del participante: "))
        participante["pais"] = input("Ingrese el país del participante: ")
        participante["equipo"] = input("Ingrese el equipo del participante: ")
        participante["tiempo"] = int(input("Ingrese tiempo en minutos del participante: "))
        participantes.append(participante)
    elif flag == 2:
        print(f"Estos son los participantes en la lista: {participantes}")
    elif flag == 3:
        buscarParticipante = int(input("Ingrese por favor el id del participante para corregir el tiempo "))
        flag2 = False
        for participanteSeleccionado in participantes:
            if participanteSeleccionado["id"] == buscarParticipante:
                participanteSeleccionado["tiempo"] = int(input("Ingrese el nuevo tiempo del participante: "))
                flag2 = True
                break
            else:
                print("El participante no fue encontrado")
    elif flag == 4:
        buscarParticipante = int(input("Ingrese por favor ciclista a eliminar: "))
        for participanteSeleccionado in participantes:
            if participanteSeleccionado["id"] == buscarParticipante:
               participantes.remove(participanteSeleccionado)
               print(f"La lista de ciclistas a quedado así: {participantes}" ) 
            else:
                print("El participante no fue encontrado")
    else:
        print("Opcion no valida")

