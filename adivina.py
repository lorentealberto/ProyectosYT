import random, sys

random.seed()

numero_oculto = random.randrange(1, 9)
vidas = 3

while vidas > 0:
    eleccion = int(input("Introduce un número: "))

    if eleccion < numero_oculto:
        print("Tu número es más pequeño")
        vidas -= 1
    elif eleccion > numero_oculto:
        print("Tu número es más grande")
        vidas -= 1
    else:
        print("Enhorabuena, has acertad")
        sys.exit(0)
print("Lo siento, pero has perdido y no has conseguido adivinar el número")
print("El  número oculto era: " + str(numero_oculto))
sys.exit(0)
