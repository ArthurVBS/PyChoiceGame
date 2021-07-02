def world_01(selected_option, random, window, w, items, foods):
    global game_over
    global level
    global world
    global hearts

    game_over = False

    if w == 1:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2:
                lbl_toplevel = "As frutinhas não eram tão\ncomestíveis assim."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 3:
                lbl_toplevel = "As frutinhas até que são\ncomestíveis."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "As frutinhas são simplesmente\ndeliciosas, levarei um pouco\npara mais tarde."
                losewin_hearts = 0
                losewin_foods = +0.5

        elif selected_option == "B":
            lbl_toplevel = "A caminhada é longa e a\nfome é sua inimiga, ignora-lá\né custoso."
            losewin_hearts = -0.5
            losewin_foods = 0

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Uma simples fruta, isso\nsacia a sua fome."
                losewin_hearts = 0
                losewin_foods = -0.5

            elif random == 4:
                lbl_toplevel = "Guloseimas são tão gostosas,\npegarei só mais uma, ~Ops~\nacabei exagerando..."
                losewin_hearts = 0
                losewin_foods = -1

    elif w == 2:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2:
                lbl_toplevel = "Você consegue libertar\no lobinho que corre de volta\npara a mata"
                losewin_hearts = 0
                losewin_foods = 0
                items['future_friendship'] = True

            elif random == 3 or random == 4:
                lbl_toplevel = "Ao libertar o lobinho você se\nmachuca com a armadilha, mas\nconsegue libertar o lobinho que\n" +\
                "corre de volta para a mata"
                losewin_hearts = -0.5
                losewin_foods = 0
                items['future_friendship'] = True

        elif selected_option == "B":
            lbl_toplevel = "Nada ocorre, você segue\nem frente"
            losewin_hearts = 0
            losewin_foods = 0

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "O lobo dá seu último uivo e\nvocê consegue o seu couro e\ncarne, então você parte em\nfrente"
                losewin_hearts = 0
                losewin_foods = +1
                items['wolfhide'] = True

            elif random == 4:
                lbl_toplevel = "O lobo dá seu último uivo,\nvocê pega o seu couro e carne,\nmas ao longe vem vindo outro\n" + \
                "lobo então você corre, foge,\nmas havia se arranhado na mata"
                losewin_hearts = -1
                losewin_foods = +1
                items['wolfhide'] = True

    elif w == 3:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1:
                lbl_toplevel = "Em um vão da casa você\nencontra um remédio"
                losewin_hearts = 0.5
                losewin_foods = 0

            elif random == 2:
                lbl_toplevel = "Em um vão da casa você\nencontra uma fruta intacta"
                losewin_hearts = 0
                losewin_foods = 0.5

            elif random == 3:
                lbl_toplevel = "Em um vão da casa você\ntropeça e se machuca"
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Você não acho nada de\ninteressante na casa"
                losewin_hearts = 0
                losewin_foods = 0

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "A constante chuva a\ndeixou resfriada"
                losewin_hearts = -1
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Você andou por debaixo\ndas copas e você nem nota\na chuva constante"
                losewin_hearts = 0
                losewin_foods = 0

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "A chuva passou e você\nsegue o seu caminho"
                losewin_hearts = 0
                losewin_foods = 0
            
            elif random == 4:
                lbl_toplevel = "A chuva veio, mas a\ndona aranha continuou a\nsubir e a picou"
                losewin_hearts = -1
                losewin_foods = 0

    elif w == 4:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2:
                lbl_toplevel = "No fim da ponte você\nolha para trás e percebe\nque deu tudo certo"
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 3 or random == 4:
                lbl_toplevel = "No fim da ponte, a\nmadeira sobre seu pé racha\nao meio e você cai no riacho,\n" +\
                "próximo a margem você\nconsegue se salvar"
                losewin_hearts = -0.5
                losewin_foods = 0

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Ao caminhar tanto você\ncomeça a sentir muita fome,\nportanto você come algo\n" +\
                "de sua mochila"
                losewin_hearts = 0
                losewin_foods = -1

            elif random == 4:
                lbl_toplevel = "Ao caminhar tanto você\ncomeça a sentir muita fome,\nentão você come algo da\n" +\
                "mochila, além disso\nseus pés estão doendo"
                losewin_hearts = -0.5
                losewin_foods = -1

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Não era tão raso assim,\na correnteza a leva e você\nse afoga"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
    

            elif random == 4:
                lbl_toplevel = "Shalow Now\nvocê consegue atravessar de boa"
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 5:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if foods >= 4:
                lbl_toplevel = "Um urso é atraído pela\nsua comida e tem um\nbelo banquete"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
    

            else:
                if random == 1 or random == 2:
                    lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu bem e partiu\nna manhã seguinte"
                    losewin_hearts = 0
                    losewin_foods = -0.5

                elif random == 3 or random == 4:
                    lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu mal e teve de partir\nna manhã seguinte"
                    losewin_hearts = -0.5
                    losewin_foods = -0.5

        elif selected_option == "B":
            if foods >= 4:
                lbl_toplevel = "As formigas são atraídas\npela sua comida e levam\nparte dela"
                losewin_hearts = 0
                losewin_foods = -2

            else:
                if random == 1 or random == 2:
                    lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu bem e partiu\nna manhã seguinte"
                    losewin_hearts = 0
                    losewin_foods = -0.5

                elif random == 3 or random == 4:
                    lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu mal e teve de partir\nna manhã seguinte"
                    losewin_hearts = -0.5
                    losewin_foods = -0.5

        elif selected_option == "C":
            if random == 1 or random == 2:
                lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu mal e teve de partir\nna manhã seguinte"
                losewin_hearts = -0.5
                losewin_foods = -0.5

            elif random == 3:
                lbl_toplevel = "A noite foi longa,\nvocê se alimentou,\ndormiu bem e partiu\nna manhã seguinte"
                losewin_hearts = 0
                losewin_foods = -0.5

            elif random == 4:
                lbl_toplevel = "O chão é o lar de\nmuitos animais, inclusive\nda cobra que te deu\num beijinho de boa noite"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
    
    elif w == 6:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2:
                lbl_toplevel = "O cogumelo Azul lhe traz\numa sensação de fraqueza"
                losewin_hearts = -1
                losewin_foods = 0

            elif random == 3 or random == 4:
                lbl_toplevel = "O cogumelo Azul lhe traz\numa sensação de saciedade"
                losewin_hearts = 0
                losewin_foods = 1

        elif selected_option == "B":
            if random == 1 or random == 2:
                lbl_toplevel = "O cogumelo Vermelho\nlhe traz uma sensação\nde força"
                losewin_hearts = 1
                losewin_foods = 0

            elif random == 3 or random == 4:
                lbl_toplevel = "O cogumelo Vermelho\nlhe traz uma fome\nimensa"
                losewin_hearts = 0
                losewin_foods = -1

        elif selected_option == "C":
            lbl_toplevel = "Você segue em frente e\ncome algo de sua mochila"
            losewin_hearts = 0
            losewin_foods = -0.5

    elif w == 7:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            lbl_toplevel = "Ao passar pelas flores\nvocê sente náuseas"
            losewin_hearts = 0
            losewin_foods = 0
            items['nausea'] = True

        elif selected_option == "B":
            if items['wolfhide'] == True: #Couro de lobo
                lbl_toplevel = "Tudo ocorreu bem,\nafinal o couro de lobo a\nprotegeu dos espinhos"
                losewin_hearts = 0
                losewin_foods = 0

            else:
                if random == 1 or random == 2 or random == 3:
                    lbl_toplevel = "Ao passar pelas espinhos\nvocê se corta várias vezes"
                    losewin_hearts = -1
                    losewin_foods = 0

                elif random == 4:
                    lbl_toplevel = "Ao passar pelos espinhos\nvocê se arranha levemente"
                    losewin_hearts = -0.5
                    losewin_foods = 0

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "À medida que você caminhava\nno lamaceiro você começa\na afundar até que percebes\n" +\
                "que era na verdade\nareia movediça"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
    

            elif random == 4:
                lbl_toplevel = "No meio para o final do\nlamaceiro você começa a\nafundar, porém consegue fugir\n" +\
                "da então areia movediça"
                losewin_hearts = -0.5
                losewin_foods = 0

    elif w == 8:
        window.title(f"Level 01")
        items['shotgun'] = True
        if selected_option == "A":
            lbl_toplevel = "Uma mina explode em sua\nfrente, devido a sua falta\nde cuidado"
            losewin_hearts = 0
            losewin_foods = 0
            game_over = True


        elif selected_option == "B":
            lbl_toplevel = "É voltando que se pega\nimpulso, você passa pela\narmadilha com calma e tudo\n"  +\
            "ocorre bem"
            losewin_hearts = 0
            losewin_foods = 0

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Você segue até a fonte do\nfio e encontra uma armadilha\nplantada, então você\n" +\
                "decide desarmar, com êxito\nvocê desarma a armadilha"
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Você segue até a fonte do\nfio e encontra uma armadilha\nplantada, então você\n" +\
                "decide desarmar, com êxito\na mina terrestre é acionada"
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
    
    resume = {'lbl_toplevel' : lbl_toplevel, 'losewin_hearts' : losewin_hearts,
             'losewin_foods' : losewin_foods, 'game_over' : game_over}

    return resume

