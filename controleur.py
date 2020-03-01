import random
import math

from robot import *
from Arene import *
from Capteur import *


class Controleur:
	""" classe premettant de créer un controleur"""

	def __init__(self,robot):
		self.robot=robot

	def alea(self,capteur,arene):
		#si le robot est à l'arret
		if((int)(self.robot.vecteurVitesse.v)==0):
			#on vérifie qu'il n'y a rien devant le robot
			if(capteur.distanceObstacle()>distance_arret):
				#on lui donne une vitesse de 1 case par unité de temps
				self.robot.changementVitesse(15)
			else:
				#on le fait tourner aléatoirement
				c=random.random()
				self.robot.tourner(c*(math.pi*2))	

		else:
			#si il y a un obstacle sur la trajectoire du robot
			if(capteur.distanceObstacle()<=distance_arret):
				#on arrete le robot
				self.robot.changementVitesse(0)

	def aleaLarge(self,capteur,arene):
		#si le robot est à l'arret
		if((int)(self.robot.vecteurVitesse.v)==0):
			#on vérifie qu'il n'y a rien devant le robot
			if(capteur.distanceObstacleLarge()>distance_arret):
				#on lui donne une vitesse de 1 case par unité de temps
				self.robot.changementVitesse(5)
			else:
				#on le fait tourner aléatoirement
				c=random.random()
				self.robot.tourner(c*(math.pi*2))	

		else:
			#si il y a un obstacle sur la trajectoire du robot
			if(capteur.distanceObstacleLarge()<=distance_arret):
				#on arrete le robot
				self.robot.changementVitesse(0)

	def set_motor_dps(self,dps):
		self.robot.changementVitesse(15)
		
	def tourner(self,angle):
		self.robot.tourner(angle)
