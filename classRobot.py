import math

class Robot:
        """Classe permettant de créer un personnage"""
        def __init__(self,cX,cY,X,Y) :
                """int * int * float * float -> void
                """
                #Position du personnage en cases et en coordonnée réelles
                self.case_x = cX
                self.case_y = cY
                self.x = X
                self.y = Y
                self.vX = 0.0
                self.vY = 0.0
                self.alpha = 0

        def avancer(self):
                self.x += vX
                self.y += vY
                case_x = int(x)
                case_y = int(y)

        def tourner(self,angle):
		self.vX = vX*math.cos(angle) - self.vY*math.sin(angle)
                self.vY = vX*math.sin(angle) + self.vY*math.cos(angle)
                alpha += angle%360

        def changementVitesse(self,d):
                if(vX == 0.0 && vY == 0.0):
                        vX= math.cos(self.alpha)*d
                        vY= math.sin(self.alpha)*d

        def getCaseX(self):
                return self.case_x

        def getCaseY(self):
                return self.case_y

        def getX(self):
                return self.x

        def getY(self):
                return self.y

        def getVX(self):
                return self.vX

        def getVY(self):
                return self.vY

        def getAlpha(self):
                return alpha