def world_02(selected_option, random, window, w, items, foods):
    global game_over
    global level
    global world
    global hearts

    game_over = False

    if w == 1:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if items['future_friendship'] == True: #Futura Amizade
                    lbl_toplevel = "Indo em direção ao urso\nvocê o ataca e tem uma ajuda\nespecial de um certo lobinho\n" +\
                    "que retribuiu e partiu de\nvolta a mata."
                    losewin_hearts = 0
                    losewin_foods = 0

            else:
                if random == 1 or random == 2 or random == 3:
                    lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                    "o urso veio e a pegou."
                    losewin_hearts = 0
                    losewin_foods = 0
                    game_over = True

                elif random == 4:
                    lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                    "todavia estava sem munição,\nentão o urso a pegou."
                    losewin_hearts = 0
                    losewin_foods = 0
                    game_over = True

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 2:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 3:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 4:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 5:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 6:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 7:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 8:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True

        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    resume = {'lbl_toplevel' : lbl_toplevel, 'losewin_hearts' : losewin_hearts,
             'losewin_foods' : losewin_foods, 'game_over' : game_over}

    return resume

def world_03(selected_option, random, window, w, items, foods):
    global game_over
    global level
    global world
    global hearts

    game_over = False

    if w == 1:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if items['future_friendship'] == True: #Futura Amizade
                    lbl_toplevel = "Indo em direção ao urso\nvocê o ataca e tem uma ajuda\nespecial de um certo lobinho\n" +\
                    "que retribuiu e partiu de\nvolta a mata."
                    losewin_hearts = 0
                    losewin_foods = 0

            else:
                if random == 1 or random == 2 or random == 3:
                    lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                    "o urso veio e a pegou."
                    losewin_hearts = 0
                    losewin_foods = 0
                    game_over = True
                    

                elif random == 4:
                    lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                    "todavia estava sem munição,\nentão o urso a pegou."
                    losewin_hearts = 0
                    losewin_foods = 0
                    game_over = True               

        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 2:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                

            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 3:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 4:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 5:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 6:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 7:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    elif w == 8:
        window.title(f"Level 0{w+1}")
        if selected_option == "A":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Para uma escopeta funcionar\né necessário ter munição,\nvocê tentou atirar e falhou,\n" +\
                "o urso veio e a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
            elif random == 4:
                lbl_toplevel = "O urso é atingido, porém\nele vem ferozmente em sua\ndireção e você tenta atirar,\n" +\
                "todavia estava sem munição,\nentão o urso a pegou."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "B":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, ele parte\ne você segue em frente."
                losewin_hearts = 0
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Aguardando pacientemente o\nurso partir, você sente\nfome e decide comer,\n" +\
                "não se dando conta de que\nvocê se tornou uma isca."
                losewin_hearts = 0
                losewin_foods = 0
                game_over = True
                
        elif selected_option == "C":
            if random == 1 or random == 2 or random == 3:
                lbl_toplevel = "Na tentativa de arrodear\nvocê acaba se arranhando,\nmas consegue passar pelo\nurso."
                losewin_hearts = -0.5
                losewin_foods = 0

            elif random == 4:
                lbl_toplevel = "Ao arrodear o urso, você\nconsegue passar ileso\npelo matagal."
                losewin_hearts = 0
                losewin_foods = 0

    resume = {'lbl_toplevel' : lbl_toplevel, 'losewin_hearts' : losewin_hearts,
             'losewin_foods' : losewin_foods, 'game_over' : game_over}

    return resume

