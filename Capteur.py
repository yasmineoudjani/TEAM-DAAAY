import pygame
import math
from pygame.locals import *
from constantes import *
from Arene import *
from droite import *
from point import *
from droite import *
from vecteur import *
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

        x = (int)(self.robot.centre.x) 
        i = 0
        while self.niveau.pixel[(int)(droite.a * x + droite.b)][x] != obstacle:
            x+=1
            i+=1
        
        y =(int)(droite.a * i + droite.b)
        distance = (int)(math.sqrt(i**2 + y**2))
        print("l'obstacle se trouve à ",distance," pixel")
        return distance