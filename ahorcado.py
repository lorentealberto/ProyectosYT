import random, sys
IMAGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palabras = [
    "gato",
    "perro",
    "persona"
]


def get_palabra_aleatoria(_palabras):
    return _palabras[random.randrange(len(_palabras))]


def menu(_palabra, _fallos, _aciertos):
    letras_acertas = []

    if len(_fallos) == 0:
        n_fallos = 0
    else:
        n_fallos = len(_fallos) - 1

    print(IMAGENES_AHORCADO[n_fallos])
    print()
    print("Éstas son las letras que has usado " + _fallos)

    if n_fallos == 6:
        print("Has perdido")
        sys.exit(0)

    for i in range(len(_palabra)):
        for j in range(len(_aciertos)):
            if _aciertos[j] == _palabra[i]:
                letras_acertas.append(_aciertos[j])
    print(" ".join(letras_acertas))
    if "".join(letras_acertas) == _palabra:
        print("Has ganado")
        sys.exit(0)


random.seed()

palabra = get_palabra_aleatoria(palabras)

fallos = ""
letra = ""
aciertos = []

while True:

    letra = input("Introduce una letra: ")

    if not letra in palabra:
        fallos += letra
    else:
        aciertos.append(letra)

    menu(palabra, fallos, aciertos)