from classArene import *
from classRobot import *
import math

class Capteur:
	"""classe permettant de créer un capteur de distance"""

	def __init__(self,robot):
		
		self.robot = robot
		self.x = robot.getCaseX
		self.y = robot.getCaseY

	def Obstacle(self , arene):
		""" retourne true si il y a un obstacle sur le chemin que va parcourir le robot en une unité de temps, false sinon"""
		structure = arene.getStructure()
		alpha = self.robot.getAlpha()
		print("angle alpha =",alpha)
		self.x = self.robot.getCaseX()
		self.y = self.robot.getCaseY()
		vx = int(self.robot.getVX())
		vy = int(self.robot.getVY())
		#si le robot est à l'arrêt , on regarde si il y a un obstacle à une case en avant
		if(vx == 0 and vy == 0 ):
			vx=1
			vy=1


		#si le robot est tourné vers la droite
		if (alpha > 0*(math.pi/2)-1 and alpha < 0*(math.pi/2)+1  ):
			print("je regarde à droite")
			#on regarde les vx prochaine cases
			for i in range(1,abs(vx)+1):

				#si une de ces cases contiennent un obstacle on retourne true
				if (structure[(self.x)+i][(self.y)] == '1'):
					print("obstacle devant le robot")
					return True

		#si le robot est tourné vers le bas
		if (alpha > 1*(math.pi/2)-1 and alpha < 1*(math.pi/2)+1  ):
			print("je regarde en bas")
			for i in range(1,abs(vy)+1):
				if (structure[(self.x)][(self.y)+i] == '1'):
					print("obstacle devant le robot")
					return True

		#si le robot est tourné vers la gauche
		if (alpha > 2*(math.pi/2)-1 and alpha < 2*(math.pi/2)+1  ):
			print("je regarde à gauche")
			for i in range(1,abs(vx)+1):
				if (structure[(self.x)-i][(self.y)] == '1'):
					print("obstacle devant le robot")
					return True

		#si le robot est tourné vers le haut
		if (alpha > 3*(math.pi/2)-1 and alpha < 3*(math.pi/2)+1  ):
			print("je regarde en haut")
			for i in range(1,abs(vy)+1):
				if (structure[(self.x)][(self.y)-i] == '1'):
					print("obstacle devant le robot")
					return True

		print("pas d'obstacle devant le robot")




