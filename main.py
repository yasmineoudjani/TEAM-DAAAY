from classRobot import *
from classArene import *
from classCapteur import *
from classControlleur import *
from Affichage import *
import pygame
from pygame.locals import *
import time

arene = Arene("terrain2")
arene.generer()
robot = Robot(1,1,1.0,1.0,"images/robot_haut.png", "images/robot_bas.png","images/robot_droite.png", "images/robot_gauche.png")
capteur = Capteur(robot)
controlleur = Controlleur()
affichage = Affichage(arene,robot)
continuer = 1

while continuer:
       for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer=0
                controlleur.sortieLab(capteur,arene,robot)
                affichage.AfficherArene()
                affichage.AfficherRobot()
                robot.avancer()
                print("\n")
                time.sleep(0.2)
print("pygame s'arrete")
pygame.quit()





        
        
        



