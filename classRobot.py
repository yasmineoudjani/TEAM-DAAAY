import math
import pygame
from pygame.locals import *

class Robot:
        """Classe permettant de créer un personnage"""
        def __init__(self,cX,cY,X,Y) :
                """int * int * float * float -> void
                """
                
                #Position du personnage en cases et en coordonnée réelles
                self.case_x = cX
                self.case_y = cY
                self.x = X
                self.y = Y
                self.vX = 0.0
                self.vY = 0.0
                self.alpha = 0

        def avancer(self):
                self.x += self.vX
                self.y += self.vY
                self.case_x = int(self.x)
                self.case_y = int(self.y)
                print("le robot avance vx=", self.vX , " vy=" , self.vY , "\n pox=" , self.x , " posy=" , self.y)
                print("angle alpha=" , self.alpha)

        def tourner(self,angle):
                vX = self.vX
                vY = self.vY
                self.vX = vX*math.cos(angle) - vY*math.sin(angle)
                self.vY = vX*math.sin(angle) + vY*math.cos(angle)
                self.alpha = (self.alpha+angle)%(2*math.pi)
                print("le robot tourne. nouvelle angle : ", self.alpha)

        def changementVitesse(self,d):
                self.vX= math.cos(self.alpha)*d
                self.vY= math.sin(self.alpha)*d
                print("le robot change de vitesse")

        def getCaseX(self):
                return self.case_x

        def getCaseY(self):
                return self.case_y

        def getX(self):
                return self.x

        def getY(self):
                return self.y

        def getVX(self):
                return self.vX

        def getVY(self):
                return self.vY

        def getAlpha(self):
                return self.alpha
