from point import *
class droite:
    """ classe permettant de calculer l'équation d'une droite à partir de deux points"""

    def __init__(self,p1,p2):
        self.a=(p1.y-p2.y)/(p1.x1-p2.y)
        self.b=p1.y-self.a*p1.x
        
