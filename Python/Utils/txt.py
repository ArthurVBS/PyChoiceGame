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
