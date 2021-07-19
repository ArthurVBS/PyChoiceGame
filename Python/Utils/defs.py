#Import - Libraries _________________________________________________________________________________________

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
from time import sleep

#Import - Packages __________________________________________________________________________________________

if __name__ == '__main__':
    from audio import mixer_pm, soundtrack
    from txt import show_menu_options, show_top_level

else:
    from Utils.audio import mixer_pm, soundtrack
    from Utils.txt import show_menu_options, show_top_level

#Variables __________________________________________________________________________________________________

bg = fg = '#fefefe'
bg_light = '#e1e1e1'
bg_gray = '#545454'
bg_dark = '#000'

#Main Functions _____________________________________________________________________________________________

def main_roots(window):
    root_play_game = Frame(window, bg=bg)
    root_main_menu = Frame(window, bg=bg)
    root_game_over = Frame(window, bg=bg_dark)
    root_credits = Frame(window, bg=bg)
    root_options = Frame(window, bg=bg)

    main_roots = {
        'root_play_game' : root_play_game, 'root_main_menu' : root_main_menu, 'root_game_over' : root_game_over,
        'root_credits' : root_credits, 'root_options' : root_options}

    return main_roots

#Functions - Game ___________________________________________________________________________________________

def game_roots(main_roots):
    root_hearts_foods = Frame(main_roots['root_play_game'], bg=bg_light, bd = 2, relief = 'sunken')
    root_hearts_foods.place(x = 5, y = 125, width = 260, height = 45)

    root_items_world_1 = Frame(main_roots['root_play_game'], bg=bg_light, bd = 2, relief = 'sunken')
    root_items_world_1.place(x = 5, y = 175, width = 85, height = 85)

    root_items_world_2 = Frame(main_roots['root_play_game'], bg=bg_light, bd = 2, relief = 'sunken')
    root_items_world_2.place(x = 92.5, y = 175, width = 85, height = 85)

    root_items_world_3 = Frame(main_roots['root_play_game'], bg=bg_light, bd = 2, relief = 'sunken')
    root_items_world_3.place(x = 180, y = 175, width = 85, height = 85)

    root_scenario = Frame(main_roots['root_play_game'], bg=bg_light, bd = 2, relief = 'sunken')
    root_scenario.place(x = 5 , y = 310, width = 260, height = 110)

    root_txt = Frame(main_roots['root_play_game'], bg=bg_dark)
    root_txt.place(x = 0, y = 0, width = 710, height = 120)

    root_text = Frame(main_roots['root_play_game'], bg=bg_light, bd = 2, relief = 'sunken')
    root_text.place(x = 270, y = 125, width = 435, height = 295)

    root_back_next = Frame(main_roots['root_play_game'], bg=bg_dark)
    root_back_next.place(x = 0, y = 425, width = 710, height = 45)

    root_ways = Frame(main_roots['root_play_game'], bg=bg_light, bd = 2, relief = 'sunken')
    root_ways.place(x = 5, y = 265, width = 260, height = 40)

    game_roots = {
        'root_hearts_foods' : root_hearts_foods, 'root_items_world_1' : root_items_world_1,
        'root_items_world_2' : root_items_world_2, 'root_items_world_3' : root_items_world_3,
        'root_scenario' : root_scenario, 'root_txt' : root_txt, 'root_text' : root_text,
        'root_back_next' : root_back_next, 'root_ways' : root_ways}

    return game_roots

