#!/usr/bin/python3
# -*- coding: Utf-8 -*


import sys
import pygame
from pygame.locals import *
from affichage import *
from robot import *
from arene import *
from constantes import *
from capteur import *
from controleur import *


choix='terrain2'
niveau = Arene(choix)
niveau.generer()
affichage=Affichage("images/robot_droite.png", "images/robot_gauche.png","images/robot_haut.png", "images/robot_bas.png")
robot= Robot(70.0,70.0,capteur)
affichage.chargement(niveau,robot)
capteur = Capteur(niveau,robot)
controleur = Controleur(robot)

controleurBasic = ControleurBasic(robot,capteur)


"""partie pour bouger aléatoirement"""

while True:
	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(5)
	robot.update()
	if(robot.collision(niveau)):
			print("le robot viens de se crasher")
			sys.exit()
	if(controleur.carre(6,capteur) > 0):
		exit()
	"""print("tour de boucle")"""

	affichage.refresh(robot)
	
print("collision")


