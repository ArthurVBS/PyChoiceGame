#Import - Libraries _________________________________________________________________________________________

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

#Import - Packages __________________________________________________________________________________________

try:
    from sounds import soundEffect
except:
    from Utils.sounds import soundEffect

#Colors _____________________________________________________________________________________________________

color_light = '#fefefe'
color_default = '#e1e1e1'
color_gray = '#545454'
color_dark = '#000'
color_green = '#008000'
color_yellow = '#b8860b'
color_red = '#ab4043'

#Variables __________________________________________________________________________________________________

version = 'v 0.3'
status = {'win' : 0, 'draw' : 0, 'lose' : 0}

#Main Functions _____________________________________________________________________________________________

def roots(window):
    root_menu = Frame(window, bg=color_light)
    root_game = Frame(window, bg=color_dark)

    roots = {
        'root_menu' : root_menu, 'root_game' : root_game}
    
    return roots


def show(window, directory, roots, assets):

    def show_menu(window, directory, roots, assets):
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
                                command=lambda:click_show(window, directory, roots, assets, type='game'))
        btn_menu_play.place(x = 175, y = 130, width = 260, height = 50)

        btn_menu_tutorial = Button(roots['root_menu'], text = 'Tutorial', font = 'courier 20 bold', bg=color_light, bd=3, relief='ridge',
                                cursor='hand2', activebackground=color_gray)
        btn_menu_tutorial.place(x = 175, y = 195, width = 260, height = 50)

        btn_menu_settings = Button(roots['root_menu'], text = 'Ajustes', font = 'courier 20 bold', bg=color_light, bd=3, relief='ridge',
                                cursor='hand2', activebackground=color_gray, command=lambda:click_reset(assets))
        btn_menu_settings.place(x = 175, y = 260, width = 260, height = 50)

        btn_menu_credits = Button(roots['root_menu'], text = 'Créditos', font = 'courier 14 bold', bg=color_light, bd=1.5, relief='ridge',
                                cursor='hand2', activebackground=color_gray)
        btn_menu_credits.place(x = 0, y = 330, width = 220, height = 30)

        btn_menu_quit = Button(roots['root_menu'], text = 'Sair', font = 'courier 14 bold', bg=color_light, bd=1.5, relief='ridge',
                                cursor='hand2', activebackground=color_gray, command=lambda:click_quit(window))
        btn_menu_quit.place(x = 390, y = 330, width = 220, height = 30)


    def show_game(window, directory, roots, assets):
        global lbl_game_cpu_image, lbl_game_cpu_text, lbl_game_player_image, lbl_game_player_text
        global var_option, lbl_game_win, lbl_game_draw, lbl_game_lose
        #Data
        sub_root_data = Frame(roots['root_game'], bg=color_light)
        sub_root_data.place(x = 0, y = 0, width = 220, height = 325)

        lbl_game_data_title_01 = Label(sub_root_data, text = 'Resultados', font = 'courier 20 bold', bg=color_light,
                                        bd=5, relief='solid')
        lbl_game_data_title_01.place(x = -5, y = -5, width = 230, height = 50)

        lbl_game_data_title_02 = Label(sub_root_data, text = 'Última partida', font = 'courier 18 bold', bg=color_light,
                                        bd=5, relief='solid')
        lbl_game_data_title_02.place(x = -5, y = 165, width = 230, height = 50)

        lbl_game_win = Label(sub_root_data, text=f'Vitórias: {status["win"]}', font='courier 12 bold', bg=color_light, fg=color_green)
        lbl_game_win.place(x = 25, y = 55, width = 170, height = 30)

        lbl_game_draw = Label(sub_root_data, text=f'Empates:  {status["draw"]}', font='courier 12 bold', bg=color_light, fg=color_yellow)
        lbl_game_draw.place(x = 25, y = 90, width = 170, height = 30)

        lbl_game_lose = Label(sub_root_data, text=f'Derrotas: {status["lose"]}', font='courier 12 bold', bg=color_light, fg=color_red)
        lbl_game_lose.place(x = 25, y = 125, width = 170, height = 30)

        lbl_game_player_image = Label(sub_root_data, image = assets['question_mark_dic'], bg=color_light)
        lbl_game_player_image.place(x = 25, y = 220, width = 70, height = 70)

        lbl_game_player_text = Label(sub_root_data, text = 'PLAYER', font = 'courier 12 bold', bg=color_light)
        lbl_game_player_text.place(x = 25, y = 295, width = 70, height = 30)

        lbl_game_cpu_image = Label(sub_root_data, image = assets['question_mark_dic'], bg=color_light)
        lbl_game_cpu_image.place(x = 125, y = 220, width = 70, height = 70)

        lbl_game_cpu_text = Label(sub_root_data, text = 'CPU', font = 'courier 12 bold', bg=color_light)
        lbl_game_cpu_text.place(x = 125, y = 295, width = 70, height = 30)

        #Choice
        sub_root_choice = Frame(roots['root_game'], bg=color_default)
        sub_root_choice.place(x = 225, y = 0, width = 385, height = 325)

        lbl_game_choice_title = Label(sub_root_choice, text = 'Faça a sua\nescolha!', font = 'courier 28 bold', bg=color_default)
        lbl_game_choice_title.place(x = 5, y = 5, width = 375, height = 80)

        lbl_game_rock = Label(sub_root_choice, text = 'Pedra', font = 'courier 12 bold', bg=color_default)
        lbl_game_rock.place(x = 25, y = 170, width = 70, height = 30)

        lbl_game_paper = Label(sub_root_choice, text = 'Papel', font = 'courier 12 bold', bg=color_default)
        lbl_game_paper.place(x = 157.5, y = 170, width = 70, height = 30)
        
        lbl_game_scissors = Label(sub_root_choice, text = 'Tesoura', font = 'courier 12 bold', bg=color_default)
        lbl_game_scissors.place(x = 290, y = 170, width = 70, height = 30)

        var_option = StringVar()
        var_option.set(None)

        rbt_game_rock = Radiobutton(sub_root_choice, indicatoron=0, image=assets['rock_dic'], cursor='hand2',
                                    variable = var_option, value = 'rock', bg=color_light, bd=2)
        rbt_game_rock.place(x = 25, y = 95, width = 70, height = 70)

        rbt_game_paper = Radiobutton(sub_root_choice, indicatoron=0, image=assets['paper_dic'], cursor='hand2',
                                    variable = var_option, value = 'paper', bg=color_light, bd=2)
        rbt_game_paper.place(x = 157.5, y = 95, width = 70, height = 70)

        rbt_game_scissors = Radiobutton(sub_root_choice, indicatoron=0, image=assets['scissors_dic'], cursor='hand2',
                                    variable = var_option, value = 'scissors', bg=color_light, bd=2)
        rbt_game_scissors.place(x = 290, y = 95, width = 70, height = 70)

        #Back_Next
        sub_root_back_next = Frame(roots['root_game'], bg=color_dark)
        sub_root_back_next.place(x = 0, y = 325, width = 610, height = 35)

        lbl_game_version = Label(sub_root_back_next, text = version, font = 'courier 12 bold', bg=color_dark, fg=color_light)
        lbl_game_version.place(x = 220, y = 5, width = 170, height = 30)
        
        btn_game_back = Button(sub_root_back_next, text = 'Ir ao menu', font = 'courier 14 bold', bg=color_dark, bd=1.5, relief='ridge',
                                cursor='hand2', activebackground=color_gray, fg=color_light,
                                command=lambda:click_show(window, directory, roots, assets, type='menu'))
        btn_game_back.place(x = 0, y = 5, width = 220, height = 30)

        btn_game_choice = Button(sub_root_back_next, text = 'Avançar', font = 'courier 14 bold', bg=color_dark, bd=1.5, relief='ridge',
                                cursor='hand2', activebackground=color_gray, fg=color_light,
                                command=lambda:click_next(directory, assets))
        btn_game_choice.place(x = 390, y = 5, width = 220, height = 30)




    show_menu(window, directory, roots, assets)
    show_game(window, directory, roots, assets)

