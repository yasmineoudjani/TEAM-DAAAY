import random
import math

from classRobot import *
from classArene import *
from classCapteur import *


class Controlleur:
	""" classe premettant de créer un controlleur"""

	def __init__(self):
		self.id=1

	def alea(self,capteur,arene,robot):
		#si le robot est à l'arret 
		if(robot.getVX() == 0.0 and robot.getVY() == 0.0):
			print("le robot est à l'arrêt")
			#on vérifie qu'il n'y a rien devant le robot
			if(not(capteur.Obstacle(arene))):
				#on lui donne une vitesse de 1 case par unité de temps
				robot.changementVitesse(1)
			else:
				#on le fait tourner aléatoirement
				c=random.randint(0, 3)
				robot.tourner(c*(math.pi/2))	

		else:
			#si il y a un obstacle sur la trajectoire du robot
			print("deuxieme cas")
			if(capteur.Obstacle(arene)):
				#on arrete le robot
				robot.changementVitesse(0)
		
	def sortieLab(self,capteur,arene,robot):

		#si le robot est à l'arret 
		if(robot.getVX() == 0.0 and robot.getVY() == 0.0):
			#on vérifie qu'il n'y a rien devant le robot
			if(not(capteur.Obstacle(arene))):
				#on lui donne une vitesse de 1 case par unité de temps
				robot.changementVitesse(1)
				return
			else:
				#on le fait tourner de 90 degré 
				robot.tourner(math.pi/2)
				return

		else:
			#si il y a un obstacle sur la trajectoire du robot
			if(capteur.Obstacle(arene)):
				#on arrete le robot
				robot.changementVitesse(0)
				return

