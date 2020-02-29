import pygame
import math
from pygame.locals import *
from constantes import *
from Arene import *
from droite import *
from point import *

class Capteur:
    def __init__(self, niveau, robot):
        self.niveau = niveau
        self.robot = robot



    """retourne le nombre de case avant un obstacle a droite"""
    def murD(self, case_x , case_y):
        i=1
        while self.niveau.structure[case_y][case_x+i] != '1':
            i=i+1
        return i

    """retourne le nombre de case avant un obstacle a gauche"""
    def murG(self, case_x , case_y):
        i=1
        while self.niveau.structure[case_y][case_x-i] != '1':
            i=i+1
        return i

    """retourne le nombre de case avant un obstacle en haut"""
    def murA(self, case_x , case_y):
        i=1
        while self.niveau.structure[case_y-i][case_x] != '1':
            i=i+1
        return i

    """retourne le nombre de case avant un obstacle en bas"""
    def murR(self, case_x , case_y):
        i=1
        while self.niveau.structure[case_y+i][case_x] != '1':
            i=i+1
        return i

    def distanceObstacle(self):
        """retourne en pixel , la ditance du prochaine obstacle dans l'arene , dans la direction actuel du robot
        """

        droite = Droite(robot.centre , robot.centre.update(robot.vecteurVitesse))

        x = 1
        while self.niveau.pixel[(int)(droite.a * x + droite.b)][x] != mur:
            x++

        y =(int)(droite.a * x + droite.b)
        return math.sqrt(x**2 + y**2)



