
import random

opciones_validas = ["piedra", "papel", "tijera"]

while True:
    jugador1 = input("jugador1 (piedra/papel/tijera): ").lower()
    if jugador1 in opciones_validas:
        break
    else:
        print("Error: Debes ingresar 'piedra', 'papel' o 'tijera'")

jugador2 = random.choice(opciones_validas)
print(f"jugador2 eligió: {jugador2}")

if jugador1 == jugador2:
    print("empate")
elif jugador1 == "piedra" and jugador2 == "papel":
    print("jugador2 gana")
elif jugador1 == "piedra" and jugador2 == "tijera":
    print("jugador1 gana")
elif jugador1 == "papel" and jugador2 == "piedra":
    print("jugador1 gana")
elif jugador1 == "papel" and jugador2 == "tijera":
    print("jugador2 gana")
elif jugador1 == "tijera" and jugador2 == "piedra":
    print("jugador2 gana")
elif jugador1 == "tijera" and jugador2 == "papel":
    print("jugador1 gana")
else:
    print("jugador2 gana")