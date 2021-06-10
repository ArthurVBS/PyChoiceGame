#____________________________________________________________________________________________________________
#Import
from tkinter import *
from tkinter import messagebox
from random import randint
from pygame import mixer
import os
#____________________________________________________________________________________________________________
#Functions

#Game Over
def gameover(value):
    if value == "True":
        root_status.place_forget()
        root_narrative.place_forget()
        clear_all()
        btn_continue.config(command = lambda: click_nothing(), fg = "#ccc", relief = "flat", cursor = "arrow",
                            activebackground=None, activeforeground=None)

        window.title("Game Over")
        root.config(bg = "#000")

        lbl_gameover_01 = Label(root, text = "- Game Over -", fg = fg, bg = "#000", font = "courier 50 bold")
        lbl_gameover_02 = Label(root, text = "Tente Novamente", bg = "#000", fg = fg, font = "courier 32 bold", anchor = N)
        btn_back_gameover = Button(root, text= "Voltar", bg = "#000", fg = fg, bd = 2, relief = "ridge", cursor="hand2",
        command = lambda: back_gameover(), font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)

        lbl_gameover_01.place(x = 10, y = 10, width = width - 40, height = 65)
        lbl_gameover_02.place(x = 10, y = 110, width = width - 40, height = 65)
        btn_back_gameover.place(x = 225, y = 365, width = 250, height = 60)

        def back_gameover():
            lbl_gameover_01.place_forget()
            lbl_gameover_02.place_forget()
            btn_back_gameover.place_forget()
            clear_all()
            show_main_menu()

    else:
        pass

#Show
def show_main_menu():
    window.title("Main Menu")
    root.config(bg = bg)

    lbl_title.place(x = 10, y = 10, width = width - 40, height = 65)
    lbl_subtitle.place(x = 10, y = 75, width = width - 40, height = 65)
    lbl_version.place(x = 585, y = 420, width = 110, height = 25)
    btn_newgame.place(x = 225, y = 140, width = 250, height = 60)
    btn_continue.place(x = 225, y = 215, width = 250, height = 60)
    btn_credits.place(x = 225, y = 290, width = 250, height = 60)
    btn_quit.place(x = 225, y = 365, width = 250, height = 60)

def show_heart(hearts):
    global game_over
    #Heart - +5
    if hearts > 5:
        hearts = 5

    #Heart - 1
    if hearts >= 1:
        lbl_heart_01.config(image = heart_11_dic)
    elif hearts == 0.5:
        lbl_heart_01.config(image = heart_01_dic)
    elif hearts < 0.5:
        lbl_heart_01.config(image = heart_00_dic)
        game_over = True
        gameover("True")

    #Heart - 2
    if hearts >= 2:
        lbl_heart_02.config(image = heart_11_dic)
    elif hearts == 1.5:
        lbl_heart_02.config(image = heart_01_dic)
    elif hearts < 1.5:
        lbl_heart_02.config(image = heart_00_dic)

    #Heart - 3
    if hearts >= 3:
        lbl_heart_03.config(image = heart_11_dic)
    elif hearts == 2.5:
        lbl_heart_03.config(image = heart_01_dic)
    elif hearts < 2.5:
        lbl_heart_03.config(image = heart_00_dic)

    #Heart - 4
    if hearts >= 4:
        lbl_heart_04.config(image = heart_11_dic)
    elif hearts == 3.5:
        lbl_heart_04.config(image = heart_01_dic)
    elif hearts < 3.5:
        lbl_heart_04.config(image = heart_00_dic)

    #Heart - 5
    if hearts == 5:
        lbl_heart_05.config(image = heart_11_dic)
    elif hearts == 4.5:
        lbl_heart_05.config(image = heart_01_dic)
    elif hearts < 4.5:
        lbl_heart_05.config(image = heart_00_dic)

def show_food(foods):
    global game_over
    #Foods - +5
    if foods > 5:
        foods = 5

    #Food - 1
    if foods >= 1:
        lbl_food_01.config(image = food_11_dic)
    elif foods == 0.5:
        lbl_food_01.config(image = food_01_dic)
    elif foods < 0.5:
        lbl_food_01.config(image = food_00_dic)
        game_over = True
        gameover("True")

    #Food - 2
    if foods >= 2:
        lbl_food_02.config(image = food_11_dic)
    elif foods == 1.5:
        lbl_food_02.config(image = food_01_dic)
    elif foods < 1.5:
        lbl_food_02.config(image = food_00_dic)

    #Food - 3
    if foods >= 3:
        lbl_food_03.config(image = food_11_dic)
    elif foods == 2.5:
        lbl_food_03.config(image = food_01_dic)
    elif foods < 2.5:
        lbl_food_03.config(image = food_00_dic)

    #Food - 4
    if foods >= 4:
        lbl_food_04.config(image = food_11_dic)
    elif foods == 3.5:
        lbl_food_04.config(image = food_01_dic)
    elif foods < 3.5:
        lbl_food_04.config(image = food_00_dic)

    #Food - 5
    if foods >= 5:
        lbl_food_05.config(image = food_11_dic)
    elif foods == 4.5:
        lbl_food_05.config(image = food_01_dic)
    elif foods < 4.5:
        lbl_food_05.config(image = food_00_dic)

def show_item(lighter, wolfhide, future_friendship, nausea, shotgun, crowbar, screwdriver, gear):
    #lighter
    if lighter == True:
        lbl_item_lighter.config(image = item_lighter_dic)
    elif lighter == False:
        lbl_item_lighter.config(image = empty_01_dic)
    
    #wolfhide
    if wolfhide == True:
        lbl_item_wolfhide.config(image = item_wolfhide_dic)
    elif wolfhide == False:
        lbl_item_wolfhide.config(image = empty_01_dic)

    #future_friendship
    if future_friendship == True:
        lbl_item_future_friendship.config(image = item_future_friendship_dic)
    elif future_friendship == False:
        lbl_item_future_friendship.config(image = empty_01_dic)

    #nausea
    if nausea == True:
        lbl_item_nausea.config(image = item_nausea_dic)
    elif nausea == False:
        lbl_item_nausea.config(image = empty_01_dic)

    #shotgun
    if shotgun == True:
        lbl_item_shotgun.config(image = item_shotgun_dic)
    elif shotgun == False:
        lbl_item_shotgun.config(image = empty_01_dic)

    #crowbar
    if crowbar == True:
        lbl_item_crowbar.config(image = item_crowbar_dic)
    elif crowbar == False:
        lbl_item_crowbar.config(image = empty_01_dic)

    #screwdriver
    if screwdriver == True:
        lbl_item_screwdriver.config(image = item_screwdriver_dic)
    elif screwdriver == False:
        lbl_item_screwdriver.config(image = empty_01_dic)

    #gear
    if gear == True:
        lbl_item_gear.config(image = item_gear_dic)
    elif gear == False:
        lbl_item_gear.config(image = empty_01_dic)

def show_key():
    #Key - B
    if bronze_key == True:
        lbl_key_B.config(image = key_B_dic)
    elif bronze_key == False:
        lbl_key_B.config(image = key_E_dic)

    #Key - S
    if silver_key == True:
        lbl_key_S.config(image = key_S_dic)
    elif silver_key == False:
        lbl_key_S.config(image = key_E_dic)

    #Key - G
    if golden_key == True:
        lbl_key_G.config(image = key_G_dic)
    elif golden_key == False:
        lbl_key_G.config(image = key_E_dic)

