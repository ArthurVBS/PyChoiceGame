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
            title['text'] = 'Após acordar e começar a caminhar em busca de sua\n'  +\
                            'amiga, você ouve um uivo. Paralisada, você observa\n' +\
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
    losewin_heart = losewin_food = 0
    new_item = new_key =  None
    txt_result = 'Nothing'
    game_over = False

    if world == 1:
        if level == 1:
            if option == 'A':
                if rand == 1 or rand == 2:
                    txt_result = 'As frutinhas não eram tão\ncomestíveis assim.'
                    losewin_heart = -10
                    losewin_food = 0
                elif rand == 3:
                    txt_result = 'As frutinhas até que eram\ncomestíveis.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'As frutinhas são simplesmente\ndeliciosas, levaremos um pouco\npara mais tarde.'
                    losewin_heart = 0
                    losewin_food = 1

            elif option == 'B':
                txt_result = 'A caminhada é longa e a\nfome é sua inimiga, ignora-lá\né custoso.'
                losewin_heart = -10
                losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Uma simples fruta, isso\nsacia a fome.'
                    losewin_heart = 0
                    losewin_food = -1
                elif rand == 4:
                    txt_result = 'Guloseimas são tão gostosas,\npegaremos só mais uma, ~Ops~\nacabamos exagerando...'
                    losewin_heart = 0
                    losewin_food = -2

        elif level == 2:
            if option == 'A':
                if items_values['food'] >= 6:
                    txt_result = 'Um urso é atraído pela\nsua comida e tem um\nbelo banquete.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                else:
                    txt_result = 'A longa noite passou num\ninstante, mas você se dá\nconta do sumiço de sua amiga.\n' +\
                                'Você observa o óculos dela\nquebrado em uma direção...'
                    losewin_heart = 0
                    losewin_food = 0

            elif option == 'B':
                txt_result = 'A longa noite passou num\ninstante, mas você se dá\nconta do sumiço de sua amiga.\n' +\
                            'Você observa o óculos dela\nquebrado em uma direção...'
                losewin_heart = 0
                losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'A longa noite passou num\ninstante, mas você se dá\nconta do sumiço de sua amiga.\n' +\
                                'Você observa o óculos dela\nquebrado em uma direção...'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'O chão é o lar de\nmuitos animais, inclusive\nda cobra que as deu\num beijinho de boa noite.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True

        elif level == 3:
            if option == 'A':
                new_item = 'future_friendship'
                if rand == 1 or rand == 2:
                    txt_result = 'Você consegue libertar\no lobinho que corre de volta\npara a mata.'
                    losewin_heart = 0
                    losewin_food = 0

                elif rand == 3 or rand == 4:
                    txt_result = 'Ao libertar o lobinho você se\nmachuca com a armadilha, mas\nconsegue libertar o lobinho que\n' +\
                                    'corre de volta para a mata.'
                    losewin_heart = -10
                    losewin_food = 0

            elif option == 'B':
                txt_result = 'Nada ocorre, você segue\nem frente.'
                losewin_heart = 0
                losewin_food = 0

            elif option == 'C':
                new_item = 'wolfhide'
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'O lobo dá seu último uivo e\nvocê consegue o seu couro e\ncarne, então você parte em\nfrente.'
                    losewin_heart = 0
                    losewin_food = 1
                elif rand == 4:
                    txt_result = 'O lobo dá seu último uivo,\nvocê pega o seu couro e carne,\nmas ao longe vem vindo outro\n' +\
                                    'lobo então você corre, foge,\nmas havia se arranhado na mata.'
                    losewin_heart = -20
                    losewin_food = 1

        elif level == 4:
            if option == 'A':
                soundEffect(directory, vol, soundEffect = "Door")
                if rand == 1:
                    txt_result = 'Em um vão da casa você\nencontra um remédio.'
                    losewin_heart = 10
                    losewin_food = 0
                elif rand == 2:
                    txt_result = 'Em um vão da casa você\nencontra uma fruta intacta.'
                    losewin_heart = 0
                    losewin_food = 1
                elif rand == 3:
                    txt_result = 'Em um vão da casa você\ntropeça e se machuca.'
                    losewin_heart = -10
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Você não acho nada de\ninteressante na casa.'
                    losewin_heart = 0
                    losewin_food = 0
                
            elif option == 'B':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'A constante chuva a\ndeixou resfriada.'
                    losewin_heart = -20
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Você andou por debaixo\ndas copas e você nem notou\na chuva constante.'
                    losewin_heart = 0
                    losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'A chuva passou e você\nsegue o seu caminho.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'A chuva veio, mas a\ndona aranha continuou a\nsubir e a picou.'
                    losewin_heart = -20
                    losewin_food = 0
         
        elif level == 5:
            if option == 'A':
                if rand == 1 or rand == 2:
                    txt_result = 'No fim da ponte você\nolha para trás e percebe\nque deu tudo certo.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 3 or rand == 4:
                    txt_result = 'No fim da ponte, a\nmadeira sobre seu pé racha\nao meio e você cai no riacho,\n' +\
                                    'próximo a margem você\nconsegue se salvar.'
                    losewin_heart = -10
                    losewin_food = 0

            elif option == 'B':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Ao caminhar tanto você\ncomeça a sentir muita fome,\nportanto você come algo\n' +\
                                    'de sua mochila.'
                    losewin_heart = 0
                    losewin_food = -2
                elif rand == 4:
                    txt_result = 'Ao caminhar tanto você\ncomeça a sentir muita fome,\nentão você come algo da\n' +\
                                    'mochila, além disso\nseus pés estão doendo.'
                    losewin_heart = -10
                    losewin_food = -2

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Não era tão raso assim...\nA correnteza a leva e você\nse afoga.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                elif rand == 4:
                    txt_result = 'Shalow Now...\nVocê consegue atravessar\ntranquilamente.'
                    losewin_heart = 0
                    losewin_food = 0

        elif level == 6:
            new_item = 'shotgun'
            new_key = 'S'

            if option == 'A':
                txt_result = 'Uma mina explode em sua\nfrente, devido a sua falta\nde cuidado.'
                losewin_heart = 0
                losewin_food = 0
                game_over = True

            elif option == 'B':
                txt_result = 'É voltando que se pega\nimpulso, você passa pela\narmadilha com calma e tudo\n' +\
                                'ocorre bem.'
                losewin_heart = 0
                losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Você segue até a fonte do\nfio e encontra uma armadilha\nplantada, então você\n' +\
                                    'decide desarmar, com êxito\nvocê desarma a armadilha.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Você segue até a fonte do\nfio e encontra uma armadilha\nplantada, então você\n' +\
                                    'decide desarmar, com êxito\na mina terrestre é acionada.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                
    else:
        soundEffect(directory, vol, soundEffect = 'Door')


    items_values['heart'] += losewin_heart
    items_values['food'] += losewin_food

    if new_item != None:
        items_values[f'item_{new_item}'] = True
    if new_key != None:
        items_values[f'key_{new_key}'] = True

    resume = {
        'title' : f'Level {world}-{level} {option}', 'txt_result' : txt_result,
        'new_item' : new_item, 'new_key' : new_key, 'game_over' : game_over,
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
            history['text']='Elas gritaram pelo John, o guia, porém\n' +\
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
        title['text'] = '- Pegadas -'
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
