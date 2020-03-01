import math

#Paramètres de la fenêtre
nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite

#Personnalisation de la fenêtre
titre_fenetre = "Arene"
image_icone = "images/robot_droite.png"

#Listes des images du jeu
image_accueil = "images/accueil.png"
image_fond = "images/fond.jpg"
image_mur = "images/mur.png"
image_depart = "images/depart.png"
image_arrivee = "images/arrivee.png"


#constantes pour le controlleur
distance_arret = 27

#constante pour l'arene
vide = '0'
obstacle = '1'


#parametre pour tracer une figure 
nb_cote = 3
longeur_cote = 100
angle_entre_cote = math.pi*2/3
vitesse_robot = 10

#constante de l'affichage du robot
largeur_robot = 30
