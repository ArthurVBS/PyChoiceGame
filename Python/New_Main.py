#Import - Libraries _________________________________________________________________________________________

import os
from tkinter import *

#Import - Packages __________________________________________________________________________________________

from Utils.widgets import images
from Utils.audio import soundtrack
from Utils.defs import main_roots, game_roots, default, show_items_values
from Utils.defs import game_widgets, menu_widgets, credits_widgets, options_widgets, gameover_widgets

#Variables __________________________________________________________________________________________________

version = 'layout v 2.7.2'
directory = os.path.dirname(__file__)

global items_values
items_values = {
    'level' : 1, 'world' : 1,

    'food' : 5, 'heart' : 80,

    'key_B' : True, 'key_S' : False, 'key_G' : False,

    'item_lighter' : True, 'item_future_friendship' : False,
    'item_wolfhide' : False, 'item_shotgun' : False,
    'item_nausea' : False, 'item_crowbar' : False,
    'item_screwdriver' : False, 'item_gear' : False}

#Tkinter ____________________________________________________________________________________________________

window = Tk()

width = 720
height = 470
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

images = images(directory)
vol = soundtrack(directory, vol = 0.5, soundtrack = 0)

main_roots = main_roots(window)
game_roots = game_roots(main_roots)
game_widgets = game_widgets(window, main_roots, directory, game_roots, images, version, menu_widgets)

default(window, images, game_widgets)
show_items_values(images, game_widgets)

menu_widgets = menu_widgets(window, main_roots, directory, default, version, images, game_widgets)
credits_widgets = credits_widgets(window, main_roots, directory, version)
options_widgets = options_widgets(window, main_roots, directory, images)
gameover_widgets = gameover_widgets(window, main_roots, directory, menu_widgets)

window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
window.title('Main Menu')
window.iconbitmap(directory + '/Images/Icons/icon_01.ico')
window.resizable(False,False)
window.configure(background = '#000')

main_roots['root_main_menu'].place(x = 5, y = 5, width = 710, height = 460)

window.mainloop()
