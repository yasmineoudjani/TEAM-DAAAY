import pygame
from pygame.locals import *
from constantes import *
class Affichage:
    def __init__(self,droite,gauche,haut,bas):
        pygame.init()

        #Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
        self.fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
        #Icone
        self.icone = pygame.image.load(image_icone)
        pygame.display.set_icon(self.icone)
        #Titre
        pygame.display.set_caption(titre_fenetre)
        
        self.robotDroite = pygame.image.load(droite).convert_alpha()
        self.robotGauche = pygame.image.load(gauche).convert_alpha()
        self.robotHaut = pygame.image.load(haut).convert_alpha()
        self.robotBas = pygame.image.load(bas).convert_alpha()

    def chargement(self, niveau, robot):

        self.robot = robot
        self.niveau= niveau
        #Chargement et affichage de l'écran d'accueil
        self.accueil = pygame.image.load(image_fond).convert()
        self.fenetre.blit(self.accueil, (0,0))
    	#Rafraichissement
        pygame.display.flip()
        self.fond = pygame.image.load(image_fond).convert()

        self.fenetre.blit(self.fond, (0,0))
        niveau.afficher(self.fenetre)
        self.fenetre.blit(self.robotDroite, (self.robot.CaseX-15, self.robot.CaseY-15))
        pygame.display.flip()

    def refresh(self, robot):
        self.robot = robot
        self.fenetre.blit(self.fond, (0,0))
        self.niveau.afficher(self.fenetre)
        self.fenetre.blit(self.robotDroite, (self.robot.CaseX-15, self.robot.CaseY-15)) #self.robot.direction = l'image dans la bonne direction
        pygame.display.flip()
        
	
