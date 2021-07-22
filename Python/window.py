#Import - Libraries _________________________________________________________________________________________
import os
from tkinter import *
from time import sleep
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

root_history = Frame(window, bg=bg)
root_history.place(x = 5, y = 5, width = 710, height = 460)
images = images(directory)

window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
window.resizable(False,False)
window.configure(background = '#000')

page_number_his = 0

def pages_history(page, action):
    global page_number_his
    if action == 'next':
        page_number_his += 1
        page = page_number_his
    elif action == 'back':
        page_number_his -= 1
        page = page_number_his

    if page == 0:
        print('exit')
    if page == 1:
        lbl_his_text['text'] = f'h59 - {page}'
    elif page == 2:
        lbl_his_text['text'] = f'h59 - {page}'
    else:
        lbl_his_text['text'] = f'h8 - {page}'

    print(page_number_his)

#Labels
lbl_his_main = Label(root_history, text = '- Introdução -', bg=bg, font = 'courier 40 bold')
lbl_his_main.place(x = 5, y = 5, width = 700, height = 115)

lbl_his_text = Label(root_history, text = '', bg=bg, bd = 5, relief = 'solid', font = 'courier 18 italic')
lbl_his_text.place(x = -5, y = 125, width = 720, height = 305)

lbl_his_version = Label(root_history, text = version, bg=bg, font = 'courier 10 bold')
lbl_his_version.place(x = 275, y = 430, width = 160, height = 30)

#Buttons
btn_his_next = Button(root_history, text= 'Voltar', bg=bg, bd = 2, relief = 'ridge', cursor='hand2',
                font = 'courier 14 bold', activebackground='#ccc', activeforeground=fg,
                command=lambda : pages_history(page_number_his, 'back'))
btn_his_next.place(x = 0, y = 430, width = 270, height = 30)

btn_his_back = Button(root_history, text= 'Próximo', bg=bg, bd = 2, relief = 'ridge', cursor='hand2',
                font = 'courier 14 bold', activebackground='#ccc', activeforeground=fg,
                command=lambda : pages_history(page_number_his, 'next'))
btn_his_back.place(x = 440, y = 430, width = 270, height = 30)



window.mainloop()

