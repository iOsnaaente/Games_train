#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""#
#"				PAGINA ONDE OCORRERA O JOGO				   "# 
#"	   DEVE SER UMA PÁGINA COM DIMENSÕES DE 16X15          "#
#"	 DENTRO DA PÁGINA PRINCIPAL HAVERA UMA SURFACE         "#
#"														   "#
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""#


cor_fundo = [150,150,150]

import pygame 
from Stages import Stages

pygame.init()
pygame.font.init()


screenDimensions = [32*16, 32*15]

mainScreen = pygame.display.set_mode(screenDimensions)  #16 BLOCOS POR 15 BLOCOS
#DEVE SER PEGA PELO __INIT__ DA CLASE, RECEBE COMO PARAMETRO


#DEFINICAO DAS FUNCOES
surfaceGame    = pygame.surface.Surface((32*12, 32*13))    #SURFACE DO JOGO
surfaceTanks   = pygame.surface.Surface((32*2, 32*6))      #SURFACE DOS TANQUES RESTANTES
surfaceLifes   = pygame.surface.Surface((32*2, 32*3))      #SURFACE DE PLOTAGEM DAS VIDAS
surfaceStages  = pygame.surface.Surface((32*2, 32*2))      #SURFACE DE PLOTAGEM DO NÍVEL DA FASE

Fase =  Stages(surfaceGame)

#FUNCAO PARA FACILITAR A ESCRITA
def writeTextOnSurface(surface, pos, text, color=[0,0,0], size=16):
	fonte = pygame.font.SysFont("monospace", size)
	label = fonte.render(text, True, color) 
	surface.blit(label, pos)


#SURFACES
surfaceGame.fill([0,0,0])
surfaceTanks.fill(cor_fundo)
surfaceLifes.fill(cor_fundo)
surfaceStages.fill(cor_fundo)


#IMAGENS QUE DEVEM SER PEGAS DE OUTRA CLASSE/FUNCAO
tanqueImg = pygame.image.load("redTank4.png")

twoPlayers = True
#recebe o modo de jogo

play1 = pygame.image.load("blueTank.png")
play2 = pygame.image.load("greenTank.png")


star  = pygame.image.load("star.png") 
star  = pygame.transform.scale(star, [48,48]) 

pygame.display.set_caption("View Game")
clock = pygame.time.Clock()


tanquesVivos = [[0,0],[32,0],[0,32],[32,32],[0,64],[32,64],[0,96],[32,96],[0,128],[32,128]]
#tanquesVivos = funcao_Que_Retorna_Array_TanquesVivos()
vidasPlay1 = 2
#vidasPlay1 = funcao_Que_Retorna_Vidas_Player1()
vidasPlay2 = 2
#vidasPlay1 = funcao_Que_Retorna_Vidas_Player2()

num_fase = 1 
Fase.readStage(num_fase)
#deve receber o número da fase 



while True:

	mainScreen.fill(cor_fundo)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()



	#PLOTAM AS SURFACES DE CADA ELEMENTO NA TELA
	mainScreen.blit(surfaceGame, [24,32])
	mainScreen.blit(surfaceTanks, [screenDimensions[0]-96, 32])
	mainScreen.blit(surfaceLifes, [screenDimensions[0]-96, 32*8])
	mainScreen.blit(surfaceStages, [screenDimensions[0]-96, 32*12])

	#PLOTA OS TANQUES QUE FALTA SEREM DESTRUIDOS
	for i in range(len(tanquesVivos)):
		surfaceTanks.blit(tanqueImg, (tanquesVivos[i]))


	#PLOTA AS VIDAS 
	writeTextOnSurface(surfaceLifes, [8,0], "IP", [0,0,0], 32)
	
	surfaceLifes.blit(play1, [0,32])
	writeTextOnSurface(surfaceLifes, [32,32], str(vidasPlay1), [0,0,0], 32)
	
	if (twoPlayers):
		surfaceLifes.blit(play2, [0,64])
		writeTextOnSurface(surfaceLifes, [32,64], str(vidasPlay2), [0,0,0], 32)


	#PLOTA O NÍVEL DA FASE 
	writeTextOnSurface(surfaceStages, [32,32], str(num_fase), [0,0,0], 32)
	surfaceStages.blit(star, [0,0])

	#PLOTA A FASE    - CHAMA A FUNCAO DE PLOTAGEM
	Fase.plotStage()




	pygame.display.update()
	clock.tick(60)
