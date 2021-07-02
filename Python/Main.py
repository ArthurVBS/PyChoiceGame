#Import - Libraries _________________________________________________________________________________________
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

#Import - Modules ___________________________________________________________________________________________
from Utils.Defs_Sound import sound, mixer_pm
from Utils.Defs_Texts import world_01, world_02, world_03, menu
from Utils.Defs_Images import images, roots, sub_roots, sub_sub_roots, labels, buttons

#Functions - Show ___________________________________________________________________________________________
def show_main_menu():
    window.title("Main Menu")
    root.config(bg = bg)

    lbl_title.place(x = 10, y = 10, width = width - 40, height = 65)
    lbl_subtitle.place(x = 10, y = 75, width = width - 40, height = 65)
    lbl_version.place(x = 585, y = 420, width = 110, height = 25)
    btn_newgame.place(x = 225, y = 145, width = 250, height = 50)
    btn_continue.place(x = 225, y = 205, width = 250, height = 50)
    btn_options.place(x = 225, y = 265, width = 250, height = 50)
    btn_credits.place(x = 225, y = 325, width = 250, height = 50)
    btn_quit.place(x = 225, y = 385, width = 250, height = 50)

def show_heart(hearts):
    global game_over
    #Heart - +5
    if hearts > 5:
        hearts = 5

    #Heart - 1
    if hearts >= 1:
        labels['lbl_heart_01'].config(image = img['heart_11_dic'])
    elif hearts == 0.5:
        labels['lbl_heart_01'].config(image = img['heart_01_dic'])
    elif hearts < 0.5:
        labels['lbl_heart_01'].config(image = img['heart_00_dic'])
        game_over = True
        gameover("True")

    #Heart - 2
    if hearts >= 2:
        labels['lbl_heart_02'].config(image = img['heart_11_dic'])
    elif hearts == 1.5:
        labels['lbl_heart_02'].config(image = img['heart_01_dic'])
    elif hearts < 1.5:
        labels['lbl_heart_02'].config(image = img['heart_00_dic'])

    #Heart - 3
    if hearts >= 3:
        labels['lbl_heart_03'].config(image = img['heart_11_dic'])
    elif hearts == 2.5:
        labels['lbl_heart_03'].config(image = img['heart_01_dic'])
    elif hearts < 2.5:
        labels['lbl_heart_03'].config(image = img['heart_00_dic'])

    #Heart - 4
    if hearts >= 4:
        labels['lbl_heart_04'].config(image = img['heart_11_dic'])
    elif hearts == 3.5:
        labels['lbl_heart_04'].config(image = img['heart_01_dic'])
    elif hearts < 3.5:
        labels['lbl_heart_04'].config(image = img['heart_00_dic'])

    #Heart - 5
    if hearts == 5:
        labels['lbl_heart_05'].config(image = img['heart_11_dic'])
    elif hearts == 4.5:
        labels['lbl_heart_05'].config(image = img['heart_01_dic'])
    elif hearts < 4.5:
        labels['lbl_heart_05'].config(image = img['heart_00_dic'])

def show_food(foods):
    global game_over
    #Foods - +5
    if foods > 5:
        foods = 5

    #Food - 1
    if foods >= 1:
        labels['lbl_food_01'].config(image = img['food_11_dic'])
    elif foods == 0.5:
        labels['lbl_food_01'].config(image = img['food_01_dic'])
    elif foods < 0.5:
        labels['lbl_food_01'].config(image = img['food_00_dic'])
        game_over = True
        gameover("True")

    #Food - 2
    if foods >= 2:
        labels['lbl_food_02'].config(image = img['food_11_dic'])
    elif foods == 1.5:
        labels['lbl_food_02'].config(image = img['food_01_dic'])
    elif foods < 1.5:
        labels['lbl_food_02'].config(image = img['food_00_dic'])

    #Food - 3
    if foods >= 3:
        labels['lbl_food_03'].config(image = img['food_11_dic'])
    elif foods == 2.5:
        labels['lbl_food_03'].config(image = img['food_01_dic'])
    elif foods < 2.5:
        labels['lbl_food_03'].config(image = img['food_00_dic'])

    #Food - 4
    if foods >= 4:
        labels['lbl_food_04'].config(image = img['food_11_dic'])
    elif foods == 3.5:
        labels['lbl_food_04'].config(image = img['food_01_dic'])
    elif foods < 3.5:
        labels['lbl_food_04'].config(image = img['food_00_dic'])

    #Food - 5
    if foods >= 5:
        labels['lbl_food_05'].config(image = img['food_11_dic'])
    elif foods == 4.5:
        labels['lbl_food_05'].config(image = img['food_01_dic'])
    elif foods < 4.5:
        labels['lbl_food_05'].config(image = img['food_00_dic'])

