#Import - Libraries _________________________________________________________________________________________

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
from time import sleep

#Import - Packages __________________________________________________________________________________________

try:
    from sound import  mixer_pm, soundtrack, voice_over
    from txt import show_menu_options, show_top_level, show_tutorial, show_history
except:
    from Utils.sound import mixer_pm, soundtrack, voice_over
    from Utils.txt import show_menu_options, show_top_level, show_tutorial, show_history

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
    root_end_of_the_game = Frame(window, bg=bg_dark)
    root_credits = Frame(window, bg=bg)
    root_options = Frame(window, bg=bg)
    root_tutorial = Frame(window, bg=bg)
    root_history = Frame(window, bg=bg)

    main_roots = {
        'root_play_game' : root_play_game, 'root_main_menu' : root_main_menu, 'root_tutorial' : root_tutorial,
        'root_game_over' : root_game_over, 'root_credits' : root_credits, 'root_options' : root_options,
        'root_history' : root_history, 'root_end_of_the_game' : root_end_of_the_game}

    return main_roots


def start_the_game(window, main_roots, directory):
    global vol

    #Menu
    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)

    #Sound
    vol = soundtrack(directory, vol = 0.5, soundtrack = 0)

    #Window
    window.title('Main Menu')
    window.iconbitmap(directory + '/Assets/Icons/icon_01.ico')


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


def game_widgets(window, main_roots, directory, game_roots, images, version, history_widgets):
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

    btn_next = Button(game_roots['root_back_next'], text = 'Avançar', bg=bg_dark, bd = 1.5, relief = 'ridge',
                    cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                    fg=fg, command=lambda: click_next_level(window, directory, var_option, images, game_widgets, main_roots, history_widgets))
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


def click_next_level(window, directory, var_option, images, game_widgets, main_roots, history_widgets):
    global items_values
    global vol

    if var_option.get() in 'ABC':
        history = False
        resume = show_top_level(directory, items_values["world"], items_values["level"],
                                var_option.get(), random_number(), items_values, vol)

        #Level up
        items_values['level'] += 1

        if items_values['level'] > 6:
            #World up
            items_values['level'] = 1
            items_values['world'] += 1

            #Show history
            click_history(window, main_roots, directory, history_widgets)
            history = True

            #End Game
            if items_values['world'] > 3:
                click_end_of_the_game(window, main_roots, directory)
            

        #Show items
        show_items_values(images, game_widgets)

        #Title
        if history:
            window.title('História')
        else:
            window.title(f'Level {items_values["world"]}-{items_values["level"]}')

        #Show menu_options
        show_menu_options(items_values['world'], items_values['level'], game_widgets)

        #If game_over == True
        if items_values['heart'] <= 0 or items_values['food'] <= 0 or resume['game_over']:
            click_game_over(window, directory, main_roots)

        #Show toplevel
        var_option.set('E')
        toplevel_result(directory, images, title = resume['title'], txt_result = resume['txt_result'],
                        losewin_heart = resume['losewin_heart'], losewin_food = resume['losewin_food'],
                        new_item = resume['new_item'], new_key = resume['new_key'])

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
    window.iconbitmap(directory + '/Assets/Icons/icon_01.ico')

    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)


#Functions - Main Menu ______________________________________________________________________________________

def menu_widgets(window, main_roots, directory, default, version, images, game_widgets, title, tutorial_widgets, history_widgets):
    #Labels
    lbl_title = Label(main_roots['root_main_menu'], text = title, bg=bg, font = "courier 42 bold", justify=CENTER)
    lbl_title.place(x = 5, y = 5, width = 700, height = 150)

    lbl_version = Label(main_roots['root_main_menu'], text = version, bg=bg, font = "courier 10 bold")
    lbl_version.place(x = 275, y = 430, width = 160, height = 30)

    lbl_line_01 = Label(main_roots['root_main_menu'], bg=bg_dark)
    lbl_line_01.place(x = 0, y = 425, width = 710, height = 5)

    lbl_line_02 = Label(main_roots['root_main_menu'], bg=bg_dark)
    lbl_line_02.place(x = 0, y = 160, width = 710, height = 5)

    #Buttons
    btn_newgame = Button(main_roots['root_main_menu'], text= "Novo jogo", bg=bg, bd = 2, relief = "ridge", cursor="hand2",
                    font = "courier 26 bold", activebackground=bg_gray, activeforeground=fg, command=lambda :
                    click_new_game(window, main_roots, directory, default, images, game_widgets, menu_widgets, history_widgets))
    btn_newgame.place(x = 55, y = 212.5, width = 275, height = 50)

    btn_continue = Button(main_roots['root_main_menu'], text= "Continuar", bg=bg, bd = 2, relief = "flat", 
                    cursor="arrow", font = "courier 26 bold", fg = "#ccc", command=lambda : click_nothing())
    btn_continue.place(x = 55, y = 272.5, width = 275, height = 50)

    btn_credits = Button(main_roots['root_main_menu'], text= "Créditos", bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", font = "courier 26 bold", activebackground=bg_gray, activeforeground=fg,
                    command=lambda : click_credits(window, main_roots, directory))
    btn_credits.place(x = 55, y = 332.5, width = 275, height = 50)

    btn_tutorial = Button(main_roots['root_main_menu'], text= "Tutorial", bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", font = "courier 26 bold", activebackground=bg_gray, activeforeground=fg,
                    command=lambda : click_tutorial(window, main_roots, directory, tutorial_widgets))
    btn_tutorial.place(x = 380, y = 212.5, width = 275, height = 50)

    btn_options = Button(main_roots['root_main_menu'], text = 'Ajustes',  bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", font = "courier 26 bold", activebackground=bg_gray, activeforeground=fg,
                    command=lambda : click_options(window, main_roots, directory))
    btn_options.place(x = 380, y = 272.5, width = 275, height = 50)

    btn_quit = Button(main_roots['root_main_menu'], text= "Sair", bg=bg, bd = 2, relief = "ridge", cursor="hand2", 
                    font = "courier 26 bold", activebackground=bg_gray, activeforeground=fg,
                    command=lambda : click_quit(window))
    btn_quit.place(x = 380, y = 332.5, width = 275, height = 50)

    menu_widgets = {
        'lbl_title' : lbl_title, 'lbl_version' : lbl_version,
        'lbl_line_01' : lbl_line_01, 'lbl_line_02' : lbl_line_02,
        'btn_newgame' : btn_newgame, 'btn_continue' : btn_continue,
        'btn_options' : btn_options, 'btn_credits' : btn_credits,
        'btn_quit' : btn_quit}

    return menu_widgets