def show_way():
    global level
    global bronze_key
    global silver_key
    global golden_key
    global world

    lbl_just_way_01.config(image = just_way_dic)
    lbl_just_way_02.config(image = just_way_dic)
    lbl_just_way_03.config(image = just_way_dic)
    lbl_just_way_04.config(image = just_way_dic)
    lbl_just_way_05.config(image = just_way_dic)
    lbl_just_way_06.config(image = just_way_dic)
    lbl_just_way_07.config(image = just_way_dic)
    lbl_just_way_08.config(image = just_way_dic)

    if level == 1:
        lbl_just_way_01.config(image = way_dic)
    elif level == 2:
        lbl_just_way_02.config(image = way_dic)
    elif level == 3:
        lbl_just_way_03.config(image = way_dic)
    elif level == 4:
        lbl_just_way_04.config(image = way_dic)
    elif level == 5:
        lbl_just_way_05.config(image = way_dic)
    elif level == 6:
        lbl_just_way_06.config(image = way_dic)
    elif level == 7:
        lbl_just_way_07.config(image = way_dic)
    elif level == 8:
        lbl_just_way_08.config(image = way_dic)
    else:
        print("Level Up")
        level = 1
        world += 1
        lbl_just_way_01.config(image = way_dic)

    if world == 1:
        bronze_key = True
    elif world == 2:
        silver_key = True
    elif world == 3:
        golden_key = True

    show_key()
    show_scenario()

def show_scenario():
    global world
    if world == 1:
        lbl_scenario.config(image = scenario_01_dic)
    elif world == 2:
        lbl_scenario.config(image = scenario_02_dic)
    elif world == 3:
        lbl_scenario.config(image = scenario_03_dic)

def show_toplevel(title, lbl_text, losewin_hearts, losewin_foods, w, selected_option):
    global world
    global game_over

    #Tkinter
    win_toplevel = Toplevel()
    win_toplevel.geometry(f"370x320+{pos_x + 200}+{pos_y + 100}")
    win_toplevel.title(title)
    win_toplevel.iconbitmap(directory + "/Images/Icons/icon_02.ico")
    win_toplevel.resizable(False, False)
    win_toplevel.configure(background = bg_frames)

    #Labels and Buttons

    lbl_tl_main = Label(win_toplevel, text = "A sua escolha ocasionou:", justify=CENTER, font = "courier 16 bold", bg = bg_frames)
    lbl_tl = Label(win_toplevel, text = f"{lbl_text}", justify=CENTER, font = "courier 14 italic",
                anchor = N, bg = bg, bd = 1, relief = "sunken")
    btn_tl = Button(win_toplevel, text= "OK", bg=bg, bd = 2, relief = "ridge", command = lambda: show_narrative_01(),
                    cursor="hand2", font = "courier 14 bold", activebackground="#ccc", activeforeground=fg)

    def show_narrative_01():
        win_toplevel.destroy()

    def show_narrative_02():
        show_introduction_and_tutorial_02()
        win_toplevel.destroy()
    
    def show_narrative_03():
        """show_introduction_and_tutorial_03()"""
        win_toplevel.destroy()

    if game_over != True:
        if w == 8:
            lbl_next = Label(win_toplevel, text = "Clique em Ok para avançar!!!", font = "courier 14 italic", bg=bg_frames)
            lbl_next.place(x=10, y = 235, width = 350, height = 30)
            if world == 2:
                btn_tl.config(command= lambda: show_narrative_02())
            if world == 3:
                btn_tl.config(command= lambda: show_narrative_03())
        else:
            pass

    #Frame and Labels (PhotoImage)

    frame_toplevel_heart = Frame(win_toplevel, bd = 1, relief = "sunken", bg = bg)
    frame_toplevel_food = Frame(win_toplevel, bd = 1, relief = "sunken", bg = bg)
    frame_toplevel_item_key = Frame(win_toplevel, bd = 1, relief = "sunken", bg = bg)

    #Hearts
    if losewin_hearts >= 0:
        sinal_hearts = "+"

    elif losewin_hearts < 0:
        sinal_hearts = "-" 

    if losewin_hearts == 0:
        phImg_heart_01 = heart_00_dic
        phImg_heart_02 = heart_00_dic

    elif losewin_hearts == 0.5 or losewin_hearts == -0.5:
        phImg_heart_01 = heart_01_dic
        phImg_heart_02 = heart_00_dic

    elif losewin_hearts == 1 or losewin_hearts == -1:
        phImg_heart_01 = heart_11_dic
        phImg_heart_02 = heart_00_dic

    elif losewin_hearts == 1.5 or losewin_hearts == -1.5:
        phImg_heart_01 = heart_11_dic
        phImg_heart_02 = heart_01_dic

    elif losewin_hearts == 2 or losewin_hearts == -2:
        phImg_heart_01 = heart_11_dic
        phImg_heart_02 = heart_11_dic

    #Foods
    if losewin_foods >= 0:
        sinal_foods = "+"

    elif losewin_foods < 0:
        sinal_foods = "-"

    if losewin_foods == 0:
        phImg_food_01 = food_00_dic
        phImg_food_02 = food_00_dic

    elif losewin_foods == 0.5 or losewin_foods == -0.5:
        phImg_food_01 = food_01_dic
        phImg_food_02 = food_00_dic

    elif losewin_foods == 1 or losewin_foods == -1:
        phImg_food_01 = food_11_dic
        phImg_food_02 = food_00_dic

    elif losewin_foods == 1.5 or losewin_foods == -1.5:
        phImg_food_01 = food_11_dic
        phImg_food_02 = food_01_dic

    elif losewin_foods == 2 or losewin_foods == -2:
        phImg_food_01 = food_11_dic
        phImg_food_02 = food_11_dic

    #Item / Key
    if w == 2 and selected_option == "A": #friendship
        phImg_item_01 = item_future_friendship_dic
        phImg_item_02 = empty_00_dic

    elif w  == 2 and selected_option == "C": #wolfhide
        phImg_item_01 = item_wolfhide_dic
        phImg_item_02 = empty_00_dic

    elif w == 7 and selected_option == "A": #nausea
        phImg_item_01 = item_nausea_dic
        phImg_item_02 = empty_00_dic

    elif w == 8: #shotgun and key silver
        phImg_item_01 = item_shotgun_dic
        phImg_item_02 = key_S_dic

    else:
        phImg_item_01 = empty_00_dic
        phImg_item_02 = empty_00_dic

    if phImg_item_01 != empty_00_dic or phImg_item_02 != empty_00_dic:
        sinal_item_key = "+"
    elif phImg_item_01 == empty_00_dic and phImg_item_02 == empty_00_dic:
        sinal_item_key = ""

    lbl_heart = Label(frame_toplevel_heart, text = sinal_hearts, justify=CENTER, font = "courier 16 italic", bg = bg)
    lbl_food = Label(frame_toplevel_food, text = sinal_foods, justify=CENTER, font = "courier 16 italic", bg = bg)
    lbl_item_key = Label(frame_toplevel_item_key, text = sinal_item_key, justify=CENTER, font = "courier 16 italic", bg = bg)

    lbl_heart_losewin_01 = Label(frame_toplevel_heart, image = phImg_heart_01, bg = bg)
    lbl_heart_losewin_02 = Label(frame_toplevel_heart, image = phImg_heart_02, bg = bg)

    lbl_food_losewin_01 = Label(frame_toplevel_food, image = phImg_food_01, bg = bg)
    lbl_food_losewin_02 = Label(frame_toplevel_food, image = phImg_food_02, bg = bg)

    lbl_item_key_01 = Label(frame_toplevel_item_key, image = phImg_item_01, bg = bg)
    lbl_item_key_02 = Label(frame_toplevel_item_key, image = phImg_item_02, bg = bg)

    #.Place

    lbl_tl_main.place(x = 10, y = 10, width = 350, height = 30)
    lbl_tl.place(x = 10, y = 50, width = 350, height = 120)
    btn_tl.place(x = 145, y = 270, width = 80, height = 40)

    frame_toplevel_heart.place(x = 10, y = 180, width = 110, height = 45)
    frame_toplevel_food.place(x = 130, y = 180, width = 110, height = 45)
    frame_toplevel_item_key.place(x = 250, y = 180, width = 110, height = 45)

    lbl_heart.place(x = 5, y = 5, width = 30, height = 35)
    lbl_food.place(x = 5, y = 5, width = 30, height = 35)
    lbl_item_key.place(x = 5, y = 5, width = 30, height = 35)

    lbl_heart_losewin_01.place(x = 35, y = 5, width = 35, height = 35)
    lbl_heart_losewin_02.place(x = 70, y = 5, width = 35, height = 35)

    lbl_food_losewin_01.place(x = 35, y = 5, width = 35, height = 35)
    lbl_food_losewin_02.place(x = 70, y = 5, width = 35, height = 35)

    lbl_item_key_01.place(x = 35, y = 5, width = 35, height = 35)
    lbl_item_key_02.place(x = 70, y = 5, width = 35, height = 35)

    win_toplevel.mainloop()