def show_item(items):
    #lighter
    if items['lighter'] == True:
        labels['lbl_item_lighter'].config(image = img['item_lighter_dic'])
    elif items['lighter'] == False:
        labels['lbl_item_lighter'].config(image = img['empty_01_dic'])
    
    #wolfhide
    if items['wolfhide'] == True:
        labels['lbl_item_wolfhide'].config(image = img['item_wolfhide_dic'])
    elif items['wolfhide'] == False:
        labels['lbl_item_wolfhide'].config(image = img['empty_01_dic'])

    #future_friendship
    if items['future_friendship'] == True:
        labels['lbl_item_future_friendship'].config(image = img['item_future_friendship_dic'])
    elif items['future_friendship'] == False:
        labels['lbl_item_future_friendship'].config(image = img['empty_01_dic'])

    #nausea
    if items['nausea'] == True:
        labels['lbl_item_nausea'].config(image = img['item_nausea_dic'])
    elif items['nausea'] == False:
        labels['lbl_item_nausea'].config(image = img['empty_01_dic'])

    #shotgun
    if items['shotgun'] == True:
        labels['lbl_item_shotgun'].config(image = img['item_shotgun_dic'])
    elif items['shotgun'] == False:
        labels['lbl_item_shotgun'].config(image = img['empty_01_dic'])

    #crowbar
    if items['crowbar'] == True:
        labels['lbl_item_crowbar'].config(image = img['item_crowbar_dic'])
    elif items['crowbar'] == False:
        labels['lbl_item_crowbar'].config(image = img['empty_01_dic'])

    #screwdriver
    if items['screwdriver'] == True:
        labels['lbl_item_screwdriver'].config(image = img['item_screwdriver_dic'])
    elif items['screwdriver'] == False:
        labels['lbl_item_screwdriver'].config(image = img['empty_01_dic'])

    #gear
    if items['gear'] == True:
        labels['lbl_item_gear'].config(image = img['item_gear_dic'])
    elif items['gear'] == False:
        labels['lbl_item_gear'].config(image = img['empty_01_dic'])

def show_key(keys):
    #Key - B
    if keys['bronze_key'] == True:
        labels['lbl_key_B'].config(image = img['key_B_dic'])
    elif keys['bronze_key'] == False:
        labels['lbl_key_B'].config(image = img['key_E_dic'])

    #Key - S
    if keys['silver_key'] == True:
        labels['lbl_key_S'].config(image = img['key_S_dic'])
    elif keys['silver_key'] == False:
        labels['lbl_key_S'].config(image = img['key_E_dic'])

    #Key - G
    if keys['golden_key'] == True:
        labels['lbl_key_G'].config(image = img['key_G_dic'])
    elif keys['golden_key'] == False:
        labels['lbl_key_G'].config(image = img['key_E_dic'])