def menu(op, wd):

    if op == 1:
        if wd == 1: #A Floresta
            crossroads_text = "Você está caminhando a um\ncerto tempo, o seu estômago\nronca. Você encontra algumas\n" +\
            "frutinhas azuis em um arbusto\nque aparentam ser comestíveis."
            opt_A_text = "Pegar as frutinhas do\narbusto e saciar a sua fome;"
            opt_B_text = "Ignorar as frutinhas e\nseguir em frente;"
            opt_C_text = "Pegar alguma comida da\nmochila;"

        elif wd == 2: #OS Alpes
            crossroads_text = "Ao caminhar você observa um\nurso passeando pela trilha\nque dá nos Alpes, estando\n" +\
            "ele de costas para você e\ncaminhando em direção aos\nAlpes, você deveria..."
            opt_A_text = "Tentar matar o urso\natirando pelas costas e\nseguir em frente;"
            opt_B_text = "Parar onde está e\nesperar o urso sair\nda trilha;"
            opt_C_text = "Tentar passar pelo\nurso arrodeando pelo\nmatagal ao lado da trilha;"

        elif wd == 3: #AS Minas
            crossroads_text = "hi."
            opt_A_text = "123;"
            opt_B_text = "456;"
            opt_C_text = "789;"
    
    elif op == 2:
        if wd == 1:
            crossroads_text = "Em pleno dia você ouve um\nuivo, paralisada, você observa\nque o uivo vem de um lobo\n" +\
            "filhote preso a uma armadilha\nde urso."
            opt_A_text = "Salvar o lobinho daquele\nsofrimento;"
            opt_B_text = "Seguir em frente, como se\nnada tivesse ocorrido;"
            opt_C_text = "Matar o lobinho e pegar\nsua carne e couro;"

        elif wd == 2:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78" 

        elif wd == 3:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78"

    elif op == 3:
        if wd == 1:
            crossroads_text = "Seguindo a caminhada, uma\nlonga chuva toma a floresta.\nNa sua frente há um abrigo\n" +\
            "abandonado, aparentemente\nseguro e bem sujo."
            opt_A_text = "Entrar na casa, explorar e\nesperar a chuva passar;"
            opt_B_text = "Seguir em frente, apesar\n da chuva pesada;"
            opt_C_text = "Esperar a chuva passar na\n sacada do abrigo;"

        elif wd == 2:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78" 

        elif wd == 3:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78"

    elif op == 4:
        if wd == 1:
            crossroads_text = "Após a longa chuva você se\ndepara com um grande e fundo\nriacho, há uma velha ponte\n" +\
            "suspensa, uma margem bem ao\nlonge e uma parte\naparentemente rasa."
            opt_A_text = "Atravessar pela velha\nponte suspensa;"
            opt_B_text = "Atravessar pela margem\nque está distante;"
            opt_C_text = "Atravessar pela parte\naparentemente mais rasa;"

        elif wd == 2:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78" 

        elif wd == 3:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78"

    elif op == 5:
        if wd == 1:
            crossroads_text = "Ate aqui o sol a acompanhava,\nporém a noite vem a espreita,\né necessário parar, comer e\n" +\
            "dormir, você observa uma\ncaverna, um espaço entre as\ncopas das árvores e um\nlocal no chão para dormir."
            opt_A_text = "Dormir na caverna;"
            opt_B_text = "Dormir nas copas das\nárvores;"
            opt_C_text = "Dormir no chão da\nfloresta;"

        elif wd == 2:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78" 

        elif wd == 3:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78"

    elif op == 6:
        if wd == 1:
            crossroads_text = "Ao caminhar você começa a\nsentir fome, você observa a\nsua esquerda e a sua direita\n" +\
            "cogumelos de duas cores\ndistintas (Azuis e Vermelhos)\ncrescendo sobre os troncos\ndas árvores."
            opt_A_text = "Comer o cogumelo Azul;"
            opt_B_text = "Comer o cogumelo Vermelho;"
            opt_C_text = "Seguir em frente, ignorar\nos cogumelos, pois não sou o\nMario;"

        elif wd == 2:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78" 

        elif wd == 3:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78"

    elif op == 7:
        if wd == 1:
            crossroads_text = "Próximo ao fim da floresta\nvocê encontra uma trifurcação,\nhá um caminho cheio de flores\n" +\
            "com um aroma bem forte,\nhá um caminho cheio de\nespinhos e há um lamaceiro"
            opt_A_text = "Passar pelas flores de\naroma forte;"
            opt_B_text = "Passar pelo caminho\nespinhoso;"
            opt_C_text = "Passar por um lamaceiro"

        elif wd == 2:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78" 

        elif wd == 3:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78"

    elif op == 8:
        if wd == 1:
            crossroads_text = "Ao caminhar você sente um\nfio esticar em sua perna\ndireita, seu corpo para e\n" +\
            "reflete rapidamente no\nque fazer..."
            opt_A_text = "Tentar avançar, ignorando\n o fio;"
            opt_B_text = "Tentar voltar e passar\npor cima do fio;"
            opt_C_text = "Tentar ir até a fonte\ndo fio e tentar desarma-lo;"
        
        elif wd == 2:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78" 

        elif wd == 3:
            crossroads_text = "12"
            opt_A_text = "34"
            opt_B_text = "56"
            opt_C_text = "78"
        
        op = 0
        wd += 1

    resume = {'crossroads_text' : crossroads_text, 'wd' : wd, 'op' : op,
              'opt_A_text' : opt_A_text, 'opt_B_text' : opt_B_text, 'opt_C_text' : opt_C_text}

    return resume