def show_button_continue():
    if ok_cancel_newgame == True:
            window.title("Level 01")
            btn_continue.config(fg = "#000", relief = "ridge", command = lambda: click_continue(), activebackground="#ccc",
                                activeforeground=fg, cursor="hand2")

def show_game():
    root_status.place(x = 0, y = 280, width = width - 23, height = 175)
    root_narrative.place(x = 0, y = 0, width = width - 23, height = 280)
    btn_back_newgame.place(x = 605, y = 60, width = 85, height = 45)

    default()

    show_heart(hearts)
    show_food(foods)
    show_item(lighter, wolfhide, future_friendship, nausea, shotgun, crowbar, screwdriver, gear)
    show_key()
    show_way()
    show_labels_options()

    clear_main_menu()

def show_introduction_and_tutorial_01():
    global ok_cancel_newgame
    global executions_made
    window.title("Introdução")
    clear_all()

    #Show Introductions
    def show_introduction_01():
        global executions_made
        introduction_text = "Buscando descanso, após um longo e\n" +\
        "complicado ano na capital, Sam - Você -\n" +\
        "decide visitar os seus pais que moram num\n" +\
        "antigo vilarejo bem distante da capital.\n\n" +\
        "Você pega seu carro e parte na estrada\n" +\
        "até o vilarejo."

        lbl_int_and_tut.config(text = introduction_text)
    
    def show_introduction_02():
        global executions_made
        introduction_text = "Chegando próximo a principal entrada do\n" +\
        "vilarejo, o portão leste, você observa que ele\n" +\
        "se encontra entreaberto e que há uma mensagem\n" +\
        "escrita em um tom de vermelho bem peculiar.\n\n\n" +\
        "Não ultrapasse!!! Não ultrapasse!!!\n"

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_03():
        global executions_made
        introduction_text = "Você se pergunta o motivo, mas segue em\n" +\
        "frente, ao adentrar no vilarejo, você\n" +\
        "busca a casa de seus pais, chegando lá\n" +\
        "você não os encontra e começa a notar o\n" +\
        "silêncio eloquente daquele vilarejo.\n"

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_04():
        global executions_made
        introduction_text = "Na tentavia de perguntar a alguém onde\n" +\
        "estão seus pais, Você falha miseravelmente,\n" +\
        "afinal você não encontrou uma alma sequer,\n" +\
        "somente um caderno de anotação de um outro\n" +\
        "morador do vilarejo que dizia:\n"

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_05():
        global executions_made
        introduction_text = "2005/03/22 - Página 1/3\n\n" +\
        "O vilarejo já não é mais o mesmo,\n" +\
        "desde que aquele estranho minerador\n" +\
        "encontrou um minério nas [...]\n\n" +\
        "- O resto dessa página foi arrancado às pressas -\n"

        lbl_int_and_tut.config(text = introduction_text)
        
    def show_introduction_06():
        global executions_made
        introduction_text = "2005/03/23 - Página 2/3\n\n" +\
        "As pessoas estão indo cegamente até\n" +\
        "esse lugar para conseguir mais daquele\n" +\
        "minério bobo, todos querem ficar ricos.\n\n" +\
        "O vilarejo tem ficado bem vazio desde então.\n"


        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_07():
        global executions_made
        introduction_text = "2005/03/24 - Página 3/3\n\n" +\
        "Prefiro como era antes, uma vida mais\n" +\
        "animada, sem perda de tempo atrás de\n" +\
        "riquezas, por isso optei em viver em\n" +\
        "minha casa na árvore, longe de todo e\n" +\
        "qualquer tipo de ganância.\n\n" +\
        "A Floresta tornou-se meu novo lar."

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_08():
        window.title("Introdução")
        lbl_int_and_tut_main.config(text = "- Introdução -")

        global executions_made
        introduction_text = "Tendo somente essa informação, Você se\n" +\
        "direciona ao portão norte do Vilarejo,\n" +\
        "trancado por um cadeado de bronze, o portão\n" +\
        "pode ser aberto através da chave de bronze\n" +\
        "que você portava.\n\n" +\
        "Esse caminho dá direto para a Floresta\n" +\
        "A sua busca para saber o que houve\n" +\
        " naquele vilarejo começa aqui..."

        lbl_int_and_tut.config(text = introduction_text)

    #Show Tutorial
    def show_tutorial_01():
        window.title("Tutorial")
        lbl_int_and_tut_main.config(text = "- Tutorial -")

        global executions_made
        introduction_text = "O jogo consiste em sobreviver e avançar na\n" +\
        "história, possuindo portanto o efeito borboleta.\n\n" +\
        "Sendo exposto a várias perguntas suas\n" +\
        "decisões tem consequências a longo e curto prazo.\n\n" +\
        "Possuindo um número limitado de vida e de comida\n" +\
        "em sua mochila você deve fazer escolhas sábias\n" +\
        "para que nada lhe falte."

        lbl_int_and_tut.config(text = introduction_text)

    def show_tutorial_02():
        global executions_made
        introduction_text = "O número de comida e de vida variam entre\n" +\
        "0 e 5, ao chegar em 0 game over.\n\n" +\
        "O jogo se inicia com 3 de vida, 3 de comidas\n" +\
        "na mochila, uma chave de bronze e um isqueiro."

        lbl_int_and_tut.config(text = introduction_text) 

    #Next and Back
    def next_(x):
        global executions_made
        if x == 1:
            window.title("Introdução")
            show_introduction_01()
            executions_made +=1

        elif x == 2:
            show_introduction_02()
            executions_made += 1

        elif x == 3:
            show_introduction_03()
            executions_made += 1

        elif x == 4:
            show_introduction_04()
            executions_made += 1

        elif x == 5:
            show_introduction_05()
            executions_made += 1

        elif x == 6:
            show_introduction_06()
            executions_made += 1

        elif x == 7:
            show_introduction_07()
            executions_made += 1

        elif x == 8:
            show_introduction_08()
            executions_made += 1

        elif x == 9:
            show_tutorial_01()
            executions_made += 1

        elif x == 10:
            show_tutorial_02()
            executions_made += 1

        elif x == 11:
            lbl_int_and_tut_main.place_forget()
            lbl_int_and_tut.place_forget()
            btn_int_and_tut_next.place_forget()
            btn_int_and_tut_back.place_forget()
            show_game()
            show_button_continue()
        
    def back_(x):
        global executions_made
        x -= 2
        if x == 0:
            lbl_int_and_tut_main.place_forget()
            lbl_int_and_tut.place_forget()
            btn_int_and_tut_next.place_forget()
            btn_int_and_tut_back.place_forget()
            show_main_menu()

        elif x == 1:
            show_introduction_01()
            executions_made -= 1

        elif x == 2:
            show_introduction_02()
            executions_made -= 1

        elif x == 3:
            show_introduction_03()
            executions_made -= 1

        elif x == 4:
            show_introduction_04()
            executions_made -= 1

        elif x == 5:
            show_introduction_05()
            executions_made -= 1

        elif x == 6:
            show_introduction_06()
            executions_made -= 1

        elif x == 7:
            show_introduction_07()
            executions_made -= 1

        elif x == 8:
            show_introduction_08()
            executions_made -= 1

        elif x == 9:
            show_tutorial_01()
            executions_made -= 1

        elif x == 10:
            show_tutorial_02()
            executions_made -= 1

    #Labels & Buttons
    executions_made = 2

    lbl_int_and_tut_main = Label(root, text = " - Introdução - ", bg=bg, font = "courier 40 bold")
    lbl_int_and_tut = Label(root, text = "", bg=bg, bd = 5, relief = "solid", font = "courier 16 italic",
    anchor = CENTER, justify = CENTER)
    show_introduction_01()
    btn_int_and_tut_next = Button(root, text= "Próximo", bg=bg, bd = 2, relief = "ridge", command = lambda: next_(executions_made), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)
    btn_int_and_tut_back = Button(root, text= "Voltar", bg=bg, bd = 2, relief = "ridge", command = lambda: back_(executions_made), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)

    #Place
    lbl_int_and_tut_main.place(x = 10, y = 10, width = width - 40, height = 65)
    lbl_int_and_tut.place(x = 10, y = 80, width = width -40, height = 300)
    btn_int_and_tut_next.place(x = 440, y = 390, width = 250, height = 50)
    btn_int_and_tut_back.place(x = 10, y = 390, width = 250, height = 50)

