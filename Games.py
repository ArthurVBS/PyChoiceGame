#Só tá aí pra tá

from random import randint
from time import sleep
import os

red = "\033[31m"
green = "\033[32m"
cyan = "\033[36m"
normal = "\033[m"
bolder = "\033[1m"
invertido = "\033[7;34;107m"
barra = "<=>" * 10
menu_principal = "Menu Principal"
opção_inválida_text = "Opção Inválida"

def limpar_terminal():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def opção_inválida():

    print(f"{red}{barra}{normal}\n{bolder}{opção_inválida_text:^30}{normal}\n{red}{barra}{normal}")
    sleep(1.5)

c = 0
while c == 0:

#Menu

    limpar_terminal()

    print(f"{cyan}{barra}{normal}\n{bolder}{menu_principal:^30}{normal}\n{cyan}{barra}{normal}")
    selecionar_menu = str(input("[0] Exit\n[1] Jokenpô\n[2] Par ou Ímpar\n>>> "))

    limpar_terminal()

#Encerrar 

    if selecionar_menu == "0":
        print(f"{bolder}encerrando...{normal}")
        sleep(1.5)
        limpar_terminal()
        print(f"{invertido}by: Arthur V.B.S.{normal}")
        break

#Jogo 001 - Jokenpô

    elif selecionar_menu == "1":

        parar = False
        while parar == False:
            Jokenpô = "Jokenpô"

            print(f"{cyan}{barra}{normal}\n{bolder}{Jokenpô:^30}{normal}\n{cyan}{barra}{normal}")
            
            jogar = str(input("[0] Exit\n[1] Jogar\n>>> "))

            if jogar == "0":

                parar = True

            elif jogar == "1":

                limpar_terminal()
                print(f"{cyan}{barra}{normal}")
                player = int(input("[0] Pedra\n[1] Papel\n[2] Tesoura\n>>> "))

                if player == 0 or player == 1 or player == 2:

                    cpu = randint(0, 2)
                    lista = ["Pedra","Papel","Tesoura"]

                    print(f"{cyan}{barra}{normal}\n         CPU  ||  {lista[cpu]}\n      Player  ||  {lista[player]}\n{cyan}{barra}{normal}")

                    if cpu == 0 and player == 2 or cpu == 1 and player == 0 or cpu == 2 and player == 1:
                        cpu_win = "CPU -- WIN"
                        print(f"{cpu_win:^30}")

                    elif player == 0 and cpu == 2 or player == 1 and cpu == 0 or player == 2 and cpu ==1:
                        player_win = "PLAYER -- WIN   "
                        print(f"{player_win:^30}")

                    else:
                        draw = "  DRAW -- EMPATE"
                        print(f"{draw:^30}")

                    input()
                    limpar_terminal()
                        
                else:
                    limpar_terminal()
                    opção_inválida()
                    limpar_terminal()

            else:
                limpar_terminal()
                opção_inválida()
                limpar_terminal()

#Jogo 002 - Par ou Ímpar

    elif selecionar_menu == "2":

        parar = False
        while parar == False:
            par_ou_ímpar = "Par ou Ímpar"

            print(f"{cyan}{barra}{normal}\n{bolder}{par_ou_ímpar:^30}{normal}\n{cyan}{barra}{normal}")
            
            jogar = str(input("[0] Exit\n[1] Jogar\n>>> "))

            if jogar == "0":

                parar = True

            elif jogar == "1":

                win_consecutivos = 0

                while True:

                    cpu = randint(1, 10)

                    player = int(input(f"{cyan}{barra}{normal}\nDiga um valor (1-10): "))
                    jogar = str(input("Par ou Ímpar? [P/I]  ")).replace(" ", "").upper()
                    print(f"{cyan}{barra}{normal}")
                    resultado = (cpu + player)

                    if player > 10 or player < 1 or jogar not in "PpIi":
                        print("Opção inválida...")
                        continue

                    if jogar in "Pp":

                        if resultado % 2 == 0:#Win Par

                            w = "PAR"
                            win = "Player Win"
                            print(f"Player {cyan}{player}{normal} || CPU  {cyan}{cpu}{normal}\nO total deu {cyan}{resultado}{green} {w}\n\n{win:^30}{normal}")
                            win_consecutivos += 1

                        elif resultado % 2 == 1:#Win Ímpar

                            w = "ÍMPAR"
                            win = "CPU Win"
                            print(f"Player {cyan}{player}{normal} || CPU  {cyan}{cpu}{normal}\nO total deu {cyan}{resultado}{red} {w}\n\n{win:^30}{normal}")
                            break

                    if jogar in "Ii":

                        if resultado % 2 == 1:#Win Ímpar

                            w = "ÍMPAR"
                            win = "Player Win"
                            print(f"Player {cyan}{player}{normal} || CPU  {cyan}{cpu}{normal}\nO total deu {cyan}{resultado}{green} {w}\n\n{win:^30}{normal}")
                            win_consecutivos += 1

                        elif resultado % 2 == 0:#Win Par

                            w = "PAR"
                            win = "CPU Win"
                            print(f"Player {cyan}{player}{normal} || CPU  {cyan}{cpu}{normal}\nO total deu {cyan}{resultado}{red} {w}\n\n{win:^30}{normal}")
                            break

                print(f"\n\033[31mGAME OVER!\033[m Você venceu {win_consecutivos} vezes.")
                input()
                limpar_terminal()

            else:
                limpar_terminal()
                opção_inválida()
                limpar_terminal()

#Opção Inválida

    else: 
        
        limpar_terminal()
        opção_inválida()
