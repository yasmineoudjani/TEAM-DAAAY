
import pygame
from pygame.locals import *

from classRobot import *
from constantes import *

pygame.init()
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)


continuer = 1
while continuer:	
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	pygame.display.flip()

	continuer_jeu = 1
	continuer_accueil = 1

	while continuer_accueil:
	
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				choix = 0
				
			elif event.type == KEYDOWN:		
				if event.key == K_F1:
					continuer_accueil = 0	
					choix = 'n1'		
				elif event.key == K_F2:
					continuer_accueil = 0
					choix = 'n2'
			
		

	
	if choix != 0:
		
		fond = pygame.image.load(image_fond).convert()

		
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		
		dk = Perso("images/dk_droite.png", "images/dk_gauche.png", 
		"images/dk_haut.png", "images/dk_bas.png", niveau)

				
	
	while continuer_jeu:
	
		
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					continuer_jeu = 0
					
				elif event.key == K_RIGHT:
					dk.deplacer('droite')
				elif event.key == K_LEFT:
					dk.deplacer('gauche')
				elif event.key == K_UP:
					dk.deplacer('haut')
				elif event.key == K_DOWN:
					dk.deplacer('bas')			
			
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(dk.direction, (dk.x, dk.y))
		pygame.display.flip()

		if niveau.structure[dk.case_y][dk.case_x] == 'a':
			continuer_jeu = 0
