import math

class Angle:
"""représente une angle en radian
"""

	def __init__(self,a):
		"""prend en paramètre la valeur de l'angle en radian
		"""
		self.valeur = a

	def addition(self,a):
		"""additionne à l'angle un angle a modulo 2pi 
		"""
		self.valeur = (self.valeur + a)%(2*math.pi)

