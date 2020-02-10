class Robot:
	def __init__(self,image):
		self.image = image
		self.x = 1
		self.y = 1
		self.vitesse = 0
		self.sensX = 1
		self.sensY = 0

	def avancer(self):
		self.x = self.x + self.sensX
		self.y = self.y + self.sensY

	def tourner(self,s):
	#s est le paramètre permettant de savoir dans quel sens on tourne , 0 sens horaire , 1 sens anti-horaire
		if(s=0):
			if(x=1 and y=0):
				self.sensX = 0
				self.sensY = 1
			if(x=0 and y=1):
				self.sensX = -1
				self.sensY = 0
			if(x=-1 and y=0):
				self.sensX = 0
				self.sensY = -1
			if(x=0 and y=-1):
				self.sensX = 1
				self.sensY = 0
		if(s=1):
			if(x=0 and y=-1):
				self.sensX = -1
				self.sensY = 0
			if(x=-1 and y=0):
				self.sensX = 0
				self.sensY = 1
			if(x=0 and y=1):
				self.sensX = 1
				self.sensY = 0
			if(x=1 and y=0):
				self.sensX = 0
				self.sensY = -1

	def gestionVitesse(self,v):
	# v est le paramètre de la vitesse. 0 , 1 ou 2.
		self.vitesse = v 



