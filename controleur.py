import random
import math

from robot import *
from Arene import *
from Capteur import *


class Controleur:
	""" classe premettant de créer un controleur"""

	def __init__(self):
		self.id=1

	def alea(self,capteur,arene,robot):
		#si le robot est à l'arret
		if((int)(robot.vecteurVitesse.v)==0):
			print("le robot est à l'arrêt")
			#on vérifie qu'il n'y a rien devant le robot
			if(capteur.distanceObstacle()>distance_arret):
				#on lui donne une vitesse de 1 case par unité de temps
				robot.changementVitesse(15)
			else:
				#on le fait tourner aléatoirement
				c=random.random()
				robot.tourner(c*(math.pi*2))	

		else:
			#si il y a un obstacle sur la trajectoire du robot
			print("le robot n'est pas à l'arrêt")
			if(capteur.distanceObstacle()<=distance_arret):
				#on arrete le robot
				robot.changementVitesse(0)
		
