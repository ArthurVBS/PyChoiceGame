#Import - Libraries _________________________________________________________________________________________

from tkinter import * 
from tkinter import messagebox
from random import randint

#Import - Packages __________________________________________________________________________________________

try:
    from sounds import soundEffect
except:
    from Utils.sounds import soundEffect

#Variables __________________________________________________________________________________________________

version = 'v 0.5'
text_credits = 'Aluno: Arthur Vinícius Bezerra da Silva\n' +\
               'Curso: ADS - IFPE - 1º período - 2021.1\n\n' +\
               'Início: 2021.07.29      Fim: 2021.08.02'

status = {'win' : 0, 'draw' : 0, 'lose' : 0}
colors = {'white' : '#fefefe', 'light' : '#e1e1e1', 'gray' : '#545454', 'dark' : '#000', 
          'green' : '#008000', 'yellow' : '#b8860b', 'red' : '#ab4043'}

#Main Functions _____________________________________________________________________________________________

def roots(window):
    root_menu = Frame(window, bg=colors['white'])
    root_game = Frame(window, bg=colors['dark'])
    root_credits = Frame(window, bg=colors['white'])
    root_tutorial = Frame(window, bg=colors['white'])
    root_settings = Frame(window, bg=colors['white'])

    roots = {
        'root_menu' : root_menu, 'root_game' : root_game, 'root_credits' : root_credits,
        'root_tutorial' : root_tutorial, 'root_settings' : root_settings}
    
    return roots


