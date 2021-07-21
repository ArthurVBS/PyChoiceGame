import os
from tkinter import *

from time import sleep
from Utils.widgets import images

bg = fg = '#fefefe'
bg_light = '#e1e1e1'
bg_gray = '#545454'
bg_dark = '#000'
title = 'w-l (op)'
directory = os.path.dirname(__file__)

txt_result = 'hi'
losewin_heart = 0
losewin_food = 0

def toplevel_result(directory, images, title, txt_result, losewin_heart, losewin_food):
    win_toplevel = Tk()

    width = 720
    height = 470
    width_screen = win_toplevel.winfo_screenwidth()
    height_screen = win_toplevel.winfo_screenheight()
    pos_x = int(width_screen / 2 - width / 2)
    pos_y = int(height_screen / 2 - height / 2)

    root_result = Frame(win_toplevel, bg=bg_light)
    root_result.place(x = 5, y = 5, width = 360, height = 310)
    images = images(directory)

    win_toplevel.geometry(f"370x320+{pos_x + 200}+{pos_y + 100}")
    win_toplevel.title(title)
    win_toplevel.resizable(False, False)
    win_toplevel.iconbitmap(directory + "/Images/Icons/icon_02.ico")
    win_toplevel.configure(background = '#000')
    win_toplevel.update()
    sleep(0.5)

    #Text
    lbl_result_title = Label(root_result, text = "A sua escolha ocasionou:", bg=bg_light, font = "courier 16 bold", justify=CENTER)
    lbl_result_title.place(x = 5, y = 5, width = 350, height = 40)

    win_toplevel.update()
    sleep(0.8)

    lbl_result_subtitle = Label(root_result, text = txt_result, bg=bg_light, font = "courier 16 bold", justify=CENTER, relief='sunken', bd=1.5)
    lbl_result_subtitle.place(x = 5, y = 50, width = 350, height = 165)

    win_toplevel.update()
    sleep(2)

    #Roots
    root_result_heart = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')
    root_result_heart.place(x = 5, y = 220, width = 115, height = 50)

    win_toplevel.update()
    sleep(0.3)

    root_result_items = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')
    root_result_items.place(x = 122.5, y = 220, width = 115, height = 50)

    win_toplevel.update()
    sleep(0.3)

    root_result_food = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')
    root_result_food.place(x = 240, y = 220, width = 115, height = 50)

    win_toplevel.update()
    sleep(0.5)

    #Heart
    if losewin_heart <= 0:
        pos_neg_heart = ''
    elif losewin_heart > 0:
        pos_neg_heart = '+'

    lbl_img_heart = Label(root_result_heart, bg=bg_light, image = images['heart_11_dic'])
    lbl_img_heart.place(x = 5, y = 5, width = 40, height = 40)

    win_toplevel.update()
    sleep(0.5)

    lbl_value_heart = Label(root_result_heart, bg=bg_light, font = "courier 14 bold",
                            text = f'{pos_neg_heart}{losewin_heart}% ')
    lbl_value_heart.place(x = 45, y = 5, width = 65, height= 40)

    win_toplevel.update()
    sleep(0.5)

    #Items
    lbl_value_item = Label(root_result_items, bg=bg_light, text = '+', font = "courier 14 bold")
    lbl_value_item.place(x = 5, y = 5, width = 25, height= 40)

    win_toplevel.update()
    sleep(0.5)

    lbl_img_item_01 = Label(root_result_items, bg=bg_light, image = images['item_lighter_dic'])
    lbl_img_item_01.place(x = 30, y = 5, width = 40, height = 40)

    win_toplevel.update()
    sleep(0.5)

    lbl_img_item_02 = Label(root_result_items, bg=bg_light, image = images['key_S_dic'])
    lbl_img_item_02.place(x = 70, y = 5, width = 40, height= 40)

    win_toplevel.update()
    sleep(0.5)

    #Food
    if losewin_food <= 0:
        pos_neg_food = ''
    elif losewin_food> 0:
        pos_neg_food = '+'

    lbl_img_food = Label(root_result_food, bg=bg_light, image = images['food_11_dic'])
    lbl_img_food.place(x = 5, y = 5, width = 40, height = 40)
    win_toplevel.update()

    sleep(0.5)

    lbl_value_food = Label(root_result_food, bg=bg_light, font = "courier 14 bold",
                            text = f'{pos_neg_food}{losewin_food}/10')
    lbl_value_food.place(x = 45, y = 5, width = 65, height= 40)

    win_toplevel.update()
    sleep(0.5)

    #Button
    lbl_bg_dark = Label(root_result, bg=bg_dark)
    lbl_bg_dark.place(x = 0, y = 275, width = 360, height = 35)

    btn_result_next = Button(root_result, text = 'Avançar', bg=bg_dark, bd = 1, relief = 'ridge',
                    cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                    fg=fg)
    btn_result_next.place(x = 95, y = 280, width = 175, height = 30)


    win_toplevel.mainloop()

