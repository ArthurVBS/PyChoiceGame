#Import - Libraries _________________________________________________________________________________________
import os
from tkinter import *
#Import - Packages __________________________________________________________________________________________
from Utils.widgets import images
#Variables __________________________________________________________________________________________________
bg = fg = '#fefefe'
bg_light = '#e1e1e1'
bg_gray = '#545454'
bg_dark = '#000'
version = 'layout v 2.2.1'
directory = os.path.dirname(__file__)
#Tkinter ____________________________________________________________________________________________________
window = Tk()

width = 720
height = 470
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

root_play_game = Frame(window, bg=bg)
root_main_menu = Frame(window, bg=bg)
root_game_over = Frame(window, bg=bg)

window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
window.title('In search of the truth')
window.iconbitmap(directory + '/Images/Icons/icon_02.ico')
window.resizable(False,False)
window.configure(background = '#000')

images = images(directory)

def default():
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
    window.title('Level 1-1')

    #Music


    #Scenario
    lbl_scenario['image'] = images['scenario_01_dic']

    #Heart
    lbl_value_heart['text'] = '80%'
    lbl_heart['image'] = images['heart_11_dic']

    #Food
    lbl_value_food['text'] = '5/10'
    lbl_food['image'] = images['food_01_dic']

    #Keys
    lbl_key_B['image'] = images['key_B_dic']
    lbl_key_S['image'] = images['key_E_dic']
    lbl_key_G['image'] = images['key_E_dic']

    #Way
    lbl_way_01['image'] = images['way_dic']
    lbl_way_02['image'] = images['just_way_dic']
    lbl_way_03['image'] = images['just_way_dic']
    lbl_way_04['image'] = images['just_way_dic']
    lbl_way_05['image'] = images['just_way_dic']
    lbl_way_06['image'] = images['just_way_dic']

    #Items
    lbl_item_lighter['image'] = images['item_lighter_dic']
    lbl_item_future_friendship['image'] = images['empty_01_dic']
    lbl_item_wolfhide['image'] = images['empty_01_dic']
    lbl_item_shotgun['image'] = images['empty_01_dic']
    lbl_item_nausea['image'] = images['empty_01_dic']
    lbl_item_crowbar['image'] = images['empty_01_dic']
    lbl_item_screwdriver['image'] = images['empty_01_dic']
    lbl_item_gear['image'] = images['empty_01_dic']


def show_items_values():
    global items_values

    def heart():
        if items_values["heart"] >= 100:
            items_values["heart"] = 100

        if 100 >= items_values['heart'] > 75: #100 - 75
            lbl_heart['image'] = images['heart_11_dic']

        elif 75 >= items_values['heart'] > 25: #75 - 25
            lbl_heart['image'] = images['heart_01_dic']

        elif 25 >= items_values['heart'] >= 0: #25 - 0
            lbl_heart['image'] = images['heart_00_dic']

        lbl_value_heart['text'] = f'{items_values["heart"]}%'
    
    def food():
        if items_values["food"] >= 10:
            items_values["food"] = 10

        if 10 >= items_values['food'] > 7.5: #10 - 7.5
            lbl_food['image'] = images['food_11_dic']

        elif 7.5 >= items_values['food'] > 2.5: #7.5 - 2.5
            lbl_food['image'] = images['food_01_dic']

        elif 2.5 >= items_values['food'] >= 0: #2.5 - 0
            lbl_food['image'] = images['food_00_dic']

        lbl_value_food['text'] = f'{items_values["food"]}/10'

    def keys():
        lbl_key_B['image'] = images['key_E_dic']
        lbl_key_S['image'] = images['key_E_dic']
        lbl_key_G['image'] = images['key_E_dic']

        if items_values["key_B"] == True: #Bronze
            lbl_key_B['image'] = images['key_B_dic']

        if items_values["key_S"] == True: #Silver
            lbl_key_S['image'] = images['key_S_dic']

        if items_values["key_G"] == True: #Golden
            lbl_key_G['image'] = images['key_G_dic']

    def items():
        lbl_item_lighter['image'] = images['empty_01_dic']
        lbl_item_future_friendship['image'] = images['empty_01_dic']
        lbl_item_wolfhide['image'] = images['empty_01_dic']
        lbl_item_shotgun['image'] = images['empty_01_dic']
        lbl_item_nausea['image'] = images['empty_01_dic']
        lbl_item_crowbar['image'] = images['empty_01_dic']
        lbl_item_screwdriver['image'] = images['empty_01_dic']
        lbl_item_gear['image'] = images['empty_01_dic']

        if items_values['item_lighter'] == True: 
            lbl_item_lighter['image'] = images['item_lighter_dic']

        if items_values['item_future_friendship'] == True:
            lbl_item_future_friendship['image'] = images['item_future_friendship_dic']

        if items_values['item_wolfhide'] == True:
            lbl_item_wolfhide['image'] = images['item_wolfhide_dic']

        if items_values['item_shotgun'] == True:
            lbl_item_shotgun['image'] = images['item_shotgun_dic']

        if items_values['item_nausea'] == True:
            lbl_item_nausea['image'] = images['item_nausea_dic']

        if items_values['item_crowbar'] == True:
            lbl_item_crowbar['image'] = images['item_crowbar_dic']

        if items_values['item_screwdriver'] == True:
            lbl_item_screwdriver['image'] = images['item_screwdriver_dic']

        if items_values['item_gear'] == True:
            lbl_item_gear['image'] = images['item_gear_dic']
  
    def ways(): #(Level)
        if 6 >= items_values['level'] >= 1:
            lbl_way_01['image'] = images['just_way_dic']
            lbl_way_02['image'] = images['just_way_dic']
            lbl_way_03['image'] = images['just_way_dic']
            lbl_way_04['image'] = images['just_way_dic']
            lbl_way_05['image'] = images['just_way_dic']
            lbl_way_06['image'] = images['just_way_dic']

            if items_values['level'] == 1:
                lbl_way_01['image'] = images['way_dic']
            elif items_values['level'] == 2:
                lbl_way_02['image'] = images['way_dic']
            elif items_values['level'] == 3:
                lbl_way_03['image'] = images['way_dic']
            elif items_values['level'] == 4:
                lbl_way_04['image'] = images['way_dic']
            elif items_values['level'] == 5:
                lbl_way_05['image'] = images['way_dic']
            elif items_values['level'] == 6:
                lbl_way_06['image'] = images['way_dic']

        else: # LEVEL 7?! (world += 1)
            items_values['level'] = 1
            items_values['world'] += 1

    def scenario(): #(World)
        if items_values['world'] == 1:
            lbl_scenario['image'] = images['scenario_01_dic']

        elif items_values['world'] == 2:
            lbl_scenario['image'] = images['scenario_02_dic']

        elif items_values['world'] == 3:
            lbl_scenario['image'] = images['scenario_03_dic']

        else: # WORLD 4?!
            items_values['world'] = 1
            lbl_scenario['image'] = images['scenario_01_dic']

    heart()
    food()
    keys()
    items()
    ways()
    scenario()


