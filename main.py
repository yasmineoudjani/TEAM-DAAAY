from classRobot import *
from classArene import *
from classCapteur import *
from classControlleur import *


arene = Arene("terrain1")
arene.generer()
robot = Robot(7,8,7.0,8.0)
capteur = Capteur(robot)
controlleur = Controlleur()
for i  in range(0,10):
	controlleur.alea(capteur,arene,robot)
	print("tour de boucle")
	


