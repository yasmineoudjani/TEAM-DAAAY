class Point:
	"""un point est composé de deux coordonnées : sa coordonnée en x : x et sa coordonnée en y : y"""
	def __init__(self,x,y):
		"""prend en paramètre ses deux coordonnées"""
		self.x = x
		self.y =y

	def update(self,vecteur):
		"""translate le point par rapport au vecteur donné en paramètre"""
		self.x += vecteur.vx
		self.y += vecteur.vy