def click_new_game(window, main_roots, directory, default, images, game_widgets, menu_widgets, history_widgets):
    ok_cancel_newgame = messagebox.askokcancel(title = "Novo Jogo", message = "Desejas Iniciar um novo Jogo?",
    detail = "Caso possua um Save anterior ele será sobrescito")
    if ok_cancel_newgame:
        default(window, images, game_widgets)
        show_items_values(images, game_widgets)

        click_history(window, main_roots, directory, history_widgets)

        main_roots['root_main_menu'].place_forget()
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
    window.iconbitmap(directory + '/Assets/Icons/icon_02.ico')

    if items_values['world'] == 1:
        soundtrack(directory, vol = vol, soundtrack = 1)
    elif items_values['world'] == 2:
        soundtrack(directory, vol = vol, soundtrack = 2)
    elif items_values['world'] == 3:
        soundtrack(directory, vol = vol, soundtrack = 3)

    main_roots['root_play_game'].place(x = 5, y = 5, width = 710, height = 460)


def click_tutorial(window, main_roots, directory, tutorial_widgets):
    window.title('Tutorial')
    window.iconbitmap(directory + '/Assets/Icons/icon_02.ico')

    show_tutorial(tutorial_widgets, page=0)
    tutorial_widgets['btn_next_tut'].place(x = 440, y = 5, width = 270, height = 30)
    main_roots['root_tutorial'].place(x = 5, y = 5, width = 710, height = 460)


def click_history(window, main_roots, directory, history_widgets):
    global items_values
    window.title('História')
    window.iconbitmap(directory + '/Assets/Icons/icon_02.ico')
    show_history(history_widgets , page = 0, world = items_values['world'])

    main_roots['root_history'].place(x = 5, y = 5, width = 710, height = 460)


def click_end_of_the_game(window, main_roots, directory):
    window.title('Fim de Jogo')
    window.iconbitmap(directory + '/Assets/Icons/icon_02.ico')

    main_roots['root_end_of_the_game'].place(x = 5, y = 5, width = 710, height = 460)


def click_game_over(window, directory, main_roots):
    global vol
    main_roots['root_main_menu'].place_forget()
    main_roots['root_history'].place_forget()
    main_roots['root_game_over'].place(x = 5, y = 5, width = 710, height = 460)
    soundtrack(directory, vol = vol, soundtrack = -1)
    window.title('Game Over')


def click_options(window, main_roots, directory):
    window.title('Ajustes')
    window.iconbitmap(directory + '/Assets/Icons/icon_02.ico')

    main_roots['root_options'].place(x = 5, y = 5, width = 710, height = 460)


def click_credits(window, main_roots, directory):
    window.title('Créditos')
    window.iconbitmap(directory + '/Assets/Icons/icon_02.ico')

    main_roots['root_credits'].place(x = 5, y = 5, width = 710, height = 460)


def click_quit(window):
    ok_cancel_quit = messagebox.askokcancel(title = "Sair?", message = "Você realmente deseja sair?\t\t",
    detail = "Desde já obrigado por jogar")
    if ok_cancel_quit == True:
        window.destroy()


#Functions - Credits ________________________________________________________________________________________