def show_way():
    global level
    global keys
    global world

    labels['lbl_just_way_01'].config(image = img['just_way_dic'])
    labels['lbl_just_way_02'].config(image = img['just_way_dic'])
    labels['lbl_just_way_03'].config(image = img['just_way_dic'])
    labels['lbl_just_way_04'].config(image = img['just_way_dic'])
    labels['lbl_just_way_05'].config(image = img['just_way_dic'])
    labels['lbl_just_way_06'].config(image = img['just_way_dic'])
    labels['lbl_just_way_07'].config(image = img['just_way_dic'])
    labels['lbl_just_way_08'].config(image = img['just_way_dic'])

    if level == 1:
        labels['lbl_just_way_01'].config(image = img['way_dic'])
    elif level == 2:
        labels['lbl_just_way_02'].config(image = img['way_dic'])
    elif level == 3:
        labels['lbl_just_way_03'].config(image = img['way_dic'])
    elif level == 4:
        labels['lbl_just_way_04'].config(image = img['way_dic'])
    elif level == 5:
        labels['lbl_just_way_05'].config(image = img['way_dic'])
    elif level == 6:
        labels['lbl_just_way_06'].config(image = img['way_dic'])
    elif level == 7:
        labels['lbl_just_way_07'].config(image = img['way_dic'])
    elif level == 8:
        labels['lbl_just_way_08'].config(image = img['way_dic'])
    else:
        level = 1
        labels['lbl_just_way_01'].config(image = img['way_dic'])

    if world == 1:
        keys['bronze_key'] = True
    elif world == 2:
        keys['silver_key'] = True
    elif world == 3:
        keys['golden_key'] = True

    show_key(keys)
    show_scenario()

def show_scenario():
    global world
    if world == 1:
        labels['lbl_scenario'].config(image = img['scenario_01_dic'])
    elif world == 2:
        labels['lbl_scenario'].config(image = img['scenario_02_dic'])
    elif world == 3:
        labels['lbl_scenario'].config(image = img['scenario_03_dic'])

def show_toplevel(title, lbl_text, losewin_hearts, losewin_foods, w, selected_option):#Alterações Futuras
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
            world +=1
            if world == 2:
                btn_tl.config(command= lambda: show_narrative_02())
            if world == 3:
                btn_tl.config(command= lambda: show_narrative_03())

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
        phImg_heart_01 = img['heart_00_dic']
        phImg_heart_02 = img['heart_00_dic']

    elif losewin_hearts == 0.5 or losewin_hearts == -0.5:
        phImg_heart_01 = img['heart_01_dic']
        phImg_heart_02 = img['heart_00_dic']

    elif losewin_hearts == 1 or losewin_hearts == -1:
        phImg_heart_01 = img['heart_11_dic']
        phImg_heart_02 = img['heart_00_dic']

    elif losewin_hearts == 1.5 or losewin_hearts == -1.5:
        phImg_heart_01 = img['heart_11_dic']
        phImg_heart_02 = img['heart_01_dic']

    elif losewin_hearts == 2 or losewin_hearts == -2:
        phImg_heart_01 = img['heart_11_dic']
        phImg_heart_02 = img['heart_11_dic']

    #Foods
    if losewin_foods >= 0:
        sinal_foods = "+"

    elif losewin_foods < 0:
        sinal_foods = "-"

    if losewin_foods == 0:
        phImg_food_01 = img['food_00_dic']
        phImg_food_02 = img['food_00_dic']

    elif losewin_foods == 0.5 or losewin_foods == -0.5:
        phImg_food_01 = img['food_01_dic']
        phImg_food_02 = img['food_00_dic']

    elif losewin_foods == 1 or losewin_foods == -1:
        phImg_food_01 = img['food_11_dic']
        phImg_food_02 = img['food_00_dic']

    elif losewin_foods == 1.5 or losewin_foods == -1.5:
        phImg_food_01 = img['food_11_dic']
        phImg_food_02 = img['food_01_dic']

    elif losewin_foods == 2 or losewin_foods == -2:
        phImg_food_01 = img['food_11_dic']
        phImg_food_02 = img['food_11_dic']

    #Item / Key
    if world == 1:
        if w == 2 and selected_option == "A": #friendship
            phImg_item_01 = img['item_future_friendship_dic']
            phImg_item_02 = img['empty_00_dic']

        elif w == 2 and selected_option == "C": #wolfhide
            phImg_item_01 = img['item_wolfhide_dic']
            phImg_item_02 = img['empty_00_dic']

        elif w == 7 and selected_option == "A": #nausea
            phImg_item_01 = img['item_nausea_dic']
            phImg_item_02 = img['empty_00_dic']

        else:
            phImg_item_01 = img['empty_00_dic']
            phImg_item_02 = img['empty_00_dic']

    elif world - 1 == 1:
        if w == 8: #shotgun and key silver
            phImg_item_01 = img['item_shotgun_dic']
            phImg_item_02 = img['key_S_dic']

        else:
            phImg_item_01 = img['empty_00_dic']
            phImg_item_02 = img['empty_00_dic']

    if world == 2:#Alterações Futuras
        if 10 == 9:
            print("")

        else:
            phImg_item_01 = img['empty_00_dic']
            phImg_item_02 = img['empty_00_dic']

    elif world - 1 == 2:#Alterações Futuras
        if 10 == 9:
            print("")

        else:
            phImg_item_01 = img['empty_00_dic']
            phImg_item_02 = img['empty_00_dic']

    if world == 3:#Alterações Futuras
        if 10 == 9:
            print("")
            
        else:
            phImg_item_01 = img['empty_00_dic']
            phImg_item_02 = img['empty_00_dic']

    elif world - 3 == 2:#Alterações Futuras
        if 10 == 9:
            print("")

        else:
            phImg_item_01 = img['empty_00_dic']
            phImg_item_02 = img['empty_00_dic']

    if phImg_item_01 != img['empty_00_dic'] or phImg_item_02 != img['empty_00_dic']:
        sinal_item_key = "+"
        
    elif phImg_item_01 == img['empty_00_dic'] and phImg_item_02 == img['empty_00_dic']:
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

    show_way()
    show_scenario()
    win_toplevel.mainloop()