def build(window, directory, roots, assets):

    def build_menu():
        #Labels
        lbl_menu_title = Label(roots['root_menu'], text = 'Rock - Paper - Scissors', font = 'courier 30 bold',
                                bg=colors['white'], bd=1, relief='sunken')
        lbl_menu_title.place(x = 5, y = 5, width = 600, height = 100)

        lbl_menu_line_01 = Label(roots['root_menu'], bg=colors['dark'])
        lbl_menu_line_01.place(x = 0, y = 110, width = 610, height = 5)

        lbl_menu_line_02 = Label(roots['root_menu'], bg=colors['dark'])
        lbl_menu_line_02.place(x = 0, y = 325, width = 610, height = 5)

        lbl_credits_version = Label(roots['root_menu'], text = version, font = 'courier 12 bold', bg=colors['white'])
        lbl_credits_version.place(x = 220, y = 330, width = 170, height = 30)

        #Buttons
        btn_menu_play = Button(roots['root_menu'], text = 'Jogar', font = 'courier 20 bold', bg=colors['white'], bd=3,
                                relief='ridge', cursor='hand2', activebackground=colors['gray'],
                                command=lambda:click_show(window, directory, roots, type='game'))
        btn_menu_play.place(x = 175, y = 130, width = 260, height = 50)

        btn_menu_tutorial = Button(roots['root_menu'], text = 'Tutorial', font = 'courier 20 bold', bg=colors['white'],
                                bd=3, relief='ridge', cursor='hand2', activebackground=colors['gray'],
                                command=lambda:click_show(window, directory, roots, type='tutorial'))
        btn_menu_tutorial.place(x = 175, y = 195, width = 260, height = 50)

        btn_menu_settings = Button(roots['root_menu'], text = 'Ajustes', font = 'courier 20 bold', bg=colors['white'],
                                bd=3, relief='ridge', cursor='hand2', activebackground=colors['gray'],
                                command=lambda:click_show(window, directory, roots, type='settings'))
        btn_menu_settings.place(x = 175, y = 260, width = 260, height = 50)

        btn_menu_credits = Button(roots['root_menu'], text = 'Créditos', font = 'courier 14 bold', bg=colors['white'],
                                bd=1.5, relief='ridge', cursor='hand2', activebackground=colors['gray'],
                                command=lambda:click_show(window, directory, roots, type='credits'))
        btn_menu_credits.place(x = 0, y = 330, width = 220, height = 30)

        btn_menu_quit = Button(roots['root_menu'], text = 'Sair', font = 'courier 14 bold', bg=colors['white'],
                                bd=1.5, relief='ridge', cursor='hand2', activebackground=colors['gray'],
                                command=lambda:click_quit(window))
        btn_menu_quit.place(x = 390, y = 330, width = 220, height = 30)


    def build_game():
        global lbl_game_cpu_image, lbl_game_cpu_text, lbl_game_player_image, lbl_game_player_text
        global var_option, lbl_game_win, lbl_game_draw, lbl_game_lose
        #Data
        sub_root_data = Frame(roots['root_game'], bg=colors['light'])
        sub_root_data.place(x = 0, y = 0, width = 220, height = 325)

        lbl_game_data_title_01 = Label(sub_root_data, text = 'Resultados', font = 'courier 20 bold', bg=colors['white'],
                                        bd=5, relief='solid')
        lbl_game_data_title_01.place(x = -5, y = -5, width = 230, height = 50)

        lbl_game_data_title_02 = Label(sub_root_data, text = 'Última jogada', font = 'courier 18 bold', bg=colors['white'],
                                        bd=5, relief='solid')
        lbl_game_data_title_02.place(x = -5, y = 165, width = 230, height = 50)

        lbl_game_win = Label(sub_root_data, text=f'Vitórias: {status["win"]}', font='courier 12 bold', bg=colors['light'],
                            fg=colors['green'])
        lbl_game_win.place(x = 25, y = 55, width = 170, height = 30)

        lbl_game_draw = Label(sub_root_data, text=f'Empates:  {status["draw"]}', font='courier 12 bold', bg=colors['light'],
                            fg=colors['yellow'])
        lbl_game_draw.place(x = 25, y = 90, width = 170, height = 30)

        lbl_game_lose = Label(sub_root_data, text=f'Derrotas: {status["lose"]}', font='courier 12 bold', bg=colors['light'],
                            fg=colors['red'])
        lbl_game_lose.place(x = 25, y = 125, width = 170, height = 30)

        lbl_game_player_image = Label(sub_root_data, image = assets['question_mark_dic'], bg=colors['light'])
        lbl_game_player_image.place(x = 25, y = 220, width = 70, height = 70)

        lbl_game_player_text = Label(sub_root_data, text = 'PLAYER', font = 'courier 12 bold', bg=colors['light'])
        lbl_game_player_text.place(x = 25, y = 290, width = 70, height = 30)

        lbl_game_cpu_image = Label(sub_root_data, image = assets['question_mark_dic'], bg=colors['light'])
        lbl_game_cpu_image.place(x = 125, y = 220, width = 70, height = 70)

        lbl_game_cpu_text = Label(sub_root_data, text = 'CPU', font = 'courier 12 bold', bg=colors['light'])
        lbl_game_cpu_text.place(x = 125, y = 290, width = 70, height = 30)

        #Choice
        sub_root_choice = Frame(roots['root_game'], bg=colors['light'])
        sub_root_choice.place(x = 225, y = 0, width = 385, height = 325)

        lbl_game_choice_title = Label(sub_root_choice, text = 'Faça a sua escolha!', bd=5, relief='solid',
                                        font = 'courier 20 bold', bg=colors['white'])
        lbl_game_choice_title.place(x = -5, y = -5, width = 395, height = 50)

        lbl_game_rock = Label(sub_root_choice, text = 'Pedra', font = 'courier 12 bold', bg=colors['light'])
        lbl_game_rock.place(x = 25, y = 125, width = 70, height = 30)

        lbl_game_paper = Label(sub_root_choice, text = 'Papel', font = 'courier 12 bold', bg=colors['light'])
        lbl_game_paper.place(x = 157.5, y = 125, width = 70, height = 30)
        
        lbl_game_scissors = Label(sub_root_choice, text = 'Tesoura', font = 'courier 12 bold', bg=colors['light'])
        lbl_game_scissors.place(x = 290, y = 125, width = 70, height = 30)

        lbl_game_vs = Label(sub_root_choice, text = '- VS -', font = 'courier 20 bold', bg=colors['light'])
        lbl_game_vs.place(x = 0, y = 165, width = 385, height = 50)
        
        lbl_game_choice_cpu_image = Label(sub_root_choice, image = assets['question_mark_dic'], bg=colors['light'])
        lbl_game_choice_cpu_image.place(x = 157.5, y = 220, width = 70, height = 70)

        lbl_game_choice_cpu_text = Label(sub_root_choice, text = 'CPU', font = 'courier 12 bold', bg=colors['light'])
        lbl_game_choice_cpu_text.place(x = 157.5, y = 290, width = 70, height = 30)

        var_option = StringVar()
        var_option.set(None)

        rbt_game_rock = Radiobutton(sub_root_choice, indicatoron=0, image=assets['rock_dic'], cursor='hand2',
                                    variable = var_option, value = 'rock', bg=colors['white'], bd=2)
        rbt_game_rock.place(x = 25, y = 55, width = 70, height = 70)

        rbt_game_paper = Radiobutton(sub_root_choice, indicatoron=0, image=assets['paper_dic'], cursor='hand2',
                                    variable = var_option, value = 'paper', bg=colors['white'], bd=2)
        rbt_game_paper.place(x = 157.5, y = 55, width = 70, height = 70)

        rbt_game_scissors = Radiobutton(sub_root_choice, indicatoron=0, image=assets['scissors_dic'], cursor='hand2',
                                    variable = var_option, value = 'scissors', bg=colors['white'], bd=2)
        rbt_game_scissors.place(x = 290, y = 55, width = 70, height = 70)

        #Back_Next
        sub_root_back_next = Frame(roots['root_game'], bg=colors['dark'])
        sub_root_back_next.place(x = 0, y = 325, width = 610, height = 35)

        lbl_game_version = Label(sub_root_back_next, text = version, font = 'courier 12 bold', bg=colors['dark'],
                                fg=colors['light'])
        lbl_game_version.place(x = 220, y = 5, width = 170, height = 30)
        
        btn_game_back = Button(sub_root_back_next, text = 'Ir ao menu', font = 'courier 14 bold', bg=colors['dark'], bd=1.5,
                                 relief='ridge', cursor='hand2', activebackground=colors['gray'], fg=colors['light'],
                                command=lambda:click_show(window, directory, roots, type='menu'))
        btn_game_back.place(x = 0, y = 5, width = 220, height = 30)

        btn_game_choice = Button(sub_root_back_next, text = 'Avançar', font = 'courier 14 bold', bg=colors['dark'], bd=1.5,
                                relief='ridge', cursor='hand2', activebackground=colors['gray'], fg=colors['light'],
                                command=lambda:click_next(directory, assets))
        btn_game_choice.place(x = 390, y = 5, width = 220, height = 30)


    def build_credits():
        #Labels
        lbl_credits_title = Label(roots['root_credits'], text = '- Créditos -', font = 'courier 30 bold',
                                bg=colors['white'], bd=1,relief='sunken')
        lbl_credits_title.place(x = 5, y = 5, width = 600, height = 100)
        
        lbl_credits_line_01 = Label(roots['root_credits'], bg=colors['dark'])
        lbl_credits_line_01.place(x = 0, y = 110, width = 610, height = 5)

        lbl_credits_line_02 = Label(roots['root_credits'], bg=colors['dark'])
        lbl_credits_line_02.place(x = 0, y = 325, width = 610, height = 35)

        lbl_credits_text = Label(roots['root_credits'], text = text_credits, font='courier 18 italic', bg=colors['white'])
        lbl_credits_text.place(x = 5, y = 120, width = 600, height = 200)

        lbl_credits_version = Label(roots['root_credits'], text = version, font = 'courier 12 bold', bg=colors['dark'],
                                        fg=colors['light'])
        lbl_credits_version.place(x = 220, y = 330, width = 170, height = 30)

        #Button
        btn_credits_back = Button(roots['root_credits'], text = 'Ir ao menu', font = 'courier 14 bold', bg=colors['dark'],
                                cursor='hand2', activebackground=colors['gray'], bd=1.5, relief='ridge', fg=colors['light'],
                                command=lambda:click_show(window, directory, roots, type='menu'))
        btn_credits_back.place(x = 0, y = 330, width = 220, height = 30)


    def build_tutorial():
        #Labels
        text_tutorial = 'Você tem algum problema? Como assim você não sabe o que\n' +\
                        'é Pedra Papel ou Tesoura? Você não teve infância não?\n\n'+\
                        'Bem... Em resumo é isto:\n' +\
                        'Verde ganha, Amarelo empata e Vermelho perde.'

        lbl_tutorial_title = Label(roots['root_tutorial'], text = text_tutorial, font = 'courier 12 bold',
                                bg=colors['white'], bd=1,relief='sunken')
        lbl_tutorial_title.place(x = 5, y = 5, width = 600, height = 100)
        
        lbl_tutorial_line_01 = Label(roots['root_tutorial'], bg=colors['dark'])
        lbl_tutorial_line_01.place(x = 0, y = 110, width = 610, height = 5)

        lbl_tutorial_line_02 = Label(roots['root_tutorial'], bg=colors['dark'])
        lbl_tutorial_line_02.place(x = 0, y = 325, width = 610, height = 35)

        lbl_tutorial_line_03 = Label(roots['root_tutorial'], bg=colors['dark'])
        lbl_tutorial_line_03.place(x = 0, y = 220, width = 610, height = 5)

        lbl_tutorial_version = Label(roots['root_tutorial'], text = version, font = 'courier 12 bold', bg=colors['dark'],
                                    fg=colors['light'])
        lbl_tutorial_version.place(x = 220, y = 330, width = 170, height = 30)

        #Paper x Rock
        lbl_tutorial_versus_01 = Label(roots['root_tutorial'], text = 'VS', font = 'courier 10 bold', bg = colors['white'])
        lbl_tutorial_versus_01.place(x = 80, y = 145, width = 40, height = 40)

        lbl_tutorial_paper_01 = Label(roots['root_tutorial'], image=assets['paper_dic'], bg=colors['white'])
        lbl_tutorial_paper_01.place(x = 10, y = 125, width = 70, height = 70)

        lbl_tutorial_paper_01_text = Label(roots['root_tutorial'], text = 'Papel', font='courier 10 bold',
                                            fg=colors['green'], bg=colors['white'])
        lbl_tutorial_paper_01_text.place(x = 10, y = 195, width = 70, height = 20)

        lbl_tutorial_rock_01 = Label(roots['root_tutorial'], image=assets['rock_dic'], bg=colors['white'])
        lbl_tutorial_rock_01.place(x = 120, y = 125, width = 70, height = 70)

        lbl_tutorial_rock_01_text = Label(roots['root_tutorial'], text = 'Pedra', font='courier 10 bold',
                                            fg=colors['red'], bg=colors['white'])
        lbl_tutorial_rock_01_text.place(x = 120, y = 195, width = 70, height = 20)

        #Scissors x Paper
        lbl_tutorial_versus_02 = Label(roots['root_tutorial'], text = 'VS', font = 'courier 10 bold', bg = colors['white'])
        lbl_tutorial_versus_02.place(x = 290, y = 145, width = 40, height = 40)

        lbl_tutorial_scissors_01 = Label(roots['root_tutorial'], image=assets['scissors_dic'], bg=colors['white'])
        lbl_tutorial_scissors_01.place(x = 220, y = 125, width = 70, height = 70)

        lbl_tutorial_scissors_01_text = Label(roots['root_tutorial'], text = 'Tesoura', font='courier 10 bold',
                                            fg=colors['green'], bg=colors['white'])
        lbl_tutorial_scissors_01_text.place(x = 220, y = 195, width = 70, height = 20)

        lbl_tutorial_paper_02 = Label(roots['root_tutorial'], image=assets['paper_dic'], bg=colors['white'])
        lbl_tutorial_paper_02.place(x = 330, y = 125, width = 70, height = 70)

        lbl_tutorial_paper_02_text = Label(roots['root_tutorial'], text = 'Papel', font='courier 10 bold',
                                            fg=colors['red'], bg=colors['white'])
        lbl_tutorial_paper_02_text.place(x = 330, y = 195, width = 70, height = 20)

        #Rock x Scissors
        lbl_tutorial_versus_03 = Label(roots['root_tutorial'], text = 'VS', font = 'courier 10 bold', bg = colors['white'])
        lbl_tutorial_versus_03.place(x = 490, y = 145, width = 40, height = 40)

        lbl_tutorial_rock_02 = Label(roots['root_tutorial'], image=assets['rock_dic'], bg=colors['white'])
        lbl_tutorial_rock_02.place(x = 420, y = 125, width = 70, height = 70)

        lbl_tutorial_rock_02_text = Label(roots['root_tutorial'], text = 'Pedra', font='courier 10 bold',
                                            fg=colors['green'], bg=colors['white'])
        lbl_tutorial_rock_02_text.place(x = 420, y = 195, width = 70, height = 20)

        lbl_tutorial_scissors_02 = Label(roots['root_tutorial'], image=assets['scissors_dic'], bg=colors['white'])
        lbl_tutorial_scissors_02.place(x = 530, y = 125, width = 70, height = 70)

        lbl_tutorial_scissors_02_text = Label(roots['root_tutorial'], text = 'Tesoura', font='courier 10 bold',
                                            fg=colors['red'], bg=colors['white'])
        lbl_tutorial_scissors_02_text.place(x = 530, y = 195, width = 70, height = 20)

        #Rock x Rock
        lbl_tutorial_versus_04 = Label(roots['root_tutorial'], text = 'VS', font = 'courier 10 bold', bg = colors['white'])
        lbl_tutorial_versus_04.place(x = 80, y = 250, width = 40, height = 40)

        lbl_tutorial_rock_03 = Label(roots['root_tutorial'], image=assets['rock_dic'], bg=colors['white'])
        lbl_tutorial_rock_03.place(x = 10, y = 230, width = 70, height = 70)

        lbl_tutorial_rock_03_text = Label(roots['root_tutorial'], text = 'Pedra', font='courier 10 bold',
                                            fg=colors['yellow'], bg=colors['white'])
        lbl_tutorial_rock_03_text.place(x = 10, y = 300, width = 70, height = 20)

        lbl_tutorial_rock_04 = Label(roots['root_tutorial'], image=assets['rock_dic'], bg=colors['white'])
        lbl_tutorial_rock_04.place(x = 120, y = 230, width = 70, height = 70)

        lbl_tutorial_rock_04_text = Label(roots['root_tutorial'], text = 'Pedra', font='courier 10 bold',
                                            fg=colors['yellow'], bg=colors['white'])
        lbl_tutorial_rock_04_text.place(x = 120, y = 300, width = 70, height = 20)

        #Paper x Paper
        lbl_tutorial_versus_05 = Label(roots['root_tutorial'], text = 'VS', font = 'courier 10 bold', bg = colors['white'])
        lbl_tutorial_versus_05.place(x = 290, y = 250, width = 40, height = 40)

        lbl_tutorial_paper_03 = Label(roots['root_tutorial'], image=assets['paper_dic'], bg=colors['white'])
        lbl_tutorial_paper_03.place(x = 220, y = 230, width = 70, height = 70)

        lbl_tutorial_paper_03_text = Label(roots['root_tutorial'], text = 'Papel', font='courier 10 bold',
                                            fg=colors['yellow'], bg=colors['white'])
        lbl_tutorial_paper_03_text.place(x = 220, y = 300, width = 70, height = 20)

        lbl_tutorial_paper_04 = Label(roots['root_tutorial'], image=assets['paper_dic'], bg=colors['white'])
        lbl_tutorial_paper_04.place(x = 330, y = 230, width = 70, height = 70)

        lbl_tutorial_paper_04_text = Label(roots['root_tutorial'], text = 'Papel', font='courier 10 bold',
                                            fg=colors['yellow'], bg=colors['white'])
        lbl_tutorial_paper_04_text.place(x = 330, y = 300, width = 70, height = 20)

        #Scissors x Scissors
        lbl_tutorial_versus_06 = Label(roots['root_tutorial'], text = 'VS', font = 'courier 10 bold', bg = colors['white'])
        lbl_tutorial_versus_06.place(x = 490, y = 250, width = 40, height = 40)

        lbl_tutorial_scissors_03 = Label(roots['root_tutorial'], image=assets['scissors_dic'], bg=colors['white'])
        lbl_tutorial_scissors_03.place(x = 420, y = 230, width = 70, height = 70)

        lbl_tutorial_scissors_03_text = Label(roots['root_tutorial'], text = 'Tesoura', font='courier 10 bold',
                                            fg=colors['yellow'], bg=colors['white'])
        lbl_tutorial_scissors_03_text.place(x = 420, y = 300, width = 70, height = 20)

        lbl_tutorial_scissors_04 = Label(roots['root_tutorial'], image=assets['scissors_dic'], bg=colors['white'])
        lbl_tutorial_scissors_04.place(x = 530, y = 230, width = 70, height = 70)

        lbl_tutorial_scissors_04_text = Label(roots['root_tutorial'], text = 'Tesoura', font='courier 10 bold',
                                            fg=colors['yellow'], bg=colors['white'])
        lbl_tutorial_scissors_04_text.place(x = 530, y = 300, width = 70, height = 20)

        #Button
        btn_tutorial_back = Button(roots['root_tutorial'], text = 'Ir ao menu', font = 'courier 14 bold', bg=colors['dark'],
                                cursor='hand2', activebackground=colors['gray'], bd=1.5, relief='ridge', fg=colors['light'],
                                command=lambda:click_show(window, directory, roots, type='menu'))
        btn_tutorial_back.place(x = 0, y = 330, width = 220, height = 30)


    def build_settings():
        lbl_settings_title = Label(roots['root_settings'], text = '- Ajustes -', font = 'courier 30 bold',
                                bg=colors['white'], bd=1,relief='sunken')
        lbl_settings_title.place(x = 5, y = 5, width = 600, height = 100)
        
        lbl_settings_line_01 = Label(roots['root_settings'], bg=colors['dark'])
        lbl_settings_line_01.place(x = 0, y = 110, width = 610, height = 5)

        lbl_settings_line_02 = Label(roots['root_settings'], bg=colors['dark'])
        lbl_settings_line_02.place(x = 0, y = 325, width = 610, height = 35)

        lbl_settings_text = Label(roots['root_settings'], font='courier 22', bg=colors['white'],
        text = 'Para reiniciar a contagem de\nvitórias, empates e derrotas,\nclique no botão abaixo:')
        lbl_settings_text.place(x = 5, y = 120, width = 600, height = 125)

        lbl_settings_version = Label(roots['root_settings'], text = version, font = 'courier 12 bold', bg=colors['dark'], 
                                        fg=colors['light'])
        lbl_settings_version.place(x = 220, y = 330, width = 170, height = 30)

        #Buttons
        btn_settings_reset = Button(roots['root_settings'], text = 'Reset', font = 'courier 20 bold', bg=colors['white'],
                                cursor='hand2', activebackground=colors['gray'], bd=3, relief='ridge',
                                command=lambda:click_reset(assets))
        btn_settings_reset.place(x = 175, y = 260, width = 260, height = 50)

        btn_settings_back = Button(roots['root_settings'], text = 'Ir ao menu', font = 'courier 14 bold', bg=colors['dark'],
                                cursor='hand2', activebackground=colors['gray'], bd=1.5, relief='ridge', fg=colors['light'],
                                command=lambda:click_show(window, directory, roots, type='menu'))
        btn_settings_back.place(x = 0, y = 330, width = 220, height = 30)

    build_menu()
    build_game()
    build_credits()
    build_tutorial()
    build_settings()