toplevel_result(directory, images, title, txt_result, losewin_heart, losewin_food)


'''window.title('Level {world}-{level} ({option})')
window.geometry(f'370x320+{pos_x + 200}+{pos_y + 50}')
window.update()

txt_result = 'hi'
losewin_heart = '20'
positive_negative_heart = '-'
losewin_food = '2'
positive_negative_food = '+'

sleep(0.5)
#Text
lbl_result_title = Label(root_result, text = "A sua escolha ocasionou:", bg=bg_light, font = "courier 16 bold", justify=CENTER)
lbl_result_title.place(x = 5, y = 5, width = 350, height = 40)

window.update()
sleep(1)
window.update()

lbl_result_subtitle = Label(root_result, text = txt_result, bg=bg_light, font = "courier 16 bold", justify=CENTER, relief='sunken', bd=1.5)
lbl_result_subtitle.place(x = 5, y = 50, width = 350, height = 165)

window.update()
sleep(2.5)
window.update()

#Heart
root_result_heart = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')
root_result_heart.place(x = 5, y = 220, width = 115, height = 50)

lbl_img_heart = Label(root_result_heart, bg=bg_light, image = images['heart_11_dic'])
lbl_img_heart.place(x = 5, y = 5, width = 40, height = 40)

lbl_value_heart = Label(root_result_heart, bg=bg_light, font = "courier 14 bold",
                        text = f'{positive_negative_heart}{losewin_heart}% ')
lbl_value_heart.place(x = 45, y = 5, width = 65, height= 40)

window.update()
sleep(0.5)
window.update()

#Items
root_result_items = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')
root_result_items.place(x = 122.5, y = 220, width = 115, height = 50)

lbl_value_item = Label(root_result_items, bg=bg_light, text = '+', font = "courier 14 bold")
lbl_value_item.place(x = 5, y = 5, width = 25, height= 40)

lbl_img_item_01 = Label(root_result_items, bg=bg_light, image = images['item_lighter_dic'])
lbl_img_item_01.place(x = 30, y = 5, width = 40, height = 40)

lbl_img_item_02 = Label(root_result_items, bg=bg_light, image = images['key_S_dic'])
lbl_img_item_02.place(x = 70, y = 5, width = 40, height= 40)


window.update()
sleep(0.5)
window.update()

#Food
root_result_food = Frame(root_result, bg=bg_light, bd=1.5, relief='sunken')

root_result_food.place(x = 240, y = 220, width = 115, height = 50)

lbl_img_food = Label(root_result_food, bg=bg_light, image = images['food_11_dic'])
lbl_img_food.place(x = 5, y = 5, width = 40, height = 40)

lbl_value_food = Label(root_result_food, bg=bg_light, font = "courier 14 bold",
                        text = f'{positive_negative_food}{losewin_food}/10')
lbl_value_food.place(x = 45, y = 5, width = 65, height= 40)

window.update()
sleep(0.5)
window.update()

#Button
lbl_bg_dark = Label(root_result, bg=bg_dark)
lbl_bg_dark.place(x = 0, y = 275, width = 360, height = 35)

btn_result_next = Button(root_result, text = 'Avançar', bg=bg_dark, bd = 1, relief = 'ridge',
                cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                fg=fg)
btn_result_next.place(x = 95, y = 280, width = 175, height = 30)
'''

