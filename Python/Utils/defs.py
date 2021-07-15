#Import - Libraries _________________________________________________________________________________________

from tkinter import *
from tkinter import messagebox

#Variables __________________________________________________________________________________________________

bg = fg = '#fefefe'
bg_light = '#e1e1e1'
bg_gray = '#545454'
bg_dark = '#000'

#Main Functions _____________________________________________________________________________________________

def main_roots(window):
    root_play_game = Frame(window, bg=bg)
    root_main_menu = Frame(window, bg=bg)
    root_game_over = Frame(window, bg=bg)
    root_credits = Frame(window, bg=bg)

    main_roots = {
        'root_play_game' : root_play_game, 'root_main_menu' : root_main_menu, 'root_game_over' : root_game_over,
        'root_credits' : root_credits}

    return main_roots

#Functions - Internals _______________________________________________________________________________________

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

    #Music


    #Scenario
    game_widgets['lbl_scenario']['image'] = images['scenario_01_dic']

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

        elif 25 >= items_values['heart'] >= 0: #25 - 0
            game_widgets['lbl_heart']['image'] = images['heart_00_dic']

        game_widgets['lbl_value_heart']['text'] = f'{items_values["heart"]}%'
    
    def food():
        if items_values["food"] >= 10:
            items_values["food"] = 10

        if 10 >= items_values['food'] > 7.5: #10 - 7.5
            game_widgets['lbl_food']['image'] = images['food_11_dic']

        elif 7.5 >= items_values['food'] > 2.5: #7.5 - 2.5
            game_widgets['lbl_food']['image'] = images['food_01_dic']

        elif 2.5 >= items_values['food'] >= 0: #2.5 - 0
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

#Game & Credits
def click_next_level(window, var_option, images, game_widgets):
    global items_values
    if var_option.get() not in 'ABC':
        messagebox.showerror(title = "Escolha", icon = messagebox.INFO,
        message = "Escolha uma das opções presente\npara poder continuar.")

    else:
        var_option.set('E')
        items_values['level'] += 1

        if items_values['level'] > 6:
            items_values['level'] = 1
            items_values['world'] += 1

            if items_values['world'] > 3:
                print('END GAME')

        show_items_values(images, game_widgets)
        window.title(f'Level {items_values["world"]}-{items_values["level"]}')

def click_back_to_menu(window, main_roots, directory):
    main_roots['root_play_game'].place_forget()
    main_roots['root_credits'].place_forget()
    window.title('Main Menu')
    window.iconbitmap(directory + '/Images/Icons/icon_01.ico')

    main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)

#Menu
def click_new_game(window, main_roots, directory, default, images, game_widgets, menu_widgets):
    ok_cancel_newgame = messagebox.askokcancel(title = "Novo Jogo", message = "Desejas Iniciar um novo Jogo?",
    detail = "Caso possua um Save anterior ele será sobrescito")
    if ok_cancel_newgame:
        default(window, images, game_widgets)
        show_items_values(images, game_widgets)

        main_roots['root_main_menu'].place_forget()
        window.title(f'Level {items_values["world"]}-{items_values["level"]}')
        window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

        main_roots['root_play_game'].place(x = 5, y = 5, width = 710, height = 710)
        menu_widgets['btn_continue'].config(cursor="hand2", activebackground=bg_gray, activeforeground=fg,
        relief = "ridge", fg='#000', command=lambda : click_continue(window, main_roots, directory))

def click_nothing():
    messagebox.showerror(title = "Continuar - Error", icon = messagebox.INFO,
    message = "Inicie um Novo Jogo para que você\npossa continuar de onde parou.")

def click_continue(window, main_roots, directory):
    global items_values
    main_roots['root_main_menu'].place_forget()
    window.title(f'Level {items_values["world"]}-{items_values["level"]}')
    window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

    main_roots['root_play_game'].place(x = 5, y = 5, width = 710, height = 460)

def click_credits(window, main_roots, directory):
    window.title('Créditos')
    window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

    main_roots['root_credits'].place(x = 5, y = 5, width = 710, height = 460)

def click_quit(window):
    ok_cancel_quit = messagebox.askokcancel(title = "Sair?", message = "Você realmente deseja sair?\t\t",
    detail = "Desde já obrigado por jogar")
    if ok_cancel_quit == True:
        window.destroy()

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

def game_widgets(window, main_roots, directory, game_roots, images, version):
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
                    fg=fg, command=lambda : click_back_to_menu(window, main_roots, directory))
    btn_back.place(x = 0, y = 5, width = 270, height = 30)

    btn_next = Button(game_roots['root_back_next'], text = 'Avançar', bg=bg_dark, bd = 1, relief = 'ridge',
                    cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                    fg=fg, command=lambda: click_next_level(window, var_option, images, game_widgets))
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
                    cursor="hand2", font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg)
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
                    command=lambda : click_back_to_menu(window, main_roots, directory),
                    cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
    btn_back.place(x = 230, y = 400, width = 250, height = 50)

    credits_widgets = {
        'lbl_credits_title' : lbl_credits_title, 'lbl_credits_version' : lbl_credits_version,
        'lbl_credits' : lbl_credits, 'btn_back' : btn_back}

    return credits_widgets
