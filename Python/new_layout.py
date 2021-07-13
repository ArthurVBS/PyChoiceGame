#Import - Libraries _________________________________________________________________________________________
import os
from tkinter import *
#Import - Packages __________________________________________________________________________________________
from Utils.widgets import images
#Variables __________________________________________________________________________________________________
bg = fg = '#fbfbfb'
bg_frames = '#e1e1e1'
directory = os.path.dirname(__file__)
#Tkinter ____________________________________________________________________________________________________
window = Tk()

width = 720
height = 470
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

root_main = Frame(window, bd = 1, relief = 'sunken', bg='#fff')
root_main.place(x = 10, y = 10, width = width - 20, height = height - 20)

window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
window.title('In search of the truth')
window.iconbitmap(directory + '/Images/Icons/icon_02.ico')
window.resizable(False,False)
window.configure(background = '#000')

images = images(directory)

#Hearts and Foods

root_hearts_foods = Frame(root_main, bd = 1, relief = 'sunken', bg=bg_frames)
root_hearts_foods.place(x = 5, y = 140, width = 260, height = 45)

lbl_heart = Label(root_hearts_foods, image = images['heart_11_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_heart.place(x = 5, y = 5, width = 35, height = 32.5)

lbl_value_heart = Label(root_hearts_foods, text = f'100%', bg=bg, font = 'courier 12 bold', bd = 2, relief = 'ridge')
lbl_value_heart.place(x = 37.5, y = 5, width = 90, height = 32.5)

lbl_food = Label(root_hearts_foods, image = images['food_11_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_food.place(x = 130, y = 5, width = 35, height = 32.5)

lbl_value_food = Label(root_hearts_foods, text = f'9/10', bg=bg, font = 'courier 12 bold', bd = 2, relief = 'ridge')
lbl_value_food.place(x = 162.5, y = 5, width = 90, height = 32.5)

#Items - World 1

root_items_world_1 = Frame(root_main, bd = 1, relief = 'sunken', bg=bg_frames)
root_items_world_1.place(x = 5, y = 190, width = 85, height = 85)

lbl_item_lighter = Label(root_items_world_1, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_item_wolfhide = Label(root_items_world_1, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_item_future_friendship = Label(root_items_world_1, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_key_B = Label(root_items_world_1, image = images['key_E_dic'], bg=bg, bd = 2, relief = 'ridge')

lbl_item_lighter.place(x = 5, y = 5, width = 35, height = 35)
lbl_item_wolfhide.place(x = 42.5, y = 5, width = 35, height = 35)
lbl_item_future_friendship.place(x = 42.5, y = 42.5, width = 35, height = 35)
lbl_key_B.place(x = 5, y = 42.5, width = 35, height = 35)

#Items - World 2

root_items_world_2 = Frame(root_main, bd = 1, relief = 'sunken', bg=bg_frames)
root_items_world_2.place(x = 92.5, y = 190, width = 85, height = 85)

lbl_item_shotgun = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_item_nausea = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_item_crowbar = Label(root_items_world_2, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_key_S = Label(root_items_world_2, image = images['key_E_dic'], bg=bg, bd = 2, relief = 'ridge')

lbl_item_shotgun.place(x = 5, y = 5, width = 35, height = 35)
lbl_item_nausea.place(x = 42.5, y = 5, width = 35, height = 35)
lbl_item_crowbar.place(x = 42.5, y = 42.5, width = 35, height = 35)
lbl_key_S.place(x = 5, y = 42.5, width = 35, height = 35)

#Items - World 3

root_items_world_3 = Frame(root_main, bd = 1, relief = 'sunken', bg=bg_frames)
root_items_world_3.place(x = 180, y = 190, width = 85, height = 85)

lbl_item_screwdriver = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_item_gear = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_unknown = Label(root_items_world_3, image = images['empty_01_dic'], bg=bg, bd = 2, relief = 'ridge')
lbl_key_G = Label(root_items_world_3, image = images['key_E_dic'], bg=bg, bd = 2, relief = 'ridge')

lbl_item_screwdriver.place(x = 5, y = 5, width = 35, height = 35)
lbl_item_gear.place(x = 42.5, y = 5, width = 35, height = 35)
lbl_unknown.place(x = 42.5, y = 42.5, width = 35, height = 35)
lbl_key_G.place(x = 5, y = 42.5, width = 35, height = 35)

#Scenario

root_scenario = Frame(root_main, bd = 0.5, relief = 'groove', bg=bg_frames)
root_scenario.place(x = 5 , y = 280, width = 260, height = 110)

lbl_scenario = Label(root_scenario, image = images['empty_00_dic'], bg=bg, anchor = CENTER)
lbl_scenario.place(x = 5, y = 5, width= 250, height = 100)#250x100

#TXT

root_txt = Frame(root_main, bd = 1, relief = 'sunken', bg=bg_frames)
root_txt.place(x = 5, y = 5, width = 690, height = 130)

lbl_main_text = Label(root_txt, text = 'Texto principal', bg=bg_frames, justify= CENTER, font = 'courier 16 bold')
lbl_main_text.place(x = 2.5, y = 2.5, width = 680, height = 120)

lbl_main_text['text'] = 'Você está caminhando a um certo tempo, o seu\n' +\
                        'estômago ronca. Você encontra algumas frutinhas\n' +\
                        'azuis em um arbusto que podem ser comestíveis.'

#Texts

root_text = Frame(root_main, bd = 1, relief = 'sunken', bg=bg_frames)
root_text.place(x = 270, y = 140, width = 425, height = 250)

var_option = StringVar()
var_option.set('E')

rb_option_A = Radiobutton(root_text, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 2.5, text = '', cursor = 'hand2', 
                            variable = var_option, value = 'A', activebackground='#aaa', activeforeground=fg)
rb_option_A.place(x = 5, y = 5, width = 410, height = 75)

rb_option_B = Radiobutton(root_text, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 2.5, text = '', cursor = 'hand2', 
                            variable = var_option, value = 'B', activebackground='#aaa', activeforeground=fg)
rb_option_B.place(x = 5, y = 85, width = 410, height = 75)

rb_option_C = Radiobutton(root_text, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 2.5, text = '', cursor = 'hand2', 
                            variable = var_option, value = 'C', activebackground='#aaa', activeforeground=fg)
rb_option_C.place(x = 5, y = 165, width = 410, height = 75)

rb_option_A['text'] = 'Pegar as frutinhas do arbusto e\nsaciar a sua fome;'
rb_option_B['text'] = 'Ignorar as frutinhas e seguir em\nfrente;'
rb_option_C['text'] = 'Pegar alguma comida da mochila;'

#Back, Next and Way

root_next_back_way = Frame(root_main, bd = 1, relief = 'sunken', bg=bg_frames)
root_next_back_way.place(x = 5, y = 395, width = 690, height = 50)

btn_back = Button(root_next_back_way, text = 'Ir ao Menu', bg=bg, bd = 2, relief = 'ridge', cursor='hand2',
                font = 'courier 18 bold', activebackground='#aaa', activeforeground=fg)
btn_back.place(x = 5, y = 5, width = 205, height = 40)

btn_next = Button(root_next_back_way, text = 'Avançar', bg=bg, bd = 2, relief = 'ridge', cursor='hand2',
                font = 'courier 18 bold', activebackground='#aaa', activeforeground=fg)
btn_next.place(x = 475, y = 5, width = 205, height = 40)

lbl_way_01 = Label(root_next_back_way, image = images['just_way_dic'], bg=bg_frames)
lbl_way_01.place(x = 225, y = 2.5, width = 40, height = 40)

lbl_way_02 = Label(root_next_back_way, image = images['just_way_dic'], bg=bg_frames)
lbl_way_02.place(x = 265, y = 2.5, width = 40, height = 40)

lbl_way_03 = Label(root_next_back_way, image = images['just_way_dic'], bg=bg_frames)
lbl_way_03.place(x = 305, y = 2.5, width = 40, height = 40)

lbl_way_04 = Label(root_next_back_way, image = images['just_way_dic'], bg=bg_frames)
lbl_way_04.place(x = 345, y = 2.5, width = 40, height = 40)

lbl_way_05 = Label(root_next_back_way, image = images['just_way_dic'], bg=bg_frames)
lbl_way_05.place(x = 385, y = 2.5, width = 40, height = 40)

lbl_way_06 = Label(root_next_back_way, image = images['just_way_dic'], bg=bg_frames)
lbl_way_06.place(x = 425, y = 2.5, width = 40, height = 40)

#default

window.title('Level 1-1')

lbl_value_heart['text'] = '80%'

lbl_value_food['text'] = '5/10'

lbl_key_B['image'] = images['key_B_dic']

lbl_item_lighter['image'] = images['item_lighter_dic']

lbl_scenario['image'] = images['scenario_01_dic']

lbl_way_04['image'] = images['way_dic']

if var_option.get() == 'E':
    print('Selecione uma das opções para seguir!!!')

window.mainloop()