def game_widgets(window, main_roots, directory, game_roots, images, version, menu_widgets):
    #Hearts and Foods

    lbl_heart = Label(game_roots['root_hearts_foods'], image = images['heart_11_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_heart.place(x = 2.5, y = 2.5, width = 35, height = 32.5)

    lbl_value_heart = Label(game_roots['root_hearts_foods'], text = f'100%', bg=bg, font = 'courier 13 bold', bd = 3, relief = 'ridge')
    lbl_value_heart.place(x = 35, y = 2.5, width = 90, height = 32.5)

    lbl_food = Label(game_roots['root_hearts_foods'], image = images['food_11_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_food.place(x = 127.5, y = 2.5, width = 35, height = 32.5)

    lbl_value_food = Label(game_roots['root_hearts_foods'], text = f'9/10', bg=bg, font = 'courier 13 bold', bd = 3, relief = 'ridge')
    lbl_value_food.place(x = 160, y = 2.5, width = 90, height = 32.5)

    #Items - World 1

    lbl_item_lighter = Label(game_roots['root_items_world_1'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_lighter.place(x = 3, y = 3, width = 35, height = 35)

    lbl_item_wolfhide = Label(game_roots['root_items_world_1'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_wolfhide.place(x = 43, y = 3, width = 35, height = 35)

    lbl_item_future_friendship = Label(game_roots['root_items_world_1'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_future_friendship.place(x = 43, y = 43, width = 35, height = 35)

    lbl_key_B = Label(game_roots['root_items_world_1'], image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_key_B.place(x = 3, y = 43, width = 35, height = 35)

    #Items - World 2

    lbl_item_shotgun = Label(game_roots['root_items_world_2'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_shotgun.place(x = 3, y = 3, width = 35, height = 35)

    lbl_item_nausea = Label(game_roots['root_items_world_2'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_nausea.place(x = 43, y = 3, width = 35, height = 35)

    lbl_item_crowbar = Label(game_roots['root_items_world_2'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_crowbar.place(x = 43, y = 43, width = 35, height = 35)

    lbl_key_S = Label(game_roots['root_items_world_2'], image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_key_S.place(x = 3, y = 43, width = 35, height = 35)

    #Items - World 3

    lbl_item_screwdriver = Label(game_roots['root_items_world_3'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_screwdriver.place(x = 3, y = 3, width = 35, height = 35)

    lbl_item_gear = Label(game_roots['root_items_world_3'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_gear.place(x = 43, y = 3, width = 35, height = 35)

    lbl_unknown = Label(game_roots['root_items_world_3'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_unknown.place(x = 43, y = 43, width = 35, height = 35)

    lbl_key_G = Label(game_roots['root_items_world_3'], image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_key_G.place(x = 3, y = 43, width = 35, height = 35)

    #Scenario

    lbl_scenario = Label(game_roots['root_scenario'], image = images['empty_00_dic'], bg=bg, anchor = CENTER)
    lbl_scenario.place(x = 3, y = 3, width= 250, height = 100)#250x100

    #TXT

    lbl_main_text = Label(game_roots['root_txt'], text = 'Texto principal', bg=bg, justify= LEFT,
                    font = 'courier 16 bold', bd = 4, relief = 'ridge')
    lbl_main_text.place(x = 0, y = 0, width = 710, height = 115)

    #Texts

    var_option = StringVar()
    var_option.set('E')

    rb_option_A = Radiobutton(game_roots['root_text'], bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2', 
                                variable = var_option, value = 'A', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
    rb_option_A.place(x = 5, y = 5, width = 420, height = 90)

    rb_option_B = Radiobutton(game_roots['root_text'], bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2', 
                                variable = var_option, value = 'B', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
    rb_option_B.place(x = 5, y = 100, width = 420, height = 90)

    rb_option_C = Radiobutton(game_roots['root_text'], bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2',
                                variable = var_option, value = 'C', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
    rb_option_C.place(x = 5, y = 195, width = 420, height = 90)

    #Back & Next

    lbl_version_in_game = Label(game_roots['root_back_next'], bg=bg_dark, font = 'courier 10 bold', text = version, fg=fg)
    lbl_version_in_game.place(x = 275, y = 5, width = 160, height = 30)

    btn_back = Button(game_roots['root_back_next'], text = 'Retornar ao Menu', bg=bg_dark, bd = 1.5, relief = 'ridge',
                    cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                    fg=fg, command=lambda : click_game_to_menu(window, main_roots, directory, var_option, with_sound=True))
    btn_back.place(x = 0, y = 5, width = 270, height = 30)

    btn_next = Button(game_roots['root_back_next'], text = 'Avançar', bg=bg_dark, bd = 1, relief = 'ridge',
                    cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                    fg=fg, command=lambda: click_next_level(window, directory, var_option, images, game_widgets, main_roots, menu_widgets))
    btn_next.place(x = 440, y = 5, width = 270, height = 30)

    #Ways

    lbl_way_01 = Label(game_roots['root_ways'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_01.place(x = 7.5, y = 0, width = 35, height = 35)

    lbl_way_02 = Label(game_roots['root_ways'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_02.place(x = 47.5, y = 0, width = 35, height = 35)

    lbl_way_03 = Label(game_roots['root_ways'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_03.place(x = 87.5, y = 0, width = 35, height = 35)

    lbl_way_04 = Label(game_roots['root_ways'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_04.place(x = 127.5, y = 0, width = 35, height = 35)

    lbl_way_05 = Label(game_roots['root_ways'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_05.place(x = 167.5, y = 0, width = 35, height = 35)

    lbl_way_06 = Label(game_roots['root_ways'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_06.place(x = 207.5, y = 0, width = 35, height = 35)

    game_widgets = {
        'lbl_heart' : lbl_heart, 'lbl_value_heart' : lbl_value_heart,
        'lbl_food' : lbl_food, 'lbl_value_food' : lbl_value_food,

        'lbl_item_lighter' : lbl_item_lighter, 'lbl_item_wolfhide' : lbl_item_wolfhide,
        'lbl_item_future_friendship' : lbl_item_future_friendship, 'lbl_key_B' : lbl_key_B,

        'lbl_item_shotgun' : lbl_item_shotgun, 'lbl_item_nausea' : lbl_item_nausea,
        'lbl_item_crowbar' : lbl_item_crowbar, 'lbl_key_S' : lbl_key_S,

        'lbl_item_screwdriver' : lbl_item_screwdriver, 'lbl_item_gear' : lbl_item_gear,
        'lbl_unknown' : lbl_unknown, 'lbl_key_G' : lbl_key_G,

        'lbl_scenario' : lbl_scenario,
        'lbl_main_text' : lbl_main_text,

        'var_option' : var_option, 'rb_option_A' : rb_option_A,
        'rb_option_B' : rb_option_B , 'rb_option_C' : rb_option_C,

        'lbl_version_in_game' : lbl_version_in_game, 'btn_back' : btn_back, 'btn_next' : btn_next, 

        'lbl_way_01' : lbl_way_01, 'lbl_way_02' : lbl_way_02, 'lbl_way_03' : lbl_way_03,
        'lbl_way_04' : lbl_way_04, 'lbl_way_05' : lbl_way_05, 'lbl_way_06' : lbl_way_06}

    return game_widgets

def click_next_level(window, directory, var_option, images, game_widgets, main_roots, menu_widgets):
    global items_values
    global vol

    if var_option.get() in 'ABC':
        resume = show_top_level(items_values["world"], items_values["level"], var_option.get(), random_number(), items_values)

        items_values['level'] += 1

        if items_values['level'] > 6:
            items_values['level'] = 1
            items_values['world'] += 1

            if items_values['world'] == 1:
                soundtrack(directory, vol = vol, soundtrack = 1)
                print('World 1')
            elif items_values['world'] == 2:
                soundtrack(directory, vol = vol, soundtrack = 2)
                print('World 2')
            elif items_values['world'] == 3:
                soundtrack(directory, vol = vol, soundtrack = 3)
                print('World 3')

            elif items_values['world'] > 3:
                print('END GAME')

        show_items_values(images, game_widgets)
        window.title(f'Level {items_values["world"]}-{items_values["level"]}')
        show_menu_options(items_values['world'], items_values['level'], game_widgets)

        if items_values['heart'] <= 0 or items_values['food'] <= 0:
            Game_Over(window, directory, main_roots)

        var_option.set('E')
        toplevel_result(directory, images, title = resume['title'], txt_result = resume['txt_result'],
                        losewin_heart = resume['losewin_heart'], losewin_food = resume['losewin_food'])

    else:
        messagebox.showerror(title = "Escolha", icon = messagebox.INFO,
        message = "Escolha uma das opções presente\npara poder continuar.")

def click_game_to_menu(window, main_roots, directory, var_option, with_sound = False):
    global vol
    var_option.set('E')

    if with_sound == True:
        soundtrack(directory, vol = vol, soundtrack = 0)

    main_roots['root_play_game'].place_forget()

    window.title('Main Menu')
    window.iconbitmap(directory + '/Images/Icons/icon_01.ico')

    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)

#Functions - Main Menu ______________________________________________________________________________________

def menu_widgets(window, main_roots, directory, default, version, images, game_widgets):
    #Labels
    lbl_title = Label(main_roots['root_main_menu'], text = " - In search - \n of the truth ", bg=bg, font = "courier 40 bold", justify=CENTER)
    lbl_title.place(x = 5, y = 5, width = 700, height = 140)

    lbl_version = Label(main_roots['root_main_menu'], text = version, bg=bg, font = "courier 10 bold", anchor = SE)
    lbl_version.place(x = 575, y = 425, width = 125, height = 25)

    #Buttons
    btn_newgame = Button(main_roots['root_main_menu'], text= "Novo jogo", bg=bg, bd = 2, relief = "ridge", cursor="hand2",
                    font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg, command=lambda :
                    click_new_game(window, main_roots, directory, default, images, game_widgets, menu_widgets))
    btn_newgame.place(x = 230, y = 160, width = 250, height = 50)

    btn_continue = Button(main_roots['root_main_menu'], text= "Continuar", bg=bg, bd = 2, relief = "flat", 
                    cursor="arrow", font = "courier 25 bold", fg = "#ccc", command=lambda : click_nothing())
    btn_continue.place(x = 230, y = 220, width = 250, height = 50)

    btn_options = Button(main_roots['root_main_menu'], text = 'Ajustes',  bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg,
                    command=lambda : click_options(window, main_roots, directory))
    btn_options.place(x = 230, y = 280, width = 250, height = 50)

    btn_credits = Button(main_roots['root_main_menu'], text= "Créditos", bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg,
                    command=lambda : click_credits(window, main_roots, directory))
    btn_credits.place(x = 230, y = 340, width = 250, height = 50)

    btn_quit = Button(main_roots['root_main_menu'], text= "Sair", bg=bg, bd = 2, relief = "ridge", cursor="hand2", 
                    font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg,
                    command=lambda : click_quit(window))
    btn_quit.place(x = 230, y = 400, width = 250, height = 50)

    menu_widgets = {
        'lbl_title' : lbl_title, 'lbl_version' : lbl_version,
        'btn_newgame' : btn_newgame, 'btn_continue' : btn_continue,
        'btn_options' : btn_options, 'btn_credits' : btn_credits,
        'btn_quit' : btn_quit}

    return menu_widgets

def click_new_game(window, main_roots, directory, default, images, game_widgets, menu_widgets):
    ok_cancel_newgame = messagebox.askokcancel(title = "Novo Jogo", message = "Desejas Iniciar um novo Jogo?",
    detail = "Caso possua um Save anterior ele será sobrescito")
    if ok_cancel_newgame:
        default(window, images, game_widgets)
        show_items_values(images, game_widgets)

        soundtrack(directory, vol = vol, soundtrack = 1)

        main_roots['root_main_menu'].place_forget()
        window.title(f'Level {items_values["world"]}-{items_values["level"]}')
        window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

        main_roots['root_play_game'].place(x = 5, y = 5, width = 710, height = 710)
        menu_widgets['btn_continue'].config(cursor="hand2", activebackground=bg_gray, activeforeground=fg,
        relief = "ridge", fg='#000', command=lambda : click_continue(window, main_roots, directory))

def click_nothing():
    messagebox.showerror(title = "Continuar?", icon = messagebox.INFO,
    message = "Inicie um Novo Jogo para que você possa\ncontinuar de onde parou.\t")

def click_continue(window, main_roots, directory):
    global items_values
    global vol

    main_roots['root_main_menu'].place_forget()
    window.title(f'Level {items_values["world"]}-{items_values["level"]}')
    window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

    if items_values['world'] == 1:
        soundtrack(directory, vol = vol, soundtrack = 1)
    elif items_values['world'] == 2:
        soundtrack(directory, vol = vol, soundtrack = 2)
    elif items_values['world'] == 3:
        soundtrack(directory, vol = vol, soundtrack = 3)

    main_roots['root_play_game'].place(x = 5, y = 5, width = 710, height = 460)

def click_options(window, main_roots, directory):
    window.title('Ajustes')
    window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

    main_roots['root_options'].place(x = 5, y = 5, width = 710, height = 460)

def click_credits(window, main_roots, directory):
    window.title('Créditos')
    window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

    main_roots['root_credits'].place(x = 5, y = 5, width = 710, height = 460)

def click_quit(window):
    ok_cancel_quit = messagebox.askokcancel(title = "Sair?", message = "Você realmente deseja sair?\t\t",
    detail = "Desde já obrigado por jogar")
    if ok_cancel_quit == True:
        window.destroy()

#Functions - Credits ________________________________________________________________________________________

def credits_widgets(window, main_roots, directory, version):
    #Labels
    lbl_credits_title = Label(main_roots['root_credits'], text = ' - In search - \n of the truth ', bg=bg, font = 'courier 40 bold', justify=CENTER)
    lbl_credits_title.place(x = 5, y = 5, width = 700, height = 140)

    lbl_credits_version = Label(main_roots['root_credits'], text = version, bg=bg, font = 'courier 10 bold', anchor = SE)
    lbl_credits_version.place(x = 575, y = 425, width = 125, height = 25)

    lbl_credits = Label(main_roots['root_credits'], font = 'courier 20 italic', text='Aluno: Arthur Vinícius Bezerra da Silva\n' +\
                        'Curso: ADS - IFPE - 1º período - 2021.1\n\nInício: 2021.05.31      Fim: 2021.--.--\n', bg=bg)
    lbl_credits.place(x = 5, y = 145, width = 700, height = 210)

    #Buttons
    btn_back = Button(main_roots['root_credits'], text = 'Voltar', bg=bg, bd = 2, relief = "ridge",
                    command=lambda : click_credits_to_menu(window, main_roots, directory),
                    cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
    btn_back.place(x = 230, y = 400, width = 250, height = 50)

    credits_widgets = {
        'lbl_credits_title' : lbl_credits_title, 'lbl_credits_version' : lbl_credits_version,
        'lbl_credits' : lbl_credits, 'btn_back' : btn_back}

    return credits_widgets

def click_credits_to_menu(window, main_roots, directory):
    window.title('Main Menu')
    window.iconbitmap(directory + '/Images/Icons/icon_01.ico')

    main_roots['root_credits'].place_forget()
    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)

#Functions - Options ________________________________________________________________________________________

def options_widgets(window, main_roots, directory, images):
    global vol
    vol = 0.5

    #Labels
    lbl_options_title =  Label(main_roots['root_options'], text = " - Ajustes - ", bg=bg, font = "courier 40 bold", justify=CENTER)
    lbl_options_title.place(x = 5, y = 5, width = 700, height = 100)

    lbl_volume = Label(main_roots['root_options'], text = " Volume ", bg=bg, font = "courier 32 bold")
    lbl_volume.place(x = 5, y = 85, width = 350, height = 65)

    lbl_language = Label(main_roots['root_options'], text = " Idioma ", bg=bg, font = "courier 32 bold")
    lbl_language.place(x = 355, y = 85, width = 350, height = 65)

    lbl_flag_UK = Label(main_roots['root_options'], image = images['flag_UK_dic'], bg=bg)
    lbl_flag_UK.place(x = 370, y = 160, width = 50, height = 50)

    lbl_flag_FR = Label(main_roots['root_options'], image = images['flag_FR_dic'], bg=bg)
    lbl_flag_FR.place(x = 370, y = 220, width = 50, height = 50)

    lbl_flag_BR = Label(main_roots['root_options'], image = images['flag_BR_dic'], bg=bg)
    lbl_flag_BR.place(x = 370, y = 280, width = 50, height = 50)

    lbl_flag_SP = Label(main_roots['root_options'], image = images['flag_SP_dic'], bg=bg)
    lbl_flag_SP.place(x = 370, y = 340, width = 50, height = 50)

    lbl_flag_GE = Label(main_roots['root_options'], image = images['flag_GE_dic'], bg=bg)
    lbl_flag_GE.place(x = 370, y = 400, width = 50, height = 50)

    lbl_vol = Label(main_roots['root_options'], text = f'{vol*100:.1f}%', bg=bg, font = "courier 16 bold")
    lbl_vol.place(x = 10, y = 205, width = 335, height = 30)

    #Buttons
    btn_vol_max = Button(main_roots['root_options'], image = images['vol_max_dic'], bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", activebackground="#ccc", activeforeground=fg, command= lambda: volume("max", options_widgets))
    btn_vol_max.place(x = 270, y = 320, width = 75, height = 70)

    btn_vol_plus = Button(main_roots['root_options'], image = images['vol_plus_dic'], bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", activebackground="#ccc", activeforeground=fg, command= lambda: volume("plus", options_widgets))
    btn_vol_plus.place(x = 185, y = 320, width = 75, height = 70)

    btn_vol_minus = Button(main_roots['root_options'], image = images['vol_minus_dic'], bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", activebackground="#ccc", activeforeground=fg, command= lambda: volume("minus", options_widgets))
    btn_vol_minus.place(x = 97.5, y = 320, width = 75, height = 70)

    btn_vol_mute = Button(main_roots['root_options'], image = images['vol_mute_dic'], bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", activebackground="#ccc", activeforeground=fg, command= lambda: volume("mute", options_widgets))
    btn_vol_mute.place(x = 10, y = 320, width = 75, height = 70)

    btn_back = Button(main_roots['root_options'], text = 'Voltar', bg=bg, bd = 2, relief = "ridge", cursor="hand2",
                    font = "courier 25 bold", activebackground="#ccc", activeforeground=fg,
                    command=lambda : click_options_to_menu(window, main_roots, directory, options_widgets))
    btn_back.place(x = 10, y = 400, width = 335, height = 50)

    #RadioButtons
    var_language = StringVar()
    var_language.set("BR")

    rb_lan_UK = Radiobutton(main_roots['root_options'], text = "English", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
                variable = var_language, value = "UK", bd=5, cursor="hand2")
    rb_lan_UK.place(x = 430, y = 160, width = 205, height = 50)

    rb_lan_FR = Radiobutton(main_roots['root_options'], text = "Français", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
                variable = var_language, value = "FR", bd=5, cursor="hand2")
    rb_lan_FR.place(x = 430, y = 220, width = 205, height = 50)

    rb_lan_BR = Radiobutton(main_roots['root_options'], text = "Português", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#000",
                variable = var_language, value = "BR", bd=5, cursor="hand2")
    rb_lan_BR.place(x = 430, y = 280, width = 205, height = 50)

    rb_lan_SP = Radiobutton(main_roots['root_options'], text = "Español", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
                variable = var_language, value = "SP", bd=5, cursor="hand2")
    rb_lan_SP.place(x = 430, y = 340, width = 205, height = 50)

    rb_lan_GE = Radiobutton(main_roots['root_options'], text = "Deutsch", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
                variable = var_language, value = "GE", bd=5, cursor="hand2")
    rb_lan_GE.place(x = 430, y = 400, width = 205, height = 50)

    #ProgressBar
    var_progressBar = DoubleVar()
    var_progressBar.set(vol)

    pb_vol = ttk.Progressbar(main_roots['root_options'], variable = var_progressBar, maximum = 1)
    pb_vol.place(x = 10 , y = 160, width = 335, height = 40)

    options_widgets = {
        'lbl_options_title' : lbl_options_title, 'lbl_volume' : lbl_volume, 'lbl_language' : lbl_language,
        'lbl_flag_UK' : lbl_flag_UK, 'lbl_flag_FR' : lbl_flag_FR, 'lbl_flag_BR' : lbl_flag_BR,
        'lbl_flag_SP' : lbl_flag_SP, 'lbl_flag_GE' : lbl_flag_GE, 'lbl_vol' : lbl_vol,

        'btn_vol_max' : btn_vol_max, 'btn_vol_plus' : btn_vol_plus, 'btn_vol_minus' : btn_vol_minus,
        'btn_vol_mute' : btn_vol_mute, 'btn_back' : btn_back,

        'var_language' : var_language, 'rb_lan_UK' : rb_lan_UK, 'rb_lan_FR' : rb_lan_FR,
        'rb_lan_BR' : rb_lan_BR, 'rb_lan_SP' : rb_lan_SP, 'rb_lan_GE' : rb_lan_GE,

        'var_progressBar' : var_progressBar, 'pb_vol' : pb_vol}

    return options_widgets

def click_options_to_menu(window, main_roots, directory, options_widgets):
    value_var_language = options_widgets['var_language'].get()

    if value_var_language != "BR":
        messagebox.showerror(title = "Idioma Indisponível", icon = messagebox.INFO,
        message = "O idioma selecionado encontra-se\nindisponível no momento.\n\n" +\
        "Por favor, selecione um idioma\ndisponível para prosseguir.")
    else:
        main_roots['root_options'].place_forget()

        window.title('Main Menu')
        window.iconbitmap(directory + '/Images/Icons/icon_01.ico')

        main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)

#Functions - Game over ______________________________________________________________________________________

def gameover_widgets(window, main_roots, directory, menu_widgets):
    #Labels
    lbl_gameover_title = Label(main_roots['root_game_over'], text = '- Game Over -', bg=bg_dark, font = 'courier 50 bold', justify=CENTER, fg=fg)
    lbl_gameover_title.place(x = 5, y = 5, width = 700, height = 100)

    lbl_try_again = Label(main_roots['root_game_over'], text = 'Tente Novamente', bg=bg_dark, font = 'courier 26 bold', justify=CENTER, fg=fg)
    lbl_try_again.place(x = 5, y = 115, width = 700, height = 100)

    #Buttons
    btn_gameover_back = Button(main_roots['root_game_over'], text = 'Voltar', bg=bg_dark, bd = 2, relief = "ridge", fg=fg,
                        command=lambda : click_gameover_to_menu(window, main_roots, directory, menu_widgets),
                        cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
    btn_gameover_back.place(x = 225, y = 400, width = 260, height = 50)

    gameover_widgets = {
        'lbl_gameover_title' : lbl_gameover_title, 'lbl_try_again' : lbl_try_again,
        'btn_gameover_back' : btn_gameover_back}

    return gameover_widgets

def click_gameover_to_menu(window, main_roots, directory, menu_widgets):
    global vol
    main_roots['root_game_over'].place_forget()

    window.title('Main Menu')
    window.iconbitmap(directory + '/Images/Icons/icon_01.ico')
    soundtrack(directory, vol = vol, soundtrack = 0)
        
    menu_widgets['btn_continue'].config(command = lambda: click_nothing(), fg = "#ccc", relief = "flat", cursor = "arrow",
                                        activebackground=None, activeforeground=None) 

    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)

#Functions - Result _________________________________________________________________________________________

def toplevel_result(directory, images, title = 'title', txt_result = 'text', losewin_heart = 0, losewin_food = 0):
    win_toplevel = Toplevel()

    width = 720
    height = 470
    width_screen = win_toplevel.winfo_screenwidth()
    height_screen = win_toplevel.winfo_screenheight()
    pos_x = int(width_screen / 2 - width / 2)
    pos_y = int(height_screen / 2 - height / 2)

    root_result = Frame(win_toplevel, bg=bg_light)
    root_result.place(x = 5, y = 5, width = 360, height = 310)

    win_toplevel.geometry(f"370x320+{pos_x + 175}+{pos_y + 50}")
    win_toplevel.title(title)
    win_toplevel.resizable(False, False)
    win_toplevel.iconbitmap(directory + "/Images/Icons/icon_01.ico")
    win_toplevel.configure(background = '#000')
    win_toplevel.update()
    sleep(0.3)

    #Text
    lbl_result_title = Label(root_result, text = "A sua escolha ocasionou:", bg=bg_light, font = "courier 16 bold", justify=CENTER)
    lbl_result_title.place(x = 5, y = 5, width = 350, height = 40)

    win_toplevel.update()
    sleep(0.5)

    lbl_result_subtitle = Label(root_result, text = txt_result, bg=bg_light, font = "courier 16 bold", justify=CENTER, relief='sunken', bd=1.5)
    lbl_result_subtitle.place(x = 5, y = 50, width = 350, height = 165)

    win_toplevel.update()
    sleep(1.2)

    #Roots
    root_result_heart = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')
    root_result_heart.place(x = 5, y = 220, width = 115, height = 50)

    win_toplevel.update()
    sleep(0.2)

    root_result_items = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')
    root_result_items.place(x = 122.5, y = 220, width = 115, height = 50)

    win_toplevel.update()
    sleep(0.2)

    root_result_food = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')
    root_result_food.place(x = 240, y = 220, width = 115, height = 50)

    win_toplevel.update()
    sleep(0.3)

    #Heart
    if losewin_heart <= 0:
        pos_neg_heart = ''
    elif losewin_heart > 0:
        pos_neg_heart = '+'

    lbl_img_heart = Label(root_result_heart, bg=bg_light, image = images['heart_11_dic'])
    lbl_img_heart.place(x = 5, y = 5, width = 40, height = 40)

    win_toplevel.update()
    sleep(0.3)

    lbl_value_heart = Label(root_result_heart, bg=bg_light, font = "courier 14 bold",
                            text = f'{pos_neg_heart}{losewin_heart}% ')
    lbl_value_heart.place(x = 45, y = 5, width = 65, height= 40)

    win_toplevel.update()
    sleep(0.3)

    #Items
    lbl_value_item = Label(root_result_items, bg=bg_light, text = '', font = "courier 14 bold")
    lbl_value_item.place(x = 5, y = 5, width = 25, height= 40)

    win_toplevel.update()
    sleep(0.3)

    lbl_img_item_01 = Label(root_result_items, bg=bg_light, image = images['empty_00_dic'])
    lbl_img_item_01.place(x = 30, y = 5, width = 40, height = 40)

    win_toplevel.update()
    sleep(0.3)

    lbl_img_item_02 = Label(root_result_items, bg=bg_light, image = images['empty_00_dic'])
    lbl_img_item_02.place(x = 70, y = 5, width = 40, height= 40)

    win_toplevel.update()
    sleep(0.3)

    #Food
    if losewin_food <= 0:
        pos_neg_food = ''
    elif losewin_food> 0:
        pos_neg_food = '+'

    lbl_img_food = Label(root_result_food, bg=bg_light, image = images['food_11_dic'])
    lbl_img_food.place(x = 5, y = 5, width = 40, height = 40)
    win_toplevel.update()

    sleep(0.3)

    lbl_value_food = Label(root_result_food, bg=bg_light, font = "courier 14 bold",
                            text = f'{pos_neg_food}{losewin_food}/10')
    lbl_value_food.place(x = 45, y = 5, width = 65, height= 40)

    win_toplevel.update()
    sleep(0.2)

    #Button
    lbl_bg_dark = Label(root_result, bg=bg_dark)
    lbl_bg_dark.place(x = 0, y = 275, width = 360, height = 35)

    btn_result_next = Button(root_result, text = 'OK', bg=bg_dark, bd = 1, relief = 'ridge',
                    cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                    fg=fg, command=lambda : win_toplevel.destroy())
    btn_result_next.place(x = 122.5, y = 280, width = 115, height = 30)
    

    win_toplevel.mainloop()

#Functions - Others _________________________________________________________________________________________

def default(window, images, game_widgets):
    global items_values

    items_values = {
        'level' : 1, 'world' : 1,

        'food' : 5, 'heart' : 80,

        'key_B' : True, 'key_S' : False, 'key_G' : False,

        'item_lighter' : True, 'item_future_friendship' : False,
        'item_wolfhide' : False, 'item_shotgun' : False,
        'item_nausea' : False, 'item_crowbar' : False,
        'item_screwdriver' : False, 'item_gear' : False}

    #Title
    window.title(f'Level {items_values["world"]}-{items_values["level"]}')

    #Scenario
    game_widgets['lbl_scenario']['image'] = images['scenario_01_dic']

    #Menu_Options
    show_menu_options(items_values['world'], items_values['level'], game_widgets)

    #Heart
    game_widgets['lbl_value_heart']['text'] = '80%'
    game_widgets['lbl_heart']['image'] = images['heart_11_dic']

    #Food
    game_widgets['lbl_value_food']['text'] = '5/10'
    game_widgets['lbl_food']['image'] = images['food_01_dic']

    #Keys
    game_widgets['lbl_key_B']['image'] = images['key_B_dic']
    game_widgets['lbl_key_S']['image'] = images['key_E_dic']
    game_widgets['lbl_key_G']['image'] = images['key_E_dic']

    #Way
    game_widgets['lbl_way_01']['image'] = images['way_dic']
    game_widgets['lbl_way_02']['image'] = images['just_way_dic']
    game_widgets['lbl_way_03']['image'] = images['just_way_dic']
    game_widgets['lbl_way_04']['image'] = images['just_way_dic']
    game_widgets['lbl_way_05']['image'] = images['just_way_dic']
    game_widgets['lbl_way_06']['image'] = images['just_way_dic']

    #Items
    game_widgets['lbl_item_lighter']['image'] = images['item_lighter_dic']
    game_widgets['lbl_item_future_friendship']['image'] = images['empty_01_dic']
    game_widgets['lbl_item_wolfhide']['image'] = images['empty_01_dic']
    game_widgets['lbl_item_shotgun']['image'] = images['empty_01_dic']
    game_widgets['lbl_item_nausea']['image'] = images['empty_01_dic']
    game_widgets['lbl_item_crowbar']['image'] = images['empty_01_dic']
    game_widgets['lbl_item_screwdriver']['image'] = images['empty_01_dic']
    game_widgets['lbl_item_gear']['image'] = images['empty_01_dic']

def show_items_values(images, game_widgets):
    global items_values

    def heart():
        if items_values["heart"] >= 100:
            items_values["heart"] = 100

        if 100 >= items_values['heart'] > 75: #100 - 75
            game_widgets['lbl_heart']['image'] = images['heart_11_dic']

        elif 75 >= items_values['heart'] > 25: #75 - 25
            game_widgets['lbl_heart']['image'] = images['heart_01_dic']

        elif 25 >= items_values['heart'] > 0: #25 - 0
            game_widgets['lbl_heart']['image'] = images['heart_00_dic']

        game_widgets['lbl_value_heart']['text'] = f'{items_values["heart"]}%'
    
    def food():
        if items_values["food"] >= 10:
            items_values["food"] = 10

        if 10 >= items_values['food'] > 7.5: #10 - 7.5
            game_widgets['lbl_food']['image'] = images['food_11_dic']

        elif 7.5 >= items_values['food'] > 2.5: #7.5 - 2.5
            game_widgets['lbl_food']['image'] = images['food_01_dic']

        elif 2.5 >= items_values['food'] > 0: #2.5 - 0
            game_widgets['lbl_food']['image'] = images['food_00_dic']

        game_widgets['lbl_value_food']['text'] = f'{items_values["food"]}/10'

    def keys():
        game_widgets['lbl_key_B']['image'] = images['key_E_dic']
        game_widgets['lbl_key_S']['image'] = images['key_E_dic']
        game_widgets['lbl_key_G']['image'] = images['key_E_dic']

        if items_values["key_B"] == True: #Bronze
            game_widgets['lbl_key_B']['image'] = images['key_B_dic']

        if items_values["key_S"] == True: #Silver
            game_widgets['lbl_key_S']['image'] = images['key_S_dic']

        if items_values["key_G"] == True: #Golden
            game_widgets['lbl_key_G']['image'] = images['key_G_dic']

    def items():
        game_widgets['lbl_item_lighter']['image'] = images['empty_01_dic']
        game_widgets['lbl_item_future_friendship']['image'] = images['empty_01_dic']
        game_widgets['lbl_item_wolfhide']['image'] = images['empty_01_dic']
        game_widgets['lbl_item_shotgun']['image'] = images['empty_01_dic']
        game_widgets['lbl_item_nausea']['image'] = images['empty_01_dic']
        game_widgets['lbl_item_crowbar']['image'] = images['empty_01_dic']
        game_widgets['lbl_item_screwdriver']['image'] = images['empty_01_dic']
        game_widgets['lbl_item_gear']['image'] = images['empty_01_dic']

        if items_values['item_lighter'] == True: 
            game_widgets['lbl_item_lighter']['image'] = images['item_lighter_dic']

        if items_values['item_future_friendship'] == True:
            game_widgets['lbl_item_future_friendship']['image'] = images['item_future_friendship_dic']

        if items_values['item_wolfhide'] == True:
            game_widgets['lbl_item_wolfhide']['image'] = images['item_wolfhide_dic']

        if items_values['item_shotgun'] == True:
            game_widgets['lbl_item_shotgun']['image'] = images['item_shotgun_dic']

        if items_values['item_nausea'] == True:
            game_widgets['lbl_item_nausea']['image'] = images['item_nausea_dic']

        if items_values['item_crowbar'] == True:
            game_widgets['lbl_item_crowbar']['image'] = images['item_crowbar_dic']

        if items_values['item_screwdriver'] == True:
            game_widgets['lbl_item_screwdriver']['image'] = images['item_screwdriver_dic']

        if items_values['item_gear'] == True:
            game_widgets['lbl_item_gear']['image'] = images['item_gear_dic']
  
    def ways(): #(Level)
        if 6 >= items_values['level'] >= 1:
            game_widgets['lbl_way_01']['image'] = images['just_way_dic']
            game_widgets['lbl_way_02']['image'] = images['just_way_dic']
            game_widgets['lbl_way_03']['image'] = images['just_way_dic']
            game_widgets['lbl_way_04']['image'] = images['just_way_dic']
            game_widgets['lbl_way_05']['image'] = images['just_way_dic']
            game_widgets['lbl_way_06']['image'] = images['just_way_dic']

            if items_values['level'] == 1:
                game_widgets['lbl_way_01']['image'] = images['way_dic']
            elif items_values['level'] == 2:
                game_widgets['lbl_way_02']['image'] = images['way_dic']
            elif items_values['level'] == 3:
                game_widgets['lbl_way_03']['image'] = images['way_dic']
            elif items_values['level'] == 4:
                game_widgets['lbl_way_04']['image'] = images['way_dic']
            elif items_values['level'] == 5:
                game_widgets['lbl_way_05']['image'] = images['way_dic']
            elif items_values['level'] == 6:
                game_widgets['lbl_way_06']['image'] = images['way_dic']

    def scenario(): #(World)
        if items_values['world'] == 1:
            game_widgets['lbl_scenario']['image'] = images['scenario_01_dic']

        elif items_values['world'] == 2:
            game_widgets['lbl_scenario']['image'] = images['scenario_02_dic']

        elif items_values['world'] == 3:
            game_widgets['lbl_scenario']['image'] = images['scenario_03_dic']

    heart()
    food()
    keys()
    items()
    ways()
    scenario()

def Game_Over(window, directory, main_roots):
    global vol
    main_roots['root_main_menu'].place_forget()
    main_roots['root_game_over'].place(x = 5, y = 5, width = 710, height = 460)
    soundtrack(directory, vol = vol, soundtrack = -1)
    window.title('Game Over')

def volume(option, options_widgets):
    global vol

    if option == "max":
        vol = round(mixer_pm(vol = 1, plus_or_minus = "plus"), 2)
    elif option == "plus":
        vol = round(mixer_pm(vol, plus_or_minus = "plus"), 2)
    elif option == "minus":
        vol = round(mixer_pm(vol, plus_or_minus = "minus"), 2)
    elif option == "mute":
        vol = round(mixer_pm(vol = 0, plus_or_minus = "minus"), 2)

    vol_pb(options_widgets)

def vol_pb(options_widgets):
    global vol
    var_progressBar = DoubleVar()
    var_progressBar.set(vol)
    text_vol = f'{vol*100:.1f}%'

    options_widgets['pb_vol'].configure(variable = var_progressBar)
    options_widgets['pb_vol'].place(x = 10 , y = 160, width = 335, height = 40)

    options_widgets['lbl_vol'].configure(text = text_vol)
    options_widgets['lbl_vol'].place(x = 10, y = 205, width = 335, height = 30)

def random_number():
    return randint(1,4)