#Functions - Click __________________________________________________________________________________________

def click_show(window, directory, roots, assets, type):
    global var_option, status
    #Variables
    title = ''
    icon = randint(1, 3)
    var_option.set(None)

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


def click_reset(assets):
    global status
    #Images
    lbl_game_player_image['image'] = assets['question_mark_dic']
    lbl_game_cpu_image['image'] = assets['question_mark_dic']

    #Text
    lbl_game_player_text['fg'] = color_dark
    lbl_game_cpu_text['fg'] = color_dark
    
    #Status
    status = {'win' : 0, 'draw' : 0, 'lose' : 0}
    lbl_game_win['text'] = f'Vitórias: {status["win"]}'
    lbl_game_draw['text'] = f'Empates:  {status["draw"]}'
    lbl_game_lose['text'] = f'Derrotas: {status["lose"]}'


def cpu_random():
    global cpu
    option = randint(1, 3)
    if option == 1:
        cpu = 'rock'
    elif option == 2:
        cpu = 'paper'
    elif option == 3:
        cpu = 'scissors'
    else:
        cpu = None


def click_next(directory, assets):
    global lbl_game_cpu_image, lbl_game_player_image
    cpu_random()
    player = var_option.get()
    var_option.set(None)

    #Show Images
    if player == 'rock' or player == 'scissors' or player == 'paper':
        lbl_game_player_image['image'] = assets[f'{player}_dic']
    else:
        messagebox.showerror(title = "Avançar?", icon = messagebox.INFO,
        message = "É necessário escolher uma das\nopções para avançar!")
        return None

    if cpu != None:
        lbl_game_cpu_image['image'] = assets[f'{cpu}_dic']
    else:
        lbl_game_cpu_image['image'] = assets['question_mark_dic']

    ##Draw
    if player == cpu:
        soundEffect(directory, soundEffect = 'draw')
        status['draw'] += 1
        lbl_game_player_text['fg'] = color_yellow
        lbl_game_cpu_text['fg'] = color_yellow

    ##Win
    elif player == 'rock' and cpu == 'scissors' or player == 'scissors' and cpu == 'paper' or player == 'paper' and cpu == 'rock':
        soundEffect(directory, soundEffect = 'win')
        status['win'] += 1
        lbl_game_player_text['fg'] = color_green
        lbl_game_cpu_text['fg'] = color_red

    ##Lose
    elif player == 'scissors' and cpu == 'rock' or player == 'paper' and cpu == 'scissors' or player == 'rock' and cpu == 'paper':
        soundEffect(directory, soundEffect = 'lose')
        status['lose'] += 1
        lbl_game_player_text['fg'] = color_red
        lbl_game_cpu_text['fg'] = color_green

    #Show Status
    lbl_game_win['text'] = f'Vitórias: {status["win"]}'
    lbl_game_draw['text'] = f'Empates:  {status["draw"]}'
    lbl_game_lose['text'] = f'Derrotas: {status["lose"]}'


def click_quit(window):
    ok_cancel_quit = messagebox.askokcancel(title = "Sair?", message = "Você realmente deseja sair?\t\t",
    detail = "Desde já obrigado por jogar")
    if ok_cancel_quit == True:
        window.destroy()

