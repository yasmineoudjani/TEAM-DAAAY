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
robot= Robot(70.0,70.0)
affichage.chargement(niveau,robot)
capteur = Capteur(niveau,robot)
controleur = Controleur(robot)

"""partie pour bouger aléatoirement"""

while True:
	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(20)
	robot.avancer()
	if(robot.collision(niveau)):
			print("le robot viens de se crasher")
			sys.exit()
	controleur.carre(6,capteur)
	affichage.refresh(robot)
	
print("collision")

"""partie pour faire un carré"""
"""
for i in range(0,nb_cote):
	pygame.time.Clock().tick(5)
	controleur.set_motor_dps(vitesse_robot)
	for j in range(0,int(longeur_cote/vitesse_robot)):
		pygame.time.Clock().tick(5)
		robot.avancer()
		if(robot.collision(niveau)):
			print("le robot viens de se crasher")
			sys.exit()
		affichage.refresh(robot)
	controleur.tourner(angle_entre_cote)
	affichage.refresh(robot)
"""
