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