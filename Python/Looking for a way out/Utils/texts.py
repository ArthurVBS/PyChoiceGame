#Import - Packages __________________________________________________________________________________________

try:
    from sounds import soundEffect
except:
    from Utils.sounds import soundEffect

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

    elif world == 2:
        if level == 1:
            title['text'] = 'Seguindo pela trilha a fome começa a bater na porta.\n' +\
                            'Você observa a sua esquerda e a sua direita, alguns\n' +\
                            'cogumelos de cores distintas - Azuis e Vermelhos -\n' +\
                            'que estão crescendo nos troncos das árvores.'
            
            option_A['text'] = 'Comer o cogumelo Azul;'
            option_B['text'] = 'Comer o cogumelo Vermelho;'
            option_C['text'] = 'Pegar alguma comida da mochila;'

        elif level == 2:
            title['text'] = 'Seguindo em frente você se depara com uma grande\n' +\
                            'trifurcação, há um caminho cheio de flores com\n' +\
                            'um aroma forte, há um caminho cheio de espinhos\n' +\
                            'e também há caminho em direção a um lamaceiro.'

            option_A['text'] = 'Passar pelas flores de aroma\nforte;'
            option_B['text'] = 'Passar pelo caminho espinhoso;'
            option_C['text'] = 'Passar por um lamaceiro;'

        elif level == 3:
            title['text'] = 'Após a trifurcação, você observa um grande urso\n' +\
                            'passeando pela trilha, estando ele de costas para\n' +\
                            'você e indo em direção ao pico da montanha, você\n' +\
                            'decide...'

            option_A['text'] = 'Tentar matar o urso atirando pelas\ncostas e seguir em frente;'
            option_B['text'] = 'Parar onde está e esperar o urso\nsair da trilha;'
            option_C['text'] = 'Tentar passar pelo urso arrodeando\npelo matagal ao lado da trilha;'

        elif level == 4:
            title['text'] = 'Seguindo pela trilha você chega ao fim dela, pois\n' +\
                            'tornou-se muito ingrime para subir, você observa\n' +\
                            'ao lado, uma cabana abandonada caindo aos pedaços\n' +\
                            'que permitirá passar e um local para tentar escalar.'

            option_A['text'] = 'Entrar na cabana, a explorar e ir\naté a saída;'
            option_B['text'] = 'Entrar na cabana e ir direto para\na saída;'
            option_C['text'] = 'Tentar escalar pelo muro de gelo;'

        elif level == 5:
            title['text'] = 'Próximo ao topo da montanha você chega ao antigo\n' +\
                            'cemitério da capela, você observa um frasco de\n' +\
                            'remédio em cima de um túmulo e você se questiona\n' +\
                            'se deve pegá-lo, deixá-lo ali ou jogá-lo fora.'

            option_A['text'] = 'Pegar o remédio e o ingerir;'
            option_B['text'] = 'Não pegar o remédio e seguir;'
            option_C['text'] = 'Pegar o remédio e jogá-lo ao longe;'

        elif level == 6:
            title['text'] = 'Após passar pelo cemitério da capela, você chega\n' +\
                            'finalmente a capela, ao adentrar você observa que\n' +\
                            'ela está completamente escura e você sente também\n' +\
                            'um cheiro esquisito vindo dos fundos...'

            option_A['text'] = 'Usar o isqueiro para iluminar a capela\ne seguir até a saída;'
            option_B['text'] = 'Tentar seguir até a saída pelo meio\nda capela escura;'
            option_C['text'] = 'Seguir até fonte do cheiro e depois\nprocurar a saída da capela;'

    elif world == 3:
        if level == 1:
            title['text'] = 'Ao chegar na mina abandonada você se depara com\n' +\
                            'um baú bem enferrujado e que apesar de não\n' +\
                            'possuir uma tranca aparenta ser difícil a sua\n' +\
                            'abertura...'

            option_A['text'] = 'Utilizar algo como uma ferramenta\npara tentar abrir o baú;'
            option_B['text'] = 'Utilizar alguma pedra próxima para\ntentar abrir o baú;'
            option_C['text'] = 'Simplesmente ignorar o baú e seguir\nadiante;'

        elif level == 2:
            title['text'] = 'Seguindo pela parte iluminada da mina você chega\n' +\
                            'a uma outra trifurcação, o primeiro caminho é de\n' +\
                            'dar arrepios, o segundo está envolto numa neblina,\n' +\
                            'já o terceiro ouve-se um som agudo e distante.'

            option_A['text'] = 'Ir pelo caminho que dá arrepios;'
            option_B['text'] = 'Ir pelo caminho cheio de neblina;'
            option_C['text'] = 'Ir pelo caminho que ouve-se um\nsom agudo e distante;'

        elif level == 3:
            title['text'] = 'Seguindo um caminho na mina você se depara com\n' +\
                            'o corpo de um animal morto... Após vomitar\n' +\
                            'de nojo, você percebe que há alguma coisa\n' +\
                            'brilhante dentro do animal.'

            option_A['text'] = 'Seguir como se nada tivesse ocorrido;'
            option_B['text'] = 'Ir em direção ao animal e procurar\npela coisa brilhante;'
            option_C['text'] = 'Comer a carne daquele animal;'

        elif level == 4:
            title['text'] = 'Em uma parte do caminho você chega a uma porta\n' +\
                            'trancada que só poderá ser liberada apertando\n' +\
                            'o botão com a resposta correta, sendo a charada\n' +\
                            'a seguinte: 7+6=1; 8+8=4; então 9+5 é igual a?'

            option_A['text'] = 'A resposta é 14;'
            option_B['text'] = 'A resposta é 1;'
            option_C['text'] = 'A resposta é 2;'

        elif level == 5:
            title['text'] = 'Você finalmente chega a um local que parece um\n' +\
                            'laboratório, nele você observa a sua amiga presa\n' +\
                            'em uma cela com o cadiado cor de ouro e também\n' +\
                            'um homem solitário e maluco no meio do caminho.'

            option_A['text'] = 'Jogar uma pedra ao longe para\ndistraí-lo;'
            option_B['text'] = 'Atacar aquele homem por trás;'
            option_C['text'] = 'Tentar passar sem ser vista e\nir até a cela;'

        elif level == 6:
            title['text'] = 'Após libertar a sua amiga e sair correndo dali\n' +\
                            'o cara maluco percebe o que você fez e grita:\n' +\
                            '\'Vocês nunca escaparão com vida\' e puxa uma\n' +\
                            'alavanca que faz desmoronar aquele laboratório.' 

            option_A['text'] = 'Tentar fugir pelo elevador que\nvocê veio;'
            option_B['text'] = 'Tentar fugir por uma saída\nalternativa da mina;'
            option_C['text'] = 'Tentar fugir pelos carrinhos da\nmina abandonada;'


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
                    txt_result = 'A longa noite passou num\ninstante, mas você se dá\nconta do sumiço de Annie.\n' +\
                                'Você observa o óculos dela\nquebrado em uma direção...'
                    losewin_heart = 0
                    losewin_food = 0

            elif option == 'B':
                txt_result = 'A longa noite passou num\ninstante, mas você se dá\nconta do sumiço de Annie.\n' +\
                            'Você observa o óculos dela\nquebrado em uma direção...'
                losewin_heart = 0
                losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'A longa noite passou num\ninstante, mas você se dá\nconta do sumiço de Annie.\n' +\
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
                    txt_result = 'No fim da ponte, a\nmadeira sobre seu pé racha\nao meio e você cai no riacho.\n' +\
                                    'Próximo a margem você\nconsegue se salvar.'
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


    elif world == 2:
        if level == 1:
            if option == 'A':
                if rand == 1 or rand == 2:
                    txt_result = 'O cogumelo Azul lhe traz uma\nsensação de fraqueza.'
                    losewin_heart = -10
                    losewin_food = 0
                elif rand == 3 or rand == 4:
                    txt_result = 'O cogumelo Azul lhe traz uma\nsensação de saciedade.'
                    losewin_heart = 0
                    losewin_food = 1

            elif option == 'B':
                if rand == 1 or rand == 2:
                    txt_result = 'O cogumelo Vermelho lhe\ntraz uma sensação de força.'
                    losewin_heart = 10
                    losewin_food = 0
                elif rand == 3 or rand == 4:
                    txt_result = 'O cogumelo Vermelho lhe\ntraz uma fome imensa.'
                    losewin_heart = 0
                    losewin_food = -1

            elif option == 'C':
                txt_result = 'Você segue em frente e come\nalgo de sua mochila.'
                losewin_heart = 0
                losewin_food = -1

        elif level == 2:
            if option == 'A':
                txt_result = 'Ao passar pelas flores você\nsente náuseas.'
                losewin_heart = 0
                losewin_food = 0
                new_item = 'nausea'

            elif option == 'B':
                if items_values['item_wolfhide']:
                    txt_result = 'Tudo ocorreu bem, afinal\no couro de lobo a protegeu\ndos espinhos.'
                    losewin_heart = 0
                    losewin_food = 0
                else:
                    if rand == 1 or rand == 2 or rand == 3:
                        txt_result = 'Ao passar pelas espinhos\nvocê se corta várias vezes.'
                        losewin_heart = -20
                        losewin_food = 0
                    elif rand == 4:
                        txt_result = 'Ao passar pelos espinhos\nvocê se arranha levemente.'
                        losewin_heart = -10
                        losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'À medida que você caminhava\nno lamaceiro você começa\na afundar até que percebes\n' +\
                                'que era na verdade\nareia movediça.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                elif rand == 4:
                    txt_result = 'No meio para o final do\nlamaceiro você começa a\nafundar, porém consegue fugir\n' +\
                                'da então areia movediça.'
                    losewin_heart = -10
                    losewin_food = 0

        elif level == 3:
            if option == 'A':
                if items_values['item_future_friendship'] and items_values['item_shotgun']:
                    txt_result = 'Indo em direção ao urso\nvocê o ataca e tem uma ajuda\nespecial de um certo lobinho\n' +\
                    'que retribuiu e partiu de\nvolta a mata..'
                    losewin_heart = 0
                    losewin_food = 0

                else:
                    txt_result = 'O urso é atingido, porém\nele vem ferozmente em sua\ndireção. Você tenta atirar,\n' +\
                    'todavia estava sem munição.\nO urso veio e a pegou.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True

            elif option == 'B':
                txt_result = 'Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente.'
                losewin_heart = -10
                losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso.'
                    losewin_heart = -10
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal.'
                    losewin_heart = 0
                    losewin_food = 0

        elif level == 4:
            if option == 'A':
                new_item = 'crowbar'
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Entrando na cabana você\ncomeça a subir para o segundo\nandar, você acha um pé de\n' +\
                                    'cabra numa quina e\nconsegue sair da cabana.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Entrando na cabana você\ncomeça a subir para o segundo\nandar, você acha um pé de\n' +\
                                    'cabra numa quina. Ao sair\nvocê se corta gravemente,\nporém você saiu com vida.'
                    losewin_heart = -20
                    losewin_food = 0

            elif option == 'B':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Ao entrar na cabana você\ncomeça a subir para o segundo\nandar, você segue em\n' +\
                                    'direção a saída e tudo\nvai bem.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Ao entrar na cabana você\ncomeça a subir para o segundo\nandar, você segue em\n' +\
                                    'direção a saída, todavia\num degrau da escada se parte\nvocê despenca e morre.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Ao tentar escalar o muro\nde gelo você escorrega e\ncai de costas no chão,\n' +\
                                    'sofrendo uma queda fatal.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                elif rand == 4:
                    txt_result = 'Você conseguiu escalar o\nmuro de gelo...'
                    losewin_heart = 0
                    losewin_food = 0

        elif level == 5:
            if option == 'A':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'O \'Remédio\' estava\nvencido a muitos anos,\ncausando-lhe um infarto.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                elif rand == 4:
                    txt_result = 'O \'Remédio\' estava\nna validade e te fez\nmuito, mas muito bem.'
                    losewin_heart = 30
                    losewin_food = 0

            elif option == 'B':
                txt_result = 'Você apenas segue em frente.'
                losewin_heart = 0
                losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Nada ocorre e você segue\nadiante.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Ao jogar fora aquele \'Remédio\'\nvocê pertubou a cova de\num antigo médico. Por causa\n' +\
                                    'disso você começa a sentir\numa enorme fraqueza.'
                    losewin_heart = -40
                    losewin_food = 0

        elif level == 6:
            new_key = 'G'

            if option == 'A':
                txt_result = 'O \'Cheiro estranho\' se\ntratava de um vazamento\nde gás e isso causou uma\ngrande explosão.'
                losewin_heart = 0
                losewin_food = 0
                game_over = True

            elif option == 'B':
                if rand == 1 or rand == 2:
                    txt_result = 'Apesar de não enxergar nada\nvocê chega a saída da capela.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 3 or rand == 4:
                    txt_result = 'Caminhado pela capela você\ntropeça em um banco, contudo\nvocê consegue seguir adiante .'
                    losewin_heart = -10
                    losewin_food = 0

            elif option == 'C':
                if rand == 1 or rand == 2:
                    txt_result = 'Você não encontra a fonte\ndo cheiro, todavia você\nacha a saída.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 3:
                    txt_result = 'Você encontra a fonte do\ncheiro, se tratava de um\nvazamento de gás. Após\nisso você vai até a saída.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Ao encontrar a fonte do\ncheiro sua garganta começa\na fechar-se, matando-a\nasfixiada pelo gás.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over == True


    elif world == 3:
        if level == 1:
            if option == 'A':
                if items_values['item_crowbar']:
                    txt_result = 'Ao utilizar o pé de cabra\nvocê consegue com muito\nesforço abrir o baú e\nencontrar uma chave de fenda.'
                    losewin_heart = 0
                    losewin_food = 0
                    new_item = 'screwdriver'
                else:
                    txt_result = 'Somente com uma ferramenta\nvocê conseguiria abrir o\nbaú, todavia você não o\ntem e então segue adiante.'
                    losewin_heart = 0
                    losewin_food = 0

            elif option == 'B':
                if rand == 1 or rand == 2:
                    txt_result = 'Apesar da força excessiva\nvocê não consegue abrir o\nbaú e segue adiante.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 3:
                    txt_result = 'Tentando forçar a abertura\nvocê acabou se machucando e\nfrustado você segue adiante.'
                    losewin_heart = -10
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Após muito tentar você\nconsegue abrir o baú e\nnele você encontra uma\nvelha chave de fenda.'
                    losewin_heart = 0
                    losewin_food = 0
                    new_item = 'screwdriver'

            elif option == 'C':
                txt_result = 'Você apenas segue em frente.'
                losewin_heart = 0
                losewin_food = 0

        elif level == 2:
            if option == 'A':
                txt_result = 'Afinal quem nunca se arrepiou\n por causa do frio?\n\nEntão você segue adiante.'
                losewin_heart = 0
                losewin_food = 0

            elif option == 'B':
                if items_values['item_nausea']:
                    txt_result = 'Ao caminhar você começa a\nver coisas no meio da\nneblina até que você chega\n' +\
                                    'a um precipício e se joga...\n\nO efeito das flores a deu\ncoragem para pular.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                else:
                    if rand == 1 or rand == 2:
                        txt_result = 'A neblina logo passa e nada\nlhe acontece.'
                        losewin_heart = 0
                        losewin_food = 0
                    elif rand == 3 or rand == 4:
                        txt_result = 'Caminhando pela neblina você\ntropeça numa pedra, mas\na neblina logo passou.'
                        losewin_heart = -10
                        losewin_food = 0

            elif option == 'C':
                if items_values['item_nausea']:
                    txt_result = 'Ao caminhar você começa a\nseguir o som e ver coisas\naté que você chega a um\n' +\
                                    'precipício e se joga...\n\nO efeito das flores a deu\ncoragem para pular.'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                else:
                    txt_result = 'Seguindo o som agudo você\napenas segue e não encontra\na fonte daquele som.'
                    losewin_heart = 0
                    losewin_food = 0

        elif level == 3:
            if option == 'A':
                txt_result = 'Você apenas segue em frente.'
                losewin_heart = 0
                losewin_food = 0

            elif option == 'B':
                txt_result = 'Ao se aproximar do animal você\nencontra a coisa brilhante que\nse tratava de uma engrenagem.'
                losewin_heart = 0
                losewin_food = 0
                new_item = 'gear'

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Ao comer a carne daquele\nanimal você passa mal e\nmorre, simples assim...'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                elif rand == 4:
                    txt_result = 'Por incrível que parece você\nnão passou mal ou morreu.\n\nVocê se sente bem e satisfeito.'
                    losewin_heart = 10
                    losewin_food = 10

        elif level == 4:
            if option == 'A':
                txt_result = 'A resposta está incorreta\ne abaixo de você abri-se um\nburaco cheio de espinhos e\n' +\
                                'nele você encontra seu fim...'
                losewin_heart = 0
                losewin_food = 0
                game_over = True

            elif option == 'B':
                txt_result = 'A resposta está incorreta\ne abaixo de você abri-se um\nburaco cheio de espinhos e\n' +\
                                'nele você encontra seu fim...'
                losewin_heart = 0
                losewin_food = 0
                game_over = True

            elif option == 'C':
                txt_result = 'A resposta está correta,\npois 9am + 5 horas = 2pm.\n\nA porta se abre e você segue.'
                losewin_heart = 0
                losewin_food = 0

        elif level == 5:
            if option == 'A':
                txt_result = 'Ao ouvir um barulho ao longe\no homem vai lá verificar\npermitindo que você chegue\n' +\
                                'até a cela de sua amiga e\na libertar...'
                losewin_heart = 0
                losewin_food = 0

            elif option == 'B':
                txt_result = 'Ao tentar atacar aquele homem\npelas costas, você o atinge,\nmas ele sabe revidar e te mata.'
                losewin_heart = 0
                losewin_food = 0
                game_over = True

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Como um ninja você consegue\npassar pelo homem e abrir a\ncela de sua amiga.'
                    losewin_heart = 0
                    losewin_food = 0
                elif rand == 4:
                    txt_result = 'Tentando passar pelo homem você\nacaba fazendo muito barulho.\n\nAo perceber, o homem te pega\n' +\
                                    'e te mata...'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True

        elif level == 6:
            if option == 'A':
                txt_result = 'Subir enquanto tudo está\ncaindo não foi uma boa ideia.\n\nVocê e sua amiga acabam morrendo\n' +\
                                'esmagadas...'
                losewin_heart = 0
                losewin_food = 0
                game_over = True

            elif option == 'B':
                if items_values['item_screwdriver'] and items_values['item_gear']:
                    txt_result = 'Chegando a porta ela estava\nfaltando uma engrenagem e\nhavia um parafuso solto.\n\n' +\
                                    'Utilizando a chave de fenda\ne a engrenagem você consegue\nabrir a porta e fugir...'
                    losewin_heart = 0
                    losewin_food = 0

                elif items_values['item_screwdriver'] and not items_values['item_gear']:
                    txt_result = 'Chegando a porta ela estava\nfaltando uma engrenagem e\nhavia um parafuso solto.\n\n' +\
                                    'Mesmo com a chave de fendas\nvocês não conseguem abrir a\nporta e morrem subterradas...'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True

                elif not items_values['item_screwdriver'] and items_values['item_gear']:
                    txt_result = 'Chegando a porta ela estava\nfaltando uma engrenagem e\nhavia um parafuso solto.\n\n' +\
                                    'Mesmo com a engrenagem\nvocês não conseguem abrir a\nporta e morrem subterradas...'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True

                else:
                    txt_result = 'Chegando a porta ela estava\nfaltando uma engrenagem e\nhavia um parafuso solto.\n\n' +\
                                    'Sem a chave de fenda e sem a\nengrenagem a porta não abre\ne vocês morrem subterradas...'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True

            elif option == 'C':
                if rand == 1 or rand == 2 or rand == 3:
                    txt_result = 'Ao tentar ir em um carrinho\nda antiga mina, vocês acabam\nseguindo por um caminho\n' +\
                                    'descontinuado e acabam\nmorrendo subterradas...'
                    losewin_heart = 0
                    losewin_food = 0
                    game_over = True
                elif rand == 4:
                    txt_result = 'Indo pelo carrinho da antiga\nmina, vocês seguem por um\ncaminho correto e conseguem\n' +\
                                    'escapar daquele lugar...'
                    losewin_heart = 0
                    losewin_food = 0

    items_values['heart'] += losewin_heart
    items_values['food'] += losewin_food

    if game_over:
        new_item = new_key = None
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
        if page == 0:
            history['text']='Após passar pela armadilha, Sam\n' +\
                            'encontra um posto militar em ruínas,\n' +\
                            'ao adentrar ela encontra uma chave\n' +\
                            'cor de prata, além de uma espingarda.\n'

        elif page == 1:
            history['text']='Após passar pelo posto militar, Sam\n' +\
                            'encontra a mochila de Annie próximo\n' +\
                            'a um portão enferrujado e trancado.\n\n'

        elif page == 2:
            history['text']='Sam pega a mochila de Annie e começa\n' +\
                            'a vasculhar, porém ela não encontra\n' +\
                            'nada. Então ela decide seguir pelo\n' +\
                            'portão enferrujado.\n'

        elif page == 3:
            history['text']='Sam inseri a chave cor de prata no\n' +\
                            'portão e consegue abri-lo.\n\n' +\
                            'O portão dá numa trilha que a guiará\n' +\
                            'em direção ao topo de uma montanha.'

    elif world == 3:
        title['text'] = '- O caminho -'
        if page == 0:
            history['text']='No alto da montanha Sam chega a uma\n' +\
                            'casa bem pequena e nela ela encontra\n' +\
                            'uma chave bem peculiar da cor do ouro.\n\n'

        elif page == 1:
            history['text']='Em um outro vão da casa Sam encontra um\n' +\
                            'elevador e próximo a porta há marcas de\n'+\
                            'sangue na parede na direção do elevador.\n\n'

        elif page == 2:
            history['text']='Sem pestanejar, Sam decide seguir para\n' +\
                            'o elevador em busca de sua amiga, afinal\n' +\
                            'essa é a única pista do sumiço dela.\n\n'

        elif page == 3:
            history['text']='O elevador possui somente os botões de\n' +\
                            'descer e de subir, estando no topo de\n' +\
                            'uma montanha Sam opta por descer.\n\n'

        elif page == 4:
            history['text']='Ao chegar na parte mais baixa do\n' +\
                            'elevador, Sam encontra uma antiga mina\n' +\
                            'abandonada, todavia bem iluminada...\n\n'

    elif world == 4:
        title['text'] = '- A saída -'
        if page == 0:
            history['text']='Após sair daquela mina abandonada\n' +\
                            'que estava desabando, Sam e Annie\n' +\
                            'conseguem finalmente achar uma saída\n\n'
    

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
