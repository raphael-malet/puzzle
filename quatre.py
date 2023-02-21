import pygame
import random

#varaible couleur utilisé
blanc = (255, 255, 255)
noir = (0, 0, 0)

#fonction pour stocker score ou non dans le fichier txt
def stockage_score(score):
    with open('score.txt', 'r') as f:
        scores = f.readlines()
        meilleur_score = int(scores[1])
        if score < meilleur_score:
            meilleur_score = str(score) + '\n'
            scores.pop(1)
            scores.insert(1, meilleur_score)
            scores = "".join(scores)
            with open('score.txt', 'w') as f:
                f.write(scores)

#focntion affichage message
def message(taille, txt, x, y):
    global fenetre
    font_style = pygame.font.SysFont('arial', taille)
    mess = font_style.render(txt, True, noir)
    fenetre.blit(mess, (x, y))

#focntion pour la grille de jeu 4X4
def jouer_4x4():
    global fenetre
    pygame.init()
    fenetre = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Puzzle')
    #variable score = au nombre de coup jouer
    score = 0
    #variable pour position des chiffres dans la grille de jeu
    x = 0
    y = 0
    jouer = True
    #liste de numéro dans la grille de jeu
    liste_4x4 = ['1', '2', '3', '4',
                 '5', '6', '7', '8',
                 '9', '10', '11', '12',
                 '13', '14', '15', None]
    #variable police chiffre grille de jeu
    font_style = pygame.font.SysFont('arial', 100)
    #on mélange la liste des chiffres de la grill de jeu
    random.shuffle(liste_4x4)

    #boucle de jeu
    while jouer:
        #conditon de victoire
        if liste_4x4 == ['1', '2', '3', '4',
                         '5', '6', '7', '8',
                         '9', '10', '11', '12',
                         '13', '14', '15', None]:
            #on vérifie si le score est le meilleur score pour l'enregistrer
            stockage_score(score)
            fenetre.fill(blanc)
            #text affichage fenetre
            message(60, 'Bravo', 220, 70)
            message(50, 'votre score: ' + str(score), 140, 120)
            message(30, 'rejouer appuyer sur R', 150, 200)
            message(30, 'Menu appuyer sur M ', 150, 230)
            message(30, 'Quitter appuyer sur ESCAPE', 100, 260)
            pygame.display.update()
            #boucle pour input pour continuer ou non
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
                        jouer_4x4()

        fenetre.fill(blanc)
        #boucle pour placer les chiffres dans la grille de jeu
        for i in range(16):
            x += 150
            if i == 0:
                x = 0
                y = 0
            if x == 600:
                x = 0
                y += 150
            pygame.draw.rect(fenetre, noir, pygame.Rect(x, y, 150, 150),  3)
            nombre = liste_4x4[i]
            #condition pour avoir la position de la case a bouger
            if nombre == None:
                nombre_deplacement = i
            mess = font_style.render(nombre, True, noir)
            mess_rect = mess.get_rect(center=(x+75, y+75))
            fenetre.blit(mess, mess_rect)



        #boucle pour déplacer la case vide
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #condtion pour ne pas dépasser la partie droite de la grille de jeu
                    if nombre_deplacement == 3 or nombre_deplacement == 7 or nombre_deplacement == 11:
                        break
                    liste_4x4.pop(nombre_deplacement)
                    nombre_deplacement += 1
                    liste_4x4.insert(nombre_deplacement, None)
                    score +=1
                if event.key == pygame.K_RIGHT:
                    #condtion pour ne pas dépasser la partie gauche de la grille de jeu
                    if nombre_deplacement %4 == 0:
                        break
                    liste_4x4.pop(nombre_deplacement)
                    nombre_deplacement -= 1
                    liste_4x4.insert(nombre_deplacement, None)
                    score += 1
                if event.key == pygame.K_UP:
                    #condition pour ne pas dépasser la partie basse de la grille de jeu
                    if nombre_deplacement >=12:
                        break
                    nb = liste_4x4[nombre_deplacement + 4]
                    liste_4x4.pop(nombre_deplacement)
                    liste_4x4.pop(nombre_deplacement +3 )
                    nombre_deplacement += 4
                    liste_4x4.insert(nombre_deplacement-4, nb)
                    liste_4x4.insert(nombre_deplacement, None)
                    score += 1

                if event.key == pygame.K_DOWN:
                    #condtion pour ne pas dépasser la partie haute de la grille de jeu
                    if nombre_deplacement  <= 3:
                        break
                    nb = liste_4x4[nombre_deplacement - 4]
                    liste_4x4.pop(nombre_deplacement)
                    liste_4x4.pop(nombre_deplacement - 4)
                    nombre_deplacement -= 4
                    liste_4x4.insert(nombre_deplacement, None)
                    liste_4x4.insert(nombre_deplacement + 4, nb)
                    score += 1
                #si on veut remélanger la grille de jeu
                if event.key == pygame.K_r:
                    random.shuffle(liste_4x4)
                    #on remet le score a 0
                    score = 0
                if event.key == pygame.K_ESCAPE:
                    import main
                    main.menu()
                    pygame.quit()
                    quit()

            pygame.display.update()
