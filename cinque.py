import pygame
import random

#varaible couleur utiliser
blanc = (255, 255, 255)
noir = (0, 0, 0)

#fonction stockage du score dans le fichier txt
def stockage_score(score):
    with open('score.txt', 'r') as f:
        scores = f.readlines()
        meilleur_score = int(scores[2])
        #conditon si le score est inférieur au meilleur score on l'écrit dans le fichier txt
        if score < meilleur_score:
            meilleur_score = str(score) + '\n'
            scores.pop(2)
            scores.insert(2, meilleur_score)
            scores = "".join(scores)
            with open('score.txt', 'w') as f:
                f.write(scores)

#fonction pour afficher text sur la fenetre de jeu
def message(taille, txt, x, y):
    global fenetre
    font_style = pygame.font.SysFont('arial', taille)
    mess = font_style.render(txt, True, noir)
    fenetre.blit(mess, (x, y))

#fonction jouer grille 5X5
def jouer_5x5():
    global fenetre
    #score de départ 0 coup jouer
    score = 0
    #initialisation de la fenetre de jeu
    pygame.init()
    fenetre = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Puzzle')

    #variable pour positionner chiffre dans la grille de jeu
    x = 0
    y = 0
    jouer = True
    #liste des chiffres dans la grille de jeu
    liste_4x4 = ['1', '2', '3', '4', '5',
                 '6', '7', '8', '9', '10',
                 '11', '12', '13', '14',  '15',
                 '16', '17', '18', '19', '20',
                 '21', '22', '23', '24', None ]
    font_style = pygame.font.SysFont('arial', 100)
    #on mélange la liste de chiffre
    random.shuffle(liste_4x4)

    #boucle de jeu
    while jouer:
        # condition de vitoire
        if liste_4x4 == ['1', '2', '3', '4', '5',
                         '6', '7', '8', '9', '10',
                         '11', '12', '13', '14', '15',
                         '16', '17', '18', '19', '20',
                         '21', '22', '23', '24' , None]:
            #on vérifie si le score est le meilleur scire
            stockage_score(score)
            fenetre.fill(blanc)
            #affichage texte sur le fenetre de jeu
            message(60, 'Bravo', 220, 70)
            message(50, 'votre score: ' + str(score), 140, 120)
            message(30, 'rejouer appuyer sur R', 150, 200)
            message(30, 'Menu appuyer sur M ', 150, 230)
            message(30, 'Quitter appuyer sur ESCAPE', 100, 260)
            pygame.display.update()
            #on prend input pour continuer ou non
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        jouer = False
                    if event.key == pygame.K_m:
                        import main
                        main.menu()
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_r:
                        jouer_5x5()

        #boucle pour faire grille de jeu et positionner les chiffre au centre
        fenetre.fill(blanc)
        for i in range(25):
            x += 120
            if i == 0:
                x = 0
                y = 0
            if x == 600:
                x = 0
                y += 120
            pygame.draw.rect(fenetre, noir, pygame.Rect(x, y, 120, 120),  3)
            nombre = liste_4x4[i]
            if nombre == None:
                nombre_deplacement = i
            mess = font_style.render(nombre, True, noir)
            mess_rect = mess.get_rect(center=(x+60, y+60))
            fenetre.blit(mess, mess_rect)



        #boucle pour prendre input pour déplacer la case vide dans la grille de jeu
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #condtion pour ne pas dépasser la droite de la grille de jeu
                    if nombre_deplacement == 4 or nombre_deplacement == 9 or nombre_deplacement == 14 or nombre_deplacement==19:
                        break
                    # on prend la postion dans la liste du nombre avec qui la case vide bouge
                    liste_4x4.pop(nombre_deplacement)
                    nombre_deplacement += 1
                    liste_4x4.insert(nombre_deplacement, None)
                    score +=1

                if event.key == pygame.K_RIGHT:
                    #condtion pour ne pas dépasser la gauche de la grill de jeu
                    if nombre_deplacement %5 == 0:
                        break
                    # on prend la postion dans la liste du nombre avec qui la case vide bouge
                    liste_4x4.pop(nombre_deplacement)
                    nombre_deplacement -= 1
                    liste_4x4.insert(nombre_deplacement, None)
                    score += 1

                if event.key == pygame.K_UP:
                    #condition pour ne pas dépasser le bas de la grille de jeu
                    if nombre_deplacement >=20:
                        break
                    # on prend la postion dans la liste du nombre avec qui la case vide bouge
                    nb = liste_4x4[nombre_deplacement + 5]
                    liste_4x4.pop(nombre_deplacement)
                    liste_4x4.pop(nombre_deplacement +4 )
                    nombre_deplacement += 5
                    liste_4x4.insert(nombre_deplacement-5, nb)
                    liste_4x4.insert(nombre_deplacement, None)
                    score += 1

                if event.key == pygame.K_DOWN:
                    #condtion pour ne pas dépasser le haut de la grill de jeu
                    if nombre_deplacement  <= 4:
                        break
                    #on prend la postion dans la liste du nombre avec qui la case vide bouge
                    nb = liste_4x4[nombre_deplacement - 5]
                    liste_4x4.pop(nombre_deplacement)
                    liste_4x4.pop(nombre_deplacement - 5)
                    nombre_deplacement -= 5
                    liste_4x4.insert(nombre_deplacement, None)
                    liste_4x4.insert(nombre_deplacement + 5, nb)
                    score += 1

                #condtion si on veut mélanger la grille de jeu et on remet de score a 0
                if event.key == pygame.K_r:
                    random.shuffle(liste_4x4)
                    score = 0
                if event.key == pygame.K_ESCAPE:
                    import main
                    main.menu()
                    pygame.quit()
                    quit()


            pygame.display.update()
