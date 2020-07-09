import pygame
import numpy as np
import time
import os

pygame.init()

######## BASIC COLOURS ##########

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

######## DISPLAY SETTINGS #######

displayWidth = 1280
displayHeight = 720
gameTick = 30
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Tanks Multiplayer')
clock = pygame.time.Clock()

####### SHAPES AND TEXT #######

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()


def show_text(text, color, size, pos, adj):
	fontType = pygame.font.SysFont('', size)
	TextSurf, TextRect = text_objects(text, fontType, color)
	if adj == 0:
		TextRect = pos
	if adj == 1:
		TextRect.center = pos
	gameDisplay.blit(TextSurf, TextRect)
	

def line(start, finish, width, color):
	pygame.draw.line(gameDisplay, color, start, finish, int(width))


def circle(pos, r, c, b):
	pygame.draw.circle(gameDisplay, c, pos, r, b)

###### GFX UPDATE ########

def screen_update():
    gameDisplay.fill(black)
    
    ##### put draw here
    
    pygame.display.update()
    
    
###### MAIN GAME #########

class Player:
    def __init__(self,playerNo,health,score,x,y,direction,vel):
        self.playerNo = playerNo
        self.health=health
        self.score=score
        self.x=x
        self.y=y
        self.dir=direction
        self.vel=vel
        self.alive=True
        self.hitbox=()
    def draw(self):
        pass
    
class Bullet:
    def __init__(self,x,y,direction,vel):
        self.x=x
        self.y=y
        self.direction=direction
        self.vel=vel
    def draw(self):
        pass
        





def main_loop():
	inMainLoop = True
	loopTimer = 0
	gameSeconds = 0

	while inMainLoop == True:
		clock.tick(gameTick)

		loopTimer += 1 


		if loopTimer == gameTick:
			loopTimer = 0
			gameSeconds += 1


		keys = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				quit()

		if event.type == pygame.KEYUP:
			pass




main_loop()
