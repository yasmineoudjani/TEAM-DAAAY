import math
import pygame
from pygame.locals import *

class Robot:
        """Classe permettant de créer un personnage"""
        def __init__(self,X,Y) :
                """int * int * float * float -> void
                """
                self._x = X
                self._y = Y
                self._v=0.0
                self._alpha = 0.0

        def avancer(self):
                self._x += self._v * math.cos(self._alpha)
                self._y += self._v * math.sin(self._alpha)
                print("j'avance")

        def tourner(self,angle):
                """prend en parametre un angle en radian. modifie self.v.
                """
                vX = self._v * math.cos(self._alpha)
                vY = self._v * math.sin(self._alpha)

                vXp = vX*math.cos(angle) - vY*math.sin(angle)
                vYp = vX*math.sin(angle) + vY*math.cos(angle)

                self._v = math.sqrt(vXp**2 + vYp**2)

                self._alpha = (self._alpha+angle)%(2*math.pi)

        def changementVitesse(self,d):
                """le robot prend la vitesse d donnée en paramètre
                """
                vX= math.cos(self._alpha)*d
                vY= math.sin(self._alpha)*d
                self._v = math.sqrt(vX**2 + vY**2)

        @property
        def x(self):
                return self._x

        @property
        def y(self):
                return self._y
        
        @property 
        def CaseX(self):
                return int(self._x)

        @property 
        def CaseY(self):
                return int(self._y)

        @property
        def getVX(self):
                return (self._v * math.cos(self._alpha))

        @property
        def getVY(self):
                return (self._v * math.sin(self._alpha))

        @property
        def getAlpha(self):
                return self._alpha
