

import math

class Vecteur:
    """un vecteur est composé: d'une norme : v , sa valeur en x : vx et sa valeur en y : vy"""
    def __init__(self,p1,p2):
        """prend en paramètre 2 Point"""
        self.vx = p2.x - p1.x
        self.vy = p2.y - p1.y
        self.v = math.sqrt(self.vx**2 + self.vy**2)

    def rotation(self,angle):
        """prend en parametre un angle
        effectue une rotation de angle radian du vecteur
        """
        vXp = self.vx
        vYp = self.vy

        self.vx = vXp*math.cos(angle.valeur) - vYp*math.sin(angle.valeur)
        self.vy = vXp*math.sin(angle.valeur) + vYp*math.cos(angle.valeur)

    def update(self,nouvelleValeur,angle):
        """affecte une nouvelle norme au vecteur
        """
        self.v = nouvelleValeur
        self.vx= math.cos(angle.valeur)*nouvelleValeur
        self.vy= math.sin(angle.valeur)*nouvelleValeur


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

class droite:
    """ classe permettant de calculer l'équation d'une droite à partir de deux points"""

    def __init__(self,p1,p2):
        self.a=(p1.y-p2.y)/(p1.x1-p2.y)
        self.b=p1.y-self.a*p1.x


import math

class Angle:
	"""représente une angle en radian"""

	def __init__(self,a):
		"""prend en paramètre la valeur de l'angle en radian
		"""
		self.valeur = a

	def addition(self,a):
		"""additionne à l'angle un angle a modulo 2pi 
		"""
		self.valeur = (self.valeur + a.valeur)%(2*math.pi)
