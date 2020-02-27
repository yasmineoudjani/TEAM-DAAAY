#!/usr/bin/python3
# -*- coding: Utf-8 -*


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
robot= Robot(30.0,30.0)
affichage.chargement(niveau,robot)
capteur = Capteur(niveau)
controleur = Controleur()

while True:
	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(30)
	robot.avancer()
	controleur.alea(capteur,niveau,robot)
	affichage.refresh(robot)
