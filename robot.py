import math
import pygame
from pygame.locals import *
from point import *
from vecteur import *
from angle import *

class Robot:
        """Classe permettant de créer un personnage"""
        def __init__(self,X,Y) :
                """int * int * float * float -> void
                """
                self.vecteurVitesse = Vecteur(Point(0,0),Point(0,0))
                self.centre = Point(X,Y)
                self.angle = Angle(0.0)

        def avancer(self):
                self.centre.update(self.vecteurVitesse)
                
        def tourner(self,angle):
                """prend en parametre un angle en radian. modifie self.v.
                """
                a = Angle(angle)
                vecteurVitesse.rotation(a)
                self.angle.addition(a)

        def changementVitesse(self,d):
                """le robot prend la vitesse d donnée en paramètre
                """
                vecteurVitesse.update(d,self.angle)
        
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

