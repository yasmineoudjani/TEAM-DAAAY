import pygame
import math
from pygame.locals import *
from constantes import *
from arene import *

from geometrie import *

from constantes import *
from robot import *

class Capteur:
    def __init__(self, niveau, robot):
        self.niveau = niveau
        self.robot = robot


    def distanceObstacle(self):
        """retourne en pixel , la ditance du prochaine obstacle dans l'arene , dans la direction actuel du robot
        """
        A = Point(self.robot.centre.x,self.robot.centre.y)
        B = Point(self.robot.centre.x + self.robot.vecteurDirection.vx ,self.robot.centre.y + self.robot.vecteurDirection.vy)
        droite = Droite(A,B)

        if(self.robot.angle.valeur < math.pi/2 or self.robot.angle.valeur > (3/2)*math.pi):
            sens=1
        else:
            sens=-1

        x = (int)(self.robot.centre.x) 
        i = 0
        while self.niveau.pixel[(int)(droite.a * x + droite.b)][x] != obstacle:
            x+=sens
            i+=1
        
        
        distance = i/abs(math.cos(self.robot.angle.valeur))
        return distance

    def distanceObstacleLarge(self):
        """retourne en pixel , la ditance du prochaine obstacle dans l'arene , dans la direction actuel du robot
        """
        A = Point(self.robot.centre.x,self.robot.centre.y)
        B = Point(self.robot.centre.x + self.robot.vecteurDirection.vx ,self.robot.centre.y + self.robot.vecteurDirection.vy)
        droite = Droite(A,B)
        if(self.robot.angle.valeur < math.pi/2 or self.robot.angle.valeur > (3/2)*math.pi):
            sens=1
        else:
            sens=-1

        mini = -1
        for ori in range(-int(largeur_robot/2) , int(largeur_robot/2)):
            x = (int)(self.robot.centre.x) 
            i = 0
            while self.niveau.pixel[(int)(droite.a * x + droite.b+ori)][x] != obstacle:
                x+=sens
                i+=1
            if(i<mini or mini<0):
                mini = i
        
        
        distance = mini/abs(math.cos(self.robot.angle.valeur))
        return distance
