class Arene:
	"""Classe permettant de créer une arene"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
		self.nbLigne = 0
		self.nbColonne = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le terrain en fonction du fichier.
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
				#on met en memoire le nombre de ligne
				self.nbLigne += 1
			#On sauvegarde cette structure
			self.structure = structure_niveau
			#on met en mémoire le nombre de colonne
			self.nbColonne = len(structure_niveau[0])

	def getNbLigne(self):
		return self.nbLigne

	def getNbColonne(self):
		return self.nbColonne

	def getStructure(self):
		return self.structure