def show_button_continue():
    if ok_cancel_newgame == True:
        window.title("Level 01")
        btn_continue.config(fg = "#000", relief = "ridge", command = lambda: click_continue(), activebackground="#ccc",
                            activeforeground=fg, cursor="hand2")

def show_game():
    roots['root_status'].place(x = 0, y = 280, width = width - 23, height = 175)
    roots['root_narrative'].place(x = 0, y = 0, width = width - 23, height = 280)
    buttons['btn_back_newgame'].place(x = 610, y = 60, width = 80, height = 100)

    default()

    show_heart(hearts)
    show_food(foods)
    show_item(items)
    show_key(keys)
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
        introduction_text = "Buscando descanso, após um longo e\n" +\
        "complicado ano na capital, Sam - Você -\n" +\
        "decide visitar os seus pais que moram num\n" +\
        "antigo vilarejo bem distante da capital.\n\n" +\
        "Você pega seu carro e parte na estrada\n" +\
        "até o vilarejo."

        lbl_int_and_tut.config(text = introduction_text)
    
    def show_introduction_02():
        introduction_text = "Chegando próximo a principal entrada do\n" +\
        "vilarejo, o portão leste, você observa que ele\n" +\
        "se encontra entreaberto e que há uma mensagem\n" +\
        "escrita em um tom de vermelho bem peculiar.\n\n\n" +\
        "Não ultrapasse!!! Não ultrapasse!!!\n"

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_03():
        introduction_text = "Você se pergunta o motivo, mas segue em\n" +\
        "frente, ao adentrar no vilarejo, você\n" +\
        "busca a casa de seus pais, chegando lá\n" +\
        "você não os encontra e começa a notar o\n" +\
        "silêncio eloquente daquele vilarejo.\n"

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_04():
        introduction_text = "Na tentavia de perguntar a alguém onde\n" +\
        "estão seus pais, Você falha miseravelmente,\n" +\
        "afinal você não encontrou uma alma sequer,\n" +\
        "somente um caderno de anotação de um outro\n" +\
        "morador do vilarejo que dizia:\n"

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_05():
        introduction_text = "2005/03/22 - Página 1/3\n\n" +\
        "O vilarejo já não é mais o mesmo,\n" +\
        "desde que aquele estranho minerador\n" +\
        "encontrou um minério nas [...]\n\n" +\
        "- O resto dessa página foi arrancado às pressas -\n"

        lbl_int_and_tut.config(text = introduction_text)
        
    def show_introduction_06():
        introduction_text = "2005/03/23 - Página 2/3\n\n" +\
        "As pessoas estão indo cegamente até\n" +\
        "esse lugar para conseguir mais daquele\n" +\
        "minério bobo, todos querem ficar ricos.\n\n" +\
        "O vilarejo tem ficado bem vazio desde então.\n"


        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_07():
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

        introduction_text = "O jogo consiste em sobreviver e avançar na\n" +\
        "história, possuindo portanto o efeito borboleta.\n\n" +\
        "Sendo exposto a várias perguntas suas\n" +\
        "decisões tem consequências a longo e curto prazo.\n\n" +\
        "Possuindo um número limitado de vida e de comida\n" +\
        "em sua mochila você deve fazer escolhas sábias\n" +\
        "para que nada lhe falte."

        lbl_int_and_tut.config(text = introduction_text)

    def show_tutorial_02():
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
            sound(directory, vol = vol, sound = 1)
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
        introduction_text = "Chegando na casa da árvore você encontra\n" +\
        "um homem falando consigo mesmo e repetindo\n" +\
        "as seguintes palavras:\n\n" +\
        "\"Não não não, a verdade não pode pegar o\n" +\
        "Lucas, o Lucas é bonzinho, aquela verdade\n" +\
        "não é de verdade, não é, não é...\""

        lbl_int_and_tut.config(text = introduction_text)
    
    def show_introduction_02():
        introduction_text = "Você decide se aproximar um pouco mais e\n" +\
        "chamar a atenção dele, Lucas então se vira\n" +\
        "para você perplexo mandando você se afastar,\n" +\
        "dizendo as seguintes palavras:\n\n" +\
        "\"Não chegue perto, saí, você não é de verdade,\n" +\
        "a Verdade não pode pegar o Lucas, o Lucas\n" +\
        "não foi ganancioso, não chega mais perto!\""

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_03():
        introduction_text = "Então você para, e tenta conversar com o\n" +\
        "Lucas para saber o que aconteceu, todavia sem\n" +\
        "sucesso ele fica te olhando com os olhos\n" +\
        "vermelhos, repetindo as seguintes palavras:\n\n" +\
        "\"A verdade veio buscar o Lucas, não, ,não, não!\n" +\
        "Essa verdade não existe! Isso é coisa de\n" +\
        "minha cabeça, não, não, não!\""

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_04():
        introduction_text = "Você decide se aproximar um pouco mais\n" +\
        "para tentar conversar com ele, todavia Lucas\n" +\
        "se treme ao te ver chegar e pega uma escopeta\n" +\
        "e aponta para a sua direção, você para, e pede\n" +\
        "para ele abaixar a arma, todavia ele lhe diz:\n\n" +\
        "\"Não, não, não, a verdade nunca vai pegar\n" +\
        " o Lucas, essa verdade está corrompida!!!\""

        lbl_int_and_tut.config(text = introduction_text)

    def show_introduction_05():
        introduction_text = "Em meio àquela floresta ouve-se ao longe\n" +\
        "um disparo de escopeta, era O Lucas seifando\n" +\
        "a sua prória vida com um tiro na cabeça!\n\n" +\
        "Você fica estagnada, não consegue nem\n" +\
        "acreditar, até que a consciência volta em si.\n\n" +\
        "Você toma para si aquela escopeta, você\n" +\
        "também encontra a chave de prata e além disso\n" +\
        "você acha outra anotação do Lucas, que diz:\n"

        lbl_int_and_tut.config(text = introduction_text)
        
    def show_introduction_06():
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
        introduction_text = "Com isso você decide ir até os Alpes e\n" +\
        "questionar a esse tal de \"Minerador\" o que\n" +\
        "está acontecendo e o que é esse cristal.\n\n" +\
        "Ao sair pelos fundos da casa da árvore você\n" +\
        "encontra uma trilha em direção ao vilarejo,\n" +\
        "seguindo toda vida você abre com a chave\n"+\
        "de prata uma antiga porta enferrujada na\n" +\
        "área nordeste do vilarejo, já é noite, mas\n" +\
        "você está de volta ao vilarejo. Um novo\n" +\
        "dia amanhece e você parte para os alpes."

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

