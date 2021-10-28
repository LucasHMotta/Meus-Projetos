#   py!

#   Este é um jogo em Python, criado ainda como protótipo de terminal.
#   Futuramente terá uma interface gráfica e interativa!

import os
import random
from colorama import Fore

game_again = "s"
jogadas = 0
game_player = 2  # 1 = CPU | #2 = Jogador
maxJogadas = 9
winner = ""
matriz = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def screen():
    global matriz
    global jogadas
    os.system("cls")
    print("\n")
    print("     0    1    2")
    print("0:    " + matriz[0][0] + " | " +
          matriz[0][1] + " | " + matriz[0][2])
    print("    -------------")
    print("1:    " + matriz[1][0] + " | " +
          matriz[1][1] + " | " + matriz[1][2])
    print("    -------------")
    print("2:    " + matriz[2][0] + " | " +
          matriz[2][1] + " | " + matriz[2][2])
    print("Jogadas: {}{}{}".format(Fore.GREEN, str(jogadas), Fore.RESET))


def player_joga():
    global jogadas
    global game_player
    global maxJogadas

    if game_player == 2 and jogadas < maxJogadas:
        l = int(input("Linha..: "))
        c = int(input("Coluna.: "))
        try:
            while matriz[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))
            matriz[l][c] = "X"
            game_player = 1
            jogadas += 1
        except:
            print("Espaço inválido!")

def cpu_joga():
    global jogadas
    global maxJogadas
    global game_player

    if game_player == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while matriz[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        matriz[l][c] = "O"
        game_player = 2
        jogadas += 1

def win_verify():
    global matriz
    vitoria = "n"
    simbolos = ["X", "O"]

    for s in simbolos:
        vitoria = "n"
        il = ic = 0

        # Verificar Linhas
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if(matriz[il][ic] == s):
                    soma += 1
                ic += 1
            if(soma == 3):
                vitoria = s
                break
            il += 1
        if(vitoria != "n"):
            break

        # Verificar Colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if(matriz[il][ic] == s):
                    soma += 1
                il += 1
            if(soma == 3):
                vitoria = s
                break
            ic += 1
        if(vitoria != "n"):
            break

        # Verifica Diagonal (esquerda -- direita)
        soma = 0
        idiag = 0
        while idiag < 3:
            if(matriz[idiag][idiag] == s):
                soma += 1
            idiag += 1
        if(soma == 3):
            vitoria = s
            break

        # Verifica Diagonal (direita -- esquerda)
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if(matriz[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if(soma == 3):
            vitoria = s
            break
    return vitoria

def reset():
    global matriz
    global jogadas
    global game_player
    global maxJogadas
    global winner
    jogadas = 0
    game_player = 2  # 1 => CPU | 2 => Jogador
    maxJogadas = 9
    winner = ""
    matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


while(game_again == "s" or game_again == "S"):
    while True:
        screen()
        player_joga()
        cpu_joga()
        winner = win_verify()
        if(winner != "n") or (jogadas >= maxJogadas):
            break

    print("\n{}Fim de Jogo{}".format(Fore.RED, Fore.YELLOW))
    if winner == "X":
        print("")
        print("Você venceu!")
    elif winner == "O":
        print("")
        print("Game Over!")
    else:
        print("")
        print("Deu velha!")
    game_again = input("{}Digite [s] para continuar: {}".format(Fore.BLUE, Fore.RESET))
    reset()