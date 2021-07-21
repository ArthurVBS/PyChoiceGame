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


def show_introduction():
    print('hi')


def show_introduction(tutorial_widgets, page):
    if page == 0:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'Hello'

    elif page == 1:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'ih'

    elif page == 2:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'TV'

    elif page == 3:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'Tel'

    elif page == 4:
        tutorial_widgets['lbl_main_text_tut']['text'] = 'Everyone'

    elif page == 5:
        tutorial_widgets['lbl_main_text_tut']['text'] = f'13215465 {page}'

        tutorial_widgets['rb_option_A_tut']['text'] = 'Essa é a 1º opção'
        tutorial_widgets['rb_option_B_tut']['text'] = 'Essa é a 2º opção'
        tutorial_widgets['rb_option_C_tut']['text'] = 'Essa é a 3º opção'

    elif page == 6:
        tutorial_widgets['lbl_main_text_tut']['text'] = f'859215 {page}'