def show_labels_options():#Alterações Futuras
    global op
    global wd

    op += 1
    
    resume = menu(op, wd)

    op = resume['op']
    wd = resume['wd']

    labels['lbl_crossroads'].config(text = resume['crossroads_text'])    
    labels['lbl_opt_A'].config(text = f"- A - {resume['opt_A_text']}")
    labels['lbl_opt_B'].config(text = f"- B - {resume['opt_B_text']}")
    labels['lbl_opt_C'].config(text = f"- C - {resume['opt_C_text']}")

#Functions - Delete _________________________________________________________________________________________
def clear_main_menu():
    lbl_title.place_forget()
    lbl_subtitle.place_forget()
    lbl_version.place_forget()
    btn_newgame.place_forget()
    btn_continue.place_forget()
    btn_options.place_forget()
    btn_credits.place_forget()
    btn_quit.place_forget()

def clear_all():
    roots['root_status'].place_forget()
    roots['root_narrative'].place_forget()

    pb_vol.place_forget()
    rb_lan_UK.place_forget()
    rb_lan_FR.place_forget()
    rb_lan_BR.place_forget()
    rb_lan_SP.place_forget()
    rb_lan_GE.place_forget()

    labels['lbl_flag_UK'].place_forget()
    labels['lbl_flag_FR'].place_forget()
    labels['lbl_flag_BR'].place_forget()
    labels['lbl_flag_SP'].place_forget()
    labels['lbl_flag_GE'].place_forget()

    lbl_title.place_forget()
    lbl_subtitle.place_forget()
    lbl_version.place_forget()
    lbl_credits.place_forget()
    lbl_vol.place_forget()
    lbl_volume.place_forget()
    lbl_language.place_forget()
    
    btn_newgame.place_forget()
    btn_continue.place_forget()
    btn_options.place_forget()
    btn_credits.place_forget()
    btn_quit.place_forget()
    btn_back.place_forget()
    btn_vol_max.place_forget()
    btn_vol_plus.place_forget()
    btn_vol_minus.place_forget()
    btn_vol_mute.place_forget()
    buttons['btn_back_newgame'].place_forget()

