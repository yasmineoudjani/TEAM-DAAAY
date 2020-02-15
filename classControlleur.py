import classRobot
import classCapteur
import classArene
import random
import math

class Controlleur:
	""" classe premettant de créer un controlleur"""

	def __init__(self):

	def alea(self,capteur,arene):

		#si le robot est à l'arret 
		if(robot.getVX == 0 && robot.getVY == 0):
			#on vérifie qu'il n'y a rien devant le robot
			if(not(capteur.obstacle(arene))):
				#on lui donne une vitesse de 1 case par unité de temps
				robot.changementVitesse(1)
			else:
				#on le fait tourner aléatoirement
				c=random.randint(0, 3)
				robot.tourner(c*(pi/2))

		else:
			#si il y a un obstacle sur la trajectoire du robot
			if(capteur.obstacle(arene)):
				#on arrete le robot
				robot.changementVitesse(0)

	def sortieLab(self,capteur,arene):

		#si le robot est à l'arret 
		if(robot.getVX == 0 && robot.getVY == 0):
			#on vérifie qu'il n'y a rien devant le robot
			if(not(capteur.obstacle(arene))):
				#on lui donne une vitesse de 1 case par unité de temps
				robot.changementVitesse(1)
			else:
				#on le fait tourner de 90 degré 
				robot.tourner(pi/2)

		else:
			#si il y a un obstacle sur la trajectoire du robot
			if(capteur.obstacle(arene)):
				#on arrete le robot
				robot.changementVitesse(0)

