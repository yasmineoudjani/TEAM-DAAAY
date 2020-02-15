import classArene

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
		self.x = self.robot.getCaseX()
		self.y = self.robot.getCaseY()
		vx = int(self.robot.getVX())
		vy = int(self.robot.getVY())

		#si le robot est à l'arrêt , on regarde si il y a un obstacle à une case en avant
		if(vx == 0 && vy == 0 ):
			vx=1
			vy=1


		#si le robot est trouné vers la droite
		if (alpha == 0):
			#on regarde les vx prochaine cases
			for i in range(0,vx):
				#si une de ces cases contiennent un obstacle on retourne true
				if (structure[self.x+1][self.y] == 1):
					return true

		#si le robot est trouné vers la haut
		if (alpha == 90):
			for i in range(0,vy):
				if (structure[self.x][self.y+1] == 1):
					return true

		#si le robot est trouné vers la gauche
		if (alpha == 180):
			for i in range(0,vx):
				if (structure[self.x-1][self.y] == 1):
					return true

		#si le robot est trouné vers le bas
		if (alpha == 270):
			for i in range(0,vy):
				if (structure[self.x][self.y-1] == 1):
					return true