'''
window.title('Game Over')

root_game_over = Frame(window, bg=bg_dark)
root_game_over.place(x = 5, y = 5, width = 710, height = 460)

#Labels
lbl_gameover_title = Label(root_game_over, text = '- Game Over -', bg=bg_dark, font = 'courier 50 bold', justify=CENTER, fg=fg)
lbl_gameover_title.place(x = 5, y = 5, width = 700, height = 100)

lbl_try_again = Label(root_game_over, text = 'Tente Novamente', bg=bg_dark, font = 'courier 26 bold', justify=CENTER, fg=fg)
lbl_try_again.place(x = 5, y = 115, width = 700, height = 100)

#Buttons
btn_gameover_back = Button(root_game_over, text = 'Voltar', bg=bg_dark, bd = 2, relief = "ridge", fg=fg,
                    cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
btn_gameover_back.place(x = 225, y = 400, width = 260, height = 50)
'''

'''root_options = Frame(window, bg=bg)
root_options.place(x = 5, y = 5, width = 710, height = 460)

#Labels
lbl_options_title =  Label(root_options, text = " - Ajustes - ", bg=bg, font = "courier 40 bold", justify=CENTER)
lbl_options_title.place(x = 5, y = 5, width = 700, height = 100)

lbl_volume = Label(root_options, text = " -> Volume <- ", bg=bg, font = "courier 32 bold")
lbl_volume.place(x = 5, y = 85, width = 350, height = 65)

lbl_language = Label(root_options, text = " -> Idioma <- ", bg=bg, font = "courier 32 bold")
lbl_language.place(x = 355, y = 85, width = 350, height = 65)

lbl_flag_UK = Label(root_options, image = images['flag_UK_dic'], bg=bg)
lbl_flag_UK.place(x = 370, y = 160, width = 50, height = 50)

lbl_flag_FR = Label(root_options, image = images['flag_FR_dic'], bg=bg)
lbl_flag_FR.place(x = 370, y = 220, width = 50, height = 50)

lbl_flag_BR = Label(root_options, image = images['flag_BR_dic'], bg=bg)
lbl_flag_BR.place(x = 370, y = 280, width = 50, height = 50)

lbl_flag_SP = Label(root_options, image = images['flag_SP_dic'], bg=bg)
lbl_flag_SP.place(x = 370, y = 340, width = 50, height = 50)

lbl_flag_GE = Label(root_options, image = images['flag_GE_dic'], bg=bg)
lbl_flag_GE.place(x = 370, y = 400, width = 50, height = 50)


#RadioButtons
var_language = StringVar()
var_language.set("BR")

rb_lan_UK = Radiobutton(root_options, text = "English", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
            variable = var_language, value = "UK", bd=5, cursor="hand2")
rb_lan_UK.place(x = 430, y = 160, width = 205, height = 50)

rb_lan_FR = Radiobutton(root_options, text = "Français", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
            variable = var_language, value = "FR", bd=5, cursor="hand2")
rb_lan_FR.place(x = 430, y = 220, width = 205, height = 50)

rb_lan_BR = Radiobutton(root_options, text = "Português", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#000",
            variable = var_language, value = "BR", bd=5, cursor="hand2")
rb_lan_BR.place(x = 430, y = 280, width = 205, height = 50)

rb_lan_SP = Radiobutton(root_options, text = "Español", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
            variable = var_language, value = "SP", bd=5, cursor="hand2")
rb_lan_SP.place(x = 430, y = 340, width = 205, height = 50)

rb_lan_GE = Radiobutton(root_options, text = "Deutsch", bg=bg, font = "courier 18 bold", indicatoron=0, fg = "#888",
            variable = var_language, value = "GE", bd=5, cursor="hand2")
rb_lan_GE.place(x = 430, y = 400, width = 205, height = 50)

#Buttons

btn_vol_max = Button(root_options, image = images['vol_max_dic'], bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", activebackground="#ccc", activeforeground=fg, command= lambda: volume("max"))
btn_vol_max.place(x = 270, y = 320, width = 75, height = 70)

btn_vol_plus = Button(root_options, image = images['vol_plus_dic'], bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", activebackground="#ccc", activeforeground=fg, command= lambda: volume("plus"))
btn_vol_plus.place(x = 185, y = 320, width = 75, height = 70)

btn_vol_minus = Button(root_options, image = images['vol_minus_dic'], bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", activebackground="#ccc", activeforeground=fg, command= lambda: volume("minus"))
btn_vol_minus.place(x = 97.5, y = 320, width = 75, height = 70)

btn_vol_mute = Button(root_options, image = images['vol_mute_dic'], bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", activebackground="#ccc", activeforeground=fg, command= lambda: volume("mute"))
btn_vol_mute.place(x = 10, y = 320, width = 75, height = 70)

btn_back = Button(root_options, text = 'Voltar', bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
btn_back.place(x = 10, y = 400, width = 335, height = 50)

#ProgressBar

def volume(option):
    global vol

    if option == "max":
        vol = round(mixer_pm(vol = 1, plus_or_minus = "plus"), 2)
    elif option == "plus":
        vol = round(mixer_pm(vol, plus_or_minus = "plus"), 2)
    elif option == "minus":
        vol = round(mixer_pm(vol, plus_or_minus = "minus"), 2)
    elif option == "mute":
        vol = round(mixer_pm(vol = 0, plus_or_minus = "minus"), 2)

    vol_pb()

def vol_pb():
    global vol
    var_progressBar = DoubleVar()
    var_progressBar.set(vol)
    text_vol = f'{vol*100:.1f}%'

    pb_vol.configure(variable = var_progressBar)
    pb_vol.place(x = 10 , y = 160, width = 335, height = 40)

    lbl_vol.configure(text = text_vol)
    lbl_vol.place(x = 10, y = 205, width = 335, height = 30)

var_progressBar = DoubleVar()
var_progressBar.set(0.5)
vol = 0.5

pb_vol = ttk.Progressbar(root_options, variable = var_progressBar, maximum = 1)
pb_vol.place(x = 10 , y = 160, width = 335, height = 40)

lbl_vol = Label(root_options, text = f'{vol*100:.1f}%', bg=bg, font = "courier 16 bold")
lbl_vol.place(x = 10, y = 205, width = 335, height = 30)'''


