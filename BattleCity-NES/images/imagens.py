#! usr/bin/dev python	

import pygame 
import os


# TANQUES INIMIGOS
redTank1 = pygame.image.load(os.path.join('images', "redTank1.png"))
redTank2 = pygame.image.load(os.path.join('images', "redTank2.png"))
redTank3 = pygame.image.load(os.path.join('images', "redTank3.png"))
redTank4 = pygame.image.load(os.path.join('images', "redTank4.png"))

# TANQUES JOGADOR
blueTank = pygame.image.load(os.path.join('images', 'blueTank.png'))
greenTank = pygame.image.load(os.path.join('images', 'greenTank.png'))

# TERRENOS
bushes = pygame.image.load(os.path.join('images',"bushes.png"))
bricks = pygame.image.load(os.path.join('images',"brick.png"))
pool   = pygame.image.load(os.path.join('images',"pool.png"))
iron   = pygame.image.load(os.path.join('images',"iron.png"))
ice    = pygame.image.load(os.path.join('images',"ice.png"))

# ITENS
shieldTanque1 = pygame.image.load(os.path.join('images',"shieldTanque1.png"))
shieldTanque2 = pygame.image.load(os.path.join('images',"shieldTanque2.png"))

shovel = pygame.image.load(os.path.join('images',"shovel.png"))
star   = pygame.image.load(os.path.join('images',"star.png"))

#time
#bomb


""" 
# TANQUES INIMIGOS
redTank1 = pygame.image.load("redTank1.png")
redTank2 = pygame.image.load("redTank2.png")
redTank3 = pygame.image.load("redTank3.png")
redTank4 = pygame.image.load("redTank4.png")

# TANQUES JOGADOR
blueTank = pygame.image.load('blueTank.png')
greenTank = pygame.image.load('greenTank.png')

# TERRENOS
bushes = pygame.image.load("bushes.png")
bushes   = pygame.transform.scale(bushes, (32,32))

bricks = pygame.image.load("brick.png")
pool   = pygame.image.load("pool.png")

iron   = pygame.image.load("iron.png")
iron   = pygame.transform.scale(iron, (32,32))

ice    = pygame.image.load("ice.png")

# ITENS
shieldTanque1 = pygame.image.load("shieldTanque1.png")
shieldTanque2 = pygame.image.load("shieldTanque2.png")

shovel = pygame.image.load("shovel.png")
star   = pygame.image.load("star.png")
"""




