#! usr/bin/dev python	

#IMAGENS DOS TERRENOS
from images import imagens
import os 

class Stages:

	#ONDE FICARAO GUARDADAS AS INFORMACOES DE BLOCO E POSICAO
	arrayWalls = []
	
	#NUMERO PARA SER IMPRESSO
	index = 0

	#QUANTIDADE DE STAGES DISPONIVEIS
	n_stages = 1

	#ENTRADA DA TELA
	screen = 0

	'''
	IPs:
	0  - bricks 
	1  - backgroun
	2  - steels
	3  - bushes
	4  - ice
	5  - pools
	'''

	#DEFINE A TELA ONDE SERAO PLOTADOS AS IMAGENS
	def __init__(self, screen):
		self.screen = screen



	## MELHORAR ESSA PARTE DO CODIGO ESTRUTURALMENTE ##
	## 				TRANFORMAR OS 2 FOR EM 1         ##

	#VAI LER O TXT COM OS IPS DOS TERRENOS
	def readStage(self, index):
		txt = open(os.path.join("stages","stage_"+str(index)+".txt"), 'r')				#le o txt
		x,y = 0,0												#para definir as posicoes		
		for lines in txt:                                 	    #le as linhas do txt
			for num in lines.replace(" ", ""):					#le os elementos 
				try:											#se não for possivel dar um append significa que eh quebra de linha
					self.arrayWalls.append((int(num),[x,y]))
					x = x +32
				except:											#na quebra de linha y cresce 32 bits
					y = y +32
					x = 0

		txt.close()   #Fecha o txt


	#PLOTA A FASE NO MAPA LENDO O CODIGO DO ELEMENTO DA ARRAY E PONDO NA POSICAO DEFINIDA
	def plotStage(self):
		for i in range(len(self.arrayWalls)):
			if self.arrayWalls[i][0] is 0:
				self.screen.blit(imagens.bricks, [self.arrayWalls[i][1][0], self.arrayWalls[i][1][1]])
			
			elif self.arrayWalls[i][0] is 2:
				self.screen.blit(imagens.iron, [self.arrayWalls[i][1][0], self.arrayWalls[i][1][1]])
			
			elif self.arrayWalls[i][0] is 3:
				self.screen.blit(bushes, [self.arrayWalls[i][1][0], self.arrayWalls[i][1][1]])
			
			elif self.arrayWalls[i][0] is 4:
				self.screen.blit(imagens.ice, [self.arrayWalls[i][1][0], self.arrayWalls[i][1][1]])
			
			elif self.arrayWalls[i][0] is 5:
				self.screen.blit(imagens.pool, [self.arrayWalls[i][1][0], self.arrayWalls[i][1][1]])
			

	#CRIAR FUTURAMENTE NA OPCAO DO JOGO CRIAR CENARIO
	def createStage(self, array ):
		pass