'''btn_lan_up = Button(root_options, text= "up", bg=bg, bd = 2, relief = "ridge", cursor="hand2",
                    font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg)
btn_lan_up.place(x = 500, y = 160, width = 95, height = 45)

btn_lan_down = Button(root_options, text= "down", bg=bg, bd = 2, relief = "ridge", cursor="hand2",
                    font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg)
btn_lan_down.place(x = 500, y = 410, width = 95, height = 45)


lbl_lan = Label(root_options, text = 'x', bg=bg, font = 'courier 20 bold')
lbl_lan.place(x = 430, y = 325, width = 225, height = 50)

lbl_lan_flag = Label(root_options, image = images['flag_BR_dic'], bg=bg, font = 'courier 20 bold')
lbl_lan_flag.place(x = 500, y = 285, width = 50, height = 50)'''

'''
#Window

window.title('Main Menu')
window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

#Labels
lbl_title = Label(root_main_menu, text = " - In search - \n of the truth ", bg=bg, font = "courier 40 bold", justify=CENTER)
lbl_title.place(x = 5, y = 5, width = 700, height = 140)

lbl_version = Label(root_main_menu, text = version, bg=bg, font = "courier 10 bold", anchor = SE)
lbl_version.place(x = 575, y = 425, width = 125, height = 25)

#Buttons
btn_newgame = Button(root_main_menu, text= "Novo jogo", bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg)
btn_newgame.place(x = 230, y = 160, width = 250, height = 50)


btn_continue = Button(root_main_menu, text= "Continuar", bg=bg, bd = 2, relief = "flat", 
                cursor="arrow", font = "courier 25 bold", fg = "#ccc")
btn_continue.place(x = 230, y = 220, width = 250, height = 50)


btn_options = Button(root_main_menu, text = 'Ajustes',  bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg)
btn_options.place(x = 230, y = 280, width = 250, height = 50)


btn_credits = Button(root_main_menu, text= "Créditos", bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg)
btn_credits.place(x = 230, y = 340, width = 250, height = 50)


btn_quit = Button(root_main_menu, text= "Sair", bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", font = "courier 25 bold", activebackground=bg_gray, activeforeground=fg)
btn_quit.place(x = 230, y = 400, width = 250, height = 50)
'''