#Functions - Click __________________________________________________________________________________________
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
    sound(directory, vol = vol, sound = 1) #Caso esteja no mundo 1
    window.title(f"Level 0{level}")
    roots['root_status'].place(x = 0, y = 280, width = width - 23, height = 175)
    roots['root_narrative'].place(x = 0, y = 0, width = width - 23, height = 280)
    buttons['btn_back_newgame'].place(x = 610, y = 60, width = 80, height = 100)

    clear_main_menu()

def click_options():
    window.title('Ajustes')
    clear_all()
    vol_pb()

    labels['lbl_flag_UK'].place(x = 360, y = 145, width = 50, height = 50)
    labels['lbl_flag_FR'].place(x = 360, y = 205, width = 50, height = 50)
    labels['lbl_flag_BR'].place(x = 360, y = 265, width = 50, height = 50)
    labels['lbl_flag_SP'].place(x = 360, y = 325, width = 50, height = 50)
    labels['lbl_flag_GE'].place(x = 360, y = 385, width = 50, height = 50)

    rb_lan_UK.place(x = 440, y = 145, width = 225, height = 50)
    rb_lan_FR.place(x = 440, y = 205, width = 225, height = 50)
    rb_lan_BR.place(x = 440, y = 265, width = 225, height = 50)
    rb_lan_SP.place(x = 440, y = 325, width = 225, height = 50)
    rb_lan_GE.place(x = 440, y = 385, width = 225, height = 50)

    lbl_title.place(x = 10, y = 10, width = width - 40, height = 65)
    lbl_title.configure(text = '- Ajustes -')
    lbl_volume.place(x = 10, y = 85, width = 335, height = 65)
    lbl_language.place(x = 355, y = 85, width = 335, height = 65)

    btn_vol_max.place(x = 270, y = 290, width = 75, height = 70)
    btn_vol_plus.place(x = 185, y = 290, width = 75, height = 70)
    btn_vol_minus.place(x = 97.5, y = 290, width = 75, height = 70)
    btn_vol_mute.place(x = 10, y = 290, width = 75, height = 70)

    btn_back.place(x = 10, y = 370, width = 335, height = 65)# x = 355

def vol_pb():
    global vol
    var_progressBar = DoubleVar()
    var_progressBar.set(vol)
    text_vol = f'{vol*100:.1f}%'

    pb_vol.configure(variable = var_progressBar)
    pb_vol.place(x = 10 , y = 155, width = 335, height = 40)

    lbl_vol.configure(text = text_vol)
    lbl_vol.place(x = 10, y = 200, width = 335, height = 30)

