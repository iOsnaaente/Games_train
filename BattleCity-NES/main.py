#! usr/bin/dev python

from  stages import Stages	#Le as fases
from code import  tanks			#Responsável pelos tanques do player
from images import imagens					#imagens do jogo

import pygame
import random



screen_Dimension=[32*20,32*20]

pygame.init()

screen = pygame.display.set_mode(screen_Dimension)

pygame.display.set_caption("My_Poor_NES_Batlle_City")

clock = pygame.time.Clock()



Fase_1 = Stages.Stages(screen)
Fase_1.readStage(1)

Tank = tanks.PlayerTank(imagens.blueTank, [64,64], screen)

while True:

	screen.fill([0,0,0])

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()

			Tank.move(event)
			
	Fase_1.plotStage()
	Tank.plot()
	pygame.display.update()


	clock.tick(60)