def credits_widgets(window, main_roots, directory, version, title):
    #Labels
    lbl_credits_title = Label(main_roots['root_credits'], text = title, bg=bg, font = 'courier 42 bold', justify=CENTER)
    lbl_credits_title.place(x = 5, y = 5, width = 700, height = 150)

    lbl_credits_version = Label(main_roots['root_credits'], text = version, bg=bg, font = 'courier 10 bold')
    lbl_credits_version.place(x = 275, y = 430, width = 160, height = 30)

    lbl_credits = Label(main_roots['root_credits'], font = 'courier 20 italic', text='Aluno: Arthur Vinícius Bezerra da Silva\n' +\
                        'Curso: ADS - IFPE - 1º período - 2021.1\n\nInício: 2021.05.31      Fim: 2021.--.--', bg=bg)
    lbl_credits.place(x = 5, y = 170, width = 700, height = 250)

    lbl_credits_line_01 = Label(main_roots['root_credits'], bg=bg_dark)
    lbl_credits_line_01.place(x = 0, y = 425, width = 710, height = 5)

    lbl_credits_line_02 = Label(main_roots['root_credits'], bg=bg_dark)
    lbl_credits_line_02.place(x = 0, y = 160, width = 710, height = 5)

    #Buttons
    btn_credits_back = Button(main_roots['root_credits'], text = 'Retornar ao menu', bg=bg, bd = 2.5, relief = "ridge",
                    command=lambda : click_credits_to_menu(window, main_roots, directory),
                    cursor="hand2", font = "courier 14 bold", activebackground=bg_gray, activeforeground=fg)
    btn_credits_back.place(x = 0, y = 430, width = 270, height = 30)

    credits_widgets = {
        'lbl_credits_title' : lbl_credits_title, 'lbl_credits_version' : lbl_credits_version,
        'lbl_credits_line_01' : lbl_credits_line_01, 'lbl_credits_line_02' : lbl_credits_line_02,
        'lbl_credits' : lbl_credits, 'btn_credits_back' : btn_credits_back}

    return credits_widgets


def click_credits_to_menu(window, main_roots, directory):
    window.title('Main Menu')
    window.iconbitmap(directory + '/Assets/Icons/icon_01.ico')

    main_roots['root_credits'].place_forget()
    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)


#Functions - Options ________________________________________________________________________________________