def volume(option):
    global vol
    
    if option == "max":
        vol = round(mixer_pm(vol = 1, p_or_m = "plus"), 2)
    elif option == "plus":
        vol = round(mixer_pm(vol, p_or_m = "plus"), 2)
    elif option == "minus":
        vol = round(mixer_pm(vol, p_or_m = "minus"), 2)
    elif option == "mute":
        vol = round(mixer_pm(vol = 0, p_or_m = "minus"), 2)

    vol_pb()

def click_credits():
    window.title("Créditos")
    clear_all()

    lbl_title.place(x = 10, y = 10, width = width - 40, height = 65)
    lbl_subtitle.place(x = 10, y = 75, width = width - 40, height = 65)
    lbl_version.place(x = 585, y = 420, width = 110, height = 25)
    btn_back.place(x = 225, y = 380, width = 250, height = 50)
    lbl_credits.place(x = 10, y = 145, width = width - 40, height = 210)

def click_quit():
    ok_cancel_quit = messagebox.askokcancel(title = "Sair?", message = "Você realmente deseja sair?\t\t",
    detail = "Desde já obrigado por jogar")
    if ok_cancel_quit == True:
        quit()

def click_back_to_main_menu(with_sound = False):
    value_var_language = var_language.get()
    if with_sound == True:
        sound(directory, vol = vol, sound = 0)

    if value_var_language != "BR":
        messagebox.showerror(title = "Idioma Indisponível", icon = messagebox.INFO,
        message = "O idioma selecionado encontra-se\nindisponível no momento.\n\n" +\
        "Por favor, selecione um idioma\ndisponível para prosseguir.")
    else:
        clear_all()
        lbl_title.config(text = " - The Truth - ", bg = bg, fg = "#000")
        show_main_menu()

#Functions - Others _________________________________________________________________________________________
def default():
    global op
    global world
    global level
    global wd
    global hearts
    global foods
    global game_over
    global keys
    global items

    items = {'lighter' : True, 'wolfhide' : False, 'future_friendship' : False, 'nausea' : False,
             'shotgun' : False, 'crowbar' : False, 'screwdriver' : False, 'gear' : False}
    keys = {'bronze_key' : False, 'silver_key' : False, 'golden_key' : False}

    op = 0
    world = level = wd = 1
    hearts = foods = 3
    game_over = False

def options(selected_option):
    global game_over
    global level
    global world
    global foods
    global hearts
    w = level
    level+=1
    random = randint(1,4)
    show_way()
    show_scenario()
    show_labels_options()

    if world == 1:
        resume = world_01(selected_option, random, window, w, items, foods)
    elif world == 2:
        resume = world_02(selected_option, random, window, w, items, foods)
    elif world == 3:
        resume = world_03(selected_option, random, window, w, items, foods)

    if resume['game_over'] == True:
        gameover('True')

    hearts += resume['losewin_hearts']
    foods += resume['losewin_foods']
    show_heart(hearts)
    show_food(foods)

    show_item(items)
    show_toplevel(f"Level 0{w} - {selected_option}", resume['lbl_toplevel'], resume['losewin_hearts'], resume['losewin_foods'], w, selected_option)

def gameover(value):
    if value == "True":
        roots['root_status'].place_forget()
        roots['root_narrative'].place_forget()
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

#Variables __________________________________________________________________________________________________
bg = fg = "#fafafa"
bg_frames = "#f1f1f1"
bg_narrative = "#252525"
directory = os.path.dirname(__file__)

#Tkinter ____________________________________________________________________________________________________
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

root = Frame(window, bd = 1, relief = "sunken", bg = bg)
root.place(x = 10, y = 10, width = width - 20, height = height - 20)

