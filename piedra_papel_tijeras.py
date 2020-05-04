import random, sys

simbolos = [
    #ID     ICONO   ENEMIGO
    [1,     '✂',    3],
    [2,     '🧻',   1],
    [3,     '🗿',    2]
]


def get_simbolo(elemento):
    return simbolos[elemento][1]


def get_enemigo(elemento):
    return simbolos[elemento][2]


if __name__ == "__main__":
    random.seed()

    rival = simbolos[random.randrange(1, 3)][0]
    rival -= 1

    print("Elije una opcion")
    print("1. Tijeras")
    print("2. Papel")
    print("3. Piedra")

    eleccion = int(input("> "))

    eleccion_real = eleccion - 1

    if eleccion < 1 or eleccion > 3:
        print("¡Hey! Has introducido un número inválido.")
        sys.exit(0)
    else:
        rival_eleccion = get_enemigo(eleccion_real) - 1
        rival_rival = get_enemigo(rival) - 1

        print("Jugador: " + get_simbolo(eleccion_real) + " Enemigo: " + get_simbolo(rival))

        if rival_eleccion == rival:
            print("Has perdido")
        elif rival_rival == eleccion_real:
            print("Has ganado")
        else:
            print("Has quedado empate")

    sys.exit(0)