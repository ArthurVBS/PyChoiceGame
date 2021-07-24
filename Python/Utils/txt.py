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
            title['text'] = 'Vocês estão caminhando a um certo tempo, tanto que\n' +\
                            'já está entardecendo, além do mais vocês estão com\n' +\
                            'bastante fome. Vocês encontram algumas frutinhas\n' +\
                            'azuis em um arbusto que aparentam ser comestíveis.'

            option_A['text'] = 'Pegar as frutinhas do arbusto e\nsaciar a fome;'
            option_B['text'] = 'Ignorar as frutinhas e seguir em\nfrente;'
            option_C['text'] = 'Pegar alguma comida da mochila;'

        elif level == 2:
            title['text'] = 'Até aqui o sol as acompanhava, porém a noite vem\n' +\
                            'a espreita, é necessário parar e dormir, vocês\n' +\
                            'observam uma caverna, uma antiga casa inacabada\n' +\
                            'e um local no chão da floresta para poder dormir.'

            option_A['text'] = 'Dormir na caverna;'
            option_B['text'] = 'Dormir na casa inacabada;'
            option_C['text'] = 'Dormir no chão da floresta;'

        elif level == 3:
            title['text'] = 'Após acordar e começar a caminhar em busca de uma\n'  +\
                            'saída, você ouve um uivo, paralisada, você observa\n' +\
                            'que esse uivo vem de um lobo filhote preso a uma\n' +\
                            'armadilha de urso.'

            option_A['text'] = 'Salvar o lobinho daquele sofrimento;'
            option_B['text'] = 'Seguir em frente, como se nada\ntivesse ocorrido;' 
            option_C['text'] = 'Matar o lobinho e pegar sua carne\ne couro;'

        elif level == 4:
            title['text'] = 'Seguindo a caminhada, um toró toma a floresta.\n' +\
                            'Ao procurar um lugar para se resguardar você\n' +\
                            'encontra um abrigo abandonado, aparentemente\n' +\
                            'seguro, apesar de estar bem sujo.'

            option_A['text'] = 'Entrar no abrigo, explorar e\nesperar a chuva passar;'
            option_B['text'] = 'Seguir adiante, apesar da chuva\npesada;' 
            option_C['text'] = 'Esperar a chuva passar na\nsacada do abrigo;'

        elif level == 5:
            title['text'] = 'Após a longa chuva você se depara com um grande\n' +\
                            'e fundo riacho, há uma velha ponte suspensa,\n' +\
                            'uma margem bem ao longe e uma parte que é\n' +\
                            'aparentemente rasa.'

            option_A['text'] = 'Atravessar pela velha ponte\nsuspensa;'
            option_B['text'] = 'Atravessar pela margem distante;' 
            option_C['text'] = 'Atravessar pela parte que\naparenta ser mais rasa;'

        elif level == 6:
            title['text'] = 'Ao caminhar você sente um fio esticar em sua\n' +\
                            'perna, seu corpo para e reflete rapidamente\n' +\
                            'no que deve fazer, caso seja uma armadilha...'

            option_A['text'] = 'Avançar, ignorando o fio;'
            option_B['text'] = 'Voltar e passar por cima do fio;' 
            option_C['text'] = 'Caminhar até a fonte do fio e\ndesarma-lo;'


def show_top_level(directory, world, level, option, rand, items_values, vol):
    txt_result = 'Nothing'
    losewin_heart = 0
    losewin_food = 0

    if world == 1:
        if level == 1:
            if option == 'A':
                soundEffect(directory, vol, soundEffect = 'Door')

                if rand == 1 or rand == 2:
                    txt_result = 'As frutinhas não eram tão\ncomestíveis assim.'
                    losewin_heart = -10
                    losewin_food = 0
                elif rand == 3:
                    txt_result = 'As frutinhas até que eram\ncomestíveis.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'As frutinhas são simplesmente\ndeliciosas, levarei um pouco\npara mais tarde.'
                    losewin_heart = 0
                    losewin_food = 1

    items_values['heart'] += losewin_heart
    items_values['food'] += losewin_food

    resume = {
        'title' : f'Level {world}-{level} {option}', 'txt_result' : txt_result,
        'losewin_heart' : losewin_heart, 'losewin_food' : losewin_food}
        
    return resume


def show_history(history_widgets, page, world):
    title = history_widgets['lbl_his_main']
    history = history_widgets['lbl_his_text']

    if world == 1:
        title['text'] = '- A chegada -'

        if page == 0:
            history['text']='Após uma longa viagem de intercambio,\n' +\
                            'Sam e Annie chegam a uma bela cidade.\n\n' +\
                            'Estabelendo-se no hotel e depois de\n' +\
                            'fazer o check-in, elas elaboram o\n' +\
                            'que vão fazer no dia seguinte.\n'

        elif page == 1:
            history['text']='Elas decidiram fazer uma trilha\n' +\
                            'por uma famosa floresta, afim de\n' +\
                            'conhecer a fauna e a flora local.\n\n'+\
                            'Elas entraram em contato com um\n' +\
                            'guia para as conduzir pela trilha.\n'

        elif page == 2:
            history['text']='No dia seguinte, iniciou-se a trilha.\n\n' +\
                            'Tudo ia nos conformes até que em uma\n' +\
                            'parte densa da floresta as meninas\n' +\
                            'após tanto conversar, se distrairam\n' +\
                            'e não encontraram mais o guia.\n'

        elif page == 3:
            history['text']='Elas gritaram pelo john, o guia, porém\n' +\
                            'sem respostas, elas se cansam e decidem\n' +\
                            'voltar por onde vieram.\n\n' +\
                            'Após uma hora de caminhada elas se\n' +\
                            'dão conta que estão perdidas.\n'

        elif page == 4:
            history['text']='Desnorteadas naquela grande e densa\n' +\
                            'floresta, elas optam por seguir num\n' +\
                            'caminho que aparenta ser o correto.\n\n' +\
                            'Elas possuem somente uma chave, um\n' +\
                            'isqueiro e algumas comidas na mochila.\n'
    
    elif world == 2:
        title['text'] = '- Aterrorizada -'
        history['text']=''

    elif world == 3:
        title['text'] = '- Um caminho -'
        history['text']=''

    elif world == 4:
        title['text'] = '- Uma saída -'
        history['text']=''
    

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
                                                        'principal do jogo \'Retornar ao Menu\' para voltar.'