def show_introduction_and_tutorial_02():
    global ok_cancel_newgame
    global executions_made
    window.title("Avançando")
    clear_all()

    #Show Introductions
    def show_introduction_01():
        global executions_made
        introduction_text = "Chegando na casa da árvore você encontra\n" +\
        "um homem falando consigo mesmo e repetindo\n" +\
        "as seguintes palavras:\n\n" +\
        "\"Não não não, a verdade não pode pegar o\n" +\
        "Lucas, o Lucas é bonzinho, aquela verdade\n" +\
        "não é de verdade, não é, não é...\""

        lbl_int_and_tut.config(text = introduction_text)
    
    def show_introduction_02():
        global executions_made
        introduction_text = "Você decide se aproximar um pouco mais e\n" +\
        "chamar a atenção dele, Lucas então se vira\n" +\
        "para você perplexo mandando você se afastar,\n" +\
        "dizendo as seguintes palavras:\n\n" +\
        "\"Não chegue perto, saí, você não é de verdade,\n" +\
        "a Verdade não pode pegar o Lucas, o Lucas\n" +\
        "não foi ganancioso, não chega mais perto!\""

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_03():
        global executions_made
        introduction_text = "Então você para, e tenta conversar com o\n" +\
        "Lucas para saber o que aconteceu, todavia sem\n" +\
        "sucesso ele fica te olhando com os olhos\n" +\
        "vermelhos, repetindo as seguintes palavras:\n\n" +\
        "\"A verdade veio buscar o Lucas, não, ,não, não!\n" +\
        "Essa verdade não existe! Isso é coisa de\n" +\
        "minha cabeça, não, não, não!\""

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_04():
        global executions_made
        introduction_text = "Você decide se aproximar um pouco mais\n" +\
        "para tentar conversar com ele, todavia Lucas\n" +\
        "se treme ao te ver chegar e pega uma escopeta\n" +\
        "e aponta para a sua direção, você para, e pede\n" +\
        "para ele abaixar a arma, todavia ele lhe diz:\n\n" +\
        "\"Não, não, não, a verdade nunca vai pegar\n" +\
        " o Lucas, essa verdade está corrompida!!!\""

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_05():
        global executions_made
        introduction_text = "Em meio àquela floresta ouve-se ao longe\n" +\
        "um disparo de escopeta, era O Lucas seifando\n" +\
        "a sua prória vida com um tiro na cabeça!\n\n" +\
        "Você fica estagnada, não consegue nem\n" +\
        "acreditar, até que a consciência volta em si.\n\n" +\
        "Você toma para si aquela escopeta de chumbinho\n" +\
        "que possui apenas uma munição, você também\n" +\
        "encontra a chave de prata e além disso você\n" +\
        "acha outra anotação do Lucas, que diz:"

        lbl_int_and_tut.config(text = introduction_text)
        
    def show_introduction_06():
        global executions_made
        introduction_text = "2005/03/25 - Página 1/1\n\n" +\
        "Voltei ao vilarejo, mas não encontrei\n" +\
        "ninguém, somente vi indo em direção\n" +\
        "aos Alpes aquele minerador, ele me viu\n" +\
        "e vindo até mim, me ofereceu um cristal\n" +\
        "que revelaria a verdade, eu de imediato\n"+\
        "recusei, mas o vislumbre daquele cristal\n" +\
        "está me enlouquecendo!"

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_07():
        global executions_made
        introduction_text = "Com isso você decide ir até os Alpes e\n" +\
        "questionar a esse tal de \"Minerador\" o\n" +\
        "que está acontecendo e o que é esse cristal.\n\n" +\
        "Ao sair pelos fundos da casa da árvore\n" +\
        "você encontra uma trilha em direção ao\n" +\
        "vilarejo, seguindo toda vida você abre\n"+\
        "com a chave de prata uma antiga porta\n" +\
        "enferrujada na área nordeste do vilarejo, já \n" +\
        "é noite, mas você está de volta ao vilarejo."

        lbl_int_and_tut.config(text = introduction_text)

    #Next and Back
    def next_(x):
        global executions_made
        if x == 1:
            window.title("Avançando")
            show_introduction_01()
            executions_made +=1

        elif x == 2:
            show_introduction_02()
            executions_made += 1

        elif x == 3:
            show_introduction_03()
            executions_made += 1

        elif x == 4:
            show_introduction_04()
            executions_made += 1

        elif x == 5:
            show_introduction_05()
            executions_made += 1

        elif x == 6:
            show_introduction_06()
            executions_made += 1

        elif x == 7:
            show_introduction_07()
            executions_made += 1

        elif x == 8:
            lbl_int_and_tut_main.place_forget()
            lbl_int_and_tut.place_forget()
            btn_int_and_tut_next.place_forget()
            btn_int_and_tut_back.place_forget()
            click_continue()
            show_button_continue()
        
    def back_(x):
        global executions_made
        x -= 2
        if x == 0:
            pass

        elif x == 1:
            show_introduction_01()
            executions_made -= 1

        elif x == 2:
            show_introduction_02()
            executions_made -= 1

        elif x == 3:
            show_introduction_03()
            executions_made -= 1

        elif x == 4:
            show_introduction_04()
            executions_made -= 1

        elif x == 5:
            show_introduction_05()
            executions_made -= 1

        elif x == 6:
            show_introduction_06()
            executions_made -= 1

        elif x == 7:
            show_introduction_07()
            executions_made -= 1

    #Labels & Buttons
    executions_made = 2

    lbl_int_and_tut_main = Label(root, text = " - Avançando - ", bg=bg, font = "courier 40 bold")
    lbl_int_and_tut = Label(root, text = "", bg=bg, bd = 5, relief = "solid", font = "courier 16 italic",
    anchor = CENTER, justify = CENTER)
    show_introduction_01()
    btn_int_and_tut_next = Button(root, text= "Próximo", bg=bg, bd = 2, relief = "ridge", command = lambda: next_(executions_made), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)
    btn_int_and_tut_back = Button(root, text= "Voltar", bg=bg, bd = 2, relief = "ridge", command = lambda: back_(executions_made), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)

    #Place
    lbl_int_and_tut_main.place(x = 10, y = 10, width = width - 40, height = 65)
    lbl_int_and_tut.place(x = 10, y = 80, width = width -40, height = 300)
    btn_int_and_tut_next.place(x = 440, y = 390, width = 250, height = 50)
    btn_int_and_tut_back.place(x = 10, y = 390, width = 250, height = 50)

