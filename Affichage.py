from classRobot import *
from classArene import *
from classCapteur import *
from classControlleur import *
import pygame
from pygame.locals import *
from constantes import *


class Affichage:

    def __init__(self,arene,robot):
        self.robot=robot
        self.arene=arene
        self.largeur=self.arene.getNbColonne()
        self.hauteur=self.arene.getNbLigne()
        
        self.fenetre = pygame.display.set_mode((self.hauteur*taille_sprite, self.largeur*taille_sprite),RESIZABLE)
        #Icone
        icone = pygame.image.load(image_icone)
        pygame.display.set_icon(icone)
        #Titre
        pygame.display.set_caption(titre_fenetre)


    def AfficherArene(self):
        """Méthode permettant d'afficher l'arene"""
        fond = pygame.image.load(image_fond).convert()
        fond = pygame.transform.scale(fond, (self.fenetre.get_width(),self.fenetre.get_height()))
        self.fenetre.blit(fond, (0,0))
        pygame.display.flip()
        #chargement des images
        mur = pygame.image.load(image_mur).convert()
        #on parcourt la liste du terrain
        num_ligne = 0
        for ligne in self.arene.structure:
            #on parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #on calcule la position réelle en pixels
                y = num_case * taille_sprite
                x = num_ligne * taille_sprite
                if sprite == '1':
                    self.fenetre.blit(mur, (x,y))
                    pygame.display.flip()
                num_case += 1
            num_ligne += 1


    def AfficherRobot(self):
        if self.robot.getAlpha()==0*(math.pi/2):
            self.robot.direction=pygame.image.load("images/robot_droite.png").convert_alpha()
        elif self.robot.getAlpha()==1*(math.pi/2):
            self.robot.direction=pygame.image.load("images/robot_bas.png").convert_alpha()
        elif self.robot.getAlpha()==2*(math.pi/2):
            self.robot.direction=pygame.image.load("images/robot_gauche.png").convert_alpha()
        elif self.robot.getAlpha()==3*(math.pi/2):
            self.robot.direction=pygame.image.load("images/robot_haut.png").convert_alpha()
        self.fenetre.blit(self.robot.direction, (self.robot.x* taille_sprite, self.robot.y*taille_sprite))
        pygame.display.flip()
    





	
