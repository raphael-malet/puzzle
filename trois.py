import pygame
import random

#variable couleur
blanc = (255,255,255)
noir = (0, 0, 0)

global fenetre

#fonction pour stocker le meilleur score
def stockage_score(score):
    with open('score.txt', 'r') as f:
        scores = f.readlines()
        meilleur_score = int(scores[0])
        #condition si le score est inférieur ou non
        if score < meilleur_score:
            score = str(score) + '\n'
            scores.pop(0)
            scores.insert(0, score)
            scores = "".join(scores)
            #on ecrit le nouveau score dans le fichier txt
            with open('score.txt', 'w') as f:
                f.write(scores)


#fonction pour afficher message sur le fenetre de jeu
def message(taille, txt, x, y):
    font_style = pygame.font.SysFont('arial', taille)
    mess = font_style.render(txt, True, noir)
    fenetre.blit(mess, (x, y))

#fonction jouer grille 3x3
def jouer_3x3():
    global fenetre
    #initialisation de la fenetre de jeu
    pygame.init()
    fenetre = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Puzzle')
    #variable score
    score = 0
    #variable placement chiffre dans la grille de jeu
    x = 0
    y = 0
    #variable boucle de jeu
    jouer = True
    #liste de la grille de pluzzle
    liste_3x3 = ['1', '2', '3',
                 '4', '5', '6',
                 '7', '8', None]
    font_style = pygame.font.SysFont('arial', 100)
    #on melange la liste de chiffre pour les positionner de manière aléatoire dans la grille de jeu
    random.shuffle(liste_3x3)

    #boucle de jeu
    while jouer:

        #condition de victoire
        if liste_3x3 == ['1', '2', '3',
                         '4', '5', '6',
                         '7', '8', None]:
            stockage_score(score)
            #fenetre partie terminée
            fenetre.fill(blanc)
            message(60, 'Bravo', 220, 70)
            message(50, 'Votre score: '+str(score), 140, 120)
            message(30, 'Rejouer appuyer sur R', 150, 200)
            message(30, 'Menu appuyer sur M ', 150, 230)
            message(30, 'Quitter appuyer sur ESCAPE', 100, 260)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #condition on quitte l'application
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    #condition on retourne au menu de jeu
                    if event.key == pygame.K_m:
                        import main
                        main.menu()
                        pygame.quit()
                        quit()
                    #condition on rejoue
                    if event.key == pygame.K_r:
                        jouer_3x3()
        #boucle pour remplir la grille de jeu
        fenetre.fill(blanc)
        for i in range(9):
            x += 200
            if i == 0:
                x = 0
                y = 0
            if x == 600:
                x = 0
                y += 200
            pygame.draw.rect(fenetre, noir, pygame.Rect(x, y, 200, 200),  3)
            nombre = liste_3x3[i]
            if nombre is None:
                nombre_deplacement = i
            mess = font_style.render(nombre, True, noir)
            mess_rect = mess.get_rect(center=(x+100, y+100))
            fenetre.blit(mess, mess_rect)



        #boucle pour la case vide dans la grill de jeu
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #condition pour ne pas dépacer la partie droite de la grille de jeu
                    if nombre_deplacement == 2 or nombre_deplacement == 5 or nombre_deplacement == 8:
                        break
                    #on suprime la case vide et on l'insert a l'endroit voulu
                    liste_3x3.pop(nombre_deplacement)
                    nombre_deplacement += 1
                    liste_3x3.insert(nombre_deplacement, None)
                    score += 1

                if event.key == pygame.K_RIGHT:
                    #condition pour ne pas dépasser la partie gauche de la grille de jeu
                    if nombre_deplacement %3 == 0:
                        break
                    # on suprime la case vide et on l'insert a l'endroit voulu
                    liste_3x3.pop(nombre_deplacement)
                    nombre_deplacement -= 1
                    liste_3x3.insert(nombre_deplacement, None)
                    score += 1

                if event.key == pygame.K_UP:
                    #condtion pour ne pas dépasser la partie basse de la grille de jeu
                    if nombre_deplacement >=6:
                        break
                    # on suprime la case vide et on l'insert a l'endroit voulu
                    nb = liste_3x3[nombre_deplacement + 3]
                    liste_3x3.pop(nombre_deplacement)
                    liste_3x3.pop(nombre_deplacement +2 )
                    nombre_deplacement += 3

                    liste_3x3.insert(nombre_deplacement-3, nb)
                    liste_3x3.insert(nombre_deplacement, None)
                    score += 1

                if event.key == pygame.K_DOWN:
                    #contion pour ne pas dépasser la partie haute de la grille de jeu
                    if nombre_deplacement  <= 2:
                        break
                    # on suprime la case vide et on l'insert a l'endroit voulu
                    nb = liste_3x3[nombre_deplacement - 3]
                    liste_3x3.pop(nombre_deplacement)
                    liste_3x3.pop(nombre_deplacement - 3)
                    nombre_deplacement -= 3
                    liste_3x3.insert(nombre_deplacement, None)
                    liste_3x3.insert(nombre_deplacement + 3, nb)
                    score += 1

                #condition pour mélanger la grille de jeu
                if event.key == pygame.K_r:
                    random.shuffle(liste_3x3)
                    #on remet le score a 0
                    score = 0
                #condtion si on veut fermer la fenetre de jeu
                if event.key == pygame.K_ESCAPE:
                    import main
                    main.menu()
                    pygame.quit()
                    quit()



            #on actualise l'affichage de la fenetre de jeu
            pygame.display.update()