def show_labels_options():
    global op
    global wd
    op += 1
    
    if op == 1:
        if wd == 1: #A Floresta
            crossroads_text = "Você está caminhando a um\ncerto tempo, o seu estômago\nronca. Você encontra algumas\n" +\
            "frutinhas azuis em um arbusto\nque aparentam ser comestíveis."
            opt_A_text = "Pegar as frutinhas do\narbusto e saciar a sua fome;"
            opt_B_text = "Ignorar as frutinhas e\nseguir em frente;"
            opt_C_text = "Pegar alguma comida da\nmochila;"

        elif wd == 2: #OS Alpes
            crossroads_text = "hi."
            opt_A_text = "123;"
            opt_B_text = "456;"
            opt_C_text = "789;"

        elif wd == 3: #AS Minas
            crossroads_text = "hi."
            opt_A_text = "123;"
            opt_B_text = "456;"
            opt_C_text = "789;"
    
    elif op == 2:
        if wd == 1:
            crossroads_text = "Em pleno dia você ouve um\nuivo, paralisada, você observa\nque o uivo vem de um lobo\n" +\
            "filhote preso a uma armadilha\nde urso."
            opt_A_text = "Salvar o lobinho daquele\nsofrimento;"
            opt_B_text = "Seguir em frente, como se\nnada tivesse ocorrido;"
            opt_C_text = "Matar o lobinho e pegar\nsua carne e couro;"    

    elif op == 3:
        if wd == 1:
            crossroads_text = "Seguindo a caminhada, uma\nlonga chuva toma a floresta.\nNa sua frente há um abrigo\n" +\
            "abandonado, aparentemente\nseguro e bem sujo."
            opt_A_text = "Entrar na casa, explorar e\nesperar a chuva passar;"
            opt_B_text = "Seguir em frente, apesar\n da chuva pesada;"
            opt_C_text = "Esperar a chuva passar na\n sacada do abrigo;"

    elif op == 4:
        if wd == 1:
            crossroads_text = "Após a longa chuva você se\ndepara com um grande e fundo\nriacho, há uma velha ponte\n" +\
            "suspensa, uma margem bem ao\nlonge e uma parte\naparentemente rasa."
            opt_A_text = "Atravessar pela velha\nponte suspensa;"
            opt_B_text = "Atravessar pela margem\nque está distante;"
            opt_C_text = "Atravessar pela parte\naparentemente mais rasa;"

    elif op == 5:
        if wd == 1:
            crossroads_text = "Ate aqui o sol a acompanhava,\nporém a noite vem a espreita,\né necessário parar, comer e\n" +\
            "dormir, você observa uma\ncaverna, um espaço entre as\ncopas das árvores e um\nlocal no chão para dormir."
            opt_A_text = "Dormir na caverna;"
            opt_B_text = "Dormir nas copas das\nárvores;"
            opt_C_text = "Dormir no chão da\nfloresta;"

    elif op == 6:
        if wd == 1:
            crossroads_text = "Ao caminhar você começa a\nsentir fome, você observa a\nsua esquerda e a sua direita\n" +\
            "cogumelos de duas cores\ndistintas (Azuis e Vermelhos)\ncrescendo sobre os troncos\ndas árvores."
            opt_A_text = "Comer o cogumelo Azul;"
            opt_B_text = "Comer o cogumelo Vermelho;"
            opt_C_text = "Seguir em frente, ignorar\nos cogumelos, pois não sou o\nMario;"

    elif op == 7:
        if wd == 1:
            crossroads_text = "Próximo ao fim da floresta\nvocê encontra uma trifurcação,\nhá um caminho cheio de flores\n" +\
            "com um aroma bem forte,\nhá um caminho cheio de\nespinhos e há um lamaceiro"
            opt_A_text = "Passar pelas flores de\naroma forte;"
            opt_B_text = "Passar pelo caminho\nespinhoso;"
            opt_C_text = "Passar por um lamaceiro"

    elif op == 8:
        if wd == 1:
            crossroads_text = "Ao caminhar você sente um\nfio esticar em sua perna\ndireita, seu corpo para e reflete\n" +\
            "rapidamente no que fazer..."
            opt_A_text = "Tentar avançar, ignorando\n o fio;"
            opt_B_text = "Tentar voltar e passar\npor cima do fio;"
            opt_C_text = "Tentar ir até a fonte\ndo fio e tentar desarma-lo;"
        
        op = 0
        wd += 1

    lbl_crossroads.config(text = crossroads_text)    
    lbl_opt_A.config(text = f"- A - {opt_A_text}")
    lbl_opt_B.config(text = f"- B - {opt_B_text}")
    lbl_opt_C.config(text = f"- C - {opt_C_text}")

#Delete
def clear_main_menu():
    lbl_title.place_forget()
    lbl_subtitle.place_forget()
    lbl_version.place_forget()
    btn_newgame.place_forget()
    btn_continue.place_forget()
    btn_credits.place_forget()
    btn_quit.place_forget()

def clear_all():
    #Frames
    root_status.place_forget()
    root_narrative.place_forget()

    #Labels
    lbl_title.place_forget()
    lbl_subtitle.place_forget()
    lbl_version.place_forget()
    lbl_credits_01.place_forget()
    lbl_credits_02.place_forget()

    #Buttons
    btn_newgame.place_forget()
    btn_continue.place_forget()
    btn_credits.place_forget()
    btn_quit.place_forget()
    btn_back.place_forget()
    btn_back_newgame.place_forget()

#Click
def click_newgame():
    global ok_cancel_newgame
    ok_cancel_newgame = messagebox.askokcancel(title = "Novo Jogo", message = "Desejas Iniciar um novo Jogo?",
    detail = "Caso possua um Save anterior ele será sobrescito")

    if ok_cancel_newgame == True:
        btn_continue.config(command = lambda: click_nothing(), fg = "#ccc", relief = "flat", cursor = "arrow",
                            activebackground=None, activeforeground=None)

        show_introduction_and_tutorial_01()

def click_nothing():
    messagebox.showerror(title = "Continuar - Error", icon = messagebox.INFO,
    message = "Inicie um Novo Jogo para que você\npossa continuar de onde parou.")

def click_continue():
    global level
    window.title(f"Level 0{level}")
    root_status.place(x = 0, y = 280, width = width - 23, height = 175)
    root_narrative.place(x = 0, y = 0, width = width - 23, height = 280)
    btn_back_newgame.place(x = 610, y = 60, width = 80, height = 45)

    clear_main_menu()

def click_credits():
    window.title("Créditos")
    clear_all()

    lbl_title.place(x = 10, y = 10, width = width - 40, height = 65)
    lbl_subtitle.place(x = 10, y = 75, width = width - 40, height = 65)
    lbl_version.place(x = 585, y = 420, width = 110, height = 25)
    btn_back.place(x = 225, y = 365, width = 250, height = 60)
    lbl_credits_01.place(x = 125, y = 145, width = 210, height = 210)
    lbl_credits_02.place(x = 375, y = 145, width = 210, height = 210)

def click_quit():
    ok_cancel_quit = messagebox.askokcancel(title = "Sair?", message = "Você realmente deseja sair?\t\t",
    detail = "Desde já obrigado por jogar")

    if ok_cancel_quit == True:
        quit()

def click_back_to_main_menu():
    clear_all()
    lbl_title.config(text = " - The Truth - ", bg = bg, fg = "#000")
    show_main_menu()

#Others functions
def default():
    global bronze_key
    global silver_key
    global golden_key
    global game_over
    global gear
    global screwdriver
    global crowbar
    global shotgun
    global nausea
    global future_friendship
    global wolfhide
    global lighter
    global op
    global world
    global level
    global wd
    global hearts
    global foods
    global x
    bronze_key = silver_key = golden_key = False
    shotgun = nausea = future_friendship = wolfhide = False
    gear = screwdriver = crowbar = False
    lighter = True
    op = 0
    world = level = wd = 1
    hearts = foods = 3
    game_over = False

