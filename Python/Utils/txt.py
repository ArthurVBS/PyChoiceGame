#Import - Packages __________________________________________________________________________________________

try:
    from audio import soundEffect
except:
    from Utils.audio import soundEffect

#Functions - Texts __________________________________________________________________________________________

def show_menu_options(world, level, game_widgets):
    title = game_widgets['lbl_main_text']
    option_A = game_widgets['rb_option_A']
    option_B = game_widgets['rb_option_B']
    option_C = game_widgets['rb_option_C']

    if world == 1:
        if level == 1:
            title['text'] = 'Você está caminhando a um certo tempo, o seu\n' +\
                            'estômago ronca. Você encontra algumas frutinhas\n' +\
                            'azuis em um arbusto que podem ser comestíveis.'

            option_A['text'] = 'Pegar as frutinhas do arbusto e\nsaciar a sua fome;'
            option_B['text'] = 'Ignorar as frutinhas e seguir em\nfrente;'
            option_C['text'] = 'Pegar alguma comida da mochila;'

        elif level == 2:
            title['text'] = 'HI, everyone'

            option_A['text'] = 'Hi'
            option_B['text'] = 'Hi'
            option_C['text'] = 'Hi'

        elif level == 3:
            print('hi')


def show_top_level(directory, world, level, option, rand, items_values, vol):
    txt_result = 'Nothing'
    losewin_heart = 0
    losewin_food = 0

    if world == 1:
        if level == 1:
            if option == 'A':
                soundEffect(directory, vol, soundEffect = "Door")
                if rand == 1 or rand == 2:
                    txt_result = 'HI'
                    losewin_heart = -10
                    losewin_food = -2
                elif rand == 3 or rand == 4:
                    txt_result = 'God be with you'
                    losewin_heart = -20
                    losewin_food = 1


    items_values['heart'] += losewin_heart
    items_values['food'] += losewin_food

    resume = {
        'title' : f'Level {world}-{level} {option}', 'txt_result' : txt_result,
        'losewin_heart' : losewin_heart, 'losewin_food' : losewin_food}
        
    return resume


def show_history(history_widgets, page, world):
    if world == 1:
        if page == 0:
            history_widgets['lbl_his_text']['text'] = 'Hello'
        elif page == 1:
            history_widgets['lbl_his_text']['text'] = f'h51 - {page}'
        elif page == 2:
            history_widgets['lbl_his_text']['text'] = f'h57 - {page}'
        elif page == 3:
            history_widgets['lbl_his_text']['text'] = f'h54 - {page}'
        elif page == 4:
            history_widgets['lbl_his_text']['text'] = f'h56 - {page}'
    else:
        history_widgets['lbl_his_text']['text'] = f'Nothing - página {page}'
    

def show_tutorial(tutorial_widgets, page):
    if page == 0:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'O jogo consiste em escolhas, você deve decidir com\n'+\
                                                        'sabedoria, pois suas escolhas influenciarão a sua \n' +\
                                                        'grande jornada! Aperte \'Avançar\' para prosseguir.'

    elif page == 1:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'Ali está a sua saúde e a comida em sua mochila.\n'+\
                                                        'Suas escolhas alterarão os valores, portanto saiba\n' +\
                                                        'fazer ótimas escolhas! \'Avançar\' para prosseguir.'

    elif page == 2:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'Em sua jornada você encontrará itens especiais e\n' +\
                                                        'também algumas chaves, por meio deles sua jornada\n' +\
                                                        'irá se tornar única! \'Avançar\' para prosseguir.'

    elif page == 3:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'Toda aventura é composta por caminhos, mesmo que\n' +\
                                                        'eles sejam retilíneos, o importante é sempre ir\n' +\
                                                        'adiante! \'Avançar\' para prosseguir.'

    elif page == 4:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'Sua jornada se passará em cenários distintos, como\n' +\
                                                        'uma densa floresta, o alto de uma montanha ou até\n' +\
                                                        'uma mina abandonada. \'Avançar\' para prosseguir.'

    elif page == 5:
        tutorial_widgets['lbl_main_text_tut']['text'] = '\'Escolhas\', o tema principal dessa grande aventura,\n' +\
                                                        'por meio delas você abrirá oportunidades e sentirá\n' +\
                                                        'o \'efeito borboleta\'! \'Avançar\' para prosseguir.'

        tutorial_widgets['rb_option_A_tut']['text'] = 'Essa é a 1º opção'
        tutorial_widgets['rb_option_B_tut']['text'] = 'Essa é a 2º opção'
        tutorial_widgets['rb_option_C_tut']['text'] = 'Essa é a 3º opção'

    elif page == 6:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'Pronto! Agora você já compreende tudo sobre a sua\n' +\
                                                        'jornada. Inicie essa grande aventura indo ao menu\n' +\
                                                        'principal do jogo \'Retornar ao menu\' para voltar.'
