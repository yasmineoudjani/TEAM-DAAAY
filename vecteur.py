from point import *
from angle import *
import math

class Vecteur:

	def __init__(self,p1,p2):
		self.vx = p2.x - p1.x
		self.vy = p2.y - p1.y
		self.v = math.sqrt(self.vx**2 + self.vy**2)

	def rotation(self,angle):
		vXp = self.vx
        vYp = self.vy

        self.vx = vXp*math.cos(angle.valeur) - vYp*math.sin(angle.valeur)
        self.vy = vXp*math.sin(angle.valeur) + vYp*math.cos(angle.valeur)

        self.v = math.sqrt(self.vx**2 + self.vy**2)

    def update(nouvelleValeur,angle):
    	self.v = nouvelleValeur
    	self.vx= math.cos(angle.valeur)*nouvelleValeur
        self.vy= math.sin(angle.valeur)*nouvelleValeur