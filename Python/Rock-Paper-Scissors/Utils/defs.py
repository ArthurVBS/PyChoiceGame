#Import - Libraries _________________________________________________________________________________________

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

#Colors _____________________________________________________________________________________________________

color_light = '#fefefe'
color_default = '#e1e1e1'
color_gray = '#545454'
color_dark = '#000'

#Variables __________________________________________________________________________________________________

version = 'v 0.1'

#Main Functions _____________________________________________________________________________________________

def roots(window):
    root_menu = Frame(window, bg=color_light)
    root_game = Frame(window, bg=color_dark)

    roots = {
        'root_menu' : root_menu, 'root_game' : root_game}
    
    return roots


def show(window, directory, roots, assets):

    def show_menu(window, directory, roots):
        #Labels
        lbl_menu_title = Label(roots['root_menu'], text = 'Rock - Paper - Scissors', font = 'courier 30 bold', bg=color_light, bd=1,
                                relief='sunken')
        lbl_menu_title.place(x = 5, y = 5, width = 600, height = 100)

        lbl_menu_line_01 = Label(roots['root_menu'], bg=color_dark)
        lbl_menu_line_01.place(x = 0, y = 110, width = 610, height = 5)

        lbl_menu_line_02 = Label(roots['root_menu'], bg=color_dark)
        lbl_menu_line_02.place(x = 0, y = 325, width = 610, height = 5)

        lbl_menu_version = Label(roots['root_menu'], text = version, font = 'courier 12 bold', bg=color_light)
        lbl_menu_version.place(x = 220, y = 330, width = 170, height = 30)

        #Buttons
        btn_menu_play = Button(roots['root_menu'], text = 'Jogar', font = 'courier 20 bold', bg=color_light, bd=3, relief='ridge',
                                cursor='hand2', activebackground=color_gray,
                                command=lambda:click_show(window, directory, roots, type='game'))
        btn_menu_play.place(x = 175, y = 130, width = 260, height = 50)

        btn_menu_tutorial = Button(roots['root_menu'], text = 'Tutorial', font = 'courier 20 bold', bg=color_light, bd=3, relief='ridge',
                                cursor='hand2', activebackground=color_gray)
        btn_menu_tutorial.place(x = 175, y = 195, width = 260, height = 50)

        btn_menu_settings = Button(roots['root_menu'], text = 'Ajustes', font = 'courier 20 bold', bg=color_light, bd=3, relief='ridge',
                                cursor='hand2', activebackground=color_gray)
        btn_menu_settings.place(x = 175, y = 260, width = 260, height = 50)

        btn_menu_credits = Button(roots['root_menu'], text = 'Créditos', font = 'courier 14 bold', bg=color_light, bd=1.5, relief='ridge',
                                cursor='hand2', activebackground=color_gray)
        btn_menu_credits.place(x = 0, y = 330, width = 220, height = 30)

        btn_menu_quit = Button(roots['root_menu'], text = 'Sair', font = 'courier 14 bold', bg=color_light, bd=1.5, relief='ridge',
                                cursor='hand2', activebackground=color_gray, command=lambda:click_quit(window))
        btn_menu_quit.place(x = 390, y = 330, width = 220, height = 30)


    def show_game(window, directory, roots, assets):
        global var_option
        #sub_roots
        sub_root_data = Frame(roots['root_game'], bg=color_light)
        sub_root_data.place(x = 0, y = 0, width = 220, height = 325)

        sub_root_choice = Frame(roots['root_game'], bg=color_default)
        sub_root_choice.place(x = 225, y = 0, width = 385, height = 325)


        #Labels
        lbl_game_title = Label(sub_root_choice, text = 'Faça a sua\nescolha!', font = 'courier 28 bold', bg=color_gray)
        lbl_game_title.place(x = 5, y = 5, width = 375, height = 100)

        lbl_game_line_01 = Label(roots['root_game'], bg=color_dark)
        lbl_game_line_01.place(x = 0, y = 325, width = 610, height = 5)

        lbl_game_version = Label(roots['root_game'], text = version, font = 'courier 12 bold', bg=color_dark, fg=color_light)
        lbl_game_version.place(x = 220, y = 330, width = 170, height = 30)

        #Buttons
        btn_game_back = Button(roots['root_game'], text = 'Ir ao menu', font = 'courier 14 bold', bg=color_dark, bd=1.5, relief='ridge',
                                cursor='hand2', activebackground=color_gray, fg=color_light,
                                command=lambda:click_show(window, directory, roots, type='menu'))
        btn_game_back.place(x = 0, y = 330, width = 220, height = 30)

        btn_game_choice = Button(roots['root_game'], text = 'Avançar', font = 'courier 14 bold', bg=color_dark, bd=1.5, relief='ridge',
                                cursor='hand2', activebackground=color_gray, fg=color_light)
        btn_game_choice.place(x = 390, y = 330, width = 220, height = 30)

        #RadioButtons
        var_option = StringVar()
        var_option.set('None')

        rbt_game_rock = Radiobutton(sub_root_choice, indicatoron=0, image=assets['rock_dic'], cursor='hand2',
                                    variable = var_option, value = 'rock', bg=color_light, bd=2)
        rbt_game_rock.place(x = 15, y = 120, width = 70, height = 70)

        rbt_game_paper = Radiobutton(sub_root_choice, indicatoron=0, image=assets['paper_dic'], cursor='hand2',
                                    variable = var_option, value = 'paper', bg=color_light, bd=2)
        rbt_game_paper.place(x = 100, y = 120, width = 70, height = 70)

        rbt_game_scissors = Radiobutton(sub_root_choice, indicatoron=0, image=assets['scissors_dic'], cursor='hand2',
                                    variable = var_option, value = 'scissors', bg=color_light, bd=2)
        rbt_game_scissors.place(x = 180, y = 120, width = 70, height = 70)




    show_menu(window, directory, roots)
    show_game(window, directory, roots, assets)

#Functions - Click __________________________________________________________________________________________

def click_show(window, directory, roots, type):
    global var_option
    #Variables
    title = ''
    icon = randint(1, 3)
    var_option.set('None')

    #Title
    if type == 'menu':
        title = 'Menu Inicial'
    elif type == 'game':
        title = 'Rock - Paper - Scissors'

    #Window
    window.iconbitmap(directory + f'/Assets/icon_0{icon}.ico')
    window.title(title)

    #Roots
    for root in roots:
        roots[root].place_forget()

    roots[f'root_{type}'].place(x = 5, y = 5, width = 610, height = 360)


def click_quit(window):
    ok_cancel_quit = messagebox.askokcancel(title = "Sair?", message = "Você realmente deseja sair?\t\t",
    detail = "Desde já obrigado por jogar")
    if ok_cancel_quit == True:
        window.destroy()

