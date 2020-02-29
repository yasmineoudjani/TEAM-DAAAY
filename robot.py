import math
import pygame
from pygame.locals import *
from point import *
from vecteur import *
from angle import *
from constantes import *

class Robot:
        """Classe permettant de créer un personnage"""
        def __init__(self,X,Y) :
                """int * int * float * float -> void
                """
                self.vecteurVitesse = Vecteur(Point(0,0),Point(0,0))
                self.centre = Point(X,Y)
                self.angle = Angle(0.0)
                self.vecteurDirection = Vecteur(Point(0,0),Point(0,0))
                self.vecteurDirection.update(10,self.angle)

        def avancer(self):
                self.centre.update(self.vecteurVitesse)
                
        def tourner(self,angle):
                """prend en parametre un angle en radian. modifie self.v.
                """
                a = Angle(angle)
                self.vecteurVitesse.rotation(a)
                self.vecteurDirection.rotation(a)
                self.vecteurDirection.update(1,a)
                self.angle.addition(a)

        def changementVitesse(self,d):
                """le robot prend la vitesse d donnée en paramètre
                """
                self.vecteurVitesse.update(d,self.angle)

        def collision(self,arene):
            """prend en parametre une arene et regarde si à la position du robot il y a collision entre le robot et un obstacle
            renvoie true si il y a une collison, false sinon
            """
            if(arene.pixel[self.centre.y][self.centre.x] == mur):
                return true
            return false
        
        @property 
        def CaseX(self):
                return int(self.centre.x)

        @property 
        def CaseY(self):
                return int(self.centre.y)

        @property
        def getVX(self):
                return self.vecteurVitesse.vx

        @property
        def getVY(self):
                 return self.vecteurVitesse.vy

