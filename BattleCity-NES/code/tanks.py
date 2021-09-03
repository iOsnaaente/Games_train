#! usr/bin/dev python

import pygame


class PlayerTank:

	posicao = [0,0]
	direcao = 's'

	points = 0
	vidas = 1

	img = 0
	vel = 8

	blinking = False;

	screen = 0

	def __init__(self, img, posicao, screen):
		
		self.posicao = posicao
		self.screen = screen

		self.vel = 8
		self.vidas = 4
		self.points = 0

		self.direcao = 'w'
		self.img = img


	def plot(self):
		self.screen.blit(self.img, self.posicao)


	def move(self, event):
		if event.key == pygame.K_w:
			if self.direcao is 'w':
				self.posicao[1] = self.posicao[1] - self.vel

			else:
				if self.direcao == 'd':
					self.img = pygame.transform.rotate(self.img, 90)
				elif self.direcao == 'a':
					self.img = pygame.transform.rotate(self.img, 270)
				else:
					self.img =pygame.transform.rotate(self.img, 180)
				self.direcao = 'w'
					
		
		if event.key == pygame.K_a:
			if self.direcao is 'a':
				self.posicao[0] = self.posicao[0] - self.vel
				
			else:				
				if self.direcao == 'd':
					self.img =pygame.transform.rotate(self.img, 180)
				elif self.direcao == 'w':
					self.img =pygame.transform.rotate(self.img, 90)
				else:
					self.img =pygame.transform.rotate(self.img, 270)
				self.direcao = 'a'


		if event.key == pygame.K_s:
			if self.direcao is 's':
				self.posicao[1] = self.posicao[1] + self.vel
				
			else:				
				if self.direcao == 'd':
					self.img =pygame.transform.rotate(self.img, 270)
				elif self.direcao == 'w':
					self.img =pygame.transform.rotate(self.img, 180)
				else:
					self.img =pygame.transform.rotate(self.img, 90)
				self.direcao = 's'

		if event.key == pygame.K_d:
			if self.direcao is 'd':
				self.posicao[0] = self.posicao[0] + self.vel
				
			else:
				if self.direcao == 'w':
					self.img =pygame.transform.rotate(self.img, 270)
				elif self.direcao == 'a':
					self.img =pygame.transform.rotate(self.img, 180)
				else:
					self.img =pygame.transform.rotate(self.img, 90)
				self.direcao = 'd'



