import pygame
import trois
import quatre
import cinque

global fenetre

#variable couleur utilisée
blanc = (255,255,255)
noir = (0, 0, 0)

#fonction pour prendre les scores dans le fichier txt
def voir_score():
    with open('score.txt', 'r') as f:
        scores = f.readlines()
        score_3x3 = scores[0]
        score_3x3 = score_3x3[:-1]
        score_4x4 = scores[1]
        score_4x4 = score_4x4[:-1]
        score_5x5 = scores[2]
        score_5x5 = score_5x5[:-1]
    #on afficher les score avec la fonction message
    fenetre.fill(blanc)
    message(40, '3x3 meilleur score : '+ score_3x3, 100, 200)
    message(40, '4x4 meilleur score : '+ score_4x4, 100, 250)
    message(40, '5x5 meilleur score : '+ score_5x5, 100, 300)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                menu()

#focntion pour afficher text sur la fenetre de jeu
def message(taille, txt, x, y):
    font_style = pygame.font.SysFont('arial', taille)
    mess = font_style.render(txt, True, noir)
    fenetre.blit(mess, (x, y))

#fonction affichage du menu de jeu
def menu():
    global fenetre
    pygame.init()
    fenetre = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Puzzle')
    continuer = True
    #affichage du texte sur la fenetre de jeu
    fenetre.fill(blanc)
    message(60, 'Bienvenue', 160, 70)
    message(30, 'Jouer 3x3 appuyer sur 3', 140, 240)
    message(30, 'Jouer 4x4 appuyer sur 4', 140, 280)
    message(30, 'Jouer 5x5 appuyer sur 5', 140, 320)
    message(30, 'Voir scores appuyer sur S', 130, 360)
    pygame.display.update()
    #boucle pour prendre input pour continuer
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    pygame.quit()
                    trois.jouer_3x3()
                    quit()
                if event.key == pygame.K_4:
                    pygame.quit()
                    quatre.jouer_4x4()
                    quit()
                if event.key == pygame.K_5 :
                    pygame.quit()
                    cinque.jouer_5x5()
                    quit()
                if event.key == pygame.K_s:
                    voir_score()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

menu()