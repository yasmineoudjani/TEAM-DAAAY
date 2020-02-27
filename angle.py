import math

class Angle:

	def __init__(self,a):
		self.valeur = a

	def addition(self,a):
		self.valeur = (self.valeur + a)%(2*math.pi)