def show(show_root):
    if show_root == 'play_game':
        root_play_game.place(x = 5, y = 5, width = width - 10, height = height - 10)

    elif show_root == 'game_over':
        root_game_over.place(x = 10, y = 10, width = width - 20, height = height - 20)

    elif show_root == 'main_menu':
        root_main_menu.place(x = 10, y = 10, width = width - 20, height = height - 20)


def clear(clear_root = 'all'):
    if clear_root == 'play_game':
        root_play_game.place_forget()

    elif clear_root == 'game_over':
        root_game_over.place_forget()

    elif clear_root == 'main_menu':
        root_main_menu.place_forget()

    else:
        root_play_game.place_forget()
        root_game_over.place_forget()
        root_main_menu.place_forget()


#Hearts and Foods

root_hearts_foods = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_hearts_foods.place(x = 5, y = 125, width = 260, height = 45)

lbl_heart = Label(root_hearts_foods, image = images['heart_11_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_heart.place(x = 2.5, y = 2.5, width = 35, height = 32.5)

lbl_value_heart = Label(root_hearts_foods, text = f'100%', bg=bg, font = 'courier 13 bold', bd = 3, relief = 'ridge')
lbl_value_heart.place(x = 35, y = 2.5, width = 90, height = 32.5)

lbl_food = Label(root_hearts_foods, image = images['food_11_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_food.place(x = 127.5, y = 2.5, width = 35, height = 32.5)

lbl_value_food = Label(root_hearts_foods, text = f'9/10', bg=bg, font = 'courier 13 bold', bd = 3, relief = 'ridge')
lbl_value_food.place(x = 160, y = 2.5, width = 90, height = 32.5)

#Items - World 1

root_items_world_1 = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_items_world_1.place(x = 5, y = 175, width = 85, height = 85)

lbl_item_lighter = Label(root_items_world_1, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_wolfhide = Label(root_items_world_1, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_future_friendship = Label(root_items_world_1, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_key_B = Label(root_items_world_1, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')

lbl_item_lighter.place(x = 3, y = 3, width = 35, height = 35)
lbl_item_wolfhide.place(x = 43, y = 3, width = 35, height = 35)
lbl_item_future_friendship.place(x = 43, y = 43, width = 35, height = 35)
lbl_key_B.place(x = 3, y = 43, width = 35, height = 35)

#Items - World 2

root_items_world_2 = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_items_world_2.place(x = 92.5, y = 175, width = 85, height = 85)

lbl_item_shotgun = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_nausea = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_crowbar = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_key_S = Label(root_items_world_2, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')

lbl_item_shotgun.place(x = 3, y = 3, width = 35, height = 35)
lbl_item_nausea.place(x = 43, y = 3, width = 35, height = 35)
lbl_item_crowbar.place(x = 43, y = 43, width = 35, height = 35)
lbl_key_S.place(x = 3, y = 43, width = 35, height = 35)

#Items - World 3

root_items_world_3 = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_items_world_3.place(x = 180, y = 175, width = 85, height = 85)

lbl_item_screwdriver = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_gear = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_unknown = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_key_G = Label(root_items_world_3, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')

lbl_item_screwdriver.place(x = 3, y = 3, width = 35, height = 35)
lbl_item_gear.place(x = 43, y = 3, width = 35, height = 35)
lbl_unknown.place(x = 43, y = 43, width = 35, height = 35)
lbl_key_G.place(x = 3, y = 43, width = 35, height = 35)

#Scenario

root_scenario = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_scenario.place(x = 5 , y = 310, width = 260, height = 110)

lbl_scenario = Label(root_scenario, image = images['empty_00_dic'], bg=bg, anchor = CENTER)
lbl_scenario.place(x = 3, y = 3, width= 250, height = 100)#250x100

#TXT

root_txt = Frame(root_play_game, bg=bg_dark)
root_txt.place(x = 0, y = 0, width = 710, height = 120)

lbl_main_text = Label(root_txt, text = 'Texto principal', bg=bg, justify= LEFT,
                    font = 'courier 16 bold', bd = 4, relief = 'ridge')
lbl_main_text.place(x = 0, y = 0, width = 710, height = 115)

lbl_main_text['text'] = 'Você está caminhando a um certo tempo, o seu\n' +\
                        'estômago ronca. Você encontra algumas frutinhas\n' +\
                        'azuis em um arbusto que podem ser comestíveis.'

#Texts

root_text = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_text.place(x = 270, y = 125, width = 435, height = 295)

var_option = StringVar()
var_option.set('E')

rb_option_A = Radiobutton(root_text, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2', 
                            variable = var_option, value = 'A', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
rb_option_A.place(x = 5, y = 5, width = 420, height = 90)

rb_option_B = Radiobutton(root_text, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2', 
                            variable = var_option, value = 'B', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
rb_option_B.place(x = 5, y = 100, width = 420, height = 90)

rb_option_C = Radiobutton(root_text, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2',
                            variable = var_option, value = 'C', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
rb_option_C.place(x = 5, y = 195, width = 420, height = 90)

rb_option_A['text'] = 'Pegar as frutinhas do arbusto e\nsaciar a sua fome;'
rb_option_B['text'] = 'Ignorar as frutinhas e seguir em\nfrente;'
rb_option_C['text'] = 'Pegar alguma comida da mochila;'

#Back & Next

root_back_next = Frame(root_play_game, bg=bg_dark)
root_back_next.place(x = 0, y = 425, width = 710, height = 45)

lbl_version_in_game = Label(root_back_next, bg=bg_dark, font = 'courier 10 bold', text = version, fg=fg)
lbl_version_in_game.place(x = 275, y = 5, width = 160, height = 30)

btn_back = Button(root_back_next, text = 'Retornar ao Menu', bg=bg_dark, bd = 1.5, relief = 'ridge', cursor='hand2',
                font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light, fg=fg)
btn_back.place(x = 0, y = 5, width = 270, height = 30)

btn_next = Button(root_back_next, text = 'Avançar', bg=bg_dark, bd = 1, relief = 'ridge', cursor='hand2',
                font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light, fg=fg)
btn_next.place(x = 440, y = 5, width = 270, height = 30)

#Ways

root_ways = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_ways.place(x = 5, y = 265, width = 260, height = 40)

lbl_way_01 = Label(root_ways, image = images['just_way_dic'], bg=bg_light)
lbl_way_01.place(x = 7.5, y = 0, width = 35, height = 35)

lbl_way_02 = Label(root_ways, image = images['just_way_dic'], bg=bg_light)
lbl_way_02.place(x = 47.5, y = 0, width = 35, height = 35)

lbl_way_03 = Label(root_ways, image = images['just_way_dic'], bg=bg_light)
lbl_way_03.place(x = 87.5, y = 0, width = 35, height = 35)

lbl_way_04 = Label(root_ways, image = images['just_way_dic'], bg=bg_light)
lbl_way_04.place(x = 127.5, y = 0, width = 35, height = 35)

lbl_way_05 = Label(root_ways, image = images['just_way_dic'], bg=bg_light)
lbl_way_05.place(x = 167.5, y = 0, width = 35, height = 35)

lbl_way_06 = Label(root_ways, image = images['just_way_dic'], bg=bg_light)
lbl_way_06.place(x = 207.5, y = 0, width = 35, height = 35)

#default

if var_option.get() == 'E':
    print('Selecione uma das opções para seguir!!!')

default()
show_items_values()
show('play_game')

window.mainloop()