def music():
    mixer.init()
    mixer.music.load(directory + '/Sound/soundtrack.mp3')
    mixer.music.play(-1)

def options(selected_option):
    global game_over
    global hearts
    global foods
    global level
    global gear
    global screwdriver
    global crowbar
    global shotgun
    global nausea
    global future_friendship
    global wolfhide
    w = level
    level+=1
    random = randint(1,4)
    show_way()
    show_labels_options()

    if w == 1:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2:
                lbl_toplevel = "As frutinhas não eram tão\ncomestíveis assim."
                losewin_hearts = -0.5
                losewin_foods = 0
            elif random == 3:
                lbl_toplevel = "As frutinhas até que são\ncomestíveis."
                losewin_hearts = 0
                losewin_foods = 0
            elif random == 4:
                lbl_toplevel = "As frutinhas são simplesmente\ndeliciosas, levarei um pouco\npara mais tarde."
                losewin_hearts = 0
                losewin_foods = +0.5

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 01 - A", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "B":
            lbl_toplevel = "A caminhada é longa e a\nfome é sua inimiga, ignora-lá\né custoso."
            losewin_hearts = -0.5
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 01 - B", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Uma simples fruta, isso\nsacia a sua fome."
                losewin_hearts = 0
                losewin_foods = -0.5
            elif random == 4:
                lbl_toplevel = "Guloseimas são tão gostosas,\npegarei só mais uma, ~Ops~\nacabei exagerando..."
                losewin_hearts = 0
                losewin_foods = -1

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 01 - C", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

    elif w == 2:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2:
                lbl_toplevel = "Você consegue libertar\no lobinho que corre de volta\npara a mata"
                losewin_hearts = 0
                losewin_foods = 0
                future_friendship = True
            elif random == 3 or random == 4:
                lbl_toplevel = "Ao libertar o lobinho você se\nmachuca com a armadilha, mas\nconsegue libertar o lobinho que\n" +\
                "corre de volta para a mata"
                losewin_hearts = -0.5
                losewin_foods = 0
                future_friendship = True          

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_item(lighter, wolfhide, future_friendship, nausea, shotgun, crowbar, screwdriver, gear)
            show_toplevel("Level 02 - A", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "B":
            lbl_toplevel = "Nada ocorre, você segue\nem frente"
            losewin_hearts = 0
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 02 - B", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "O lobo dá seu último uivo e\nvocê consegue o seu couro e\ncarne, então você parte em\nfrente"
                losewin_hearts = 0
                losewin_foods = +1
                wolfhide = True
            elif random == 4:
                lbl_toplevel = "O lobo dá seu último uivo,\nvocê pega o seu couro e carne,\nmas ao longe vem vindo outro\n" + \
                "lobo então você corre, foge,\nmas havia se arranhado na mata"
                losewin_hearts = -1
                losewin_foods = +1
                wolfhide = True

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_item(lighter, wolfhide, future_friendship, nausea, shotgun, crowbar, screwdriver, gear)
            show_toplevel("Level 02 - C", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

    elif w == 3:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1:
                lbl_toplevel = "Em um vão da casa você\nencontra um remédio"
                losewin_hearts = 0.5
                losewin_foods = 0
            elif random == 2:
                lbl_toplevel = "Em um vão da casa você\nencontra uma fruta intacta"
                losewin_hearts = 0
                losewin_foods = 0.5
            elif random == 3:
                lbl_toplevel = "Em um vão da casa você\ntropeça e se machuca"
                losewin_hearts = -0.5
                losewin_foods = 0
            elif random == 4:
                lbl_toplevel = "Você não acho nada de\ninteressante na casa"
                losewin_hearts = 0
                losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 03 - A", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "A constante chuva a\ndeixou resfriada"
                losewin_hearts = -1
                losewin_foods = 0
            elif random == 4:
                lbl_toplevel = "Você andou por debaixo\ndas copas e você nem nota\na chuva constante"
                losewin_hearts = 0
                losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 03 - B", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "A chuva passou e você\nsegue o seu caminho"
                losewin_hearts = 0
                losewin_foods = 0
            elif random == 4:
                lbl_toplevel = "A chuva veio, mas a\ndona aranha continuou a\nsubir e a picou"
                losewin_hearts = -1
                losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 03 - C", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

    elif w == 4:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2:
                lbl_toplevel = "No fim da ponte você\nolha para trás e percebe\nque deu tudo certo"
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 3 or random == 4:
                lbl_toplevel = "No fim da ponte, a\nmadeira sobre seu pé racha\nao meio e você cai no riacho,\n" +\
                "próximo a margem você\nconsegue se salvar"
                losewin_hearts = -0.5
                losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 04 - A", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Ao caminhar tanto você\ncomeça a sentir muita fome,\nportanto você come algo\n" +\
                "de sua mochila"
                losewin_hearts = 0
                losewin_foods = -1
            elif random == 4:
                lbl_toplevel = "Ao caminhar tanto você\ncomeça a sentir muita fome,\nentão você come algo da\n" +\
                "mochila, além disso\nseus pés estão doendo"
                losewin_hearts = -0.5
                losewin_foods = -1

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 04 - B", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Não era tão raso assim,\na correnteza a leva e você\nse afoga"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                gameover("True")
            elif random == 4:
                lbl_toplevel = "Shalow Now\nvocê consegue atravessar de boa"
                losewin_hearts = 0
                losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 04 - C", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

    elif w == 5:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if foods >= 4:
                lbl_toplevel = "Um urso é atraído pela\nsua comida e tem um\nbelo banquete"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                gameover("True")
            else:
                if random == 1 or random == 2:
                    lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu bem e partiu\nna manhã seguinte"
                    losewin_hearts = 0
                    losewin_foods = -0.5
                elif random == 3 or random == 4:
                    lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu mal e teve de partir\nna manhã seguinte"
                    losewin_hearts = -0.5
                    losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 05 - A", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "B":
            if foods >= 4:
                lbl_toplevel = "As formigas são atraídas\npela sua comida e levam\nparte dela"
                losewin_hearts = 0
                losewin_foods = -2
            else:
                if random == 1 or random == 2:
                    lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu bem e partiu\nna manhã seguinte"
                    losewin_hearts = 0
                    losewin_foods = -0.5
                elif random == 3 or random == 4:
                    lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu mal e teve de partir\nna manhã seguinte"
                    losewin_hearts = -0.5
                    losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 05 - B", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "C":
            if random == 1 or random == 2:
                lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu mal e teve de partir\nna manhã seguinte"
                losewin_hearts = -0.5
                losewin_foods = -0.5
            elif random == 3:
                lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu bem e partiu\nna manhã seguinte"
                losewin_hearts = 0
                losewin_foods = -0.5
            elif random == 4:
                lbl_toplevel = "O chão é o lar de\nmuitos animais, inclusive\nda cobra que te deu\num beijinho de boa noite"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                gameover("True")

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 05 - C", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

    elif w == 6:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2:                   
                lbl_toplevel = "O cogumelo Azul lhe traz\numa sensação de fraqueza"
                losewin_hearts = -1
                losewin_foods = 0
            elif random == 3 or random == 4:
                lbl_toplevel = "O cogumelo Azul lhe traz\numa sensação de saciedade"
                losewin_hearts = 0
                losewin_foods = 1

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 06 - A", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "B":
            if random == 1 or random == 2:                   
                lbl_toplevel = "O cogumelo Vermelho\nlhe traz uma sensação\nde força"
                losewin_hearts = 1
                losewin_foods = 0
            elif random == 3 or random == 4:
                lbl_toplevel = "O cogumelo Vermelho\nlhe traz uma fome\nimensa"
                losewin_hearts = 0
                losewin_foods = -1

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 06 - B", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "C":
            lbl_toplevel = "Você segue em frente e\ncome algo de sua mochila"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 06 - C", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

    elif w == 7:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            lbl_toplevel = "Ao passar pelas flores\nvocê sente náuseas"
            losewin_hearts = 0
            losewin_foods = 0
            nausea = True
            show_item(lighter, wolfhide, future_friendship, nausea, shotgun, crowbar, screwdriver, gear)

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 07 - A", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "B":
            if wolfhide == True: #Couro de lobo
                lbl_toplevel = "Tudo ocorreu bem,\nafinal o couro de lobo a\nprotegeu dos espinhos"
                losewin_hearts = 0
                losewin_foods = 0
            else:
                if random == 1 or random == 2 or random == 3:
                    lbl_toplevel = "Ao passar pelas espinhos\nvocê se corta várias vezes"
                    losewin_hearts = -1
                    losewin_foods = 0

                elif random == 4:
                    lbl_toplevel = "Ao passar pelos espinhos\nvocê se arranha levemente"
                    losewin_hearts = -0.5
                    losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 07 - B", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "À medida que você caminhava\nno lamaceiro você começa\na afundar até que percebes\n" +\
                "que era na verdade\nareia movediça"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                gameover("True")
            elif random == 4:
                lbl_toplevel = "No meio para o final do\nlamaceiro você começa a\nafundar, porém consegue fugir\n" +\
                "da então areia movediça"
                losewin_hearts = -0.5
                losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            show_toplevel("Level 07 - C", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

    elif w == 8:
        window.title(f"Level 01")

        if selected_option == "A":
            lbl_toplevel = "Uma mina explode em sua\nfrente, devido a sua falta\nde cuidado"
            losewin_hearts = 0
            losewin_foods = 0
            game_over = True
            gameover("True")

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            shotgun = True
            show_item(lighter, wolfhide, future_friendship, nausea, shotgun, crowbar, screwdriver, gear)
            show_toplevel("Level 08 - A", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "B":
            lbl_toplevel = "É voltando que se pega\nimpulso, você passa pela\narmadilha com calma e tudo\n"  +\
            "ocorre bem"
            losewin_hearts = 0
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            shotgun = True
            show_item(lighter, wolfhide, future_friendship, nausea, shotgun, crowbar, screwdriver, gear)
            show_toplevel("Level 08 - B", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Você segue até a fonte do\nfio e encontra uma armadilha\nplantada, então você\n" +\
                "decide desarmar, com êxito\nvocê desarma a armadilha"
                losewin_hearts = 0
                losewin_foods = 0
            elif random == 4:
                lbl_toplevel = "Você segue até a fonte do\nfio e encontra uma armadilha\nplantada, então você\n" +\
                "decide desarmar, com êxito\na mina terrestre é acionada"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                gameover("True")


            hearts += losewin_hearts
            show_heart(hearts)
            foods += losewin_foods
            show_food(foods)

            shotgun = True
            show_item(lighter, wolfhide, future_friendship, nausea, shotgun, crowbar, screwdriver, gear)
            show_toplevel("Level 08 - C", lbl_toplevel, losewin_hearts, losewin_foods, w, selected_option)

#____________________________________________________________________________________________________________
#Others
bg = fg = "#fafafa"
bg_frames = "#f1f1f1"
bg_narrative = "#252525"
directory = os.path.dirname(__file__)
default()
music()
#____________________________________________________________________________________________________________
#Init Tkinter
window = Tk()

width = 720 #700
height = 470 #450
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
window.title("The Truth")
window.iconbitmap(directory + "/Images/Icons/icon_01.ico")
window.resizable(False,False)
window.configure(background = "#000")
#____________________________________________________________________________________________________________
#Create - Main Menu and Credits

root = Frame(window, bd = 1, relief = "sunken", bg = bg)
root.place(x = 10, y = 10, width = width - 20, height = height - 20)

my_name = "Arthur V.B.S."
txt_credits_01 = "Producer\nDesigner\nDeveloper"
txt_credits_02 = f"{my_name}\n{my_name}\n{my_name}"

lbl_title = Label(root, text = " - The Truth - ", bg=bg, font = "courier 40 bold")
lbl_subtitle = Label(root, text = "a corrupted idea", bg=bg, font = "courier 32 bold", anchor = N)
lbl_version = Label(root, text = "alpha v 0.2", bg=bg, font = "courier 10 bold", anchor = SE) #VERSION
lbl_credits_01 = Label(root, text=txt_credits_01, bg=bg, font = "courier 18 italic", anchor = N, justify = RIGHT)
lbl_credits_02 = Label(root, text=txt_credits_02, bg=bg, font = "courier 18 italic", anchor = N, justify = LEFT)

btn_newgame = Button(root, text= "Novo jogo", bg=bg, bd = 2, relief = "ridge", command= lambda: click_newgame(),
                        cursor="hand2", font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)
btn_continue = Button(root, text= "Continuar", bg=bg, bd = 2, relief = "flat", command= lambda: click_nothing(), 
                        cursor="arrow", font = "courier 27 bold", fg = "#ccc")
btn_credits = Button(root, text= "Créditos", bg=bg, bd = 2, relief = "ridge", command= lambda: click_credits(),
                        cursor="hand2", font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)
btn_quit = Button(root, text= "Sair", bg=bg, bd = 2, relief = "ridge", command = lambda: click_quit(),
                        cursor="hand2", font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)
btn_back = Button(root, text= "Voltar", bg=bg, bd = 2, relief = "ridge",command= lambda: click_back_to_main_menu(),
                cursor="hand2", font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)

show_main_menu()
#____________________________________________________________________________________________________________
#Create - Game

#Frames
root_status = Frame(root, bd = 1, relief = "ridge", bg = bg)
#root_status.place(x = 0, y = 280, width = width - 23, height = 175)
root_narrative = Frame(root, bd = 1, relief = "ridge", bg = bg_narrative)
#root_narrative.place(x = 0, y = 0, width = width - 23, height = 280)

root_hearts = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_hearts.place(x = 10, y = 10, width = 160, height = 40)
root_foods = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_foods.place(x = 180, y = 10, width = 160, height = 40)
root_keys = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_keys.place(x = 10, y = 60, width = 50, height = 100)
root_way = Frame(root_status, bd = 1, relief = "sunken", bg = bg_narrative)
root_way.place(x = 350, y = 0, width = 350, height = 50)
root_options = Frame(root_narrative, bd = 1, relief = "sunken", bg = bg)
root_options.place(x = -1, y = 220, width = 351, height = 60)
root_scenario = Frame(root_status, bd = 0.5, relief = "groove", bg = bg_frames)
root_scenario.place(x = 350, y = 60, width = 250, height = 100)

root_item_main = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_item_01 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_02 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_03 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_04 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_05 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_06 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_07 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_08 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)

root_item_main.place(x = 180, y = 60, width = 160, height = 100)
root_item_01.place(x = 5, y = 5, width = 35, height = 40)
root_item_02.place(x = 44, y = 5, width = 35, height = 40)
root_item_03.place(x = 82, y = 5, width = 35, height = 40)
root_item_04.place(x = 120, y = 5, width = 35, height = 40)
root_item_05.place(x = 5, y = 55, width = 35, height = 40)
root_item_06.place(x = 44, y = 55, width = 35, height = 40)
root_item_07.place(x = 82, y = 55, width = 35, height = 40)
root_item_08.place(x = 120, y = 55, width = 35, height = 40)

#Buttons
btn_back_newgame = Button(root_status, text= "Voltar", bg=bg, bd = 2, relief = "ridge", command = lambda: click_back_to_main_menu(), cursor="hand2",
                    font = "courier 12 bold", activebackground="#ccc", activeforeground=fg)
btn_opt_A = Button(root_narrative, text= "- A -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options("A"),
                    cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)
btn_opt_B = Button(root_narrative, text= "- B -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options("B"),
                    cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)
btn_opt_C = Button(root_narrative, text= "- C -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options("C"),
                    cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)

#btn_back_newgame.place(x = 610, y = 120, width = 80, height = 40)
btn_opt_A.place(x = 10, y = 230, width = 100, height = 40)
btn_opt_B.place(x = 125, y = 230, width = 100, height = 40)
btn_opt_C.place(x = 240, y = 230, width = 100, height = 40)

#Labels
lbl_crossroads = Label(root_narrative, text = "", anchor=CENTER, justify=CENTER, font = "courier 14 italic",
                        bg = bg_narrative, fg = fg)
lbl_opt_A = Label(root_narrative, text = "", anchor = NW, justify=LEFT, font = "courier 12 italic",
                        bg = bg_narrative, fg = fg)
lbl_opt_B = Label(root_narrative, text = "", anchor = NW, justify=LEFT, font = "courier 12 italic",
                        bg = bg_narrative, fg = fg)
lbl_opt_C = Label(root_narrative, text = "", anchor = NW, justify=LEFT, font = "courier 12 italic",
                        bg = bg_narrative, fg = fg)

lbl_crossroads.place(x = 10, y = 10, width = 330, height = 200)
lbl_opt_A.place(x = 360, y = 10, width = 330, height = 80)
lbl_opt_B.place(x = 360, y = 100, width = 330, height = 80)
lbl_opt_C.place(x = 360, y = 190, width = 330, height = 80)

#____________________________________________________________________________________________________________
#Hearts, Foods and Keys - PhotoImage

empty_00_dic = PhotoImage(file= directory + "/Images/empty.png")
empty_01_dic = PhotoImage(file= directory + "/Images/empty_plus.png")
Sam_dic = PhotoImage(file= directory + "/Images/Sam.png")

scenario_01_dic = PhotoImage(file= directory + "/Images/Scenarios/Scenario_01.png")
scenario_02_dic = PhotoImage(file= directory + "/Images/Scenarios/Scenario_02.png")
scenario_03_dic = PhotoImage(file= directory + "/Images/Scenarios/Scenario_03.png")

heart_11_dic = PhotoImage(file= directory + "/Images/Hearts/heart_11.png")
heart_01_dic = PhotoImage(file= directory + "/Images/Hearts/heart_01.png")
heart_00_dic = PhotoImage(file= directory + "/Images/Hearts/heart_00.png")

food_11_dic = PhotoImage(file= directory + "/Images/Foods/food_11.png")
food_01_dic = PhotoImage(file= directory + "/Images/Foods/food_01.png")
food_00_dic = PhotoImage(file= directory + "/Images/Foods/food_00.png")

key_E_dic = PhotoImage(file= directory + "/Images/Keys/Key_E.png")
key_B_dic = PhotoImage(file= directory + "/Images/Keys/Key_B.png")
key_S_dic = PhotoImage(file= directory + "/Images/Keys/Key_S.png")
key_G_dic = PhotoImage(file= directory + "/Images/Keys/Key_G.png")

just_way_dic = PhotoImage(file = directory + "/Images/Ways/just_way.png")
way_dic = PhotoImage(file = directory + "/Images/Ways/way.png")

item_lighter_dic = PhotoImage(file = directory + "/Images/Items/item_lighter.png")
item_wolfhide_dic = PhotoImage(file = directory + "/Images/Items/item_wolfhide.png")
item_future_friendship_dic = PhotoImage(file = directory + "/Images/Items/item_future_friendship.png")
item_nausea_dic = PhotoImage(file = directory + "/Images/Items/item_nausea.png")
item_shotgun_dic = PhotoImage(file = directory + "/Images/Items/item_shotgun.png")
item_crowbar_dic = PhotoImage(file = directory + "/Images/Items/item_crowbar.png")
item_screwdriver_dic = PhotoImage(file = directory + "/Images/Items/item_screwdriver.png")
item_gear_dic = PhotoImage(file = directory + "/Images/Items/item_gear.png")

#____________________________________________________________________________________________________________
#Hearts, Foods and Keys - Labels

lbl_Sam = Label(root_status, image = Sam_dic, bg = bg, anchor = CENTER)
lbl_Sam.place(x = 70, y = 60)
lbl_scenario = Label(root_scenario, image = empty_00_dic, bg = bg)
lbl_scenario.place(x = 5, y = 5, width = 240, height = 90)

lbl_heart_01 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_01.place(x = 5, y = 5, width = 30, height = 30)
lbl_heart_02 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_02.place(x = 35, y = 5, width = 30, height = 30)
lbl_heart_03 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_03.place(x = 65, y = 5, width = 30, height = 30)
lbl_heart_04 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_04.place(x = 95, y = 5, width = 30, height = 30)
lbl_heart_05 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_05.place(x = 125, y = 5, width = 30, height = 30)

lbl_food_01 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_01.place(x = 5, y = 5, width = 30, height = 30)
lbl_food_02 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_02.place(x = 35, y = 5, width = 30, height = 30)
lbl_food_03 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_03.place(x = 65, y = 5, width = 30, height = 30)
lbl_food_04 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_04.place(x = 95, y = 5, width = 30, height = 30)
lbl_food_05 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_05.place(x = 125, y = 5, width = 30, height = 30)

lbl_key_B = Label(root_keys, image = empty_00_dic, bg = bg_frames)
lbl_key_B.place(x = 10, y = 5, width = 30, height = 30)
lbl_key_S = Label(root_keys, image = empty_00_dic, bg = bg_frames)
lbl_key_S.place(x = 10, y = 35, width = 30, height = 30)
lbl_key_G = Label(root_keys, image = empty_00_dic, bg = bg_frames)
lbl_key_G.place(x = 10, y = 65, width = 30, height = 30)

lbl_just_way_01 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_01.place(x = 7.5, y = 5, width = 35, height = 35)
lbl_just_way_02 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_02.place(x = 50, y = 5, width = 35, height = 35)
lbl_just_way_03 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_03.place(x = 92.5, y = 5, width = 35, height = 35)
lbl_just_way_04 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_04.place(x = 135, y = 5, width = 35, height = 35)
lbl_just_way_05 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_05.place(x = 177.5, y = 5, width = 35, height = 35)
lbl_just_way_06 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_06.place(x = 220, y = 5, width = 35, height = 35)
lbl_just_way_07 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_07.place(x = 262.5, y = 5, width = 35, height = 35)
lbl_just_way_08 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_08.place(x = 305, y = 5, width = 35, height = 35)

lbl_item_lighter = Label(root_item_01, image = empty_01_dic, bg = bg)
lbl_item_wolfhide = Label(root_item_02, image = empty_01_dic, bg = bg)
lbl_item_future_friendship = Label(root_item_03, image = empty_01_dic, bg = bg)
lbl_item_nausea = Label(root_item_04, image = empty_01_dic, bg = bg)
lbl_item_shotgun = Label(root_item_05, image = empty_01_dic, bg = bg)
lbl_item_crowbar = Label(root_item_06, image = empty_01_dic, bg = bg)
lbl_item_screwdriver = Label(root_item_07, image = empty_01_dic, bg = bg)
lbl_item_gear = Label(root_item_08, image = empty_01_dic, bg = bg)

lbl_item_lighter.place(x = 0, y = 2.5, width = 30, height = 30)
lbl_item_wolfhide.place(x = 0, y = 2.5, width = 30, height = 30)
lbl_item_future_friendship.place(x = 0, y = 2.5, width = 30, height = 30)
lbl_item_nausea.place(x = 0, y = 2.5, width = 30, height = 30)
lbl_item_shotgun.place(x = 0, y = 2.5, width = 30, height = 30)
lbl_item_crowbar.place(x = 0, y = 2.5, width = 30, height = 30)
lbl_item_screwdriver.place(x = 0, y = 2.5, width = 30, height = 30)
lbl_item_gear.place(x = 0, y = 2.5, width = 30, height = 30)

window.mainloop()
