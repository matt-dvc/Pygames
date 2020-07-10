###################
#
# P Y G A M E    D E F A U L T   S T A R T
# v 2.0
# by matt_dvc ©2020
#
###################



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
pygame.display.set_caption('PROGRAM NAME. ESC TO EXIT')
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
    
    
    pygame.display.update()
    
    
###### MAIN LOOP #########

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