#Functions - Click __________________________________________________________________________________________

def click_show(window, directory, roots, type):
    global var_option, status
    #Variables
    title = window_title(type)
    icon = randint(1, 3)
    var_option.set(None)

    #Window
    window.iconbitmap(directory + f'/Assets/icon_0{icon}.ico')
    window.title(title)

    #Roots
    for root in roots:
        roots[root].place_forget()

    roots[f'root_{type}'].place(x = 5, y = 5, width = 610, height = 360)


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
        lbl_game_player_text['fg'] = colors['yellow']
        lbl_game_cpu_text['fg'] = colors['yellow']

    ##Win
    elif player == 'rock' and cpu == 'scissors' or player == 'scissors' and cpu == 'paper' or player == 'paper' and cpu == 'rock':
        soundEffect(directory, soundEffect = 'win')
        status['win'] += 1
        lbl_game_player_text['fg'] = colors['green']
        lbl_game_cpu_text['fg'] = colors['red']

    ##Lose
    elif player == 'scissors' and cpu == 'rock' or player == 'paper' and cpu == 'scissors' or player == 'rock' and cpu == 'paper':
        soundEffect(directory, soundEffect = 'lose')
        status['lose'] += 1
        lbl_game_player_text['fg'] = colors['red']
        lbl_game_cpu_text['fg'] = colors['green']

    #Show Status
    lbl_game_win['text'] = f'Vitórias: {status["win"]}'
    lbl_game_draw['text'] = f'Empates:  {status["draw"]}'
    lbl_game_lose['text'] = f'Derrotas: {status["lose"]}'


