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

display_width = 1280
display_height = 720
game_tick = 30
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PROGRAM NAME. EXC TO EXIT')
clock = pygame.time.Clock()

####### MAIN PROGRAM LOOP #######

class Car():
	def __init__(self,player):
		self.pos=player[0]
		self.speed=player[1]
		
		pass
	def spawn(self):
		pass
	
		


def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()


def show_text(text, color, size, pos, adj):
	font_type = pygame.font.SysFont('', size)
	font_color = color
	TextSurf, TextRect = text_objects(text, font_type, font_color)
	if adj == 0:
		TextRect = pos
	if adj == 1:
		TextRect.center = pos
	gameDisplay.blit(TextSurf, TextRect)
	

def line(start, finish, width, color):
	pygame.draw.line(gameDisplay, color, start, finish, int(width))


def circle(pos, r, c, b):
	pygame.draw.circle(gameDisplay, c, pos, r, b)


def main_loop():

	inMainLoop = True
	loop_timer = 0
	time_in_game_sec = 0

	while inMainLoop == True:

		gameDisplay.fill(black)
		######## MAIN LOOP TIMER #########

		loop_timer += 1
	   # print(time_in_game_sec, loop_timer)

		if loop_timer == game_tick:
			loop_timer = 0
			time_in_game_sec += 1
	   #     print(time_in_game_sec)

		####### KEY / EVENT LOGIC #######

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

		####### MAIN CODE BEGIN ########

		####### MAIN CODE END ##########

		####### RENDERING ##############

		pygame.display.update()
		clock.tick(game_tick)


main_loop()
