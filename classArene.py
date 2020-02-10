class Arene:

	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0

	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau	

	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		caseVide = pygame.image.load(image_mur).convert()
		mur = pygame.image.load(image_depart).convert()
		obstacle = pygame.image.load(image_arrivee).convert_alpha()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == '0':		   #m = Mur
					fenetre.blit(caseVide, (x,y))
				elif sprite == '1':		   #d = Départ
					fenetre.blit(mur, (x,y))
				elif sprite == '2':		   #a = Arrivée
					fenetre.blit(obstacle, (x,y))
				num_case += 1
			num_ligne += 1
			