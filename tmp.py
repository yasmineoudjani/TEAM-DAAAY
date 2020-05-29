import time

class ControleurBasic:

    def __init__(self,robot):
        self.robot = robot

    def stop(self):
        if robot.ditsance()<1:
            self.robot.arret_urgence()
            return True
        return False
    
    def update(self):
        pass
    def start(self):
        pass
    def get_vitesse(self):
        pass
    def avancer(self,vitesse):
        self.robot.set_motor_dps(vitesse)

class StrategyToutDroit(ControleurBasic):

    def __init__(self,robot,distance):
        self.distance = distance
        self.robot = robot
        self.timestamp = -1
        self.distance_parcouru = 0
    def start(self):
        self.timestamp =  time.time()
        self.distance_parcouru = 0

    def update(self):
        dt = time.time() - self.timestamp
        self.distance_parcouru = self.distance_parcouru + dt*self.robot.vitesse()
        self.timestamp = time.time()
        if not self.stop():
            self.avancer(VITESSE_MAX)
        else: 
            self.avancer(0)
    def stop(self):
        return super().stop() or self.distance_parcouru > self.distance


class StrategySequentiel(ControleurBasic):
    def __init__(self,lst_strat):
        self.lst_strat = lst_strat
        self.cpt = 0

    def start(self):
        self.cpt = 0
        self.cur_strategy = self.lst_strat[0]
        self.cur_strategy.start()
    def update(self):
        if not self.cur_strategy.stop():
            self.cur_strategy.update()
        else:
            self.cpt +=1
            if self.cpt<len(self.lst_strat):
                self.cur_strategy = self.lst_strat[self.cpt]
                self.cur_strategy.start()
                self.cur_strategy.update()
    def stop(self):
        self.cpt >= len(self.lst_strat)

class StrategyCarre(StrategySequentiel):
    def __init__(self,robot,longueur):
        self.lst_strat = [StrategyToutDroit(robot,longueur), StrategyTourner(robot,90), StrategyToutDroit(robot,longueur), ...]
    

