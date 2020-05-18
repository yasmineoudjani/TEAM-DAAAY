import random
import math

from robot import *
from arene import *
from capteur import *


class Controleur:
	""" classe premettant de créer un controleur"""

	def __init__(self,robot):
		self.robot=robot
		self.compteur=0
		self.compteur_nb_cote=0

	def set_motor_dps(self,dps):
		self.robot.changementVitesse(15)
		
	def tourner(self,angle):
		self.robot.tourner(angle)

	def stop(self,capteur):
		if(capteur.distanceObstacle()<=distance_arret):
			#on arrete le robot
			self.robot.changementVitesse(0)
			return 1

	def avancer(self,capteur):
		if((int)(self.robot.vecteurVitesse.v)==0):
			#on vérifie qu'il n'y a rien devant le robot
			if(capteur.distanceObstacle()>distance_arret):
				#on lui donne une vitesse de 1 case par unité de temps
				self.robot.changementVitesse(15)
				self.compteur += 1
		else:
			#si il y a un obstacle sur la trajectoire du robot
			if(self.stop(capteur) != 1):
				self.compteur += 1

	def carre(self , longueur , capteur):
		cpt = self.compteur
		cptnc = self.compteur_nb_cote
		if(self.compteur_nb_cote < 4):
			if(self.compteur == longueur):
				self.set_motor_dps(0)
				self.compteur = 0
				self.tourner((math.pi/2.01))
				self.compteur_nb_cote += 1
			else:
				self.avancer(capteur)

			if(cpt==self.compteur and cptnc==self.compteur_nb_cote):
				return 2
			return 0
		else:
			if(cpt==self.compteur and cptnc==self.compteur_nb_cote):
				return 2
			return 1


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
			self.stop(capteur)

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
			self.stop(capteur)