#Main Menu ___________________________________________________________________________________________________
lbl_title = Label(root, text = " - The Truth - ", bg=bg, font = "courier 40 bold")
lbl_subtitle = Label(root, text = "a corrupted idea", bg=bg, font = "courier 32 bold", anchor = N)
lbl_version = Label(root, text = "alpha v 1.2", bg=bg, font = "courier 10 bold", anchor = SE) #VERSION
lbl_volume = Label(root, text = "< Volume >", bg=bg, font = "courier 32 bold")
lbl_language = Label(root, text = "< Idioma >", bg=bg, font = "courier 32 bold")

txt_credits = "Aluno: Arthur Vinícius Bezerra da Silva\n" +\
"Curso: ADS - IFPE - 1º período - 2021.1\n\n" +\
"Início: 2021.05.31      Fim: 2021.--.--\n"
lbl_credits = Label(root, text=txt_credits, bg=bg, font = "courier 20 italic")

default()
img = images(directory)
vol = sound(directory, vol = 0.5, sound = 0)
roots = roots(root, bg, bg_frames, bg_narrative)
sub_roots = sub_roots(roots, bg, bg_frames, bg_narrative)
sub_sub_roots = sub_sub_roots(sub_roots, bg, bg_frames, bg_narrative)
labels = labels(roots, bg, bg_frames, bg_narrative, fg, img, sub_roots, sub_sub_roots, root)
buttons = buttons(roots, bg, bg_frames, bg_narrative, fg, options, click_back_to_main_menu)

var_language = StringVar()
var_language.set("BR")
var_progressBar = DoubleVar()
var_progressBar.set(0.5)
text_vol = f'{vol*100:.1f}%'
pb_vol = ttk.Progressbar(root, variable = var_progressBar, maximum = 1)
lbl_vol = Label(root, text = text_vol, bg=bg, font = "courier 16 bold")
rb_lan_UK = Radiobutton(root, text = "English", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
                    variable = var_language, value = "UK", relief = "flat", bd=4)
rb_lan_FR = Radiobutton(root, text = "Français", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
                    variable = var_language, value = "FR", relief = "flat", bd=4)
rb_lan_BR = Radiobutton(root, text = "Português", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#000",
                    variable = var_language, value = "BR", relief = "flat", bd=4)
rb_lan_SP = Radiobutton(root, text = "Español", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
                    variable = var_language, value = "SP", relief = "flat", bd=4)
rb_lan_GE = Radiobutton(root, text = "Deutsche", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
                    variable = var_language, value = "GE", relief = "flat", bd=4)

btn_newgame = Button(root, text= "Novo jogo", bg=bg, bd = 2, relief = "ridge", command= lambda: click_newgame(),
                        cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
btn_continue = Button(root, text= "Continuar", bg=bg, bd = 2, relief = "flat", command= lambda: click_nothing(), 
                        cursor="arrow", font = "courier 25 bold", fg = "#ccc")
btn_credits = Button(root, text= "Créditos", bg=bg, bd = 2, relief = "ridge", command= lambda: click_credits(),
                        cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
btn_options = Button(root, text = 'Ajustes',  bg=bg, bd = 2, relief = "ridge", command = lambda: click_options(),
                        cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
btn_quit = Button(root, text= "Sair", bg=bg, bd = 2, relief = "ridge", command = lambda: click_quit(),
                        cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
btn_back = Button(root, text = 'Voltar', bg=bg, bd = 2, relief = "ridge",command= lambda: click_back_to_main_menu(),
                        cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
btn_vol_max = Button(root, image = img['vol_max_dic'], bg=bg, bd = 2, relief = "ridge",command= lambda: volume("max"),
                        cursor="hand2", activebackground="#ccc", activeforeground=fg)
btn_vol_plus = Button(root, image = img['vol_plus_dic'], bg=bg, bd = 2, relief = "ridge",command= lambda: volume("plus"),
                        cursor="hand2", activebackground="#ccc", activeforeground=fg)
btn_vol_minus = Button(root, image = img['vol_minus_dic'], bg=bg, bd = 2, relief = "ridge",command= lambda: volume("minus"),
                        cursor="hand2", activebackground="#ccc", activeforeground=fg)
btn_vol_mute = Button(root, image = img['vol_mute_dic'], bg=bg, bd = 2, relief = "ridge",command= lambda: volume("mute"),
                        cursor="hand2", activebackground="#ccc", activeforeground=fg)

show_main_menu()
window.mainloop()
