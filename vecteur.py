from point import *
from angle import *
import math

class Vecteur:
"""
un vecteur est composé:
    -d'une norme : v
    -sa valeur en x : vx
    -sa valeur en y : vy
"""

	def __init__(self,p1,p2):
        """prend en paramètre 2 Point
        """
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

    def update(nouvelleValeur,angle):
        """affecte une nouvelle norme au vecteur
        """
    	self.v = nouvelleValeur
    	self.vx= math.cos(angle.valeur)*nouvelleValeur
        self.vy= math.sin(angle.valeur)*nouvelleValeur