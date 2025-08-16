
def validar_opcion(jugador_num):
    opciones_validas = ["piedra", "papel", "tijera"]
    while True:
        opcion = input(f"jugador{jugador_num} (piedra/papel/tijera): ").lower()
        if opcion in opciones_validas:
            return opcion
        else:
            print("Error: Debes ingresar 'piedra', 'papel' o 'tijera'")


jugador1 = validar_opcion(1)
jugador2 = validar_opcion(2)


if jugador1 == jugador2:
    print("Empate")
elif jugador1 == "piedra" and jugador2 == "papel":
    print("Jugador2 gana")
elif jugador1 == "piedra" and jugador2 == "tijera":
    print("Jugador1 gana")
elif jugador1 == "papel" and jugador2 == "piedra":
    print("Jugador1 gana")
elif jugador1 == "papel" and jugador2 == "tijera":
    print("Jugador2 gana")
elif jugador1 == "tijera" and jugador2 == "piedra":
    print("Jugador2 gana")
elif jugador1 == "tijera" and jugador2 == "papel":
    print("Jugador1 gana")