'''
page_number = 1

def wait(window, time = 0.5):
    window.update()
    sleep(time)

def pages_tutorial(page):
    global page_number
    page_number += 1

    if page == 1:
        lbl_main_text_tut['text'] = ''
        #Root
        root_hearts_foods_tut.place(x = 5, y = 125, width = 260, height = 45)
        wait(window)

        #Labels
        lbl_heart_tut.place(x = 2.5, y = 2.5, width = 35, height = 32.5)
        wait(window)

        lbl_value_heart_tut.place(x = 35, y = 2.5, width = 90, height = 32.5)
        wait(window)

        lbl_food_tut.place(x = 127.5, y = 2.5, width = 35, height = 32.5)
        wait(window)

        lbl_value_food_tut.place(x = 160, y = 2.5, width = 90, height = 32.5)

    elif page == 2:
        lbl_main_text_tut['text'] = ''
        #Roots
        root_items_world_1_tut.place(x = 5, y = 175, width = 85, height = 85)
        wait(window)

        root_items_world_2_tut.place(x = 92.5, y = 175, width = 85, height = 85)
        wait(window)

        root_items_world_3_tut.place(x = 180, y = 175, width = 85, height = 85)
        wait(window)

        #Labels
        lbl_item_01_tut.place(x = 3, y = 3, width = 35, height = 35)
        wait(window)

        lbl_item_02_tut.place(x = 43, y = 3, width = 35, height = 35)
        wait(window)

        lbl_item_03_tut.place(x = 43, y = 43, width = 35, height = 35)
        wait(window)

        lbl_key_01_tut.place(x = 3, y = 43, width = 35, height = 35)
        wait(window)

        lbl_item_04_tut.place(x = 3, y = 3, width = 35, height = 35)
        wait(window)

        lbl_item_05_tut.place(x = 43, y = 3, width = 35, height = 35)
        wait(window)

        lbl_item_06_tut.place(x = 43, y = 43, width = 35, height = 35)
        wait(window)

        lbl_key_02_tut.place(x = 3, y = 43, width = 35, height = 35)
        wait(window)

        lbl_item_07_tut.place(x = 3, y = 3, width = 35, height = 35)
        wait(window)

        lbl_item_08_tut.place(x = 43, y = 3, width = 35, height = 35)
        wait(window)

        lbl_item_09_tut.place(x = 43, y = 43, width = 35, height = 35)
        wait(window)

        lbl_key_03_tut.place(x = 3, y = 43, width = 35, height = 35)
        
    elif page == 3:
        lbl_main_text_tut['text'] = ''
        #Root
        root_ways_tut.place(x = 5, y = 265, width = 260, height = 40)
        wait(window)

        #Labels
        lbl_way_01_tut.place(x = 7.5, y = 0, width = 35, height = 35)
        wait(window)

        lbl_way_02_tut.place(x = 47.5, y = 0, width = 35, height = 35)
        wait(window)

        lbl_way_03_tut.place(x = 87.5, y = 0, width = 35, height = 35)
        wait(window)

        lbl_way_04_tut.place(x = 127.5, y = 0, width = 35, height = 35)
        wait(window)

        lbl_way_05_tut.place(x = 167.5, y = 0, width = 35, height = 35)
        wait(window)

        lbl_way_06_tut.place(x = 207.5, y = 0, width = 35, height = 35)

    elif page == 4:
        lbl_main_text_tut['text'] = ''
        #Root
        root_scenario_tut.place(x = 5 , y = 310, width = 260, height = 110)
        wait(window)
        #Label
        lbl_scenario_tut.place(x = 3, y = 3, width= 250, height = 100)

    elif page == 5:
        lbl_main_text_tut['text'] = ''
        #Root
        root_text_tut.place(x = 270, y = 125, width = 435, height = 295)
        wait(window)

        #RadioButtons
        rb_option_A_tut.place(x = 5, y = 5, width = 420, height = 90)
        wait(window)

        rb_option_B_tut.place(x = 5, y = 100, width = 420, height = 90)
        wait(window)

        rb_option_C_tut.place(x = 5, y = 195, width = 420, height = 90)

    elif page == 6:
        page_number = 6
    print(page)

#Roots
root_hearts_foods_tut = Frame(root_tutorial, bg=bg_light, bd = 2, relief = 'sunken')
root_items_world_1_tut = Frame(root_tutorial, bg=bg_light, bd = 2, relief = 'sunken')
root_items_world_2_tut = Frame(root_tutorial, bg=bg_light, bd = 2, relief = 'sunken')
root_items_world_3_tut = Frame(root_tutorial, bg=bg_light, bd = 2, relief = 'sunken')
root_scenario_tut = Frame(root_tutorial, bg=bg_light, bd = 2, relief = 'sunken')
root_txt_tut = Frame(root_tutorial, bg=bg_dark)
root_text_tut = Frame(root_tutorial, bg=bg_light, bd = 2, relief = 'sunken')
root_back_next_tut = Frame(root_tutorial, bg=bg_dark)
root_ways_tut = Frame(root_tutorial, bg=bg_light, bd = 2, relief = 'sunken')

root_txt_tut.place(x = 0, y = 0, width = 710, height = 120)
root_back_next_tut.place(x = 0, y = 425, width = 710, height = 45)

#Hearts and Foods
lbl_heart_tut = Label(root_hearts_foods_tut, image = images['heart_11_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_value_heart_tut = Label(root_hearts_foods_tut, text = f'100%', bg=bg, font = 'courier 13 bold', bd = 3, relief = 'ridge')
lbl_food_tut = Label(root_hearts_foods_tut, image = images['food_11_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_value_food_tut = Label(root_hearts_foods_tut, text = f'9/10', bg=bg, font = 'courier 13 bold', bd = 3, relief = 'ridge')

#Items - World 1
lbl_item_01_tut = Label(root_items_world_1_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_02_tut = Label(root_items_world_1_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_03_tut = Label(root_items_world_1_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_key_01_tut = Label(root_items_world_1_tut, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')

#Items - World 2
lbl_item_04_tut = Label(root_items_world_2_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_05_tut = Label(root_items_world_2_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_06_tut = Label(root_items_world_2_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_key_02_tut = Label(root_items_world_2_tut, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')

#Items - World 3
lbl_item_07_tut = Label(root_items_world_3_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_08_tut = Label(root_items_world_3_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_item_09_tut = Label(root_items_world_3_tut, image = images['empty_01_dic'], bg=bg, bd = 3, relief = 'ridge')
lbl_key_03_tut = Label(root_items_world_3_tut, image = images['key_E_dic'], bg=bg, bd = 3, relief = 'ridge')

#Ways
lbl_way_01_tut = Label(root_ways_tut, image = images['just_way_dic'], bg=bg_light)
lbl_way_02_tut = Label(root_ways_tut, image = images['just_way_dic'], bg=bg_light)
lbl_way_03_tut = Label(root_ways_tut, image = images['just_way_dic'], bg=bg_light)
lbl_way_04_tut = Label(root_ways_tut, image = images['just_way_dic'], bg=bg_light)
lbl_way_05_tut = Label(root_ways_tut, image = images['just_way_dic'], bg=bg_light)
lbl_way_06_tut = Label(root_ways_tut, image = images['just_way_dic'], bg=bg_light)

#Scenario
lbl_scenario_tut = Label(root_scenario_tut, image = images['empty_00_dic'], bg=bg, anchor = CENTER)

#TXT
lbl_main_text_tut = Label(root_txt_tut, text = 'Texto principal', bg=bg, justify= LEFT,
                font = 'courier 16 bold', bd = 4, relief = 'ridge')
lbl_main_text_tut.place(x = 0, y = 0, width = 710, height = 115)

#Texts

var_option = StringVar()
var_option.set('E')

rb_option_A_tut = Radiobutton(root_text_tut, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2', 
                            variable = var_option, value = 'A', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
rb_option_B_tut = Radiobutton(root_text_tut, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2', 
                            variable = var_option, value = 'B', activebackground=bg_gray, activeforeground=fg, justify = LEFT)
rb_option_C_tut = Radiobutton(root_text_tut, bg=bg, font = 'courier 12 bold', indicatoron=0, bd = 4.5, text = '', cursor = 'hand2',
                            variable = var_option, value = 'C', activebackground=bg_gray, activeforeground=fg, justify = LEFT)

#Back & Next
lbl_version_in_tut = Label(root_back_next_tut, bg=bg_dark, font = 'courier 10 bold', text = version, fg=fg)
lbl_version_in_tut.place(x = 275, y = 5, width = 160, height = 30)

btn_back_tut = Button(root_back_next_tut, text = 'Retornar ao Menu', bg=bg_dark, bd = 1.5, relief = 'ridge',
                cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                fg=fg)
btn_back_tut.place(x = 0, y = 5, width = 270, height = 30)

btn_next_tut = Button(root_back_next_tut, text = 'Avançar', bg=bg_dark, bd = 1, relief = 'ridge',
                cursor='hand2', font = 'courier 14 bold', activebackground=bg_gray, activeforeground=bg_light,
                fg=fg, command=lambda : pages_tutorial(page_number))
btn_next_tut.place(x = 440, y = 5, width = 270, height = 30)
'''