def options_widgets(window, main_roots, directory, version, images):
    global vol
    vol = 0.5
    #Labels
    lbl_options_title = Label(main_roots['root_options'], text = '- Ajustes -\n', bg=bg, font = 'courier 42 bold', justify=CENTER)
    lbl_options_title.place(x = 5, y = 5, width = 700, height = 150)

    lbl_options_line_01 = Label(main_roots['root_options'], bg=bg_dark)
    lbl_options_line_01.place(x = 0, y = 425, width = 710, height = 5)

    lbl_options_line_02 = Label(main_roots['root_options'], bg=bg_dark)
    lbl_options_line_02.place(x = 0, y = 160, width = 710, height = 5)

    lbl_options_version = Label(main_roots['root_options'], text = version, bg=bg, font = 'courier 10 bold')
    lbl_options_version.place(x = 275, y = 430, width = 160, height = 30)

    lbl_volume = Label(main_roots['root_options'], text = " Volume ", bg=bg, font = "courier 32 bold")
    lbl_volume.place(x = 5, y = 85, width = 350, height = 65)

    lbl_language = Label(main_roots['root_options'], text = " Idioma ", bg=bg, font = "courier 32 bold")
    lbl_language.place(x = 355, y = 85, width = 350, height = 65)

    lbl_vol = Label(main_roots['root_options'], text = f'{vol*100:.1f}%', bg=bg, font = "courier 20 bold")
    lbl_vol.place(x = 15, y = 220, width = 347.5, height = 40)

    #Buttons
    btn_vol_max = Button(main_roots['root_options'], image = images['vol_max_dic'], bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", activebackground=bg_gray, activeforeground=fg, command= lambda: volume("max", options_widgets))
    btn_vol_max.place(x = 285, y = 340, width = 75, height = 70)

    btn_vol_plus = Button(main_roots['root_options'], image = images['vol_plus_dic'], bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", activebackground=bg_gray, activeforeground=fg, command= lambda: volume("plus", options_widgets))
    btn_vol_plus.place(x = 195, y = 340, width = 75, height = 70)

    btn_vol_minus = Button(main_roots['root_options'], image = images['vol_minus_dic'], bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", activebackground=bg_gray, activeforeground=fg, command= lambda: volume("minus", options_widgets))
    btn_vol_minus.place(x = 105, y = 340, width = 75, height = 70)

    btn_vol_mute = Button(main_roots['root_options'], image = images['vol_mute_dic'], bg=bg, bd = 2, relief = "ridge",
                    cursor="hand2", activebackground=bg_gray, activeforeground=fg, command= lambda: volume("mute", options_widgets))
    btn_vol_mute.place(x = 15, y = 340, width = 75, height = 70)

    btn_options_back = Button(main_roots['root_options'], text = 'Retornar ao menu', bg=bg, bd = 2.5, relief = "ridge",
                    command=lambda : click_options_to_menu(window, main_roots, directory, options_widgets),
                    cursor="hand2", font = "courier 14 bold", activebackground=bg_gray, activeforeground=fg)
    btn_options_back.place(x = 0, y = 430, width = 270, height = 30)

    #RadioButtons
    var_language = StringVar()
    var_language.set("BR")

    rb_lan_UK = Radiobutton(main_roots['root_options'], text = "English", bg=bg, font = "courier 16 bold", indicatoron=0, fg = "#888",
                variable = var_language, value = "UK", bd=5, cursor="hand2")
    rb_lan_UK.place(x = 430, y = 180, width = 210, height = 40)

    rb_lan_FR = Radiobutton(main_roots['root_options'], text = "Français", bg=bg, font = "courier 16 bold", indicatoron=0, fg = "#888",
                variable = var_language, value = "FR", bd=5, cursor="hand2")
    rb_lan_FR.place(x = 430, y = 227.5, width = 210, height = 40)

    rb_lan_BR = Radiobutton(main_roots['root_options'], text = "Português", bg=bg, font = "courier 16 bold", indicatoron=0, fg = "#000",
                variable = var_language, value = "BR", bd=5, cursor="hand2")
    rb_lan_BR.place(x = 430, y = 275, width = 210, height = 40)

    rb_lan_SP = Radiobutton(main_roots['root_options'], text = "Español", bg=bg, font = "courier 16 bold", indicatoron=0, fg = "#888",
                variable = var_language, value = "SP", bd=5, cursor="hand2")
    rb_lan_SP.place(x = 430, y = 322.5, width = 210, height = 40)

    rb_lan_GE = Radiobutton(main_roots['root_options'], text = "Deutsch", bg=bg, font = "courier 16 bold", indicatoron=0, fg = "#888",
                variable = var_language, value = "GE", bd=5, cursor="hand2")
    rb_lan_GE.place(x = 430, y = 370, width = 210, height = 40)

    #ProgressBar
    var_progressBar = DoubleVar()
    var_progressBar.set(vol)

    pb_vol = ttk.Progressbar(main_roots['root_options'], variable = var_progressBar, maximum = 1)
    pb_vol.place(x = 15 , y = 180, width = 347.5, height = 35)

    options_widgets = {
        'lbl_options_title' : lbl_options_title, 'lbl_volume' : lbl_volume, 'lbl_language' : lbl_language,
        'lbl_options_line_01' : lbl_options_line_01, 'lbl_options_line_02' : lbl_options_line_02,
        'lbl_options_version' : lbl_options_version, 'lbl_vol' : lbl_vol,

        'btn_vol_max' : btn_vol_max, 'btn_vol_plus' : btn_vol_plus, 'btn_vol_minus' : btn_vol_minus,
        'btn_vol_mute' : btn_vol_mute, 'btn_options_back' : btn_options_back, 

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
        window.iconbitmap(directory + '/Assets/Icons/icon_01.ico')

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
                        cursor="hand2", font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg)
    btn_gameover_back.place(x = 225, y = 400, width = 260, height = 50)

    gameover_widgets = {
        'lbl_gameover_title' : lbl_gameover_title, 'lbl_try_again' : lbl_try_again,
        'btn_gameover_back' : btn_gameover_back}

    return gameover_widgets


def click_gameover_to_menu(window, main_roots, directory, menu_widgets):
    global vol
    main_roots['root_game_over'].place_forget()

    window.title('Main Menu')
    window.iconbitmap(directory + '/Assets/Icons/icon_01.ico')
    soundtrack(directory, vol = vol, soundtrack = 0)
        
    menu_widgets['btn_continue'].config(command = lambda: click_nothing(), fg = "#ccc", relief = "flat", cursor = "arrow",
                                        activebackground=None, activeforeground=None) 

    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)


#Functions - Result _________________________________________________________________________________________

def toplevel_result(directory, images, title = 'title', txt_result = 'text', losewin_heart = 0, losewin_food = 0,
                    new_item = None, new_key = None):
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
    win_toplevel.iconbitmap(directory + "/Assets/Icons/icon_01.ico")
    win_toplevel.configure(background = '#000')
    win_toplevel.update()
    sleep(0.3)

    #Text
    lbl_result_title = Label(root_result, text = "A sua escolha ocasionou:", bg=bg_light, font = "courier 16 bold", justify=CENTER)
    lbl_result_title.place(x = 5, y = 5, width = 350, height = 40)

    win_toplevel.update()
    sleep(0.5)

    lbl_result_subtitle = Label(root_result, text = txt_result, bg=bg_light, font = "courier 14 bold", justify=CENTER, relief='sunken', bd=1.5)
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
    sleep(0.1)

    #Items

    lbl_value_item = Label(root_result_items, bg=bg_light, text = '', font = "courier 14 bold")
    lbl_value_item.place(x = 5, y = 5, width = 25, height= 40)

    lbl_img_item_01 = Label(root_result_items, bg=bg_light, image = images['empty_00_dic'])
    lbl_img_item_01.place(x = 30, y = 5, width = 40, height = 40)

    lbl_img_item_02 = Label(root_result_items, bg=bg_light, image = images['empty_00_dic'])
    lbl_img_item_02.place(x = 70, y = 5, width = 40, height= 40)

    if new_item != None or new_key != None:
        #Text
        lbl_value_item['text'] = '+'
        #Item
        if new_item != None:
            lbl_img_item_01['image'] = images[f'item_{new_item}_dic']
        #Key
        if new_key != None:
            lbl_img_item_02['image'] = images[f'key_{new_key}_dic']

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


#Functions - End of the Game ________________________________________________________________________________

def end_of_the_game_widgets(window, main_roots, directory):
    #Labels
    lbl_end_of_the_game = Label(main_roots['root_end_of_the_game'], text = '- End Game -', bg=bg_dark,
                                font = 'courier 50 bold', justify=CENTER, fg=fg)
    lbl_end_of_the_game.place(x = 5, y = 5, width = 700, height = 100)

    lbl_thanks_for_playing = Label(main_roots['root_end_of_the_game'], bg=bg_dark, font = 'courier 26 bold',
                                    text = 'Obrigado por jogar e zerar\no meu jogo!', 
                                    justify=CENTER, fg=fg)
    lbl_thanks_for_playing.place(x = 5, y = 115, width = 700, height = 100)

    lbl_user = Label(main_roots['root_end_of_the_game'], bg=bg_dark, font = 'courier 18 bold',
                    text = 'Insira seu nome:', anchor=W, fg=fg)
    lbl_user.place(x = 10, y = 370, width = 595, height = 40)

    #Entry
    var_user = StringVar()
    entry_user = Entry(main_roots['root_end_of_the_game'], bg=bg, bd = 2, relief = "ridge", font = "courier 18 bold",
                        textvariable = var_user)
    entry_user.place(x = 10, y = 410, width = 595, height = 40)

    #Button
    btn_end_of_the_game = Button(main_roots['root_end_of_the_game'], text = '★', bg=bg_dark, bd = 2, relief = "ridge", fg=fg, 
                                cursor="hand2", activebackground=bg_gray, activeforeground=fg, font = "courier 18 bold",
                                command=lambda : end_of_the_game(window, var_user.get(), directory))
    btn_end_of_the_game.place(x = 620, y = 410, width = 80, height = 40)

    end_of_the_game_widgets = {
        'lbl_end_of_the_game' : lbl_end_of_the_game, 'lbl_thanks_for_playing' : lbl_thanks_for_playing,
        'lbl_user' : lbl_user, 'entry_user'  :entry_user, 'var_user' : var_user,
        'btn_end_of_the_game' : btn_end_of_the_game}

    return end_of_the_game_widgets


#Functions - Tutorial _______________________________________________________________________________________

def tutorial_roots(main_roots):
    root_hearts_foods_tut = Frame(main_roots['root_tutorial'], bg=bg_light, bd = 2, relief = 'sunken')
    root_items_world_1_tut = Frame(main_roots['root_tutorial'], bg=bg_light, bd = 2, relief = 'sunken')
    root_items_world_2_tut = Frame(main_roots['root_tutorial'], bg=bg_light, bd = 2, relief = 'sunken')
    root_items_world_3_tut = Frame(main_roots['root_tutorial'], bg=bg_light, bd = 2, relief = 'sunken')
    root_scenario_tut = Frame(main_roots['root_tutorial'], bg=bg_light, bd = 2, relief = 'sunken')
    root_txt_tut = Frame(main_roots['root_tutorial'], bg=bg_dark)
    root_text_tut = Frame(main_roots['root_tutorial'], bg=bg_light, bd = 2, relief = 'sunken')
    root_back_next_tut = Frame(main_roots['root_tutorial'], bg=bg_dark)
    root_ways_tut = Frame(main_roots['root_tutorial'], bg=bg_light, bd = 2, relief = 'sunken')

    root_txt_tut.place(x = 0, y = 0, width = 710, height = 120)
    root_back_next_tut.place(x = 0, y = 425, width = 710, height = 45)

    tutorial_roots = {
        'root_hearts_foods_tut' : root_hearts_foods_tut, 'root_items_world_1_tut' : root_items_world_1_tut,
        'root_items_world_2_tut' : root_items_world_2_tut, 'root_items_world_3_tut' : root_items_world_3_tut,
        'root_scenario_tut' : root_scenario_tut, 'root_txt_tut' : root_txt_tut, 'root_text_tut' : root_text_tut,
        'root_back_next_tut' : root_back_next_tut, 'root_ways_tut' : root_ways_tut}

    return tutorial_roots


def tutorial_widgets(window, main_roots, directory, tutorial_roots, images, version):
    global page_number_tut
    page_number_tut = 1
    #Hearts and Foods
    lbl_heart_tut = Label(tutorial_roots['root_hearts_foods_tut'], image = images['heart_11_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_value_heart_tut = Label(tutorial_roots['root_hearts_foods_tut'], text = f'100%', bg=bg, font = 'courier 13 bold', bd = 3, relief = 'ridge')
    lbl_food_tut = Label(tutorial_roots['root_hearts_foods_tut'], image = images['food_11_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_value_food_tut = Label(tutorial_roots['root_hearts_foods_tut'], text = f'8/10', bg=bg, font = 'courier 13 bold', bd = 3, relief = 'ridge')

    #Items - World 1
    lbl_item_01_tut = Label(tutorial_roots['root_items_world_1_tut'], image = images['item_lighter_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_02_tut = Label(tutorial_roots['root_items_world_1_tut'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_03_tut = Label(tutorial_roots['root_items_world_1_tut'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_key_01_tut = Label(tutorial_roots['root_items_world_1_tut'], image = images['key_B_dic'], bg=bg, bd = 3, relief = 'ridge')

    #Items - World 2
    lbl_item_04_tut = Label(tutorial_roots['root_items_world_2_tut'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_05_tut = Label(tutorial_roots['root_items_world_2_tut'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_06_tut = Label(tutorial_roots['root_items_world_2_tut'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_key_02_tut = Label(tutorial_roots['root_items_world_2_tut'], image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')

    #Items - World 3
    lbl_item_07_tut = Label(tutorial_roots['root_items_world_3_tut'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_08_tut = Label(tutorial_roots['root_items_world_3_tut'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_item_09_tut = Label(tutorial_roots['root_items_world_3_tut'], image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
    lbl_key_03_tut = Label(tutorial_roots['root_items_world_3_tut'], image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')

    #Ways
    lbl_way_01_tut = Label(tutorial_roots['root_ways_tut'], image = images['way_dic'], bg=bg_light)
    lbl_way_02_tut = Label(tutorial_roots['root_ways_tut'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_03_tut = Label(tutorial_roots['root_ways_tut'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_04_tut = Label(tutorial_roots['root_ways_tut'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_05_tut = Label(tutorial_roots['root_ways_tut'], image = images['just_way_dic'], bg=bg_light)
    lbl_way_06_tut = Label(tutorial_roots['root_ways_tut'], image = images['just_way_dic'], bg=bg_light)

    #Scenario
    lbl_scenario_tut = Label(tutorial_roots['root_scenario_tut'], image = images['scenario_01_dic'], bg=bg, anchor = CENTER)

    #TXT
    lbl_main_text_tut = Label(tutorial_roots['root_txt_tut'], bg=bg, bd = 4, relief = 'ridge', font = 'courier 16 bold')
    lbl_main_text_tut.place(x = 0, y = 0, width = 710, height = 115)

    #Texts

    var_option = StringVar()
    var_option.set('E')

    rb_option_A_tut = Radiobutton(tutorial_roots['root_text_tut'], bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2', 
                                variable = var_option, value = 'A', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
    rb_option_B_tut = Radiobutton(tutorial_roots['root_text_tut'], bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2', 
                                variable = var_option, value = 'B', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
    rb_option_C_tut = Radiobutton(tutorial_roots['root_text_tut'], bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2',
                                variable = var_option, value = 'C', activebackground=bg_gray, activeforeground=fg, justify = LEFT)

    #Back & Next
    lbl_version_in_tut = Label(tutorial_roots['root_back_next_tut'], bg=bg_dark, font = 'courier 10 bold', text = version, fg=fg)
    lbl_version_in_tut.place(x = 275, y = 5, width = 160, height = 30)

    btn_back_tut = Button(tutorial_roots['root_back_next_tut'], text = 'Retornar ao Menu', bg=bg_dark, bd = 1.5, relief = 'ridge',
                    cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                    fg=fg, command=lambda : click_tutorial_to_menu(window, main_roots, directory, tutorial_roots, tutorial_widgets))
    btn_back_tut.place(x = 0, y = 5, width = 270, height = 30)

    btn_next_tut = Button(tutorial_roots['root_back_next_tut'], text = 'Avançar', bg=bg_dark, bd = 1.5, relief = 'ridge',
                    cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                    fg=fg, command=lambda : pages_tutorial(window, tutorial_roots, tutorial_widgets, page_number_tut))
    btn_next_tut.place(x = 440, y = 5, width = 270, height = 30)


    tutorial_widgets = {
        'lbl_heart_tut' : lbl_heart_tut, 'lbl_value_heart_tut' : lbl_value_heart_tut,
        'lbl_food_tut' : lbl_food_tut, 'lbl_value_food_tut' : lbl_value_food_tut,

        'lbl_item_01_tut' : lbl_item_01_tut, 'lbl_item_02_tut' : lbl_item_02_tut,
        'lbl_item_03_tut' : lbl_item_03_tut, 'lbl_key_01_tut' : lbl_key_01_tut,

        'lbl_item_04_tut' : lbl_item_04_tut, 'lbl_item_05_tut' : lbl_item_05_tut,
        'lbl_item_06_tut' : lbl_item_06_tut, 'lbl_key_02_tut' : lbl_key_02_tut,

        'lbl_item_07_tut' : lbl_item_07_tut, 'lbl_item_08_tut' : lbl_item_08_tut,
        'lbl_item_09_tut' : lbl_item_09_tut, 'lbl_key_03_tut' : lbl_key_03_tut,

        'lbl_way_01_tut' : lbl_way_01_tut, 'lbl_way_02_tut' : lbl_way_02_tut,
        'lbl_way_03_tut' : lbl_way_03_tut, 'lbl_way_04_tut' : lbl_way_04_tut,
        'lbl_way_05_tut' : lbl_way_05_tut, 'lbl_way_06_tut' : lbl_way_06_tut,

        'lbl_scenario_tut' : lbl_scenario_tut, 'lbl_main_text_tut' : lbl_main_text_tut,

        'rb_option_A_tut' : rb_option_A_tut, 'rb_option_B_tut' : rb_option_B_tut,
        'rb_option_C_tut' : rb_option_C_tut, 'lbl_version_in_tut' : lbl_version_in_tut,
        'btn_back_tut' : btn_back_tut, 'btn_next_tut' : btn_next_tut,
        
        'var_option' : var_option}

    return tutorial_widgets


def click_tutorial_to_menu(window, main_roots, directory, tutorial_roots, tutorial_widgets):
    global page_number_tut
    page_number_tut = 1
    tutorial_widgets['var_option'].set('E')
    show_tutorial(tutorial_widgets, page=0)

    #Window
    window.title('Main Menu')
    window.iconbitmap(directory + '/Assets/Icons/icon_01.ico')

    #Tutorial Roots
    tutorial_roots['root_hearts_foods_tut'].place_forget()
    tutorial_roots['root_items_world_1_tut'].place_forget()
    tutorial_roots['root_items_world_2_tut'].place_forget()
    tutorial_roots['root_items_world_3_tut'].place_forget()
    tutorial_roots['root_ways_tut'].place_forget()
    tutorial_roots['root_scenario_tut'].place_forget()
    tutorial_roots['root_text_tut'].place_forget()

    #Tutorial Widgets
    tutorial_widgets['lbl_heart_tut'].place_forget()
    tutorial_widgets['lbl_value_heart_tut'].place_forget()
    tutorial_widgets['lbl_food_tut'].place_forget()
    tutorial_widgets['lbl_value_food_tut'].place_forget()

    tutorial_widgets['lbl_item_01_tut'].place_forget()
    tutorial_widgets['lbl_item_02_tut'].place_forget()
    tutorial_widgets['lbl_item_03_tut'].place_forget()
    tutorial_widgets['lbl_key_01_tut'].place_forget()

    tutorial_widgets['lbl_item_04_tut'].place_forget()
    tutorial_widgets['lbl_item_05_tut'].place_forget()
    tutorial_widgets['lbl_item_06_tut'].place_forget()
    tutorial_widgets['lbl_key_02_tut'].place_forget()

    tutorial_widgets['lbl_item_07_tut'].place_forget()
    tutorial_widgets['lbl_item_08_tut'].place_forget()
    tutorial_widgets['lbl_item_09_tut'].place_forget()
    tutorial_widgets['lbl_key_03_tut'].place_forget()

    tutorial_widgets['lbl_way_01_tut'].place_forget()
    tutorial_widgets['lbl_way_02_tut'].place_forget()
    tutorial_widgets['lbl_way_03_tut'].place_forget()
    tutorial_widgets['lbl_way_04_tut'].place_forget()
    tutorial_widgets['lbl_way_05_tut'].place_forget()
    tutorial_widgets['lbl_way_06_tut'].place_forget()

    tutorial_widgets['lbl_scenario_tut'].place_forget()
    tutorial_widgets['rb_option_A_tut'].place_forget()
    tutorial_widgets['rb_option_B_tut'].place_forget()
    tutorial_widgets['rb_option_C_tut'].place_forget()
    
    #Main
    main_roots['root_tutorial'].place_forget()
    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)


#Functions - History  _______________________________________________________________________________________

def history_widgets(window, main_roots, directory, version):
    global page_number_his
    page_number_his = 0
    #Labels
    lbl_his_main = Label(main_roots['root_history'], text = '- Introdução -', bg=bg, font = 'courier 40 bold')
    lbl_his_main.place(x = 5, y = 5, width = 700, height = 115)

    lbl_his_text = Label(main_roots['root_history'], text = '', bg=bg, bd = 5, relief = 'solid', font = 'courier 22 italic')
    lbl_his_text.place(x = -5, y = 125, width = 720, height = 305)

    lbl_his_version = Label(main_roots['root_history'], text = version, bg=bg, font = 'courier 10 bold')
    lbl_his_version.place(x = 275, y = 430, width = 160, height = 30)

    #Buttons
    btn_his_next = Button(main_roots['root_history'], text= 'Voltar', bg=bg, bd = 2.5, relief = 'ridge', cursor='hand2',
                    font = 'courier 14 bold', activebackground=bg_gray, activeforeground=fg,
                    command=lambda : pages_history(window, main_roots, directory, page_number_his, 'back', history_widgets))
    #btn_his_next.place(x = 0, y = 430, width = 270, height = 30)

    btn_his_back = Button(main_roots['root_history'], text= 'Próximo', bg=bg, bd = 2.5, relief = 'ridge', cursor='hand2',
                    font = 'courier 14 bold', activebackground=bg_gray, activeforeground=fg,
                    command=lambda : pages_history(window, main_roots, directory, page_number_his, 'next', history_widgets))
    btn_his_back.place(x = 440, y = 430, width = 270, height = 30)

    history_widgets = {
        'lbl_his_main' : lbl_his_main, 'lbl_his_text' : lbl_his_text, 'lbl_his_version' : lbl_his_version,
        'btn_his_next' : btn_his_next, 'btn_his_back' : btn_his_back}

    return history_widgets


def click_his_to_menu(window, main_roots, directory):
    global page_number_his
    page_number_his = 0

    window.title('Main Menu')
    window.iconbitmap(directory + '/Assets/Icons/icon_01.ico')

    main_roots['root_history'].place_forget()
    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)


#Others Functions ___________________________________________________________________________________________

def pages_tutorial(window, tutorial_roots, tutorial_widgets , page):
    global page_number_tut
    page_number_tut += 1

    show_tutorial(tutorial_widgets , page)
    tutorial_widgets['btn_next_tut']['text'] = '...'
    if page == 1:
        #Root
        tutorial_roots['root_hearts_foods_tut'].place(x = 5, y = 125, width = 260, height = 45)
        wait(window)

        #Labels
        tutorial_widgets['lbl_heart_tut'].place(x = 2.5, y = 2.5, width = 35, height = 32.5)
        wait(window)

        tutorial_widgets['lbl_value_heart_tut'].place(x = 35, y = 2.5, width = 90, height = 32.5)
        wait(window)

        tutorial_widgets['lbl_food_tut'].place(x = 127.5, y = 2.5, width = 35, height = 32.5)
        wait(window)

        tutorial_widgets['lbl_value_food_tut'].place(x = 160, y = 2.5, width = 90, height = 32.5)

    elif page == 2:
        #Roots
        tutorial_roots['root_items_world_1_tut'].place(x = 5, y = 175, width = 85, height = 85)
        wait(window)

        tutorial_roots['root_items_world_2_tut'].place(x = 92.5, y = 175, width = 85, height = 85)
        wait(window)

        tutorial_roots['root_items_world_3_tut'].place(x = 180, y = 175, width = 85, height = 85)
        wait(window)

        #Labels
        tutorial_widgets['lbl_item_01_tut'].place(x = 3, y = 3, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_item_02_tut'].place(x = 43, y = 3, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_item_03_tut'].place(x = 43, y = 43, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_key_01_tut'].place(x = 3, y = 43, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_item_04_tut'].place(x = 3, y = 3, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_item_05_tut'].place(x = 43, y = 3, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_item_06_tut'].place(x = 43, y = 43, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_key_02_tut'].place(x = 3, y = 43, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_item_07_tut'].place(x = 3, y = 3, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_item_08_tut'].place(x = 43, y = 3, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_item_09_tut'].place(x = 43, y = 43, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_key_03_tut'].place(x = 3, y = 43, width = 35, height = 35)
        
    elif page == 3:
        #Root
        tutorial_roots['root_ways_tut'].place(x = 5, y = 265, width = 260, height = 40)
        wait(window)

        #Labels
        tutorial_widgets['lbl_way_01_tut'].place(x = 7.5, y = 0, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_way_02_tut'].place(x = 47.5, y = 0, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_way_03_tut'].place(x = 87.5, y = 0, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_way_04_tut'].place(x = 127.5, y = 0, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_way_05_tut'].place(x = 167.5, y = 0, width = 35, height = 35)
        wait(window)

        tutorial_widgets['lbl_way_06_tut'].place(x = 207.5, y = 0, width = 35, height = 35)

    elif page == 4:
        #Root
        tutorial_roots['root_scenario_tut'].place(x = 5 , y = 310, width = 260, height = 110)
        wait(window)
        #Label
        tutorial_widgets['lbl_scenario_tut'].place(x = 3, y = 3, width= 250, height = 100)

    elif page == 5:
        #Root
        tutorial_roots['root_text_tut'].place(x = 270, y = 125, width = 435, height = 295)
        wait(window)

        #RadioButtons
        tutorial_widgets['rb_option_A_tut'].place(x = 5, y = 5, width = 420, height = 90)
        wait(window)

        tutorial_widgets['rb_option_B_tut'].place(x = 5, y = 100, width = 420, height = 90)
        wait(window)

        tutorial_widgets['rb_option_C_tut'].place(x = 5, y = 195, width = 420, height = 90)

    elif page == 6:
        page_number_tut = 6
        tutorial_widgets['btn_next_tut'].place_forget()

    tutorial_widgets['btn_next_tut']['text'] = 'Avançar'


def pages_history(window, main_roots, directory, page, action, history_widgets):
    global page_number_his
    global items_values
    if action == 'next':
        page_number_his += 1
        page = page_number_his
    elif action == 'back':
        page_number_his -= 1
        page = page_number_his

    if page <= 0:
        history_widgets['btn_his_next'].place_forget()
    elif page == 1:
        history_widgets['btn_his_next'].place(x = 0, y = 430, width = 270, height = 30)

    if items_values['world'] == 1 and page == 5:
        page_number_his = 0
        #Sound
        soundtrack(directory, vol = vol, soundtrack = 1)

        #Window
        window.title(f'Level {items_values["world"]}-{items_values["level"]}')

        #History
        history_widgets['btn_his_next'].place_forget()

        #Main_roots
        main_roots['root_history'].place_forget()

    elif items_values['world'] == 2 and page == 4:
        page_number_his = 0
        #Sound
        soundtrack(directory, vol = vol, soundtrack = 2)

        #Window
        window.title(f'Level {items_values["world"]}-{items_values["level"]}')

        #History
        history_widgets['btn_his_next'].place_forget()

        #Main_roots
        main_roots['root_history'].place_forget()

    elif items_values['world'] == 3 and page == 5:
        page_number_his = 0
        #Sound
        soundtrack(directory, vol = vol, soundtrack = 3)

        #Window
        window.title(f'Level {items_values["world"]}-{items_values["level"]}')

        #History
        history_widgets['btn_his_next'].place_forget()

        #Main_roots
        main_roots['root_history'].place_forget()

    elif items_values['world'] == 4 and page == 2:
        page_number_his = 0
        #Sound
        soundtrack(directory, vol = vol, soundtrack = 3)

        #Window
        window.title(f'Level {items_values["world"]}-{items_values["level"]}')

        #History
        history_widgets['btn_his_next'].place_forget()

        #Main_roots
        main_roots['root_history'].place_forget()

    show_history(history_widgets, page, items_values['world'])


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
    options_widgets['lbl_vol'].configure(text = text_vol)


def random_number():
    return randint(1,4)


def wait(window, time = 0.5):
    window.update()
    sleep(time)


def end_of_the_game(window, user, directory):
    global vol
    if vol != 0:
        voice_over(directory, msg = f'{user}, Muito obrigado por jogar!')
    window.destroy()