'''
#Window
window.title('Créditos')
window.iconbitmap(directory + '/Images/Icons/icon_02.ico')

#Labels
lbl_game_over_title = Label(root_credits, text = ' - In search - \n of the truth ', bg=bg, font = 'courier 40 bold', justify=CENTER)
lbl_game_over_title.place(x = 5, y = 5, width = 700, height = 140)

lbl_credits_version = Label(root_credits, text = version, bg=bg, font = 'courier 10 bold', anchor = SE)
lbl_credits_version.place(x = 575, y = 425, width = 125, height = 25)

lbl_credits = Label(root_credits, font = 'courier 20 italic', text='Aluno: Arthur Vinícius Bezerra da Silva\n' +\
                    'Curso: ADS - IFPE - 1º período - 2021.1\n\nInício: 2021.05.31      Fim: 2021.--.--\n', bg=bg)
lbl_credits.place(x = 5, y = 145, width = 700, height = 210)

#Buttons
btn_back = Button(root_credits, text = 'Voltar', bg=bg, bd = 2, relief = "ridge",
                cursor="hand2", font = "courier 25 bold", activebackground="#ccc", activeforeground=fg)
btn_back.place(x = 225, y = 380, width = 260, height = 50)
'''


'''
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
        if items_values['heart'] >= 100:
            items_values['heart'] = 100

        if 100 >= items_values['heart'] > 75: #100 - 75
            lbl_heart['image'] = images['heart_11_dic']

        elif 75 >= items_values['heart'] > 25: #75 - 25
            lbl_heart['image'] = images['heart_01_dic']

        elif 25 >= items_values['heart'] >= 0: #25 - 0
            lbl_heart['image'] = images['heart_00_dic']

        lbl_value_heart['text'] = f'{items_values['heart']}%'
    
    def food():
        if items_values['food'] >= 10:
            items_values['food'] = 10

        if 10 >= items_values['food'] > 7.5: #10 - 7.5
            lbl_food['image'] = images['food_11_dic']

        elif 7.5 >= items_values['food'] > 2.5: #7.5 - 2.5
            lbl_food['image'] = images['food_01_dic']

        elif 2.5 >= items_values['food'] >= 0: #2.5 - 0
            lbl_food['image'] = images['food_00_dic']

        lbl_value_food['text'] = f'{items_values['food']}/10'

    def keys():
        lbl_key_B['image'] = images['key_E_dic']
        lbl_key_S['image'] = images['key_E_dic']
        lbl_key_G['image'] = images['key_E_dic']

        if items_values['key_B'] == True: #Bronze
            lbl_key_B['image'] = images['key_B_dic']

        if items_values['key_S'] == True: #Silver
            lbl_key_S['image'] = images['key_S_dic']

        if items_values['key_G'] == True: #Golden
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
'''
'''
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
lbl_item_lighter.place(x = 3, y = 3, width = 35, height = 35)

lbl_item_wolfhide = Label(root_items_world_1, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_wolfhide.place(x = 43, y = 3, width = 35, height = 35)

lbl_item_future_friendship = Label(root_items_world_1, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_future_friendship.place(x = 43, y = 43, width = 35, height = 35)

lbl_key_B = Label(root_items_world_1, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_key_B.place(x = 3, y = 43, width = 35, height = 35)

#Items - World 2

root_items_world_2 = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_items_world_2.place(x = 92.5, y = 175, width = 85, height = 85)

lbl_item_shotgun = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_shotgun.place(x = 3, y = 3, width = 35, height = 35)

lbl_item_nausea = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_nausea.place(x = 43, y = 3, width = 35, height = 35)

lbl_item_crowbar = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_crowbar.place(x = 43, y = 43, width = 35, height = 35)

lbl_key_S = Label(root_items_world_2, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_key_S.place(x = 3, y = 43, width = 35, height = 35)

#Items - World 3

root_items_world_3 = Frame(root_play_game, bg=bg_light, bd = 2, relief = 'sunken')
root_items_world_3.place(x = 180, y = 175, width = 85, height = 85)

lbl_item_screwdriver = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_screwdriver.place(x = 3, y = 3, width = 35, height = 35)

lbl_item_gear = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_gear.place(x = 43, y = 3, width = 35, height = 35)

lbl_unknown = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_unknown.place(x = 43, y = 43, width = 35, height = 35)

lbl_key_G = Label(root_items_world_3, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')
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

lbl_credits_version_in_game = Label(root_back_next, bg=bg_dark, font = 'courier 10 bold', text = version, fg=fg)
lbl_credits_version_in_game.place(x = 275, y = 5, width = 160, height = 30)

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

if var_option.get() == 'E':
    print('Selecione uma das opções para seguir!!!')

default()
show_items_values()
root_play_game.place(x = 5, y = 5, width = width - 10, height = height - 10)

'''