def click_reset(assets):
    global status
    #Images
    lbl_game_player_image['image'] = assets['question_mark_dic']
    lbl_game_cpu_image['image'] = assets['question_mark_dic']

    #Text
    lbl_game_player_text['fg'] = colors['dark']
    lbl_game_cpu_text['fg'] = colors['dark']
    
    #Status
    status = {'win' : 0, 'draw' : 0, 'lose' : 0}
    lbl_game_win['text'] = f'Vitórias: {status["win"]}'
    lbl_game_draw['text'] = f'Empates:  {status["draw"]}'
    lbl_game_lose['text'] = f'Derrotas: {status["lose"]}'

    #PopUp
    messagebox.showinfo(title = 'Reset', message = 'Os valores foram resetados com êxito!')


def click_quit(window):
    ok_cancel_quit = messagebox.askokcancel(title = "Sair?", message = "Você realmente deseja sair?\t\t",
    detail = "Desde já obrigado por jogar")
    if ok_cancel_quit == True:
        window.destroy()

#Others Functions ___________________________________________________________________________________________

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


def window_title(type):
    if type == 'menu':
        title = 'Menu Inicial'
    elif type == 'game':
        title = 'Rock - Paper - Scissors'
    elif type == 'credits':
        title = 'Créditos'
    elif type == 'tutorial':
        title = 'Tutorial'
    elif type == 'settings':
        title = 'Ajustes'
    else:
        title = ''

    return title

